# SharepointNTLMProxyForwarder
REST Request Forwarder to Sharepoint using NTLM Authentication

The usecase is for 3rd party J2EE Application that can't use NTLM authentication to connect to Sharepoint REST API. This proxy service forwards inbound request to Sharepoint REST endpoint and authenticate using NTLM. The actual Sharepoint REST endpoint is passed in as uri:"endpoint" in the body request to the service. The service will extract the Sharepoint endpoint and makes a request on behalf and forwards the response back to the original requester.

Request

POST 
https://localhost:8080/api/v1/splists

HEADER
Accept:application/json
Content-Type:application/x-www-form-urlencoded

BODY 
uri:https://XXXX/sites/_api/Web/Lists(guid'XXXXX')/Items/?$select=*

