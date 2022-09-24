# Installation Instructions

---

1. Open the command line or terminal.
2. Type `python3 --version` to check whether python has been installed.
3. If you do not have python installed on your computer,
   please go to this [page](https://www.python.org/downloads/) to install python.
4. Type `pip --version` to check whether pip has been installed.
5. If you do not have pip installed on your computer,
   please go to thie [page](https://pip.pypa.io/en/stable/installation/) to install pip.
6. Copy the following command to the terminal to clone the program:

    `git clone https://github.com/Chengqunniu/T1A3.git`
7. Copy the following command to navigate to the src folder:

    `cd src`
8. Copy the following command to install all dependencies

    `chmod +x install_dependencies.sh`

    `./install_dependencies.sh`
9. There are five other executable files you can choose to, each with different purposes. Please go the [command line argments section](#command-line-argments-to-execute-the-program) below.


## Dependencies

---

Please install all modules within the [Requirement.txt](../src/requirement.txt)

## System requirements

---
No requirements

## Command line argments to execute the program

---
There are five executable files you can choose to run the file.

Note: You have to use `chmod +x file name` to obtain permissions before running the following commands.
file name is the `xxxxx.sh`

* start_system.sh

    `Command: ./start_system.sh`

    You should run this file first to set the password of your system.
    And check whether you have installed python properly.
    Then you can chose any of the three below

* full_options.sh
  
    `Command: ./full_options.sh`

    This file will run the whole system.
* order_only.sh
  
    `Command: ./order_only.sh`

    This file will only allow you to order stickers for the customer.

* display_info.sh

    `Command: ./display_info.sh`

    This fille will only display selected customer's information.

* help.sh
  
    `Command: ./help.sh`

    This file will display the content of this help document.

## Features

---

* Collect customer's information
* Order stickers and print receipt
* Allow customers to join membership and obtain discount
* Display existing customers' information
* Welcome page of the app
* Display customer order history
* Display all products
* Add and update menu
