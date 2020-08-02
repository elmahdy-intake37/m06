# M06
- Get most views endpoint for each user

Requirements
============

To run this sample code, you'll need to install the following libraries:
- django v3
- crosheaders (https://pypi.org/project/django-cors-headers/0.01/)
- restframework (https://www.django-rest-framework.org/api-guide/serializers/)
- drf_ysag swagger (https://drf-yasg.readthedocs.io/en/stable/)
- rest-auth (https://django-rest-auth.readthedocs.io/en/latest/)
- environ (https://pypi.org/project/django-environ/)

You can install these with the following command:
```
    pip install -r requirements.txt
```    

## Getting Started
- git clone https://github.com/elmahdy-intake37/m06.git

- move env.example to .env under m06/ dir project in root settings file
- To initialize your database,  run the from the `m06`

  `python manage.py makemigrations`

  Then run:

  `python manage.py migrate`

- Create an admin user for the Django admin by running the following:

  `python manage.py createsu`

- To loaddata from fixtures, run the following

    `python manage.py loaddata < apps/products/fixtures/product.json`
    `python manage.py loaddata < apps/products/fixtures/product2.json`


- To start the server, run the following from the `m06` directory:

  `python manage.py runserver`

- Open a browser and go to http://127.0.0.1:8000

Django Admin Access
--------

- Redirect to http://127.0.0.1:8000/admin

ENDPOINT URL  
--------

`/swagger/`

- to get all endpoints

`/api/v1/auth/register`
    - post request
#### JSON

```json
{
    "email": "string",
    "first_name": "string",
    "last_name":"string",
    "password": "8 charcter"
}
```

#### RESPONSE

```json
{
    "id":"",
    "email": "string",
    "first_name": "string",
    "last_name":"string",
    "auth_token": "string"
}
```

- In the header you will use **Token + value of token**
- **ex.** Authorization **Token cc1fe3ddcb6a3f2550d5d2957e97acbccd2a892a**

>`/api/v1/product/one/`
`/api/v1/product/two/`
- Get request

each time user will visit one of these endpoint will be counted 

`/api/v1/most_usage/`
- Get request
#### RESPONSE

```json
[{
    "id":"",
    "most_views_usage_name": "string",
    "count": "int",
},
{
    "id":"",
    "most_views_usage_name": "string",
    "count": "int",
}]
```

> return list of views visited by user oreder by count **most of usage views**

**rest of urls in swagger**
> ex. /api/v1/login/
/api/v1/changepassword/...

## Running the tests

`it will test trakc user`
run the following,
` python manage.py test apps.users.test.test_trackuser`




