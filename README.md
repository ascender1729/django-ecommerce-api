# Django E-commerce API

## Overview

This project is a RESTful API for an e-commerce platform built with Django and Django REST Framework. It provides endpoints for managing products, shopping carts, and orders.

## Features

- Product catalog management
- Shopping cart functionality
- Order processing
- RESTful API design
- Built with Django and Django REST Framework

## Workflow

The e-commerce API follows a typical e-commerce workflow, allowing users to browse products, add items to their cart, and place orders. Here's a detailed explanation of the workflow, illustrated by the sequence diagram below:

![E-commerce API Workflow](/img1.png)

1. **API Root Access**:
   - The client starts by sending a GET request to the API root (`/api/`).
   - The API responds with a list of available endpoints, allowing the client to discover the API's capabilities.

2. **Product Browsing**:
   - The client sends a GET request to `/api/products/` to retrieve the list of available products.
   - The API queries the database for product information.
   - The database returns the product data to the API.
   - The API sends the list of products back to the client.

3. **Adding to Cart**:
   - When a user wants to add an item to their cart, the client sends a POST request to `/api/cart/`.
   - The API processes this request and adds the item to the user's cart in the database.
   - The database confirms that the item has been added.
   - The API sends back the updated cart information to the client.

4. **Placing an Order**:
   - To place an order, the client sends a POST request to `/api/orders/`.
   - The API creates a new order in the database based on the items in the user's cart.
   - As part of the order creation process, the API also clears the user's cart.
   - The database confirms that the order has been created.
   - The API sends the order details back to the client.

5. **Viewing Orders**:
   - The client can retrieve a list of orders by sending a GET request to `/api/orders/`.
   - The API queries the database for the user's order history.
   - The database returns the order data.
   - The API sends the list of orders back to the client.

This workflow allows for a seamless e-commerce experience, from browsing products to completing purchases. The API handles all the necessary data management and interactions with the database, providing a robust backend for an e-commerce application.

## Requirements

- Python 3.8+
- Django 5.1.2
- Django REST Framework 3.14.0

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/django-ecommerce-api.git
   cd django-ecommerce-api
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser (for admin access):
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/api/`.

## API Endpoints

### API Root
- `GET /api/`: List all available endpoints

### Products
- List/Create: `GET`, `POST` `/api/products/`
- Retrieve/Update/Delete: `GET`, `PUT`, `PATCH`, `DELETE` `/api/products/{id}/`

### Cart
- List/Create: `GET`, `POST` `/api/cart/`
- Retrieve/Update/Delete: `GET`, `PUT`, `PATCH`, `DELETE` `/api/cart/{id}/`

### Orders
- List/Create: `GET`, `POST` `/api/orders/`
- Retrieve/Update/Delete: `GET`, `PUT`, `PATCH`, `DELETE` `/api/orders/{id}/`

## Usage

### Authentication

This API uses session-based authentication. To authenticate:

1. Obtain a session token:
   ```
   curl -X POST http://localhost:8000/api-auth/login/ -d "username=yourusername&password=yourpassword"
   ```

2. Include the session token in subsequent requests:
   ```
   curl -X GET http://localhost:8000/api/products/ -H "Authorization: Token YOUR_TOKEN_HERE"
   ```

### Examples

1. List all products:
   ```
   curl -X GET http://localhost:8000/api/products/
   ```

2. Create a new product:
   ```
   curl -X POST http://localhost:8000/api/products/ -H "Content-Type: application/json" -d '{"name":"New Product", "description":"Product description", "price":"19.99", "stock":100}'
   ```

3. Add an item to cart:
   ```
   curl -X POST http://localhost:8000/api/cart/ -H "Content-Type: application/json" -d '{"product": 1, "quantity": 2}'
   ```

4. Create an order:
   ```
   curl -X POST http://localhost:8000/api/orders/ -H "Content-Type: application/json" -d '{}'
   ```

## Project Structure

```
django_ecommerce_api/
├── django_ecommerce_api/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── products/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── cart/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── orders/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
├── README.md
└── img1.png
```

## Development

To contribute to this project:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## Testing

Run the test suite:

```
python manage.py test
```

## Deployment

For production deployment, make sure to:

1. Set `DEBUG = False` in `settings.py`
2. Use a production-grade server like Gunicorn
3. Set up a reverse proxy with Nginx
4. Use environment variables for sensitive information
5. Set up proper security measures (HTTPS, secure cookies, etc.)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.