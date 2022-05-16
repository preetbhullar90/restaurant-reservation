# Mochi Restaurant

![Mochi Restaurant Images](assets/testing-file/am-i-responsive1.PNG)

[View the live project here](https://mochi-restaurant.herokuapp.com)

## Contents
1. [Introduction](#Introduction)

2. [User Experience](#User-Experience)

3. [Target](#Target)

4. [Design](#Design)

5. [Features](#Features)

6.  [Flowchart](#Flowchart)

7. [Bugs](#Bugs)

8. [Other Features](#Other-Features)

9. [Features Left to Implement](#Feature-Left-to-Implement)

10. [Technologies Used](#Technologies-Used)

11. [Frameworks Libraries and Programs Used](#Frameworks-Libraries-and-Programs-Used)

12. [Testing](#Testing)

    - [Testings.md](assets/test-file/testings.md)

13. [Deployment](#Deployment)

14. [Make a clone](#Make-a-clone)

15. [Credit](#Credit)

16. [Acknowledgements](#Acknowledgements)

## Introduction

This is my 4th project at code institute. This project is a restaurant website designed to advertise the restaurant and to allow the customer to make and manage any bookings. On this website, customers need to login or register on the website, where they can manage their booking, by logging on they can view, delete and change their bookings. If the customer does not login or register, they will only see a login option on the booking page. This website is deployed on Heroku.

## User Experience

### Ideal User Demographic
* New users.
* Current users.

### User Stories

#### New users :

* For new/potential users, I have included all the information about the restaurant on one page.
* As an admin user, I can login to the website to access the site's backend.
* As an admin user, I can update, delete and accept or reject the reservations.
* As a new/potential user, I can login or register on the website to view or edit my bookings.
* As a new/potential user, I can see the Breakfast, Lunch and Dinner menu separately.


#### Current Users :
- As a current user, I can login to my account.
- As a current user, I can Edit, View and Cancel my bookings.
- As a current user, I can check my previous booking status.
- As a current user, I can contact the restaurant regarding my current booking information.
- As a current user, I can see all the new updates about the menu.


## Target

- On the website home page, I have added a large background image about the food served in the restaurant, this image would persuade customers to visit the restaurant.
- On the website home page, I have added a video clip about the restaurant’s service and food, so that people can see everything about the restaurant before booking a table.


#### Structure
In this website I have used five apps:

1.  About us - restaurant history, chefs
2.	Menu - menu display
3.	Reservation - reservations enquiries & customer management
4.	Home - Information about all the pages
5.	Contact - user feedback


### Databases

The menu, about us and reservation apps require databases to store information, so I have built 8 custom models.

#### Menu
In the menu app I created two models named Meals & Category, these are two models that provide all the information required to display the items as a part of the restaurant's menu. Each item has a name, description, price, and information on how many people the dish serves.

This model is following this flow diagram:

![](/assets/readme-file/menu-diagram.png)

#### Reservation
There are 3 models in the reservation app, Customer, Table & Reservation. These 3 models allow for the customer details to be stored, reservation enquiries to be made, managed & also enable availability checks whilst the user is enquiring.

For each reservation, there will be a customer & table assigned to it. The customer is assigned during the enquiry process and the tables are managed in the backend by the admin user. This model only works if the user is logged-in or registered. Logged-in users will have their details linked with the user email address as this is how they are located in the customer model.

The tables model is used for checking the availability of the tables in the restaurant. This process is used by the backend admin user, who checks if there is an available table in the restaurant then he can accept the user’s table request according to the availability.

This model is following this flow diagram:

![](/assets/readme-file/reservation-diagram.png)

#### Aboutus
There are 3 models in the about us app, About Us, Why_Choose_Us and Chef. The About Us model is used to display the history of the restaurant with an image. Why_Choose_Us model is created to show the 3 blocks, one is to read about our staff, the Second is about fresh food and the last one is to read about our food quality. The chef model is used to show the information about our chef with a chef’s image, name and social accounts.

This model is following this flow diagram:

![](/assets/readme-file/aboutus-diagram.png)

## Design

### Colour Schema
* I used four colours for the background and content, which are white, yellow, black and dark grey. I have also used a small amount of red for the cancel the booking button.
* I chose all the colours I used from the [theme waGon](https://themewagon.com/theme-tag/restaurant-template/) website.

#### Typography
* I selected the font I used from the [Google font](https://fonts.google.com/) website and linked it with my Css file.
* I used three font styles system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans","Liberation Sans",sans-serif.
* I have used the font Sans-serif for backup in instances where if the correct link isn’t provided to the css3 file, a font type is still available. If this occurs and the Google font does not work the backup font sans-serif will always work.

#### Imagery
* The background image used in this website plays a vital role in the user’s experience of the website.
* The image shown on the website has been selected to convince the customer to come to the restaurant.
* The Image is downloaded free from the [pexels](https://www.pexels.com/search/gym%20and%20fitness/) website.

#### Skeleton
- I used [Figma](https://www.figma.com/file/jCwcpxiv4ugqY8XK812AA8/Restaurant?node-id=0%3A1) Wireframe for the website.

## Features

* ### Header
* ### Home Page
* ### About Page
* ### Menu Page
* ### Your Booking Page
* ### Contact Page
* ### Register Page
* ### Login Page
* ### Footer

### Header
In the header the main logo of the website is on the left-hand side, and the navigation links are on the right-hand side on all the pages. On medium-sized devices such as tablets, the logo stays on the left-hand side, but the navigation links hide behind the hamburger logo.

### Tablet Mobile And Desktop
![](assets/readme-file/mobile-desktop-image.PNG)

### Home Page
The home page has a big hero image in the back. On the image I have added two buttons, one button is linked to the menu and the other one is linked to the booking a table page. Under the hero image, there is a section where there is a history of the restaurant with an image. Under the history section, there is a menu section about all the foods. Under the menu section, there is a form section for Email, Phone number, Address, restaurant Email and a link bar where the user can navigate to all the pages. A google map of the restaurant location is also featured on the home page.

![](assets/readme-file/home-page.png)

### About Page
The about page also has a large background image. Under the image there is a small section about the history of the restaurant with a small image. Under the history section, I added a section about why the customer should choose our restaurant, in this section, there are three blocks, one block is about Quality Cuisine, the other one is about Fresh Food, and the last one is about our Friendly staff. At the bottom of the page, there is a section dedicated to our professional chefs. In this section, there are also three blocks, each block has a chef image with their name and their social media accounts.

![](assets/readme-file/about-page.png)

### Menu Page
The menu page has 3 sections for Breakfast, Lunch and Dinner. In this menu customers can see all the details about any dish along with its price.

![](assets/readme-file/menu-page.png)

### Your Booking Page
In the booking page there is a section about your booking. First you have to login or register your name because without logging in the user can't see their booking. After logging in the users can see their bookings if they have previously requested a booking in the past, users can also View, Edit, and Cancel their bookings on this page. If the user has not requested a booking before then this page will take them to the book a table page.

![](assets/readme-file/your-booking-page.png)

### Contact Page
The contact page has a background image and under this image there is a large map where users can see the location of the restaurant. Under the map there is a contact us section, in this section, users can see the restaurant’s email, phone number and opening hours. On the right-hand side of this section, there is a form for contacting the restaurant where users can send an email and their feedback.

![](assets/readme-file/contact-page.png)

### Register Page
On the register for an account page there is a form section which the user can complete to get an account. Under this form, I have provided a link for signing in if the user already has an account. This form is validated, if the user doesn’t add a valid email or name then the user will see an error message on top of the form.

![](assets/readme-file/register-page.png)

### Login Page
On the login page, there is a section for the user to login. If user has already registered, then they can login to their account but if the user doesn't have an account, then I provided a link for them to register. When user logs in or registers then they can see their name on the top of the navbar.

![](assets/readme-file/login-page.png)

### Footer
A footer is featured on the bottom of every page of the website. The footer has all the detail about the restaurant, In the middle of the footer, there are links to all the pages of the website. On the right-hand side, details about the restaurant opening hours are listed.

![](assets/readme-file/footer-page.png)