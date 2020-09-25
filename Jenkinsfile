pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = "ap-southeast-1"
        PATH = "/opt/sonar-scanner/bin:/usr/bin:/home/jenkins/.local/bin:/usr/local/bin:/var/lib/jenkins/sam-venv/${BUILD_TAG}/bin:$PATH"
        SONARQUBE_CREDS = credentials('tech-hunt-token') //sonarqube token  tbd
        SONARQUBE_KEY = credentials('tech-hunt')     //sonarqube key tbd
        SONARQUBE_URL = credentials('SonarQube_URL')     //sonarqube url
        SOURCE_CODE_FOLDER = 'apps'
        SAM_PACKAGE = "packaged.yaml"
        S3_BUCKET_NAME = "tech-hunt"
        IAM_ROLE = "CAPABILITY_IAM"
        STACK_NAME = "tech-hunt"
        COV_FILE = 'coverage.xml'
    }
    stages {
        stage('Environment Setup') {
            steps {
                sh '''
                    mkdir -p /var/lib/jenkins/sam-venv
                    python3.7 -m venv /var/lib/jenkins/sam-venv/${BUILD_TAG}
                    source /var/lib/jenkins/sam-venv/${BUILD_TAG}/bin/activate
                    pip3 install -r ${SOURCE_CODE_FOLDER}/requirements.txt
                    pip3 install requests pytest pytest-mock pytest-cov radon pylint awscli aws-sam-cli boto3 mock moto
                '''
            }
        }

        stage('Unit Tests') {
            steps {
                withAWS(credentials: 'AWSCredentials') {
                    sh '''
                        source /var/lib/jenkins/sam-venv/${BUILD_TAG}/bin/activate
                        pytest -v --cov-report xml --cov=${SOURCE_CODE_FOLDER} --cov=tests.unit tests/

                    '''
                }
            }
            post {
                always {
                    junit(allowEmptyResults: true,
                            testResults: ${COV_FILE})
                }
            }
        }

        stage('Static Analysis') {
            steps {
                echo "Raw metrics"
                sh '''
                    source /var/lib/jenkins/sam-venv/${BUILD_TAG}/bin/activate
                    radon raw --json ${SOURCE_CODE_FOLDER} > raw_report.json
                    radon cc --json ${SOURCE_CODE_FOLDER} > cc_report.json
                    radon mi --json ${SOURCE_CODE_FOLDER} > mi_report.json
                    sloccount --duplicates --wide ${SOURCE_CODE_FOLDER} > sloccount.sc


                '''

                echo "PEP8 style check"
                sh '''
                    source /var/lib/jenkins/sam-venv/${BUILD_TAG}/bin/activate
                    pylint --disable=C ${SOURCE_CODE_FOLDER} || true
                '''
            }
            post {
                always {
                    step([$class             : 'CoberturaPublisher',
                          autoUpdateHealth   : false,
                          autoUpdateStability: false,
                          coberturaReportFile: ${COV_FILE},
                          failNoReports      : false,
                          failUnhealthy      : false,
                          failUnstable       : false,
                          maxNumberOfBuilds  : 10,
                          onlyStable         : false,
                          sourceEncoding     : 'ASCII',
                          zoomCoverageChart  : false])
                }
            }
        }

        stage('Static Analysis Upload') {
            steps {
                sh "sonar-scanner -Dsonar.projectKey=${env.SONARQUBE_KEY} -Dsonar.sources=. -Dsonar.host.url=${env.SONARQUBE_URL} -Dsonar.login=${env.SONARQUBE_CREDS} -Dsonar.python.coverage.reportPaths=${COV_FILE}"
            }
        }

        stage('API Tests') {
            steps {
                withAWS(credentials: 'AWSCredentials') {
                    timeout(time: 5, unit: 'MINUTES') {
                        sh '''
                            source /var/lib/jenkins/sam-venv/${BUILD_TAG}/bin/activate
                            cd tests/.api_test/
                            sh test.sh
                        '''
                    }
                }
            }

        }
        stage('Validate') {
            when {
                branch 'master'
            }
            steps {
                withAWS(credentials: 'AWSCredentials') {
                    timeout(time: 5, unit: 'MINUTES') {
                        sh '''
                            source /var/lib/jenkins/sam-venv/${BUILD_TAG}/bin/activate
                            sam validate
                        '''
					}
                }
            }
        }
        stage('Build') {
            when {
                branch 'master'
            }
            steps {
                timeout(time: 10, unit: 'MINUTES') {
                    sh '''
                        source /var/lib/jenkins/sam-venv/${BUILD_TAG}/bin/activate
                        sam build
                    '''
                }
            }
        }
        stage('Package & Deploy') {
            when {
                branch 'master'
            }
            steps {
                withAWS(credentials: 'AWSCredentials') {
                    timeout(time: 10, unit: 'MINUTES') {
                        sh '''
                            source /var/lib/jenkins/sam-venv/${BUILD_TAG}/bin/activate
                            sam package --output-template-file ${SAM_PACKAGE} --s3-bucket ${S3_BUCKET_NAME}
                            sam deploy --template-file ${SAM_PACKAGE} --stack-name ${STACK_NAME} --capabilities ${IAM_ROLE} --region ${AWS_DEFAULT_REGION}
                        '''
					}
                }
            }
        }
    }
    post {
        always {
            sh '''
                rm -r /var/lib/jenkins/sam-venv/${BUILD_TAG}
            '''
        }
    }
}
