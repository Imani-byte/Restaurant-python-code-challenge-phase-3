# Restaurant-python-code-challenge-phase-3

## Description
This Python project simulates a Yelp-style domain with three main models: Restaurant, Customer, and Review. It explores class and instance methods, object relationships, lists, and list methods.

## Classes
1. ### Customer Class
- __init__(given_name, family_name): Initializes a customer with a given name and family name.
- set_given_name(new_given_name): Sets the given name of the customer.
- set_family_name(new_family_name): Sets the family name of the customer.
- full_name(): Returns the full name of the customer.
- all(): Returns all customer instances.
2. ### Restaurant Class
- __init__(name): Initializes a restaurant with a name.
- get_name(): Returns the restaurant's name.
- all(): Returns all restaurant instances.
- reviews(): Returns a list of all reviews for that restaurant.
- customers(): Returns a unique list of all customers who have reviewed the restaurant.
3. ### Review Class
- __init__(customer, restaurant, rating): Initializes a review with a customer, restaurant, and rating.
- rating(): Returns the rating for a restaurant.
- all(): Returns all reviews.
- customer(): Returns the customer object for that review.
- restaurant(): Returns the restaurant object for that given review.

## Methods
### Additional Object Relationship Methods
#### Review Class
- customer(): Returns the customer object for that review.
- restaurant(): Returns the restaurant object for that given review.
#### Restaurant Class
- reviews(): Returns a list of all reviews for that restaurant.
- customers(): Returns a unique list of all customers who have reviewed the restaurant.
#### Customer Class
- restaurants(): Returns a unique list of all restaurants a customer has reviewed.
- add_review(restaurant, rating): Given a restaurant object and a star rating (as an integer), creates a new review and associates it with that customer and restaurant.

### Aggregate and Association Methods
#### Customer Class
- num_reviews(): Returns the total number of reviews that a customer has authored.
- find_by_name(name): Given a string of a full name, returns the first customer whose full name matches.
- find_all_by_given_name(name): Given a string of a given name, returns a list containing all customers with that given name.
#### Restaurant Class
- average_star_rating(): Returns the average star rating for a restaurant based on its reviews.

## Setup
1. Clone the repository
2. Navigate to the project directory
3. Install dependencies using Pipenv
4. Activate the virtual environment

## Author
Imani Naisiae Kasura
