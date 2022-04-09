# Mochi Restaurant

![Mochi Restaurant Images](assets/test-file/hangman-responsive.PNG)

[View the live project here](https://hangman-games.herokuapp.com/)

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

This is my 4th project at code institute.This is restaurant website designed to display to the customers and allow them to make a booking and edit,view and delete the booking.In this website customers need to login or register on the website for booking, otherwise they can't see any booking and the website will take them on login page.This website deployed on heroku.

## User Experience

### Ideal User Demographic
* New users.
* Current users.

### User Stories

#### New users :

* For new/potential user, I have included all the information about the restaurant on one page.
* As a admin user, I can login website to the access the site's backend.
* As a admin user, I can update,delete and accept or reject the reservation.
* As a new/potential user, I can login or register on website to view or edit my bookings.
* As a new/potential user, I can see Breakfat,Lunch and Dinner menu seprately.


#### Current Users :
- As a current user, I can login my account.
- As a current user, I can Edit,View and Cancel my bookings.
- As a current user, I can check my previous booking status.
- As a current user, I can contact to the restaurant regarding my current booking information.
- As a current user, I can see all the new updates about the menu.

## Target

- On the website home page I have added a big background image about the food serving in the resturant, This image push people to come in the restaurant.
- On the website home page I have added a video clip about the restautant service and food, so that people can see everything about the restaurant before book a table.

#### Structure
In this website i used five apps:

1. Aboutus - restaurant history, chefs
2. Menu - menu display
3. Reservation - reservations enquiries & customer management
4. Home - Information of all the pages
5. Contact - users feedback

### Databases

The menu, aboutus and reservation apps require databases to store information so I have built 8 custom models. 

#### Menu
In the menu app i created two models names Meals & Category, these are two models that provide all the information required to display the items as part of the restaurant's menu. Each item has a name, description, price and for how many people. 

#### Reservation
There are 3 models in reservation app, Customer, Table & Reservation.These 3 models allow for customer details to be stored, reservation enquiries to be made & managed & also enable availability checks whilst the user is enquiring. 

For each reservation, there will be a customer & table assigned to it. The customer is assigned during the enquiry process and the tables are manage in the backend by the admin user. This model only works if user is login or registerd. Logged in users will have their details with the user email address as this is how they are located in the customer model.

The tables model is used for checking the availablity of the tables in the resturant. This process used by backend admin user, Admin user checks if there is avaiable table in the restaurant then he accept user table request according to the avaliabilty.

#### Aboutus
There are 3 models in aboutus app, AboutUs, Why_Choose_Us and Chef. AboutUs model is used for display the history of the restaurant with image.Why_Choose_Us model is created for show the 3 blocks, One is to read about out staff, Second is to about fresh food and the last one is read about our food quality.Chef model is used for show the information about our chef with chef image, name and social accounts.

The type of site structure I have chosen for my website is a hierarchical structure which is demonstrated in the image below. The information architecture was arranged like this to ensure a user friendly experience as well as smooth navigation between the pages.

           # Image here