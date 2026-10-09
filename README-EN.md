# Sprint_10
API testing

Task: write API auto-tests for [the educational service "Доска"](https://qa-desk.education-services.ru/{target="_blank"}).  
Imagine that there is no API documentation yet, and a manual tester has already handed you scenarios. They need to be covered with auto-tests.

## 1. Preparation
* Chrome browser is installed.
* requests library is imported.
* Studied the ability to investigate traffic using DevTools, as well as the use of a tool for debugging/sending http requests - an API client (you can use Postman)

## 2. Study of test scenarios
### User registration
You need to check: 
* Successful registration of a new user with a unique email (you must generate a new email for each registration test)
* Repeated user registration (an email that already exists in the database is used)

### User authorization
You need to check: 
* Successful authorization of a previously registered user

### Creating an ad
You need to check: 
* Successful creation of an ad in any category

### Editing an ad
You need to check: 
* Successful editing of any field of an ad
* Editing an ad created by a different user, under the token of which the editing is performed

### Deleting an ad
You need to check: 
* Successful deletion of an ad

## 3. Writing tests
IMPORTANT! All server responses to requests, request bodies, etc. must be obtained independently by investigating requests from the front end to the server.  
Tests need to be divided by topic or functionality. Logical methods should be placed in separate modules.   
**Note**: you do not need to create a separate class for each test. Add tests for one functionality in one class. All tests should be in the `test` directory. Check that the tests run.
