class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.all_customers.append(self)

    def set_given_name(self, new_given_name):
        self.given_name = new_given_name

    def set_family_name(self, new_family_name):
        self.family_name = new_family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    def all(cls):
        return cls.all_customers


class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def get_name(self):
        return self.name

    def all(cls):
        return cls.all_restaurants

    def reviews(self):
        return self.reviews

    def customers(self):
        unique_customers = set()
        for review in self.reviews:
            unique_customers.add(review.customer())
        return list(unique_customers)


class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer_obj = customer
        self.restaurant_obj = restaurant
        self.rating = rating
        Review.all_reviews.append(self)

    def rating(self):
        return self.rating

    def all(cls):
        return cls.all_reviews

    def customer(self):
        return self.customer_obj

    def restaurant(self):
        return self.restaurant_obj


# Additional Object Relationship Methods
class Review:
    def customer(self):
        return self.customer_obj

    def restaurant(self):
        return self.restaurant_obj


class Restaurant:
    def reviews(self):
        return self.reviews

    def customers(self):
        unique_customers = set()
        for review in self.reviews:
            unique_customers.add(review.customer())
        return list(unique_customers)


class Customer:
    def restaurants(self):
        reviewed_restaurants = [review.restaurant() for review in Review.all_reviews if review.customer() == self]
        return list(set(reviewed_restaurants))

    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        restaurant.reviews.append(new_review)


# Aggregate and Association Methods
class Customer:
    def num_reviews(self):
        return len([review for review in Review.all_reviews if review.customer() == self])

    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer

    def find_all_by_given_name(cls, given_name):
        return [customer for customer in cls.all_customers if customer.given_name == given_name]


class Restaurant:
    def average_star_rating(self):
        total_ratings = sum([review.rating for review in self.reviews])
        num_reviews = len(self.reviews)
        return total_ratings / num_reviews if num_reviews > 0 else 0
