"""Data validation file"""
# Imports
from datetime import datetime

def detecting_change_data_validation(data):
    """
    Utility: data validating function for our service /detecting-change
    Data structure should look like this:
    {
        "data": [
        ["1/1/20", "False"],
        ["1/2/20", "TRUE"],
        ["1/3/20", "TRUE"],
        ["1/4/20", "False"],
        ["1/5/20", "False"],
        ["1/6/20", "TRUE"],
        ["1/7/20", "False"],
        ["1/8/20", "TRUE"],
        ["1/9/20", "TRUE"],
        ["1/10/20", "TRUE"]
        ]
    }
    """
    # Expected date format
    date_format = "%m/%d/%y"

    # First validation comes in the form of a type check; making sure our data wrapper "data"...
    # its a list other wise we return false that is latter understood as an error on the data.
    if not isinstance(data,list):
        return False

    # iterating over the data
    for instance in data:
        # Inside of our wrapper "data" we should have multiple lists and we know that each...
        # list should have a lenght of 3 for "order number", "item name" nd "status"
        if (not isinstance(instance,list)) or (len(instance) != 2):
            return False

        # checking each object within the list for the correct data type
        if (not isinstance(instance[0],str)) or (not isinstance(instance[1],str)):
            return False

        try:
            datetime.strptime(instance[0], date_format)
        except ValueError as exp:
            print(exp)
            print("This is the incorrect date string format. It should be %m/%d/%y")
            return False

    return True

def seasons_data_validation(data):
    """
    Utility: data validating function for our service /seasons
    Data structure should look like this:
    {
        "data": [
        [ "113-8909896-6940269", "9/23/19", 1],
        [ "114-0291773-7262677", "1/1/20", 1],
        [ "114-0291773-7262697", "12/5/19", 1],
        [ "114-9900513-7761000", "9/24/20", 1],
        [ "112-5230502-8173028", "1/30/20", 1],
        [ "112-7714081-3300254", "5/2/20", 1],
        [ "114-5384551-1465853", "4/2/20", 1],
        [ "114-7232801-4607440", "10/9/20", 1]
        ]
    }
    """
    # First validation comes in the form of a type check; making sure our data wrapper "data"...
    # its a list other wise we return false that is latter understood as an error on the data.
    if not isinstance(data,list):
        return False

    # Expected date format
    date_format = "%m/%d/%y"

    # iterating over the data
    for instance in data:
        # Inside of our wrapper "data" we should have multiple lists and we know that each...
        # list should have a lenght of 3 for "order number", "item name" nd "status"
        if (not isinstance(instance,list)) or (len(instance) != 3):
            return False

        # checking each object within the list for the correct data type
        if (not isinstance(instance[0],str)) or (not isinstance(instance[1],str)):
            return False

        if not isinstance(instance[2],int):
            return False

        # Well try to convert the given string to a date to confirm that it has a valid format
        # in case it does not work we will print the information and return false so 
        # that we can handle the error latter on
        try:
            datetime.strptime(instance[1], date_format)
        except ValueError as exp:
            print(exp)
            print("This is the incorrect date string format. It should be %d/%m/%y")
            return False

    #if we pass all validations for evey entry then we return True which is understood as a succes
    return True

def customer_order_status_data_validation(data):
    """"
    Utility: data validating function for our service /customer-order-status
    Data structure should look like this:
    {
        "data": [
        [ "ORD_1567", "LAPTOP", "SHIPPED"],
        [ "ORD_1567", "MOUSE", "SHIPPED"],
        [ "ORD_1567", "KEYBOARD", "PENDING"],
        [ "ORD_1234", "GAME", "SHIPPED"],
        [ "ORD_1234", "BOOK", "CANCELLED"],
        [ "ORD_1234", "BOOK", "CANCELLED"],
        [ "ORD_9834", "SHIRT", "SHIPPED"],
        [ "ORD_9834", "PANTS", "CANCELLED"],
        [ "ORD_7654", "TV", "CANCELLED"],
        [ "ORD_7654", "DVD", "CANCELLED"]
        ]
    }
    """
    # First validation comes in the form of a type check; making sure our data wrapper "data"...
    # its a list other wise we return false that is latter understood as an error on the data.
    if not isinstance(data,list):
        return False

    # iterating over the data
    for instance in data:

        # Inside of our wrapper "data" we should have multiple lists
        if not isinstance(instance,list):
            return False
        # we know that each list should have a lenght of 3 for "order number", "item name" ...
        # and "status"
        if len(instance) != 3:
            return False
        # also each object within the list should be a string
        if not all(isinstance(value, str) for value in instance):
            return False

    #if we pass all validations for evey order then we return True which is understood as a succes
    return True
