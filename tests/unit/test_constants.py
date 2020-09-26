SUCCESS_MSG_RESPONSE = "File uploaded successfully"
FAIL_VALIDATION_FAIL = "File Validation Failed"
HTTP_SUCCESS_STATUS = 200
HTTP_FAIL_STATUS = 400


BINARY_VALID_TEST_CASE_1 = "LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTYwODgxMzA1MDI1MjM5NzM3NDI4NDE0MA0KQ29udGVudC1EaXNw" \
                          "b3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJ0ZXN0X2tleSINCg0KdGVzdF9rZXlfdmFsdWUNCi0tLS0tLS0tLS0tL" \
                          "S0tLS0tLS0tLS0tLS0tLS02MDg4MTMwNTAyNTIzOTczNzQyODQxNDANCkNvbnRlbnQtRGlzcG9zaXRpb246IGZvc" \
                          "m0tZGF0YTsgbmFtZT0iZmlsZSI7IGZpbGVuYW1lPSJ2YWxpZF90ZXN0X2Nhc2UxLmNzdiINCkNvbnRlbnQtVHlwZ" \
                          "TogdGV4dC9jc3YNCg0KSGVhZGluZyBJbmZvcm1hdGlvbiwsLAplMDAwMSxocG90dGVyMSxocG90dGVyMSBQb3R0Z" \
                          "XIsMTIzNC4wMAplMDAwMixocG90dGVyMixocG90dGVyMiBXZWFzbGV5LDE5MjM0LjUwCmUwMDAzLGhwb3R0ZXIzL" \
                          "Ghwb3R0ZXIzIFNuYXBlLDQwMDAuMAplMDAwNCxocG90dGVyNCxocG90dGVyNCBQb3R0ZXIsMzk5OS45OTkKZTAwM" \
                          "DUsaHBvdHRlcjUsaHBvdHRlcjUgUG90dGVyLDUyMy40CmUwMDA2LGhwb3R0ZXI2LGhwb3R0ZXI2IFdlYXNsZXksN" \
                          "DAwMC4wMDQKZTAwMDcsaHBvdHRlcjcsaHBvdHRlcjcgU25hcGUsMC4wCmUwMDA4LGhwb3R0ZXI4LGhwb3R0ZXI4I" \
                          "FBvdHRlciwzNC4yMwojZTAwMDEwLGhwb3R0ZXIxMCwxaHBvdHRlcgplMDAwOSxocG90dGVyOSxocG90dGVyOSBQb" \
                          "3R0ZXIsMzQyMzQuNQplMDAwMTAsaHBvdHRlcjEwLGhwb3R0ZXIxMCBQb3R0ZXIsMTM0MjM0LjUKDQotLS0tLS0tL" \
                          "S0tLS0tLS0tLS0tLS0tLS0tLS0tNjA4ODEzMDUwMjUyMzk3Mzc0Mjg0MTQwLS0NCg=="

TEST_CASE_TEMPLATE = {
        "body": None,
        "resource": "/{proxy+}",
        "path": "/path/to/resource",
        "httpMethod": "POST",
        "isBase64Encoded": False,
        "queryStringParameters": {
            "foo": "bar"
        },
        "pathParameters": {
            "proxy": "/path/to/resource"
        },
        "stageVariables": {
            "baz": "qux"
        },
        "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "en-US,en;q=0.8",
            "Cache-Control": "max-age=0",
            "CloudFront-Forwarded-Proto": "https",
            "CloudFront-Is-Desktop-Viewer": "true",
            "CloudFront-Is-Mobile-Viewer": "false",
            "CloudFront-Is-SmartTV-Viewer": "false",
            "CloudFront-Is-Tablet-Viewer": "false",
            "CloudFront-Viewer-Country": "US",
            "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Custom User Agent String",
            "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
            "X-Amz-Cf-Id": "cDehVQoZnx43VYQb9j2-nvCh-9z396Uhbp027Y2JvkCPNLmGJHqlaA==",
            "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
            "X-Forwarded-Port": "443",
            "X-Forwarded-Proto": "https"
        },
        "requestContext": {
            "accountId": "123456789012",
            "resourceId": "123456",
            "stage": "prod",
            "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
            "requestTime": "09/Apr/2015:12:34:56 +0000",
            "requestTimeEpoch": 1428582896000,
            "identity": {
                "cognitoIdentityPoolId": None,
                "accountId": None,
                "cognitoIdentityId": None,
                "caller": None,
                "accessKey": None,
                "sourceIp": "127.0.0.1",
                "cognitoAuthenticationType": None,
                "cognitoAuthenticationProvider": None,
                "userArn": None,
                "userAgent": "Custom User Agent String",
                "user": None
            },
            "path": "/prod/path/to/resource",
            "resourcePath": "/{proxy+}",
            "httpMethod": "POST",
            "apiId": "1234567890",
            "protocol": "HTTP/1.1"
        }
    }