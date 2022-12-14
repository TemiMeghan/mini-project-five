# ****************************************************************
# miniproject five
# working on dictionary
# ****************************************************************
import random  #imports random method
# Task 1
print("Task 1")
print()  # indicates a space
# a dictionary that stores six pieces of information about myself
my_self = {
  "Preferred_name: ": "Temi_Meghan",
  "Last_name: ": "A",
  "Song": "Amazing God by loveworld sings",
  "Fav_food: ": "Oha soup",
  "Fav_color: ": "Maroon",
  "Fav_drink: ": "Water"
} 
# Printing each pieces of information stored in my dictionary using a for loop and .items().
for key, value in my_self.items():
  print(key, value)
print()  # indicates a space
# Task 2
print("Task 2")
print()  # indicates a space
# A dictionary that stores five classmates and their favourite foods.
collegues = {
  "Iffy: ": ["Yam", "Egusi soup", "Afang soup"],
  "Aayu: ": ["Chaat", "Pani  puri", "Basmatic rice"],
  "Walter: ": ["Burger", "Pizza", "Shawama"],
  "Bilz: ": ["Jollof rice", "Masala dosa", "Vada pav"],
  "Paul: ": ["Eggs", "Rice", "Eba"]
}
# a for loop that prints each person’s name and their favourite foods
for key, value in collegues.items(
):  # a for loop that iterates over the dictionary
  print(key, value)  # each collegues printed with their favourite foods
  print()  # indicates a space

# Task 3
#Make several dictionaries, where each dictionary represents a different person. In each dictionary, include the persons choice of food and meal, for example Jim's breakfast is toast and eggs. Store these dictionaries in a list called meals. Next, loop through your list of dictionaries using a for loop, and as you do, print everything you know about each person, meal and food.

print("Task 3")
print()  # indicates a space
meals = [{
  "Name: ": "Temi",
  "meal: ": "Breakfast",
  "food-choice: ": "Yam and egg"
}, {
  "Name: ": "Niyi",
  "meal: ": "Lunch",
  "food-choice: ": "Eba and Egusi"
}, {
  "Name: ": "Sandra",
  "meal: ": "Dinner",
  "food-choice: ": "Iyan and Vegetable"
}, {
  "Name: ": "Wilson",
  "meal: ": "Breakfast",
  "food-choice: ": "Cake and Tea"
}, {
  "Name: ": "Meghan",
  "meal: ": "Lunch",
  "food-choice: ": "Okro soup and Fried Fish"
}]  # different dictionaries representing different people in a list
for key in meals:
  # different people choice of food and meal printed in each line in a sentence using for loop
  print(
    f"{key['Name: ']} loves having {key['food-choice: ']} for {key['meal: ']}")
  print()  # indicates a space

  # Task 4
print("Task 4")
print()  # indicates a space
# Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a sub dictionary of information about each city and include the country that the city is in, its approximate population, and three facts about that city. The keys for each city’s dictionary should be something like country, population, and facts, but you are welcome to make up your own keys and values that describe the city. Print the name of each city and all of the information you have stored about it.

# a dictionary of three cities with their different informations
cities = {
  "Lagos": {
    "City name ":
    "Lagos",
    "City's country ":
    "Nigeria",
    "City's Population ":
    "10.5 million",
    "City known for ":
    "Known as the major financial centre in Nigeria, generating wealth for the nation. "
  },
  "Ottawa": {
    "City name ": "Ottawa",
    "City's country ": "Canada",
    "City's Population ": "1.5 million",
    "City known for ": "Known for its historic sites and landmarks"
  },
  "Vancouver": {
    "City name ":
    "Vancouver",
    "City's country ":
    "Canada",
    "City's Population ":
    "2.5 million",
    "City known for ":
    " Known for its scenic views, mild climate, and friendly people"
  }
}
# printing out the name of each city with their informations
for key, val in cities.items():  # used the for loop to access the dictionary
  print(f" Brief information about {key.title()}"
        )  # this gains access to the key information
  print()  # indicates a space
  for i, value in val.items():  # this gains access to the value information
    print(
      f"{key.title()} {i} : {value} "
    )  # prints information of both the key and value in the dictionary using the fstring
    print()  # indicates a space.

# Task 5
print("Task 5")
print()  # indicates a space
# Make a dictionary called stock_prices and put three keys (stock names) into it. The values should be lists that contain 10 stock prices for each stock. Using a for loop, print out the stocks, minimum price, average price, and maximum price  for each stock.

stock_prices = {
  "Amazon ":
  [10.23, 11.00, 20.55, 12.31, 15.16, 21.13, 11.34, 77.10, 90.11, 34.5],
  "Walmart ": [34.6, 56.1, 1.90, 100, 38, 95.6, 87.9, 90.65, 46.4, 34.2],
  "Visa ": [200.1, 345.1, 112.1, 37.8, 405.3, 450.0, 102.3, 30.4, 35.67, 10.0]
}  # values of each stock price in a list

for key, value in stock_prices.items():
  print(f"{key.title()} minimum value is {min(value)}"
        )  # prints the lowest value of the stock.
  print()
  print(f"{key.title()} average value is {sum(value)/10}."
        )  # prints the average value of the stock.
  print()
  print(f"{key.title()} maximum value is {max(value)}"
        )  # prints maximum value of the stock.
  print()
# Task 6
print("Task 6")
print()  # indicates a space
# You are running for president. Build an election simulator.

# In your program, use a for loop to run the program five times. Create a variable outside the loop for popularity score that starts at 0. Within each loop, create an event (print something about the event), and at each of the events add a random amount of approval to the overall total. Show (print out) what happens at each step (print how much popularity was gained), and let the user know the final result (if the candidate has over 51% of the vote they win, otherwise they lose).

# For example:

# Event 1: Sidney gives a great speech and gains 5% popularity! Total popularity is now 21%!

# Make sure each step prints out a sentence explaining what is happening and shows the final results.

# an election simulator
popularity_score = 0  # a variable stored as zero
events = [
  "Accountability", "Lifestyle", "Acheivements", "integrity", "Honesty"
]  # list of events
for i in range(5):  # a for loop that runs the program 5 times
  figure = random.randint(
    1, 20)  # randomly selects a number between 1 and 20 and assigns to figure
  popularity_score = +figure  # adds to popularity_score
  print(popularity_score)
  print(
    f"Temitope {events[i]} {figure}%. Popularity score is {popularity_score}%"
  )  # prints the result
  # condition
  if popularity_score > 51:  # if value is greater than 51
    print("Temitope wins the election ")  # result
  else:
    print("She lost to the opponent")  # if it is lesser print this result
  
print()  # indicates a space
# Task 7
print("Task 7")
print()  # indicates a space
#  Create a dictionary that contains keys of your choice with values of type int, float, string, list, dictionary, and tuple
key_types = {
  "int": 1,  # integer key
  "float ": 2.5,  #float key
  "str ": "string",  # string key
  "list ": ["welcome", "Temi", 1, 5],  # a list key with strings and integers
  "dictionary": " yeah, this is dictionary",  # a dictionary key with a string
  "tuple ": ("tuple", "apple", "saddle")  # a tuple key with a tuple
}
print(key_types)
print(type(key_types))  # prints different key_types
