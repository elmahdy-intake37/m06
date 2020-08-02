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