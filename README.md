# Terminal Application Documentation

**Link to the GitHub Repository**

**Link to the presentation**

## Purpose of the app and features

---
The aim of this application is to develop an order system for a sticker shop. This system contains several features:

* Collect customer's information
  This feature allows users to collect and store customer's name. Customer's name will be stored in the system and later used by other features. For example, customer's name will be displayed on the receipt.

* Order stickers and print receipt
  This is the main feature of this application. This feature allows users to place multiple orders for customers and print receipt for the customer.

* Allow customers to join membership and obtain discount
  This feature will add all customers to the non-rewards customer list. It will also ask whether these non-rewards customers would like to join membership. If they decide to join the memebership, they will become rewards customers and have 10% discount of their orders.

* Display existing customers information
  This feature displays all existing customers' information on the terminal, includes their name and membership status. Users could also select to display all or display one category such as non-rewards customer information only.

## Implementation Plan For Each Feature

---

### Collect customer information

***Due Date:17 Sep***

***Highest Priority***

The system will first display a message asking users to enter the customer's information. User could enter the customer's information at the terminal. System will read the input and check wether it is an valid input. If not, the system will display an error message and allowing users to enter again. Once the system receives a valid input, it will store the customer's information.

Checklist-items:

* Display a message asking the user to enter customer's name
* Read users' input (only enter a string)
* Input validation(Check users' input)
* Handling errors (If users have an invalid input, let then know and give them another chance)
* Store the valid customer information

### Order stickers and print receipt

***Due Date:17 Sep***

***Highest Priority***

The system will first ask which sticker that customers want. Once the system receives an valid input, it will then ask the quantity of the selected sticker and check whether the input is valid. If users enter an invalid input, they will be notified and have chance to enter again. After this, the system will ask wether the customer want to order another sticker. If yes, it will repeat previous steps. If not, it will calculate the total cost and print the receipt for the customer.

Checklist-items:

* Create a menu of the sticker shop
* Display a message asking the user to enter the sticker that customers want to order
* Users enter the name of the selected sticker(name of our product)
* Display a message asking the user to enter the quantity of the sticker orderd by the customer
* Users enter the quantity of the sticker(only enter positive integer)
* Display a message asking whether the customer want to order another stickers (only enter yes or no)
* If yes, ask the name and quantity of the new sticker.
* Input validation, check whether users enter a valid input
* Handling errors. If there is an invalid input, give them another chance until receives a valid input
* Calculate the total cost at the eend and print the receipt

### Allow customer to join membership and obtain discount

***Due Date:18 Sep***

***Second Priority***

This feature will be implemented by creating two list, one for non-rewards customers and one for rewards customers. The system will automatically add all customers to the non-rewards customer list, and ask the user whether the customer want to join membership(rewards customer). Rewards customer will have 10% discount for their orders.

Checklist-items:

* Create two lists: 1. Non rewards Customer 2. Rewards Customer(Customer that joins membership)
* Add all new customers to the non rewards customer list
* Display a message asking if non rewards customer would like to join rewards customer. (Users only enter yes or no)
* Input validation
* Handling errors and give user multiple chances until they enter a valid input
* If answer yes, customers will become rewards customers and have 10% discount for their orders

### Display existing customers information

***Due Date:18 Sep***

***Second Priority***

This feature will be implemented using two lists created for non-rewards customers and rewrads customers, and user choose to display all or one of these two lists.

Checklist-items:

* Store all customers' information as two groups, non-rewards and rewards customer(created in the previous feature)
* Ask users which group they want to display
* Users select one or both groups
* Input validation(only integer 1 and 2, 1 is non-rewards customer, 2 is rewards customer)
* Handling Error, if users enter an invalid input, they will have another chance
* Display all customers within that group

## Imported Libraries

---

* Rich, from [Rich](https://rich.readthedocs.io/en/stable/tables.html)
* Art
* Click
* Pytest
* Pendulum