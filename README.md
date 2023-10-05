# Shopping Cart System
Introduction
This Python program, called the "Shopping Cart System," simulates an online shopping experience with various functionalities. 
It allows users to log in, view products, add items to their cart, remove items from the cart, check out, and view their shopping history.

Features
User Classes
User: The base class that handles user login and provides access to various shopping-related options.
Product: Subclass of User, responsible for displaying a list of available products and saving products to a file.
ShoppingCart: Subclass of User, manages the user's shopping cart, including adding and removing products, and displaying the cart.
Shopping: Subclass of ShoppingCart, handles placing orders, displaying shopping history, and calculating the total bill.
CheckOut: Subclass of Shopping, displays the items in the cart and the total bill before checkout.
Logout: Logs the user out of the system.
Customer Class
A specialized class that inherits from the UserChoice class and handles customer-specific actions. 
It allows customers to view products, add products to the cart, remove products, check out, view shopping history, and log out.

Getting Started
Clone this repository to your local machine.
Ensure you have Python installed.
Open a terminal or command prompt and navigate to the directory where the code is located.
Run the main.py file to start the program.
Usage
Log in with your user ID.
Choose from the available options:
View products (a)
Add products to your cart (b)
Remove products from your cart (c)
View your cart (d)
Checkout (e)
View shopping history (f)
Logout (g)
Sample Data
The program uses sample product data for demonstration purposes. You can customize the product list by modifying the lst variable within the Product class.

File Storage
The program uses text files to save product data and shopping history. These files will be created in the same directory as the code.

Note
This program is a simplified simulation for educational purposes. It doesn't handle real payment processing and should not be used for actual online shopping.

Author
Khadija
