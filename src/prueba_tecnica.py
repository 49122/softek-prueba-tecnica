"""Flask Aplication for softtek"""

# Flask imports
from flask import Flask, request
# utilities: data validation and seasons validation
from validations.data_validations import customer_order_status_data_validation
from validations.data_validations import seasons_data_validation
from validations.data_validations import detecting_change_data_validation
from validations.seasons_validations import get_season
from validations.detect_weather_change import sort_dates,change_detection

# Initialization of our flask application
app = Flask(__name__)

# Resource customer order status
@app.route('/customer-order-status', methods=['POST'])
def customer_order_status():
    """customer order status resource:
    expected body:
    {
        "data": [
            [str,],
        ]
    }
    expected response:
    {
        "order number": "STATUS",
    }
    """

    # We check if request has data in it, other wise we respond an error message
    if request.data:
        pass
    else:
        return {"response": "No data recieved"}, 400

    # Validating of the correct wrapper for our data, other wise we respond an error message
    if request.json["data"]:
        val_data = customer_order_status_data_validation(request.json["data"])
    else:
        return {"response": "Data recieved does not have the proper structure"}, 400

    # If the data structure is not valid we return an error message
    if not val_data:
        return {"response": "Data recieved does not have the proper structure"}, 400

    # creating the object that will contain the response information
    oder_grouped = dict()

    # iteration trough our validated data
    for order in request.json["data"]:

        # If we already know that this specific order number has an item on PENDING then...
        # we would already know that the overall status will be PENDING
        if(order[0] in oder_grouped) and (oder_grouped[order[0]] == "PENDING"):
            continue

        # CANCELLED orders only really matter if every single item under that  order number...
        # is CANCELLED other wise we would use either SHIPPED or PENDING depending on the...
        # next items
        if not order[0] in oder_grouped:
            oder_grouped[order[0]] = "CANCELLED"

        # If an item has the tag PENDING we should immediatly mark the order number as such
        # this will be recognized in next iterations that have the same order number
        if order[2] == "PENDING":
            oder_grouped[order[0]] = "PENDING"

        # If an item has the tag SHIPPED we should the order number as such
        if order[2] == "SHIPPED":
            oder_grouped[order[0]] = "SHIPPED"

    # Finally we send out our response object in the form of a dictionary that flask...
    # understands and parces to json
    return oder_grouped

@app.route('/seasons', methods=['POST'])
def seasons_problem():
    """a"""

    # We check if request has data in it, other wise we respond an error message
    if request.data:
        pass
    else:
        return {"response": "No data recieved"}, 400

    # Validating of the correct wrapper for our data, other wise we respond an error message
    if request.json["data"]:
        val_data = seasons_data_validation(request.json["data"])
    else:
        return {"response": "Data recieved does not have the proper structure"}, 400

    # If the data structure is not valid we return an error message
    if not val_data:
        return {"response": "Data recieved does not have the proper structure"}, 400

    # creating the object that will contain the response information
    response_obj = dict()

    #filling our response object with the information required
    for entry in request.json["data"]:
        response_obj[entry[0]] = get_season(entry[1])

    # Finally we send out our response object in the form of a dictionary that flask...
    # understands and parces to json
    return response_obj

@app.route('/detecting-change', methods=['POST'])
def detecting_change_problem():
    """a"""

    # We check if request has data in it, other wise we respond an error message
    if request.data:
        pass
    else:
        return {"response": "No data recieved"}, 400

    # Validating of the correct wrapper for our data, other wise we respond an error message
    if request.json["data"]:
        val_data = detecting_change_data_validation(request.json["data"])
    else:
        return {"response": "Data recieved does not have the proper structure"}, 400

    # If the data structure is not valid we return an error message
    if not val_data:
        return {"response": "Data recieved does not have the proper structure"}, 400

    # Sorting dates so that we can make sure the change in weather is relevant
    sorted_data = sort_dates(request.json["data"])

    # Creation of response object with te relevant change dates
    response_obj = change_detection(sorted_data)

    # Finally we send out our response object in the form of a dictionary that flask...
    # understands and parces to json
    return response_obj
