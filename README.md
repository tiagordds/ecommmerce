# Ecommerce Project
A fully functional ecommerce platform built using Python (Django) for the backend, Java for additional functionality, and HTML/CSS for the frontend. This project allows users to browse products, add them to a cart, and complete purchases, while also providing an admin interface for managing products, orders, and user

## Features
- User Authentication: Register, log in, and log out functionality.

- Product Management: Admins can add, edit, and delete product.

- Products Sub-Category: Products can have sub-categories, like Smartphones with 128GB and 256GB.

- Shopping Cart: Users can add products to their cart and proceed to checkout.

- Order History: Users can view past orders.

- Responsive Design: Built with HTML and CSS for a seamless experience on all devices.

- Search Functionality: Search for products by name or category.

- Admin Panel: Manage users, products, and orders through the Django admin interface.

## Technologies Used
- Backend: Python (Django)

- Frontend: HTML, CSS

- Additional Functionality: Java

- Database: SQLite (default for development)

- Authentication: Django Allauth

- Styling: Custom CSS for a modern and responsive design

# Installation
Step-by-step installation:

1. Clone the repository:

```bash
git clone https://github.com/tiagordds/ecommmerce.git
cd ecommmerce
```

2. Set up a virtual environment (optional, but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```


4. Run migrations:

```bash
python manage.py migrate
```

5. Create a superuser (to access the Django admin panel):

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```


7. Access the application:

### Open your browser and go to http://127.0.0.1:8000/

### Access the admin panel at http://127.0.0.1:8000/admin/

# Screenshots
![ECCOMERCE_1](https://github.com/user-attachments/assets/9a3128d6-6083-4964-bcad-826d26209441)
![ECCOMERCE_2](https://github.com/user-attachments/assets/c2de156f-3b2f-4795-9e0a-d59e9cc2f0bd)
![ECCOMERCE_4](https://github.com/user-attachments/assets/ac8d46ca-9020-46c1-9f6e-d3896784752b)
![ECCOMERCE_3](https://github.com/user-attachments/assets/fd7f2799-6a15-4973-adbf-2f0b990e2204)


