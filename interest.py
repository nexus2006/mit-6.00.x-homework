new_balance = balance
monthly_interest_rate = annualInterestRate/12
monthly_rate = monthlyPaymentRate
paid = 0

def print_data(month, min_due, balance):
    month_str = "Month: "
    payment_str = "Minimum monthly payment: "
    balance_str = "Remaining balance: "
    
    print(month_str + str(month))
    print(payment_str + str(round(min_due,2)))
    print(balance_str + str(round(balance,2)))

def end_year(total_pay, year_end_balance):
    total_str = "Total paid: "
    balance_str = "Remaining balance: "
    
    print(total_str + str(round(total_pay,2)))
    print(balance_str + str(round(year_end_balance,2)))

def calculate_min_payment(balance,rate):
    return balance*rate

def update_balance(paid, balance):
    return balance-paid

def calc_interest(rate, balance):
    return balance + (rate*balance)

for month in range(1,13):
    month_due = calculate_min_payment(new_balance,monthly_rate)
    new_balance = update_balance(month_due, new_balance)
    new_balance = calc_interest(monthly_interest_rate, new_balance)
    paid += month_due
    print_data(month, month_due, new_balance)
end_year(paid, new_balance)
