## Description
The backend was designed based on AWS Serverless model. The original intention is 
that eventually the backend application can be deployed to AWS.

## Design
The System Design and Logic Flow can be found from the visio and pdf file under docs. There might be slight changes 
compare the original flow with the final implementation. 

## Design Consideration
1. This application serves as demo purpose at the current stage and suitable to run under localhost.

2. The production version shall take into consideration for the following sub points:
    - API Authentification/Authorization with Cognito.
    - Lambda Permission to access AWS services
    - Concurrency issues for Lambda Access Relational Database
    - Load of the eventual usage eg query per second, if high load is required, read write seperation for 
    database shall be separated
    - User file upload can be processed at frontend to allow file directly upload to S3 and only send csv file's 
    S3 link to lower down the load for backend.
    - Data classification issues, for public sector data, certain data shall reside in private network. 
    - AWS WAF shall be included for production system. For more strict security requirement, third party compliance 
    approved software define firewall shall be used.
    
3. There are many other considerations can be list above, the key point is that the design shall take into consideration
of the intend of the application, if it is only used for demo purpose, a quick prototype can be implemented, however
if this system eventually will be used in production, a strict design review shall be conducted. Production design can 
follow AWS well architect framework.

## Design Alternative
Many other alternative design can be used for this demo for example:
    - Python Flask application handle Restful call with simple DB
The above proposal is not rely on Public Cloud infrastructure for production deployment.     
