Product Management API with Django REST Framework and MySQL

Overview

This project is a Python-based backend service that provides a RESTful API for managing products. It uses Django Rest Framework (DRF) for the web framework and MySQL as the database. The service supports basic CRUD operations (Create, Read, Update, Delete) for a "Product" entity.

Features
Product Entity:

id (integer, primary key in MySQL)
name (string)
description (string)
price (float)
quantity (integer)
API Endpoints:

POST /products/ - Create a new product.
GET /products/{id}/ - Retrieve product details by ID.
PUT /products/{id}/ - Update product details by ID.
DELETE /products/{id}/ - Delete a product by ID.
Data Consistency:

All operations are performed on MySQL to ensure data consistency.
Validation and Error Handling:

Input validation and error handling are implemented to manage invalid data and database connection issues.
Requirements
Python 3.x
Django 5.0.8
Django Rest Framework 3.15.2
MySQL
MySQLClient (for connecting Django to MySQL)
