# PROBLEM:

# At a lemonade stand, each lemonade costs $5. 
# Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). 
# Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. 
# You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

# Note that you do not have any change in hand at first.

# Given an integer array bills where bills[i] is the bill the ith customer pays, 
# return true if you can provide every customer with the correct change, or false otherwise.

# Example:

# Input: bills = [5,5,5,10,20]
# Output: true
# Explanation: 
# From the first 3 customers, we collect three $5 bills in order.
# From the fourth customer, we collect a $10 bill and give back a $5.
# From the fifth customer, we give a $10 bill and a $5 bill.
# Since all customers got correct change, we output true.

# OUTPUT:

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change_5 = 0
        change_10 = 0

        for i in bills:
            if i == 5:
                change_5 += 1
            elif i == 10:
                if change_5 > 0:
                    change_5 -= 1
                    change_10 += 1
                else:
                    return False
            elif i == 20:
                if change_10 > 0 and change_5 > 0:
                    change_10 -= 1
                    change_5 -= 1
                elif change_5 >= 3:
                    change_5 -= 3
                else:
                    return False

        return True
