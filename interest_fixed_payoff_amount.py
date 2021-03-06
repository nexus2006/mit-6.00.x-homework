m_balance = balance
year_interest_rate = annualInterestRate

def sub_pay_from_balance(paid, balance):
    return balance-paid

def calc_interest(month_rate, balance):
    '''requires monthly interest rate float
    returns float of interest only'''
    return month_rate*balance

def try_payment(start_balance, payment, ap_rate, num_months):
    '''Takes float or int starting balance, fixed monthly payment, annual interest rate, and number of desired payments
    
    returns float remaining balance'''
    _bal = start_balance
    for month in range(0,num_months):
        _bal = sub_pay_from_balance(payment, _bal)
        _bal = _bal + calc_interest(ap_rate/12.0, _bal)
    return _bal

def calc_fixed_payment(bal_due, ap_rate, num_payments):
    working = True
    pay_amount = 10 #bal_due/num_payments
    while working:
        goal_balance = try_payment(bal_due, pay_amount, ap_rate, num_payments)
        if goal_balance > 0:
            pay_amount += 10
        else:
            working = False
    return pay_amount

def print_results(pay):
    out_str = "Lowest Payment: "
    print out_str + str(round(pay,2))

print_results(calc_fixed_payment(m_balance, year_interest_rate, 12))
