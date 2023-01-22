from sys import exit
from math import e,log

def present(cashflow=None, interest=None, time=None):
    '''
    Function to calculate present value of cashflow with given interest and time
    '''

    pv = -1

    try:

        if cashflow < 0:
            print("Cashflow can't be negative")
        elif interest < 0:
            print("interest can't be negative")
        elif time < 0:
            print("time can't be negative")
    except (ValueError, TypeError) as e:
        print("Make sure the values makes sense")
        exit(100)

    pv = cashflow/(1+interest/100)**time
    return pv

def future(cashflow = 0 , rate= 0, time = 0):

    return cashflow * (1 + rate)**time

def effective_rate(apr = None, frequency = 1):

    if frequency == 1:
        return apr

    if frequency >  10**6:
        return e**(apr) - 1
    
    return (1 + apr/frequency)**frequency - 1


def annuity(cashflow = None, interest = None, time = None, growth = 0):

    pv_a = 1/(interest - growth)

    pv_b = ((1 + growth)**time)/(interest - growth) * 1/((1+interest)**time)

    return cashflow * (pv_a - pv_b), (pv_a - pv_b)

def perpetuity(cashflow = None, interest = None, delay = None, growth = 0):

    return cashflow/(interest - growth)

