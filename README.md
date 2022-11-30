# Cyber Security mooc project

## How to run

1. Clone the directory
2. Run ``python manage.py migrate``
3. Run ``python manage.py makemigrations``
4. Run the server: ``python manage.py runserver``

There are two premade users:

- ``username: schmaigul``
``password: 123``

- ``username: pekkamartinoja``
``password: squarepants``
 
## Project description

This is a highly insecure web postal service web application. The main functionality is to let registered users send orders to other users on the platform. Recipient of the order is able to mark delivered orders, which after they can remove the orders from the database. 

There are 5 security laws listed by 2021 top-10 (OWASP)[https://owasp.org/www-project-top-ten/] list.

## Vulnerability 1: SQL injection.

LINK: https://github.com/schmaigul/CyberSecutrityProject/blob/3e38af58dd212ae790fd36c18d050c052efe7c13/securityproject/application/views.py#L51

LINK: https://github.com/schmaigul/CyberSecutrityProject/blob/3e38af58dd212ae790fd36c18d050c052efe7c13/securityproject/application/templates/application/index.html#L27

Application that use query parameters or other unsanitized data as a part of SQL query are prone to SQL injections if the data is not handled correctly. When setting order as 'Delivered' the database query is done by raw sql which finds the orders by the name. This allows user to name their product name as an SQL-query, which allows a hacker to insert an SQL injection to cause unintended events. The user is able to manipulate the SQL statement to choose all orders in the table, setting order status of all orders as 'Delivered'

SQL injections are commonly prevented with an API that handles the queries. The vulnerability is fixed by using Django's own library to filter the orders and making sure that only one order is removed by using .first() method.

FIX: https://github.com/schmaigul/CyberSecutrityProject/blob/3e38af58dd212ae790fd36c18d050c052efe7c13/securityproject/application/views.py#L68

FIX: https://github.com/schmaigul/CyberSecutrityProject/blob/3e38af58dd212ae790fd36c18d050c052efe7c13/securityproject/application/templates/application/index.html#L29

### How to execute:

- Send an order named `` 'or''=' `` to your or someone elses' account
- Send another order to the same account with some other regular name
- Set the order delivered
- All the other orders to the user are also set delivered!

## Vulnerability 2: Insecure Design

LINK: https://github.com/schmaigul/CyberSecutrityProject/blob/3e38af58dd212ae790fd36c18d050c052efe7c13/securityproject/application/views.py#L51

LINK: https://github.com/schmaigul/CyberSecutrityProject/blob/3e38af58dd212ae790fd36c18d050c052efe7c13/securityproject/application/templates/application/index.html#L27

Database queries should aim to use primary keys in the query when working with foreign keys in many-to-one relationship. The application uses order's name to change status of an order, when it should be the primary key 'id'. If there are multiple orders with the same name, setting one as delivered sets all the other orders as delivered.

The vulnerability is fixed by passing the product id instead of the name in the html. Filtering orders by order id and verifying that the user changing the status is the recipient of the order makes action safe.

FIX: https://github.com/schmaigul/CyberSecutrityProject/blob/3e38af58dd212ae790fd36c18d050c052efe7c13/securityproject/application/views.py#L68

FIX: https://github.com/schmaigul/CyberSecutrityProject/blob/3e38af58dd212ae790fd36c18d050c052efe7c13/securityproject/application/templates/application/index.html#L29

### How to execute:

- Send two different orders with the same name
- Mark the order as delivered
- All orders with that name are set as 'Delivered'

## Vulnerability 3: Broken Access Control

LINK: https://github.com/schmaigul/CyberSecutrityProject/blob/3e38af58dd212ae790fd36c18d050c052efe7c13/securityproject/application/views.py#L82

Access control ensures that unauthorized users are not permitted tools of higher control level users. Application should give the least privilege possible to an user to ensure safety. After logging in, the user is able to remove any order by passing the id of the order to the url. Only the recipient of the order should be able to remove the order from the database. Making a simple script can remove all the orders from the database in no time.

The vulnerability is fixed by making proper model access controls to validate the ownership of the order to the user. Verifying the user is with the corresponding order id ensures that no other user is able to remove the order.

FIX: https://github.com/schmaigul/CyberSecutrityProject/blob/3e38af58dd212ae790fd36c18d050c052efe7c13/securityproject/application/views.py#L95

### How to execute:

- Log in
- Send an order to another user
- Log in to the other user and set the order as 'Delivered'
- Log in back to the first user and brute force order ids by extending the url by ``deleteorder/orderid`` where the orderid is a positive integer.
- At some point, the order is removed from the second user

## Vulnerability 4: Security Misconfiguration

LINK: https://github.com/schmaigul/CyberSecutrityProject/blob/3e38af58dd212ae790fd36c18d050c052efe7c13/securityproject/application/views.py#L22

Lack of error handling allows user to gain sensitive data about the application stack and deeper understanding of the underlying processes within the application. My application has not implemented error handling for sending the orders. Inserting a string as the price or an invalid user as the recipient directs to an error page revealing a part of the application stack which is unwanted.

Validating correct types for each field for an order resolves the problem i.e. making sure that the item name is a string, price an int, and user an actual user in the database. Making descriptive error handling avoids user confusion.

FIX: https://github.com/schmaigul/CyberSecutrityProject/blob/3e38af58dd212ae790fd36c18d050c052efe7c13/securityproject/application/views.py#L28

### How to execute:

- Log in
- Send an order with text in the price name
- Get thrown in to an error window

## Vulnerability 5: Security Logging and Monitoring Failures

The application does not generate adequate errors or warnings for the user. In addtion, there are no security logging practices and there is no monitoring for suspicious activity. Administrators are not able to respond to possible attacks as there are no tools for finding them.

Ensuring login, accesss control and server-side input validation failures for the application is adequate pracice for this application. Logging each order and its correct cycle could be implemented. Django library offers bunch of useful loggers and handlers that alert of malicious use.

FIX: https://github.com/schmaigul/CyberSecutrityProject/blob/3e38af58dd212ae790fd36c18d050c052efe7c13/securityproject/application/views.py#L12

FIX: https://github.com/schmaigul/CyberSecutrityProject/blob/3e38af58dd212ae790fd36c18d050c052efe7c13/securityproject/application/views.py#L55

FIX: https://github.com/schmaigul/CyberSecutrityProject/blob/3e38af58dd212ae790fd36c18d050c052efe7c13/securityproject/application/views.py#L40
