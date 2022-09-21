"""Flask Aplication for softtek"""

# Flask imports
from flask import Flask, request
# utilities
from validations.data_validations import customer_order_status_data_validation

app = Flask(__name__)


@app.route('/customer-order-status', methods=['GET'])
def customer_order_status():
    """A dummy docstring."""

    if request.json["data"]:
        val_data = customer_order_status_data_validation(request.json["data"])
    else:
        return "No data recieved"

    if not val_data:
        return "Data recieved does not have the proper structure"

    customer_orders = request.json["data"]

    oder_grouped = dict()

    for order in customer_orders:

        if(order[0] in oder_grouped) and (oder_grouped[order[0]] == "PENDING"):
            continue

        if not order[0] in oder_grouped:
            oder_grouped[order[0]] = "CANCELLED"

        if order[2] == "PENDING":
            oder_grouped[order[0]] = "PENDING"

        if order[2] == "SHIPPED":
            oder_grouped[order[0]] = "SHIPPED"

    return oder_grouped
