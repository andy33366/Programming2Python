import datetime

class Loan:
    def __init__(self, principal, years, rate):

        self.years = years

        self.principal = principal

        self.rate = rate / 100

        self.date = datetime.date.today()

    def getPrincipal(self):

        return self.principal

    def getYears(self):

        return self.years
 
    def getDate(self):

        return self.date

    def getMonthlyPayment(self):

        monthlyRate = self.rate / 12

        return (self.principal * monthlyRate * (1 + monthlyRate) ** (self.years * 12))/((1+monthlyRate) ** (self.years * 12 - 1))

    def getTotalPayment(self):
        return self.getMonthlyPayment() * self.years * 12


