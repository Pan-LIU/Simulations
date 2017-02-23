### python exam project: investors simulations
### author: Pan LIU from M2 FiRE IAE Toulouse

##Part 1: Modelling bond

from math import *

class bond(object):
    def __init__(self, amount, term,price,interest_rate,mini_term):
        self.amount = amount
        self.term = term
        self.price = price
        self.interest_rate = interest_rate
        self.mini_term = mini_term

    def final_value(self,amount,interest_rate, term):
        self.amount = amount
        self.term = term
        self.interest_rate = interest_rate
        return amount * exp(interest_rate * term)

class short_term_bond(bond):
    def final_value(self,amount,interest_rate, term):
        return super(short_term_bond,self).final_value(amount, interest_rate,term)

class long_term_bond(bond):
    def final_value(self,amount,interest_rate, term):
        return super(long_term_bond,self).final_value(amount, interest_rate,term)

short_term_bond1 = short_term_bond(1000, 2, 1000, 0.01, 2 )
print(short_term_bond1.final_value(1000,0.01,2))






