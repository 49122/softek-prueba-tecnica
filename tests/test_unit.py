"""Testing module using pytest"""
from validations.data_validations import customer_order_status_data_validation

valid_data = [
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

not_valid_data_strings = [
        "ORD_1567", "LAPTOP", "SHIPPED",
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


not_valid_data_len = [
       [ "ORD_1567", "LAPTOP", "SHIPPED"],
       [ "ORD_1567", "MOUSE", "SHIPPED"],
       [ "ORD_1567", "KEYBOARD", "PENDING"],
       [ "ORD_1234", "GAME"],
       [ "ORD_1234", "BOOK", "CANCELLED"],
       [ "ORD_1234", "BOOK", "CANCELLED"],
       [ "ORD_9834", "SHIRT", "SHIPPED"],
       [ "ORD_9834", "PANTS", "CANCELLED"],
       [ "ORD_7654", "TV", "CANCELLED"],
       [ "ORD_7654", "DVD", "CANCELLED"]
    ]

not_valid_data_type = [
       [ "ORD_1567", "LAPTOP", "SHIPPED"],
       [ "ORD_1567", "MOUSE", "SHIPPED"],
       [ "ORD_1567", "KEYBOARD", "PENDING"],
       [ "ORD_1234", "GAME", "SHIPPED"],
       [ "ORD_1234", 1, "CANCELLED"],
       [ "ORD_1234", "BOOK", "CANCELLED"],
       [ "ORD_9834", "SHIRT", "SHIPPED"],
       [ "ORD_9834", "PANTS", "CANCELLED"],
       [ "ORD_7654", "TV", "CANCELLED"],
       [ "ORD_7654", "DVD", "CANCELLED"]
    ]

"""
For the following test we'll be testing:
"Given" different types of data
"When" we get a request to our service /customer-order-status
"Then" we validate the data and decide if we will be able to continue
"""

def test_valid_data():
    """Test to validate the correct functioning of our data validator"""

    assert customer_order_status_data_validation(valid_data) is True

def test_not_valid_data_strings():
    """Test to validate the correct functioning of our data validator"""

    assert customer_order_status_data_validation(not_valid_data_strings) is False

def test_not_valid_data_len():
    """Test to validate the correct functioning of our data validator"""

    assert customer_order_status_data_validation(not_valid_data_len) is False

def test_not_valid_data_type():
    """Test to validate the correct functioning of our data validator"""

    assert customer_order_status_data_validation(not_valid_data_type) is False
