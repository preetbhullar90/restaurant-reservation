# Mochi Restaurant - Testing

[README.md file](/README.md)

[View live project](https://mochi-restaurant.herokuapp.com)

## Table of contents
1. [Testing User Stories](#Testing-User-Stories)
2. [Manual File Test](#Manual-File-Test)
3. [Automated Testing](#Automated-Testing)
     - [Code Validation](#Code-Validation)
     - [Browser Validation](#Browser-Validation)
     - [Lighthouse](#Lighthouse)

## Testing User Stories
#### New user Goals:
1. For new/potential users, I have included all the information about the restaurant on one page.
   * For new users, I added menu, contact, about us and reservation pages on home page. it is very easy for new user to find all the pages from one page.
2. As an admin user, I can login to the website to access the site's backend.
   * As an admin user, I can login to the site's backend to manage the bookings and can see all the bookings which have been requested by users.
3. As an admin user, I can update, delete and accept or reject the reservations.
   * As an admin user, I can approve or reject any reservation requested by new user.
   * As an admin user, I can manage the restaurant's bookings efficiently.

4. As a new/potential user, I can login or register on the website to view or edit my bookings.
   * As a new/potential user, I can request a table reservation in the restaurant, But I have to login or register first to access the booking form.
   * As a new/potential user, I can see my booking request on a separate page and I can edit, delete or view my bookings.

5. As a new/potential user, I can see the Breakfast, Lunch and Dinner menu separately.
   * As a new user, I can also see menu on the home page and separately on the menu page this makes it easier for new users to find it out.

#### Current users Goals:
1. As a current user, I can login to my account.
   * As a current user, I can login to my old account with my username and password, but if the user is already logged in to their old account, then they don't need to login when they open the website for a second time.
   * For current users, I redirect the page to the login if user is logged out and when they open the website, they will be redirected to the login page.

2. As a current user, I can Edit, View and Cancel my bookings.
   * As a current user, I can see my old bookings. I can edit, view and cancel them but I have to login first.
3. As a current user, I can check my previous booking status.
   * As a current user, I can check my booking request status anytime. If admin approve it, then the status will change to confirmed.
4. As a current user, I can contact the restaurant regarding my current booking information.
   * Current users can contact to the restaurant to get information about their bookings, or they can send their feedback as well.
5. As a current user, I can see all the new updates about the menu.
   * As a current user, I can see any updates about the menu, because when restaurant updates their menu, it's visible immediately on the website.

[Go Top](#Table-of-contents)

## Manual File Test

### Home-Page-Responsive
* The Home page responsive on all the devices.

![](/assets/testing-file/home-page-responsive.gif)

 ### Home-Page
* Full home page.

![](/assets/testing-file/home-page.gif)

### About-Page-Responsive
* The About page responsive on all the devices.

![](/assets/testing-file/about-page-responsive.gif)

 ### About-Page
* Full about page.

![](/assets/testing-file/about-page.gif)

[Go Top](#Table-of-contents)

### Menu-Page-Responsive
* The Menu page responsive on all the devices.

![](/assets/testing-file/menu-page-responsive.gif)

 ### Menu-Page
* Full menu page.

![](/assets/testing-file/menu-page.gif)

### Booking-Page-Responsive
* The booking page responsive on all the devices.

![](/assets/testing-file/booking-page-responsive.gif)

 ### Booking-Page
* Full booking page.

![](/assets/testing-file/booking-page.gif)

### Contact-Page-Responsive
* The contact page responsive on all the devices.

![](/assets/testing-file/contact-page-responsive.gif)

 ### Contact-Page
* Full contact page.

[Go Top](#Table-of-contents)

![](/assets/testing-file/contact-page.gif)

### Register-Page-Responsive
* The Register page responsive on all the devices.

![](/assets/testing-file/form-page-responsive.gif)

 ### Register-Page
* Full register page.

![](/assets/testing-file/form-page.gif)

[Go Top](#Table-of-contents)

## Automated Testing

### Code Validation
The [W3C Markup Validator](https://validator.w3.org/) service was used to validate the `HTML` code used.

**Results:**

### **HTML File**
![](/assets/testing-file/html-pp4-test-file.PNG)

The [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) service was used to validate the `CSS` coded used.

### **Css Result**

![](/assets/testing-file/css-pp4-testing-file.PNG)

### Browser Validation
- Chrome - [test image](/assets/testing-file/browser-test/chrome.PNG)
- Edge - [test image](/assets/testing-file/browser-test/edge.PNG)
- Opera - [test image](/assets/testing-file/browser-test/opera.PNG)
- Firefox - [test image](/assets/testing-file/browser-test/firefox.PNG)



## Lighthouse

* Website performance checked in lighthouse developer-tool,with the following result :

![](/assets/testing-file/lighthouse.PNG)


## Test Coverage
* The code tested with coverage tool, with the following result:

![](/assets/testing-file/coverage-report.PNG)

[Go Top](#Table-of-contents)