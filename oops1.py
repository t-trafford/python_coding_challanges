class Line:

    def __init__(self, cor1, cor2):
        self.cor1 = cor1
        self.cor2 = cor2

    def distance(self):

        return ((self.cor2[0] - self.cor1[0])**2 +  (self.cor2[1] - self.cor1[1])**2)**0.5


    def slop(self):

        return (self.cor2[1]-self.cor1[1])/(self.cor2[0]-self.cor1[0])

cordi1 = (3,2)
cordi2 = (8,10)


li = Line(cordi1, cordi2)
li.distance()
li.slop()

x = li.distance(), li.slop()
print(x)

class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):

        return "Account owner " +  str(self.owner) + " Balance " + str(self.balance)

    def deposite(self, amount):

        self.balance = self.balance+amount
        return "current bal " + str(self.balance)


    def withdraw(self, amount):

        if self.balance-amount < 0:
            return "dont try to get money"

        else:
            self.balance = self.balance - amount
            return "current bal " + str(self.balance)

acct1 = Account("john", 100)
print(acct1)

x = acct1.deposite(50)
print(x)

x = acct1.withdraw(100)
print(x)

x = acct1.withdraw(300)
print(x)



