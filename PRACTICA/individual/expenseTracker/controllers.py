import datetime

types = ["food","transport","entertaining","unexpected","clothes","other"]

def check_type(type): 
    if type not in types:
        print("Invalid type")
        return False
    return True

def check_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print("Invalid date")
        return False
    return True

def check_amount(amount):
    try:
        float(amount)
    except ValueError:
        print("Invalid amount")
        return False
    return True
