<a name="readme-top"></a>
## About The Project

### Problem
A lot of big fast food restaurant which have a in-person establishment has in your place a toten (self service kiosk) that allows consumers to request a orders without human interaction saving time and money (contracting a employee to take orders).

### Propose
Create a fastfood restaurant REST API that allows mid or lower restaurant to have your own self service toten.


## Users Requirements Gathering (Stories)

### Consumer
##### In Person
As a consumer in in-person establishment, I want to start the order selecting if i'm eat in place or take to home, after select, i want to see the list of product splited into categories, so that i can select what to order and the details (with or without some ingredient). In the end, after select the products i want to select the payment method, pay and wait for preparation of my order. When waiting to my order be ready i want to see the status(on queue, preparing and ready) of the same on the queue screen and go get when ready.

##### On Mobile App
As a consumer on mobile app, i want to have a profile with my data and past orders for be available to promotional codes, before select the product which i want, i want to select if i'll get in in-person establishment or if i want to receive the product at home and finish the order like the same as in-person establishment.

### Manager
As a manager i want to have a cleary understand of what is the most popular product(by orders), create promotional(with or without use/time limit) codes which give discount for consumers, select when the store is open to receive orders and see total balance by day.

### Chef
As a chef i want to see in the kitchen screen the queue of orders with the details of product orders to be prepare ordered by time from latest to newer, so that i can select which one to prepare first and select when ready.

## Users Requirements Gathering (Functional)

- Place Order:  the system must support `anonymous` (only in-person establishment) or `authenticated` (in-person or mobile app) placed order.

- User Authentication: the system must support JWT authentication.

- APIs: the system has to provide RESTful API's for integration.
<p align="right"><a href="#readme-top">back to top</a></p>
