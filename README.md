# device_api

## Description:
This framework supports automation testing of APIs. 
Object Oriented Principles are used to make the code more readable, maintainable, and reusable. 
Test reports are being generated using nose-html-reporting module. 

## Pre-Requisites:
1. Python
2. requests module (pip install requests)
3. jsonpath module (pip install jsonpath)
4. nose module(pip install nose)
5. nose-html-reporting module (pip install nose-html-reporting)
6. pathlib module (pip install pathlib)
7. parameterized module (pip install parameterized)
8. PyCharm or any other desired IDE

## Test Coverage:

Automated test cases related to device APIs.
1. Verify user should be able to connect devices using POST API.
2. Verify user should not be able to send connect POST API as GET request.
3. Verify POST API should return success as False for invalid ip.
4. Verify user should be able to connect one device at a time.
5. Verify user should be able to validate device state.
6. Verify success status is False when no device is connected.
7. Verify user should be able to disconnect devices.
8. Verify GET request to get all devices.
9. Verify GET request path.
10. Verify user should be able to update device properties [with key='name', value='automation'].
11. Verify user should be able to update device properties [with key='color', value='#9FE2BF'].
12. Verify user should be able to update device properties [with key='brightness', value='5.0'].
13. Verify user should be able to update device properties.

## How to Execute:

1. Clone project.
    > git clone https://github.com/anujkumar21/device_api.git

2. Please run below command to execute specific API test cases from project directory:
	> `nosetests -s -v --nologcapture --with-html --html-report=test_report.html testcases\<testcase file>`
    
    > e.g.:

	> `nosetests -s -v --nologcapture --with-html --html-report=test_report.html testcases\test_connect_devices.py`

3. Please run below command to execute all test cases from project directory:
	> `nosetests -s -v --nologcapture --with-html --html-report=test_report.html testcases`


## Report Snapshot:
![Report Snapshot](https://github.com/anujkumar21/device_api/blob/master/Report_Snapshot.png)


## Bugs Found:
1. User is unable to update brightness=10.
2. Brightness of device does not persistent over connect/disconnect events.

## Other testing techniques for such kind of app:

Best practice for validating such applications.

1. Unit Testing: Should have unit test for each module which helps to find bugs at early stage. 
Majorly done by developers. Quality team should also help in building good unit test case coverage.
The earlier the bug found, the easier would be the bug fix. 

2. Integration Testing: Is performed to verify that different modules can work properly together as per the required functionality. 
It can be either integration of API or UI tests, or even both.

3. UI Testing: UI test validates that the user interface of application works correctly. 
User input should trigger the right actions, data should be presented to the user, the UI state should change as expected.
 