class Atm:
  def __init__(self, cardnumber, pin): 
    self.cardnumber = cardnumber
    self.pin = pin

  def balancecheck(self):
     print("Your balance is: $900")

  def moneywidthdrawal (self, amount):
      new_amount = 100-amount
      print("You withdrawed: " + str(amount) +" Your remaining balance is: "+ str(new_amount))

def main():
        name = input("Hello what is your name?")
        print("Hello, "+ name)
        cardnumber = input("Insert your card number: ") 
        pin = input("Enter your pin: ") 
        new_user = Atm(cardnumber, pin)

        print("Choose your activity")
        print("1. Balance Check") 
        print("2. money Withdrawal")
        activity = int(input("Enter activity choice: "))

        if (activity == 1):
            new_user.balancecheck()
        elif (activity == 2):
            amount = int(input("Enter the amount: "))
            new_user.moneywidthdrawal (amount)
            
        else:
           print("Enter a valid number")

if __name__=="__main___":
 main()

