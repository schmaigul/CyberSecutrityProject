# Cyber Security mooc project

## Project description

This is a highly unsecure web postal service web application. The main functionality is to let registered users send orders to other users on the platform. Recipient of the order is able to mark delivered orders, and after remove the orders from the database. 

There are 5 security laws listed by 2021 top-10 (OWASP)[https://owasp.org/www-project-top-ten/] list.

## How to run

1. Clone the directory
2. Make a virtual environment
3. Install required packages by running: ``pip install -r requirements.txt``
4. Run the server: ``python manage.py runserver``

There are two premade users:

- ``username: schmaigul``
``password: 123``

- ``username: pekkamartinoja``
``password: squarepants``
 

### Vulnerability 1: SQL injection.

- Send an order named `` 'or''=' `` to your or someone elses' account
- Send another order to the same account with some other regular name
- Set the order delivered
- All the other orders to the user are also set delivered!


