# REST-API-with-Flask
Learn REST APIs with Flask framework in Python

Deployed on  heroku at 
https://rest-api-with-flask-in-python.herokuapp.com

Use POSTMAN to call  different APIs provided by this app.
Set of APIs :
  
  Authentication :
    POST /auth
    POST /register
  
  CRUD operations :
    GET /items
    GET /item/<name> **(This API needs JWT token in header with key as Authorization and value as "JWT <access_token>")**
    POST /item/<name>
    PUT /item/<name>
    DEL /item/<name>

    GET /stores  
    GET /store/<<name>
    POST /store/<<name>
    DEL /store/<<name>
  
 
  
