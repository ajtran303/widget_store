def calculate_price(quantity):
    try:
        if quantity <= 0 or type(quantity) is float:
            return 'Invalid quantity'
        elif 0 < quantity <= 10:
            return quantity * 10
        elif quantity < 20:
            return quantity * 9
        else:
            return quantity * 8
    except TypeError:
        return 'Invalid quantity'
