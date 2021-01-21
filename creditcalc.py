import math
import argparse

DIFFERENCE = 'diff'
ANNUITY = 'annuity'


def initialize(arguments):
    if arguments.type is None:
        print("Incorrect parameters")
    else:
        determine_type_of_calculation(arguments)


def is_calculating_differentiated_payments(arguments):
    return arguments.type is not None and arguments.principal is not None and arguments.periods is not None and arguments.interest is not None


def is_calculate_how_long_it_will_take_to_repay_loan(arguments):
    return arguments.principal is not None and arguments.payment is not None and arguments.interest is not None


def determine_type_of_calculation(arguments):
    if arguments.type == DIFFERENCE and arguments.payment is not None:
        print("Incorrect parameters")
    elif arguments.type == ANNUITY and arguments.interest is None:
        print("Incorrect parameters")
    elif arguments.type == ANNUITY:
        if arguments.principal is None:
            loan_principal(arguments.payment, arguments.periods, calculate_nominal(arguments.interest))
        elif is_calculate_how_long_it_will_take_to_repay_loan(arguments):
            how_long_it_will_take(arguments.principal, arguments.payment, arguments.interest)
        else:
            calculate_the_annuity_payment(arguments.principal, arguments.periods, calculate_nominal(arguments.interest))
    else:
        if is_calculating_differentiated_payments(arguments):
            differentiated_payments(arguments.principal, arguments.periods, arguments.interest)


def generate_message_number_payments(years, months):
    if years == 0 and months > 0:
        return f"It will take 1 year and 0 months to repay this loan!"
    elif years >= 1 and months == 0:
        return f"It will take {years} years repay this loan!"
    else:
        return f"It will take {years} years and {months} months to repay this loan!"


def calculate_nominal(interest):
    return interest / (12 * 100)


def calculate_first_part(interest, periods):
    return interest * (math.pow(1 + interest, periods))


def calculate_second_part(interest, periods):
    return (math.pow(1 + interest, periods)) - 1


def calculate_overpayment(principal, total):
    return f"Overpayment = {total - principal}"


def calculate_day_payment(principal, periods, interest, day):
    i = calculate_nominal(interest)
    return math.ceil((principal / periods) + i * (principal - ((principal * (day - 1)) / periods)))


# calculating differentiated payments
def differentiated_payments(principal, periods, interest):
    total_credit_worth = 0
    for day in range(periods + 1):
        if day == 0:
            continue
        day_payment = calculate_day_payment(principal, periods, interest, day)
        print(f"Month {day}: payment is {day_payment}")
        total_credit_worth += day_payment
    print(f"Overpayment = {total_credit_worth - principal}")


# calculate the annuity payment
def calculate_the_annuity_payment(principal, periods, interest):
    total = math.ceil(principal * (calculate_first_part(interest, periods) / calculate_second_part(interest, periods)))
    print(f"Your monthly payment = {total}!")
    print(f"Overpayment = {(total * periods) - principal}")


# calculate loan principal
def calculate_loan_principal(annuity, periods, interest):
    return math.floor(annuity / (calculate_first_part(interest, periods) / calculate_second_part(interest, periods)))


def loan_principal(payment, periods, interest):
    principal = calculate_loan_principal(payment, periods, calculate_nominal(interest))
    print(f"Your loan principal = {principal}!")
    print(calculate_overpayment(principal, payment * periods))


# calculate how long it will take to repay a loan
def calculate_number_payments(principal, monthly_payment, interest):
    return math.ceil(math.log(monthly_payment / (monthly_payment - (interest * principal)), 1 + interest))


def how_long_it_will_take(principal, payment, interest):
    total_month = calculate_number_payments(principal, payment, calculate_nominal(interest))
    duration_loan = divmod(total_month, 12)
    print(generate_message_number_payments(duration_loan[0], duration_loan[1]))
    print(calculate_overpayment(principal, payment * total_month))


parser = argparse.ArgumentParser()
parser.add_argument('--type', '--type', type=str)
parser.add_argument('--principal', '--principal', type=int)
parser.add_argument('--periods', '--periods', type=int)
parser.add_argument('--interest', '--interest', type=float)
parser.add_argument('--payment', '--payment', type=int)
args = parser.parse_args()

# Run program
initialize(args)
