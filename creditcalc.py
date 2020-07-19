
# write your code here
import math
import sys

args = sys.argv
type = ''
credit_principal, months, credit_interest, month_payment = 0, 0, 0, 0
for el in args:
    if el.startswith('--type='):
        type = el[7:]
    if el.startswith('--principal='):
        credit_principal = float(el[12:])
    if el.startswith('--periods='):
        months = int(float(el[10:]))
    if el.startswith('--interest='):
        credit_interest = float(el[11:]) / (12 * 100)
    if el.startswith('--payment='):
        month_payment = float(el[10:])

if type == 'diff':
    # calculate differentiated payments
    if credit_principal > 0 and months > 0 and credit_interest > 0:
        sum = 0
        for month in range(1, months + 1):
            diff_payment = math.ceil(credit_principal / months + credit_interest * (credit_principal - (credit_principal * (month - 1) / months)))
            sum += diff_payment
            print(f'Month {month}: paid out {diff_payment}')
        print()
        print(f'Overpayment = {int(sum - credit_principal)}')
    else:
        print('Incorrect parameters')
elif type == 'annuity':
    # calculate annuity payment
    if credit_principal > 0 and months > 0 and credit_interest > 0 and month_payment == 0:
        # calculate annuity payment for period with principal and interest
        annuity_payment = math.ceil(credit_principal * (credit_interest * math.pow((1 + credit_interest), months) / (math.pow((1 + credit_interest), months) - 1)))
        print(f'Your annuity payment = {annuity_payment}!')
        print(f'Overpayment = {math.ceil(annuity_payment * months - credit_principal)}')
    elif credit_principal == 0 and months > 0 and credit_interest > 0 and month_payment > 0:
        # calculate credit principal
        credit_principal = math.floor(month_payment / (credit_interest * math.pow((1 + credit_interest), months) / (math.pow((1 + credit_interest), months) - 1)))
        print(f'Your credit principal = {credit_principal}!')
        print(f'Overpayment = {int(month_payment * months - credit_principal)}')
    elif credit_principal > 0 and months == 0 and credit_interest > 0 and month_payment > 0:
        # calculate how much time user needs to repay
        months = math.ceil(math.log((month_payment / (month_payment - credit_interest * credit_principal)), (1 + credit_interest)))
        if months < 12:
            print(f'You need {months} months to repay this credit!')
        else:
            if months % 12 == 0:
                print(f'You need {months // 12} years to repay this credit!')
            else:
                print(f'You need {months // 12} years and {months % 12} months to repay this credit!')
        print(f'Overpayment = {int(months * month_payment - credit_principal)}')

    else:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')




# print('What do you want to calculate?')
# print('type "n" - for count of months,')
# print('type "a" - for annuity monthly payment,')
# print('type "p" - for monthly payment:')
# user_choose = input()
# if user_choose == 'n':
#     print('Enter the credit principal:')
#     credit_principal = float(input())
#     print('Enter monthly payment:')
#     monthly_payment = float(input())
#     print('Enter credit interest:')
#     credit_interest = float(input()) / (12 * 100)
#     months = math.ceil(math.log((monthly_payment / (monthly_payment - credit_interest * credit_principal)), (1 + credit_interest)))
#     if months < 12:
#         print(f'You need {months} months to repay this credit!')
#     else:
#         if months % 12 == 0:
#             print(f'You need {months // 12} years to repay this credit!')
#         else:
#             print(f'You need {months // 12} years and {months % 12} months to repay this credit!')
# elif user_choose == 'a':
#     print('Enter the credit principal:')
#     credit_principal = float(input())
#     print('Enter count of periods:')
#     months = int(input())
#     print('Enter credit interest:')
#     credit_interest = float(input()) / (12 * 100)
#     annuity_payment = credit_principal * (credit_interest * math.pow((1 + credit_interest), months) / (math.pow((1 + credit_interest), months) - 1))
#     print(f'Your annuity payment = {math.ceil(annuity_payment)}')
# elif user_choose == 'p':
#     print('Enter monthly payment:')
#     monthly_payment = float(input())
#     print('Enter count of periods:')
#     months = int(input())
#     print('Enter credit interest:')
#     credit_interest = float(input()) / (12 * 100)
#     credit_principal = monthly_payment / (credit_interest * math.pow((1 + credit_interest), months) / (math.pow((1 + credit_interest), months) - 1))
#     print(f'Your credit principal = {math.floor(credit_principal)}!')
