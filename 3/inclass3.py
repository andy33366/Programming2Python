import datetime
from Loan import Loan


today = datetime.date.today()

'''
year = int(input("ENter a year:"))
month = int(input("ENter a month:"))
day = int(input("ENter a day:"))

date1 = datetime.date(year, month, day)
'''

principal = float(input("What is the principal amount?"))

years = int(input("For how many years is the loan eing taken out?"))

rate = float(input("what is the rate as a percentage?"))


loan1 = Loan(principal, years, rate)

print(f"this is a loan for ${loan1.getPrincipal():.2f} taken out on {loan1.getDate()}")

print(f"this loan will be taken out for {loan1.getYears()} at {rate:.1f}%")

print(f"the monthly payments will be ${loan1.getMonthlyPayment():.2f}")

print(f"the total payment will be ${loan1.getTotalPayment():.2f}")





