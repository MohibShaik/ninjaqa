Feature: To perform api testing
Background: 
Given read the base url 
Scenario: GET request example
	Given Set GET_api_endpoint as /api/users/2
  When Set HEADER param request content type as "application/json"
	And Set HEADER param response accept type as "application/json" 
	And Set Query param as "empty"
	And Raise "GET" HTTP request
  Then Valid HTTP response should be received
	And Response http code should be 200 
