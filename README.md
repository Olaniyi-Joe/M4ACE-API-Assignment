# MY ASSIGNMENT
## Difference Between Django and DjangoRestFramework
Django is a framework built in Python programming language used for web development. It can be used to build full-stack web applications (i.e both frontend and backend), but its major focus is on the backend of web applications.The django web framework is an open source framework that can help developers  speed up the process of developing web applications.

Django REST Framework is a powerful and flexible open-source framework used for building RESTfulAPIs. With DjangoRSF, Django can serve as the backend and through APIs, it can be connected to other frontend frames such React, Angular, Vue etc. 

## HTTP Response Status Codes
Http response status code indicates whether a specific Http request has been completed successfully or not. 
HTTP response status codes are issued by a server in response to a client's request made to the server. Here’s a breakdown of some common status codes:

1. Informational
    100 Continue: The server has received the request headers, and the client should proceed to send the request body.
    101 Switching Protocols: The requester has asked the server to switch protocols, and the server is acknowledging that it will do so.
2. Success
    200 OK: The request has succeeded.
    201 Created: The request has been fulfilled, and a new resource has been created.
    204 No Content: The server successfully processed the request, but is not returning any content.
3. Redirection
    301 Moved Permanently: The requested resource has been assigned a new permanent URI.
    302 Found (or 307 Temporary Redirect): The requested resource resides temporarily under a different URI.
    304 Not Modified: The resource has not been modified since the last request.
    4xx: Client Errors
    400 Bad Request: The server cannot or will not process the request due to a client error.
    401 Unauthorized: Authentication is required, and it has either failed or not been provided.
    403 Forbidden: The server understood the request but refuses to authorize it.
    404 Not Found: The server cannot find the requested resource.
    405 Method Not Allowed: The request method is known by the server but has been disabled and cannot be used.
5. Server Errors
    500 Internal Server Error: The server encountered an unexpected condition that prevented it from fulfilling the request.
    502 Bad Gateway: The server received an invalid response from an inbound server.
    503 Service Unavailable: The server is currently unavailable (because it is overloaded or down for maintenance).
    504 Gateway Timeout: The server, while acting as a gateway or proxy, did not receive a timely response from an upstream server.
These codes help communicate the result of the HTTP request and are important for both client-side and server-side error handling.

## requests Methods and their Functions
    HTTP request methods are used to specify the desired action to be performed on a given resource. Here are the five primary HTTP request methods and their functions:

1. GET
    Function: Retrieves data from the server. It is the most common method, used to request data from a specified resource.
    Usage: Generally used for reading or retrieving information.
    Example: Accessing a webpage, fetching data from an API.
2. POST
    Function: Sends data to the server to create or update a resource. The data sent to the server with POST is usually included in the request body.
    Usage: Commonly used for submitting form data, uploading files, or creating new records in a database.
    Example: Submitting a form on a website, uploading a file.
3. PUT
    Function: Updates an existing resource on the server or creates a new resource if it does not exist. Like POST, data is sent in the request body.
    Usage: Used for updating or replacing an existing resource entirely.
    Example: Updating user information in a database.
4. DELETE
    Function: Deletes a specified resource from the server.
    Usage: Used to remove a resource.
    Example: Deleting a user account or a file from a server.
5. PATCH
    Function: Partially updates an existing resource on the server. Unlike PUT, which replaces the entire resource, PATCH only modifies the specified fields.
    Usage: Used when you want to apply partial updates to a resource.
    Example: Updating only the user's email address in a profile without changing other fields.
These methods are part of the HTTP protocol and are used by clients (like web browsers or applications) to communicate with servers, defining the type of operation to be performed on the server's resources.