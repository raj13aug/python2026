high_income = True
good_credit = True

if high_income and good_credit:
    print("Eliglible")
    
    
student = False

if not student:
    print("Eliglible")
else:
    print("non eglible")
    
    
high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("eliglible")
else:
    print("non eligblibe")
    
    """ In python logical operator are short circuit
    """