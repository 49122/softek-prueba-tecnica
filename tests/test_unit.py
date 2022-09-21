"""Testing module using pytest"""
from validations.data_validations import customer_order_status_data_validation
from validations.data_validations import seasons_data_validation
from validations.seasons_validations import get_season

valid_data_customer_order_status = [
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

not_valid_data_str_customer_order_status = [
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


not_valid_data_len_customer_order_status = [
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

not_valid_data_type_customer_order_status = [
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

valid_data_seasons = [
       [ "113-8909896-6940269", "9/23/19", 1],
       [ "114-0291773-7262677", "1/1/20", 1],
       [ "114-0291773-7262697", "12/5/19", 1],
       [ "114-9900513-7761000", "9/24/20", 1],
       [ "112-5230502-8173028", "1/30/20", 1],
       [ "112-7714081-3300254", "5/2/20", 1],
       [ "114-5384551-1465853", "4/2/20", 1],
       [ "114-7232801-4607440", "10/9/20", 1]
    ]

not_valid_data_dtypes_seasons = [
       [ "113-8909896-6940269", "9/23/19", 1],
       [ "114-0291773-7262677", "1/1/20", "1"],
       [ "114-0291773-7262697", "12/5/19", 1],
       [ "114-9900513-7761000", "9/24/20", 1],
       [ "112-5230502-8173028", "1/30/20", 1],
       [ "112-7714081-3300254", "5/2/20", 1],
       [ "114-5384551-1465853", "4/2/20", 1],
       [ "114-7232801-4607440", "10/9/20", 1]
    ]

not_valid_data_date_seasons = [
       [ "113-8909896-6940269", "9/23/19", 1],
       [ "114-0291773-7262677", "1/1/20", 1],
       [ "114-0291773-7262697", "12/5/19", 1],
       [ "114-9900513-7761000", "20/24/20", 1],
       [ "112-5230502-8173028", "1/30/20", 1],
       [ "112-7714081-3300254", "5/2/20", 1],
       [ "114-5384551-1465853", "4/2/20", 1],
       [ "114-7232801-4607440", "10/9/20", 1]
    ]

"""
For the following test we'll be testing:
"Given" different types of data
"When" we get a request to our services
"Then" we validate the data and decide if we will be able to continue
"""

# Customer oreder status
def test_valid_data_customer_order_status():
    """Test to validate the correct functioning of our data validator"""

    assert customer_order_status_data_validation(valid_data_customer_order_status) is True

def test_not_valid_data_strings_customer_order_status():
    """Test to validate the correct functioning of our data validator"""

    assert customer_order_status_data_validation(not_valid_data_str_customer_order_status) is False

def test_not_valid_data_len_customer_order_status():
    """Test to validate the correct functioning of our data validator"""

    assert customer_order_status_data_validation(not_valid_data_len_customer_order_status) is False

def test_not_valid_data_type_customer_order_status():
    """Test to validate the correct functioning of our data validator"""

    assert customer_order_status_data_validation(not_valid_data_type_customer_order_status) is False

# Seasons
def test_valid_data_seasons():
    """Test to validate the correct functioning of our data validator"""

    assert seasons_data_validation(valid_data_seasons) is True

def test_not_dtypes_valid_data_seasons():
    """Test to validate the correct functioning of our data validator"""

    assert seasons_data_validation(not_valid_data_dtypes_seasons) is False

def test_not_valid_date():
    """Test to validate the correct date format"""

    assert seasons_data_validation(not_valid_data_date_seasons) is False
