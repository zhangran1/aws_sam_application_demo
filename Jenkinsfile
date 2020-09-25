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

    }
    post {
        always {
            node(null) {
                sh '''
                    rm -r /var/lib/jenkins/sam-venv/${BUILD_TAG}
                '''
            }
        }
    }
}
