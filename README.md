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

#### Reservation
There are 3 models in the reservation app, Customer, Table & Reservation. These 3 models allow for the customer details to be stored, reservation enquiries to be made, managed & also enable availability checks whilst the user is enquiring.

For each reservation, there will be a customer & table assigned to it. The customer is assigned during the enquiry process and the tables are managed in the backend by the admin user. This model only works if the user is logged-in or registered. Logged-in users will have their details linked with the user email address as this is how they are located in the customer model.

The tables model is used for checking the availability of the tables in the restaurant. This process is used by the backend admin user, who checks if there is an available table in the restaurant then he can accept the user’s table request according to the availability.

This model is following this flow diagram:

#### Aboutus
There are 3 models in the about us app, About Us, Why_Choose_Us and Chef. The About Us model is used to display the history of the restaurant with an image. Why_Choose_Us model is created to show the 3 blocks, one is to read about our staff, the Second is about fresh food and the last one is to read about our food quality. The chef model is used to show the information about our chef with a chef’s image, name and social accounts.

This model is following this flow diagram: