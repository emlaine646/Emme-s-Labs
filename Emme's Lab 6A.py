# ---------------- SOURCE ----------------------------------------
"""This lab is our introduction to classes where we create a costumer who makes different purchases.  I made a class called
Customer which tracks the amount of money spent, the number of purchases, and the gift credit (gift credit is earned 
when 100$ is spent AND 3 purchases are made).  Some logic I used was making sure the amount in makePurchase is always
either a float or integer.  I also made sure that it didn't go through with the purchase if amount was negative.
"""

class Customer:
    #encapsulates a data object

    # intended class constants
    DEFAULT_PURCH_AMT = 0
    DEFAULT_NUM_PURCH = 0
    DEFAULT_GIFT_CERT = 0
    PURCH_BONUS_NUM = 3
    PURCH_BONUS_AMT = 100
    GIFT_CERT = 10

    def __init__(self, pAmt=DEFAULT_PURCH_AMT, numP=DEFAULT_NUM_PURCH, gCert=DEFAULT_GIFT_CERT):
        if not self.set_pAmt(pAmt):
            self._pAmt = Customer.DEFAULT_PURCH_AMT
        if not self.set_numP(numP):
            self._numP = Customer.DEFAULT_NUM_PURCH
        if not self.set_gCert(gCert):
            self._gCert = Customer.DEFAULT_GIFT_CERT

    # mutator ("set") methods
    def makePurchase(self, amount):
        # Validate incoming purchase amount
        if type(amount) not in [int, float] or amount <= 0:
            return False
        # Accumulate the purchase amount
        self._pAmt += amount
        self._numP += 1
        # Check if gift bonus condition is met
        if self._pAmt >= Customer.PURCH_BONUS_AMT and self._numP > Customer.PURCH_BONUS_NUM:
            self.giftReached()
            return True

        return False

    def giftReached(self):
        self._gCert += Customer.GIFT_CERT
        self.set_pAmt(Customer.DEFAULT_PURCH_AMT, True)
        self.set_numP(Customer.DEFAULT_NUM_PURCH, True)
    #
    def to_string(self):
        return f"Purchase Amount: {self._pAmt} Num Purchases: {self._numP} Gift-Credit: {self._gCert}"

    # accessor ("get") methods
    def get_pAmt(self):
        return self._pAmt

    def get_numP(self):
        return self._numP

    def get_gCert(self):
        return self._gCert

    # mutator ("set") methods
    #Set method for pAmt
    def set_pAmt(self, amount, clear=False):
        if clear:
            self._pAmt = Customer.DEFAULT_PURCH_AMT
            return True
        if type(amount) in [int, float] and amount > 0:
            self._pAmt = amount
            return True
        return False
    #Set method for numP
    def set_numP(self, amount, clear=False):
        if clear:
            self._numP = Customer.DEFAULT_NUM_PURCH
            return True
        if type(amount) in [int, float] and amount > 0:
            self._numP = amount
            return True
        return False
    #set method for gCert
    def set_gCert(self, amount, clear=False):
        if clear:
            self._gCert = Customer.DEFAULT_GIFT_CERT
            return True
        if type(amount) in [int, float] and amount > 0:
            self._gCert = amount
            return True
        return False


def main():
    #prints the costumer purchase history
    Cust_1 = Customer(10, 0, 0)
    print(Cust_1.to_string())
    Cust_1.makePurchase(100)
    print(Cust_1.to_string())
    Cust_1.makePurchase(60)
    print(Cust_1.to_string())
    Cust_1.makePurchase(40)
    print(Cust_1.to_string())
    Cust_1.makePurchase(-40)
    print(Cust_1.to_string())
    Cust_1.makePurchase(100)
    print(Cust_1.to_string())
    Cust_1.makePurchase(100)
    print(Cust_1.to_string())
    Cust_1.makePurchase(100)
    print(Cust_1.to_string())
    Cust_1.makePurchase(100)
    print(Cust_1.to_string())
    Cust_1.makePurchase("hello")
    print(Cust_1.to_string())
    Cust_1.makePurchase(100)
    print(Cust_1.to_string())


main()


