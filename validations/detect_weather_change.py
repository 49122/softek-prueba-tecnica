"""Detecting change i weather"""
from datetime import datetime

def sort_dates(data: list):
    """sorting dates

    Args:
        data (list): [
            ["1/3/20", "TRUE"],
            ["1/1/20", "FALSE"],
            ["1/2/20", "TRUE"],
            ["1/4/20", "FALSE"],
            ["1/5/20", "FALSE"],
            ["1/6/20", "TRUE"],
            ["1/7/20", "FALSE"],
            ["1/8/20", "TRUE"],
            ["1/9/20", "TRUE"],
            ["1/10/20", "TRUE"]
            ]

    returns:
        dates (list):  [
            ["1/1/20", "FALSE"],
            ["1/2/20", "TRUE"],
            ["1/3/20", "TRUE"],
            ["1/4/20", "FALSE"],
            ["1/5/20", "FALSE"],
            ["1/6/20", "FALSE"],
            ["1/7/20", "FALSE"],
            ["1/8/20", "TRUE"],
            ["1/9/20", "TRUE"],
            ["1/10/20", "TRUE"]
        ]
    """
    # sorting based on the dates using a lambda fucntion
    data.sort(key=lambda lista: datetime.strptime(lista[0], "%d/%m/%y"))
    return data

def change_detection(data):
    """
    detects change and creates a list of relevant dates
    Args: data(list): already sorted dates
    returns relavant_dates(list)
    """
    # variable used to keep track of the last state of the weather (FALSE or TRUE)
    last_bool_value = None
    # list for our relevant dates
    relavant_dates = []
    # iterating over our data
    for entry in data:
        # if the state of the last and present weather match the pattern then we append...
        # the relevant entry to our list
        if last_bool_value == "FALSE" and entry[1] == "TRUE":
            relavant_dates.append(entry)
        # here we keep track of the last weather status
        last_bool_value = entry[1]

    return relavant_dates
