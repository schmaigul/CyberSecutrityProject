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
 

## Vulnerability 1: SQL injection.

LINK: https://github.com/schmaigul/CyberSecutrityProject/blob/31a5ba5efa58f9d88afe9b8d4bc72f891a3f022a/securityproject/application/views.py#L27

LINK: https://github.com/schmaigul/CyberSecutrityProject/blob/31a5ba5efa58f9d88afe9b8d4bc72f891a3f022a/securityproject/application/templates/application/index.html#L25

The database query is done by raw sql and finds the orders by the name, not by the primary key as it should. This allows user to name their product name as an SQL injection, setting all the users orders as 'Delivered' when they press 'Set Delivered'-button. The user is able to manipulate the SQL statement to choose all orders in the table, setting order status of all orders as 'Delivered'

The vulnerability is fixed by passing the order id to the server, which then sets the order status by by finding the corresponging user id, making sure that no more than one order is changed.

- Send an order named `` 'or''=' `` to your or someone elses' account
- Send another order to the same account with some other regular name
- Set the order delivered
- All the other orders to the user are also set delivered!


