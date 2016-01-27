balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


def calculateMonthlyInterestRate(annualInterestRate):
    return annualInterestRate / 12.0

def calculateMinimumMonthlyPayment(balance):
    return 0.02 * balance

def calculateMonthlyUnpaidBalance(balance, payment):
    return balance - payment

def calculateUnpaid


monthlyInterestRate = calcMonthlyInterestRate(annualInterestRate)
