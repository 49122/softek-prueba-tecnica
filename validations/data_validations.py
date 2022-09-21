"""Data validation file"""

def customer_order_status_data_validation(data):
    """"Utility: data validating function for our service /customer-order-status"""
    if not isinstance(data,list):
        return False

    for instance in data:
        if not isinstance(instance,list):
            return False
        if len(instance) != 3:
            return False

        if not all(isinstance(value, str) for value in instance):
            return False

    return True
    