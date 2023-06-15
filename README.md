# Toshkent Parfum

Toshkent Parfum, an online platform for purchasing premium perfumes. This project provides a user-friendly interface for browsing, selecting, and purchasing perfumes, along with features such as ordering, delivery.

## Features
- Extensive Collection: Browse through a wide selection of high-quality perfumes from various brands and categories.
- User Registration and Authentication: Create an account, login, and manage your profile to enhance your shopping experience.
- Product Listing and Filtering: Easily search and filter perfumes based on brand, category, price, or other attributes.
- Shopping Cart: Add perfumes to your cart, manage quantities, and proceed to checkout.
- Secure Checkout Process: Safely complete your purchase by providing shipping and payment details.
- Order Tracking: Track the status of your orders and receive updates on the delivery progress.
- Wishlist: Save your favorite perfumes to your wishlist for future reference.
- Product Reviews: Read and write reviews for perfumes to help other customers make informed decisions.
- Admin Panel: An administrative interface to manage products, orders, and user accounts.
- Payment Integration: Seamless integration with popular payment gateways for smooth and secure transactions.

# Installation and Setup
### To run the Tashkent Parfume Ecommerce project locally, follow these steps:
1. **Clone the repository:**  
   git clone https://github.com/AzizJohn/Tashkent-parfume.git
2. **Create a virtual environment and activate it:**  
*Create a new virtual environment:*    
   - python3 -m venv env  
*Activate the virtual environment:*  
*For Linux and macOS:*
   - source env/bin/activate  
*For Windows:*
   - .\env\Scripts\activate

Activating the virtual environment will isolate the project's dependencies from your system's global Python installation.

3. Install project dependencies:
   - pip install -r requirements/develop.txt

This command will install all the necessary packages and libraries required by the project.

4. Create and configure the .env file based on the .env.example file:  
5. Configure the database settings:  
   *update database settings on .env file*

6. Apply database migrations:  
   - python manage.py migrate  

This command will apply any pending database migrations and set up the necessary database tables.  

7. Run the development server:
   - python manage.py runserver  

The development server will start running, and you can access the Tashkent Parfume Ecommerce application by navigating to http://localhost:8000 in your web browser.

8. Go to the url http://127.0.0.1:8000/swagger/
   Result should be like this:
   
   ![image](https://github.com/AzizJohn/Tashkent-parfume/assets/101688328/948b6009-e3e8-4903-93cb-49fb406a1597)



