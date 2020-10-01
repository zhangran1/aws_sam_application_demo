SUCCESS_MSG_RESPONSE = "File uploaded successfully"
FAIL_VALIDATION_FAIL = "File Validation Failed"
HTTP_SUCCESS_STATUS = 200
HTTP_FAIL_STATUS = 400
EXISTING_EMPLOYEE = "test00001"
NONE_EXIST_EMPLOYEE = "ZR"
DB_SUCCESS_OPERATION = "OK"
DB_FAILED_OPERATION = "Failed"
SAMPLE_LOCK_ID = "228b27e3-2a74-4849-9eba"
INVALID_BODY_INPUT = "Invalid json payload"
INVALID_OPERATION_INPUT = "Employee exist cannot create"
VALID_CR_DB_OPERATION = "Successfully Update DB"
USER_DOES_NOT_EXIST_CANNOT_PATCH = "Patch failed"

VALID_REQUIRED_PARAMS = {'minSalary': '0', 'maxSalary': '4000', 'offset': '0', 'limit': '30', 'sort': '-name'}

INVALID_REQUIRED_PARAMS = {'minSalary': '0', 'offset': '0', 'limit': '30', 'sort': '-name'}

INVALID_REQUIRED_PARAMS_NEGATIVE_MIN_SALARY = {'minSalary': '-100', 'maxSalary': '4000',
                                               'offset': '0', 'limit': '30', 'sort': '-name'}
INVALID_REQUIRED_PARAMS_NEGATIVE_SALARY = {'minSalary': '0', 'maxSalary': '-4000',
                                           'offset': '0', 'limit': '30', 'sort': '-name'}
INVALID_REQUIRED_PARAMS_OFFSET = {'minSalary': '0', 'maxSalary': '-4000',
                                  'offset': '-10', 'limit': '30', 'sort': '-name'}
INVALID_REQUIRED_PARAMS_LIMIT = {'minSalary': '0', 'maxSalary': '4000',
                                 'offset': '0', 'limit': '-1', 'sort': '-name'}
INVALID_REQUIRED_PARAMS_SORT_SIGN = {'minSalary': '0', 'maxSalary': '4000',
                                     'offset': '0', 'limit': '30', 'sort': 'name'}

INVALID_REQUIRED_PARAMS_SORT_VALUE_CASE_1 = {'minSalary': '0', 'maxSalary': '4000',
                                             'offset': '0', 'limit': '30', 'sort': '+'}

INVALID_REQUIRED_PARAMS_SORT_VALUE_CASE_2 = {'minSalary': '0', 'maxSalary': '4000',
                                             'offset': '0', 'limit': '30', 'sort': '+time'}

VALID_REQUIRED_PARAMS_ASC_NAME = {'minSalary': '0', 'maxSalary': '4000', 'offset': '1', 'limit': '2', 'sort': '+name'}
VALID_REQUIRED_PARAMS_DESC_SALARY = {'minSalary': '0', 'maxSalary': '4000', 'offset': '1', 'limit': '2',
                                     'sort': '-salary'}
VALID_REQUIRED_PARAMS_ASC_EMPLOYEE_ID = {'minSalary': '0', 'maxSalary': '4000', 'offset': '1', 'limit': '2',
                                         'sort': '+id'}
VALID_REQUIRED_PARAMS_DESC_LOGIN = {'minSalary': '0', 'maxSalary': '4000', 'offset': '1', 'limit': '2',
                                    'sort': '-login'}

VALID_REQUIRED_PARAMS_ASC_NAME_RECORD = [{'id': 'test000012', 'login': 'adam2', 'name': 'Adam2', 'salary': '1002.5'},
                                         {'id': 'test000013', 'login': 'adam3', 'name': 'Adam3', 'salary': '1003.5'}]

VALID_REQUIRED_PARAMS_DESC_SALARY_RECORD = [
    {"id": "e0001", "login": "hpotter1", "name": "hpotter1 Potter", "salary": "1234.00"},
    {"id": "test000014", "login": "adam4", "name": "Adam4", "salary": "1004.5"}]

VALID_REQUIRED_PARAMS_ASC_EMPLOYEE_ID_RECORD = [{'id': 'e00011', 'login': '用户1', 'name': '用户名1', 'salary': '40'},
                                                {'id': 'e00012', 'login': '用户2', 'name': '用户名2', 'salary': '50'}]

VALID_REQUIRED_PARAMS_DESC_LOGIN_RECORD = [{'id': 'e00011', 'login': '用户1', 'name': '用户名1', 'salary': '40'},
                                           {'id': 'test00009', 'login': 'john9', 'name': 'John Smith9',
                                            'salary': '109.5'}]
GET_ID_BY_USER_RESPONSE = {'id': 'test00001', 'name': 'John Smith', 'login': 'john1', 'salary': '101.5'}

BINARY_VALID_TEST_CASE_1 = "LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTk5NDUwNzIzMzc2MDY1MDM4OTYwNzkyNg0KQ29udGVudC1EaXN" \
                           "wb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJmaWxlIjsgZmlsZW5hbWU9InZhbGlkX3Rlc3RfY2FzZTFfd2l0aF" \
                           "9oYXNoLmNzdiINCkNvbnRlbnQtVHlwZTogdGV4dC9jc3YNCg0KSGVhZGluZyBJbmZvcm1hdGlvbiwsLAplMDAwM" \
                           "SxocG90dGVyMSxocG90dGVyMSBQb3R0ZXIsMTIzNC4wMAplMDAwMixocG90dGVyMixocG90dGVyMiBXZWFzbGV5" \
                           "LDE5MjM0LjUwCmUwMDAzLGhwb3R0ZXIzLGhwb3R0ZXIzIFNuYXBlLDQwMDAuMAplMDAwNCxocG90dGVyNCxocG90" \
                           "dGVyNCBQb3R0ZXIsMzk5OS45OTkKZTAwMDUsaHBvdHRlcjUsaHBvdHRlcjUgUG90dGVyLDUyMy40CmUwMDA2LGhw" \
                           "b3R0ZXI2LGhwb3R0ZXI2IFdlYXNsZXksNDAwMC4wMDQKZTAwMDcsaHBvdHRlcjcsaHBvdHRlcjcgU25hcGUsMC4w" \
                           "CmUwMDA4LGhwb3R0ZXI4LGhwb3R0ZXI4IFBvdHRlciwzNC4yMwojZTAwMDEwLGhwb3R0ZXIxMCwxaHBvdHRlcgpl" \
                           "MDAwOSxocG90dGVyOSxocG90dGVyOSBQb3R0ZXIsMzQyMzQuNQplMDAwMTAsaHBvdHRlcjEwLGhwb3R0ZXIxMCBQ" \
                           "b3R0ZXIsMTM0MjM0LjUNCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS05OTQ1MDcyMzM3NjA2NTAzODk2MDc5M" \
                           "jYtLQ0K"

BINARY_VALID_TEST_CASE_2 = "LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTQwMTAxOTQ5NjE4Mjk5ODk0ODk5MzU5Ng0KQ29udGVudC1EaXN" \
                           "wb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJmaWxlIjsgZmlsZW5hbWU9InZhbGlkX3Rlc3RfY2FzZTJfd2l0aF" \
                           "9jaGluZXNlX2NoYXJhY3Rlci5jc3YiDQpDb250ZW50LVR5cGU6IHRleHQvY3N2DQoNCkhlYWRpbmcgSW5mb3JtYX" \
                           "Rpb24sLCwNCmUwMDAxLGhwb3R0ZXIxLGhwb3R0ZXIxIFBvdHRlciwxMjM0LjAwDQplMDAwMixocG90dGVyMixocG" \
                           "90dGVyMiBXZWFzbGV5LDE5MjM0LjUwDQplMDAwMyxocG90dGVyMyxocG90dGVyMyBTbmFwZSw0MDAwLjANCmUwMD" \
                           "A0LGhwb3R0ZXI0LGhwb3R0ZXI0IFBvdHRlciwzOTk5Ljk5OQ0KZTAwMDUsaHBvdHRlcjUsaHBvdHRlcjUgUG90dG" \
                           "VyLDUyMy40DQplMDAwNixocG90dGVyNixocG90dGVyNiBXZWFzbGV5LDQwMDAuMDA0DQplMDAwNyxocG90dGVyNy" \
                           "xocG90dGVyNyBTbmFwZSwwLjANCmUwMDA4LGhwb3R0ZXI4LGhwb3R0ZXI4IFBvdHRlciwzNC4yMw0KZTAwMDksaH" \
                           "BvdHRlcjksaHBvdHRlcjkgUG90dGVyLDM0MjM0LjUNCmUwMDAxMCxocG90dGVyMTAsaHBvdHRlcjEwIFBvdHRlci" \
                           "wxMzQyMzQuNQ0KZTAwMDExLOeUqOaItzEs55So5oi35ZCNMSw0MA0KZTAwMDEyLOeUqOaItzIs55So5oi35ZCNMi" \
                           "w1MA0KLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTQwMTAxOTQ5NjE4Mjk5ODk0ODk5MzU5Ni0tDQo="

BINARY_VALID_TEST_CASE_3 = "LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTk1MzQ4NDczNzc0NjYyMTkxODY4NzAyNA0KQ29udGVudC1EaXN" \
                           "wb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJmaWxlIjsgZmlsZW5hbWU9InZhbGlkX3Rlc3RfY2FzZTNfd2l0aF" \
                           "9sYXN0X2xpbmVfZW1wdHkuY3N2Ig0KQ29udGVudC1UeXBlOiB0ZXh0L2Nzdg0KDQpIZWFkaW5nIEluZm9ybWF0a" \
                           "W9uLCwsCmUwMDAxLGhwb3R0ZXIxLGhwb3R0ZXIxIFBvdHRlciwxMjM0LjAwCmUwMDAyLGhwb3R0ZXIyLGhwb3R0" \
                           "ZXIyIFdlYXNsZXksMTkyMzQuNTAKZTAwMDMsaHBvdHRlcjMsaHBvdHRlcjMgU25hcGUsNDAwMC4wCmUwMDA0LG" \
                           "hwb3R0ZXI0LGhwb3R0ZXI0IFBvdHRlciwzOTk5Ljk5OQplMDAwNSxocG90dGVyNSxocG90dGVyNSBQb3R0ZXIs" \
                           "NTIzLjQKZTAwMDYsaHBvdHRlcjYsaHBvdHRlcjYgV2Vhc2xleSw0MDAwLjAwNAplMDAwNyxocG90dGVyNyxocG" \
                           "90dGVyNyBTbmFwZSwwLjAKZTAwMDgsaHBvdHRlcjgsaHBvdHRlcjggUG90dGVyLDM0LjIzCiNlMDAwMTAsaHB" \
                           "vdHRlcjEwLDFocG90dGVyCmUwMDA5LGhwb3R0ZXI5LGhwb3R0ZXI5IFBvdHRlciwzNDIzNC41CmUwMDAxMCxo" \
                           "cG90dGVyMTAsaHBvdHRlcjEwIFBvdHRlciwxMzQyMzQuNQoNCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tL" \
                           "S05NTM0ODQ3Mzc3NDY2MjE5MTg2ODcwMjQtLQ0K"

BINARY_INVALID_TEST_CASE_1 = "LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTQ4MzQyMTg0NjQxNzE1NzQ5ODEwMTgzNw0KQ29udGVudC1Ea" \
                             "XNwb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJmaWxlIjsgZmlsZW5hbWU9ImludmFsaWRfdGVzdF9jYXNlMV9" \
                             "leHRyYV9vbmVfY29sdW1uX3JlY29yZC5jc3YiDQpDb250ZW50LVR5cGU6IHRleHQvY3N2DQoNCkhlYWRpbmcgS" \
                             "W5mb3JtYXRpb24sLCwNCmUwMDAxLGhwb3R0ZXIxLGhwb3R0ZXIxIFBvdHRlciwxMjM0LjAwDQplMDAwMixocG9" \
                             "0dGVyMixocG90dGVyMiBXZWFzbGV5LDE5MjM0LjUwDQplMDAwMyxocG90dGVyMyxocG90dGVyMyBTbmFwZSw0M" \
                             "DAwLjANCmUwMDA0LGhwb3R0ZXI0LGhwb3R0ZXI0IFBvdHRlciw0MDAwLjAsIDYwMDANCmUwMDA1LGhwb3R0ZXI" \
                             "1LGhwb3R0ZXI1IFBvdHRlciw1MjMuNA0KZTAwMDYsaHBvdHRlcjYsaHBvdHRlcjYgV2Vhc2xleSw0MDAwLjAwN" \
                             "A0KZTAwMDcsaHBvdHRlcjcsaHBvdHRlcjcgU25hcGUsMC4wDQplMDAwOCxocG90dGVyOCxocG90dGVyOCBQb3R" \
                             "0ZXIsMzQuMjMNCmUwMDA5LGhwb3R0ZXI5LGhwb3R0ZXI5IFBvdHRlciwzNDIzNC41DQplMDAwMTAsaHBvdHRlc" \
                             "jEwLGhwb3R0ZXIxMCBQb3R0ZXIsMTM0MjM0LjUNCmUwMDAxMSxocG90dGVyMTEsaHBvdHRlcjExIFBvdHRlciw" \
                             "0MA0KZTAwMDEyLGhwb3R0ZXIxMixocG90dGVyMTIgUG90dGVyLDUwDQotLS0tLS0tLS0tLS0tLS0tLS0tLS0tL" \
                             "S0tLS0tNDgzNDIxODQ2NDE3MTU3NDk4MTAxODM3LS0NCg=="

BINARY_INVALID_TEST_CASE_2 = "LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTc0NzE5NjQ2NTA0NjgxODY1ODQzMTI2OA0KQ29udGVudC1Ea" \
                             "XNwb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJmaWxlIjsgZmlsZW5hbWU9ImludmFsaWRfdGVzdF9jYXNlMl" \
                             "9taXNzaW5nX29uZV9jb2x1bW5fcmVjb3JkLmNzdiINCkNvbnRlbnQtVHlwZTogdGV4dC9jc3YNCg0KSGVhZGl" \
                             "uZyBJbmZvcm1hdGlvbiwsLA0KZTAwMDEsaHBvdHRlcjEsaHBvdHRlcjEgUG90dGVyLDEyMzQuMDANCmUwMDAyL" \
                             "Ghwb3R0ZXIyLGhwb3R0ZXIyIFdlYXNsZXksMTkyMzQuNTANCmUwMDAzLGhwb3R0ZXIzLGhwb3R0ZXIzIFNuYXB" \
                             "lLDQwMDAuMA0KZTAwMDQsaHBvdHRlcjQsaHBvdHRlcjQgUG90dGVyDQplMDAwNSxocG90dGVyNSxocG90dGVyNS" \
                             "BQb3R0ZXIsNTIzLjQNCmUwMDA2LGhwb3R0ZXI2LGhwb3R0ZXI2IFdlYXNsZXksNDAwMC4wMDQNCmUwMDA3LGhwb" \
                             "3R0ZXI3LGhwb3R0ZXI3IFNuYXBlLDAuMA0KZTAwMDgsaHBvdHRlcjgsaHBvdHRlcjggUG90dGVyLDM0LjIzDQpl" \
                             "MDAwOSxocG90dGVyOSxocG90dGVyOSBQb3R0ZXIsMzQyMzQuNQ0KZTAwMDEwLGhwb3R0ZXIxMCxocG90dGVyMT" \
                             "AgUG90dGVyLDEzNDIzNC41DQplMDAwMTEsaHBvdHRlcjExLGhwb3R0ZXIxMSBQb3R0ZXIsNDANCmUwMDAxMixo" \
                             "cG90dGVyMTIsaHBvdHRlcjEyIFBvdHRlciw1MA0KLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTc0NzE5Nj" \
                             "Q2NTA0NjgxODY1ODQzMTI2OC0tDQo="

BINARY_INVALID_TEST_CASE_3 = "LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTY4NjIyMDEyOTM1NTM1MDIzOTY0MjMzNA0KQ29udGVudC1Ea" \
                             "XNwb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJmaWxlIjsgZmlsZW5hbWU9ImludmFsaWRfdGVzdF9jYXNlM19" \
                             "pbnZhbGlkX3NhbGFyeS5jc3YiDQpDb250ZW50LVR5cGU6IHRleHQvY3N2DQoNCkhlYWRpbmcgSW5mb3JtYXRpb" \
                             "24sLCwNCmUwMDAxLGhwb3R0ZXIxLGhwb3R0ZXIxIFBvdHRlciwxMjM0LjAwDQplMDAwMixocG90dGVyMixocG9" \
                             "0dGVyMiBXZWFzbGV5LDE5MjM0LjUwDQplMDAwMyxocG90dGVyMyxocG90dGVyMyBTbmFwZSw0MDAwLjANCmUwM" \
                             "DA0LGhwb3R0ZXI0LGhwb3R0ZXI0IFBvdHRlciwzOSA5OS45OTkNCmUwMDA1LGhwb3R0ZXI1LGhwb3R0ZXI1IFB" \
                             "vdHRlciw1MjMuNA0KZTAwMDYsaHBvdHRlcjYsaHBvdHRlcjYgV2Vhc2xleSw0MDAwLjAwNA0KZTAwMDcsaHBvd" \
                             "HRlcjcsaHBvdHRlcjcgU25hcGUsMC4wDQplMDAwOCxocG90dGVyOCxocG90dGVyOCBQb3R0ZXIsMzQuMjMNCmU" \
                             "wMDA5LGhwb3R0ZXI5LGhwb3R0ZXI5IFBvdHRlciwzNDIzNC41DQplMDAwMTAsaHBvdHRlcjEwLGhwb3R0ZXIxMC" \
                             "BQb3R0ZXIsMTM0MjM0LjUNCmUwMDAxMSxocG90dGVyMTEsaHBvdHRlcjExIFBvdHRlciw0MA0KZTAwMDEyLGhwb" \
                             "3R0ZXIxMixocG90dGVyMTIgUG90dGVyLDUwDQotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tNjg2MjIwMTI5" \
                             "MzU1MzUwMjM5NjQyMzM0LS0NCg=="

BINARY_INVALID_TEST_CASE_4 = "LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTE5MzU5OTA5NjM5MTAyMDQyMzE3MjcyNg0KQ29udGVudC1E" \
                             "aXNwb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJmaWxlIjsgZmlsZW5hbWU9ImludmFsaWRfdGVzdF9jYXNl" \
                             "NF9uZWdhdGl2ZV9zYWxhcnkuY3N2Ig0KQ29udGVudC1UeXBlOiB0ZXh0L2Nzdg0KDQpIZWFkaW5nIEluZm9y" \
                             "bWF0aW9uLCwsDQplMDAwMSxocG90dGVyMSxocG90dGVyMSBQb3R0ZXIsMTIzNC4wMA0KZTAwMDIsaHBvdHRl" \
                             "cjIsaHBvdHRlcjIgV2Vhc2xleSwxOTIzNC41MA0KZTAwMDMsaHBvdHRlcjMsaHBvdHRlcjMgU25hcGUsNDAw" \
                             "MC4wDQplMDAwNCxocG90dGVyNCxocG90dGVyNCBQb3R0ZXIsLTM5OTkuOTk5DQplMDAwNSxocG90dGVyNSxo" \
                             "cG90dGVyNSBQb3R0ZXIsNTIzLjQNCmUwMDA2LGhwb3R0ZXI2LGhwb3R0ZXI2IFdlYXNsZXksNDAwMC4wMDQN" \
                             "CmUwMDA3LGhwb3R0ZXI3LGhwb3R0ZXI3IFNuYXBlLDAuMA0KZTAwMDgsaHBvdHRlcjgsaHBvdHRlcjggUG90" \
                             "dGVyLDM0LjIzDQplMDAwOSxocG90dGVyOSxocG90dGVyOSBQb3R0ZXIsMzQyMzQuNQ0KZTAwMDEwLGhwb3R0Z" \
                             "XIxMCxocG90dGVyMTAgUG90dGVyLDEzNDIzNC41DQplMDAwMTEsaHBvdHRlcjExLGhwb3R0ZXIxMSBQb3R0Z" \
                             "XIsNDANCmUwMDAxMixocG90dGVyMTIsaHBvdHRlcjEyIFBvdHRlciw1MA0KLS0tLS0tLS0tLS0tLS0tLS0tL" \
                             "S0tLS0tLS0tLTE5MzU5OTA5NjM5MTAyMDQyMzE3MjcyNi0tDQo="

BINARY_INVALID_DUPLICATE_ID = "LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTk1MDkzNjA2NzAzNDQ4MDYzMTE2MjYxNA0KQ29udGVudC1" \
                              "EaXNwb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJmaWxlIjsgZmlsZW5hbWU9ImludmFsaWRfdGVzdF9jYXN" \
                              "lX2R1cGxpY2F0ZV9pZF9sb2dpbi5jc3YiDQpDb250ZW50LVR5cGU6IHRleHQvY3N2DQoNCkhlYWRpbmcgSW5m" \
                              "b3JtYXRpb24sLCwKZTAwMDEsaHBvdHRlcjEsaHBvdHRlcjEgUG90dGVyLDEyMzQuMDAKZTAwMDIsaHBvdHRlc" \
                              "jIsaHBvdHRlcjIgV2Vhc2xleSwxOTIzNC41MAplMDAwMyxocG90dGVyMyxocG90dGVyMyBTbmFwZSw0MDAwLj" \
                              "AKZTAwMDQsaHBvdHRlcjQsaHBvdHRlcjQgUG90dGVyLDM5OTkuOTk5CmUwMDA1LGhwb3R0ZXI1LGhwb3R0ZXI" \
                              "1IFBvdHRlciw1MjMuNAplMDAwNixocG90dGVyNixocG90dGVyNiBXZWFzbGV5LDQwMDAuMDA0CmUwMDA3LGhwb" \
                              "3R0ZXI3LGhwb3R0ZXI3IFNuYXBlLDAuMAplMDAwOCxocG90dGVyOCxocG90dGVyOCBQb3R0ZXIsMzQuMjMKZTA" \
                              "wMDMsaHBvdHRlcjMsZHVwbGljYXRlIHJlY29yZCwzNC4yMwojZTAwMDEwLGhwb3R0ZXIxMCwxaHBvdHRlcgplM" \
                              "DAwOSxocG90dGVyOSxocG90dGVyOSBQb3R0ZXIsMzQyMzQuNQplMDAwMTAsaHBvdHRlcjEwLGhwb3R0ZXIxMCB" \
                              "Qb3R0ZXIsMTM0MjM0LjUKDQotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tOTUwOTM2MDY3MDM0NDgwNjMx" \
                              "MTYyNjE0LS0NCg=="

BINARY_INVALID_EMPTY_FILE = "LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTA1NDg5NTU4NTgzMzg2OTkxODY3NjA5Mg0KQ29udGVudC1E" \
                            "aXNwb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJmaWxlIjsgZmlsZW5hbWU9ImludmFsaWRfdGVzdF9lbXB0e" \
                            "V9maWxlLmNzdiINCkNvbnRlbnQtVHlwZTogdGV4dC9jc3YNCg0KDQotLS0tLS0tLS0tLS0tLS0tLS0tLS0tL" \
                            "S0tLS0tMDU0ODk1NTg1ODMzODY5OTE4Njc2MDkyLS0NCg=="

VALID_PROCESSED_DATA_TEST_CASE_1 = ['Content-Disposition: form-data; name="file"; '
                                    'filename="valid_test_case1_with_hash.csv"'
                                    '\r\nContent-Type: text/csv\r\n\r'
                                    '\nHeading Information,,,'
                                    '\ne0001,hpotter1,hpotter1 Potter,1234.00'
                                    '\ne0002,hpotter2,hpotter2 Weasley,19234.50'
                                    '\ne0003,hpotter3,hpotter3 Snape,4000.0'
                                    '\ne0004,hpotter4,hpotter4 Potter,3999.999'
                                    '\ne0005,hpotter5,hpotter5 Potter,523.4'
                                    '\ne0006,hpotter6,hpotter6 Weasley,4000.004'
                                    '\ne0007,hpotter7,hpotter7 Snape,0.0'
                                    '\ne0008,hpotter8,hpotter8 Potter,34.23'
                                    '\n#e00010,hpotter10,1hpotter'
                                    '\ne0009,hpotter9,hpotter9 Potter,34234.5'
                                    '\ne00010,hpotter10,hpotter10 Potter,134234.5\r\n', '--\r\n']

VALID_PROCESSED_DATA_TEST_CASE_2 = ['Content-Disposition: form-data; name="file"; '
                                    'filename="valid_test_case2_with_chinese_character.csv"'
                                    '\r\nContent-Type: text/csv\r\n\r'
                                    '\nHeading Information,,,\r'
                                    '\ne0001,hpotter1,hpotter1 Potter,1234.00\r'
                                    '\ne0002,hpotter2,hpotter2 Weasley,19234.50\r'
                                    '\ne0003,hpotter3,hpotter3 Snape,4000.0\r'
                                    '\ne0004,hpotter4,hpotter4 Potter,3999.999\r'
                                    '\ne0005,hpotter5,hpotter5 Potter,523.4\r'
                                    '\ne0006,hpotter6,hpotter6 Weasley,4000.004\r'
                                    '\ne0007,hpotter7,hpotter7 Snape,0.0\r'
                                    '\ne0008,hpotter8,hpotter8 Potter,34.23\r'
                                    '\ne0009,hpotter9,hpotter9 Potter,34234.5\r'
                                    '\ne00010,hpotter10,hpotter10 Potter,134234.5\r'
                                    '\ne00011,用户1,用户名1,40\r\ne00012,用户2,用户名2,50\r\n', '--\r\n']

VALID_PROCESSED_DATA_TEST_CASE_3 = ['Content-Disposition: form-data; name="file"; '
                                    'filename="valid_test_case3_with_last_line_empty.csv"'
                                    '\r\nContent-Type: text/csv\r\n\r'
                                    '\nHeading Information,,,'
                                    '\ne0001,hpotter1,hpotter1 Potter,1234.00'
                                    '\ne0002,hpotter2,hpotter2 Weasley,19234.50'
                                    '\ne0003,hpotter3,hpotter3 Snape,4000.0'
                                    '\ne0004,hpotter4,hpotter4 Potter,3999.999'
                                    '\ne0005,hpotter5,hpotter5 Potter,523.4'
                                    '\ne0006,hpotter6,hpotter6 Weasley,4000.004'
                                    '\ne0007,hpotter7,hpotter7 Snape,0.0'
                                    '\ne0008,hpotter8,hpotter8 Potter,34.23'
                                    '\n#e00010,hpotter10,1hpotter'
                                    '\ne0009,hpotter9,hpotter9 Potter,34234.5'
                                    '\ne00010,hpotter10,hpotter10 Potter,134234.5\n\r\n', '--\r\n']

INVALID_PROCESSED_DATA_TEST_CASE_1 = ['Content-Disposition: form-data; name="file"; '
                                      'filename="invalid_test_case1_extra_one_column_record.csv"\r'
                                      '\nContent-Type: text/csv\r\n\r'
                                      '\nHeading Information,,,\r'
                                      '\ne0001,hpotter1,hpotter1 Potter,1234.00\r'
                                      '\ne0002,hpotter2,hpotter2 Weasley,19234.50\r'
                                      '\ne0003,hpotter3,hpotter3 Snape,4000.0\r'
                                      '\ne0004,hpotter4,hpotter4 Potter,4000.0, 6000\r'
                                      '\ne0005,hpotter5,hpotter5 Potter,523.4\r'
                                      '\ne0006,hpotter6,hpotter6 Weasley,4000.004\r'
                                      '\ne0007,hpotter7,hpotter7 Snape,0.0\r'
                                      '\ne0008,hpotter8,hpotter8 Potter,34.23\r'
                                      '\ne0009,hpotter9,hpotter9 Potter,34234.5\r'
                                      '\ne00010,hpotter10,hpotter10 Potter,134234.5\r'
                                      '\ne00011,hpotter11,hpotter11 Potter,40\r'
                                      '\ne00012,hpotter12,hpotter12 Potter,50\r\n', '--\r\n']

INVALID_PROCESSED_DATA_TEST_CASE_2 = ['Content-Disposition: form-data; name="file"; '
                                      'filename="invalid_test_case2_missing_one_column_record.csv"\r'
                                      '\nContent-Type: text/csv\r\n\r'
                                      '\nHeading Information,,,\r'
                                      '\ne0001,hpotter1,hpotter1 Potter,1234.00\r'
                                      '\ne0002,hpotter2,hpotter2 Weasley,19234.50\r'
                                      '\ne0003,hpotter3,hpotter3 Snape,4000.0\r'
                                      '\ne0004,hpotter4,hpotter4 Potter\r'
                                      '\ne0005,hpotter5,hpotter5 Potter,523.4\r'
                                      '\ne0006,hpotter6,hpotter6 Weasley,4000.004\r'
                                      '\ne0007,hpotter7,hpotter7 Snape,0.0\r'
                                      '\ne0008,hpotter8,hpotter8 Potter,34.23\r'
                                      '\ne0009,hpotter9,hpotter9 Potter,34234.5\r'
                                      '\ne00010,hpotter10,hpotter10 Potter,134234.5\r'
                                      '\ne00011,hpotter11,hpotter11 Potter,40\r'
                                      '\ne00012,hpotter12,hpotter12 Potter,50\r\n', '--\r\n']

INVALID_PROCESSED_DATA_TEST_CASE_3 = ['Content-Disposition: form-data; name="file"; '
                                      'filename="invalid_test_case3_invalid_salary.csv"\r'
                                      '\nContent-Type: text/csv\r\n\r'
                                      '\nHeading Information,,,\r'
                                      '\ne0001,hpotter1,hpotter1 Potter,1234.00\r'
                                      '\ne0002,hpotter2,hpotter2 Weasley,19234.50\r'
                                      '\ne0003,hpotter3,hpotter3 Snape,4000.0\r'
                                      '\ne0004,hpotter4,hpotter4 Potter,39 99.999\r'
                                      '\ne0005,hpotter5,hpotter5 Potter,523.4\r'
                                      '\ne0006,hpotter6,hpotter6 Weasley,4000.004\r'
                                      '\ne0007,hpotter7,hpotter7 Snape,0.0\r'
                                      '\ne0008,hpotter8,hpotter8 Potter,34.23\r'
                                      '\ne0009,hpotter9,hpotter9 Potter,34234.5\r'
                                      '\ne00010,hpotter10,hpotter10 Potter,134234.5\r'
                                      '\ne00011,hpotter11,hpotter11 Potter,40\r'
                                      '\ne00012,hpotter12,hpotter12 Potter,50\r\n', '--\r\n']

INVALID_PROCESSED_DATA_TEST_CASE_4 = ['Content-Disposition: form-data; name="file"; '
                                      'filename="invalid_test_case4_negative_salary.csv"\r'
                                      '\nContent-Type: text/csv\r\n\r'
                                      '\nHeading Information,,,\r'
                                      '\ne0001,hpotter1,hpotter1 Potter,1234.00\r'
                                      '\ne0002,hpotter2,hpotter2 Weasley,19234.50\r'
                                      '\ne0003,hpotter3,hpotter3 Snape,4000.0\r'
                                      '\ne0004,hpotter4,hpotter4 Potter,-3999.999\r'
                                      '\ne0005,hpotter5,hpotter5 Potter,523.4\r'
                                      '\ne0006,hpotter6,hpotter6 Weasley,4000.004\r'
                                      '\ne0007,hpotter7,hpotter7 Snape,0.0\r'
                                      '\ne0008,hpotter8,hpotter8 Potter,34.23\r'
                                      '\ne0009,hpotter9,hpotter9 Potter,34234.5\r'
                                      '\ne00010,hpotter10,hpotter10 Potter,134234.5\r'
                                      '\ne00011,hpotter11,hpotter11 Potter,40\r'
                                      '\ne00012,hpotter12,hpotter12 Potter,50\r\n', '--\r\n']

INVALID_DUPLICATE_ID_PROCESSED_DATA = ['Content-Disposition: form-data; name="file"; '
                                       'filename="invalid_test_case_duplicate_id_login.csv"\r'
                                       '\nContent-Type: text/csv\r\n\r'
                                       '\nHeading Information,,,'
                                       '\ne0001,hpotter1,hpotter1 Potter,1234.00'
                                       '\ne0002,hpotter2,hpotter2 Weasley,19234.50'
                                       '\ne0003,hpotter3,hpotter3 Snape,4000.0'
                                       '\ne0004,hpotter4,hpotter4 Potter,3999.999'
                                       '\ne0005,hpotter5,hpotter5 Potter,523.4'
                                       '\ne0006,hpotter6,hpotter6 Weasley,4000.004'
                                       '\ne0007,hpotter7,hpotter7 Snape,0.0'
                                       '\ne0008,hpotter8,hpotter8 Potter,34.23'
                                       '\ne0003,hpotter3,duplicate record,34.23'
                                       '\n#e00010,hpotter10,1hpotter'
                                       '\ne0009,hpotter9,hpotter9 Potter,34234.5'
                                       '\ne00010,hpotter10,hpotter10 Potter,134234.5\n\r\n', '--\r\n']

INVALID_EMPTY_FILE_PROCESSED_DATA = ['Content-Disposition: form-data; name="file"; '
                                     'filename="invalid_test_empty_file.csv"\r'
                                     '\nContent-Type: text/csv\r\n\r\n\r\n', '--\r\n']

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
