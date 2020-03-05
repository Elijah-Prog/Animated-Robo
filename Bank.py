# Animated-Robo

class OurDate:
    def __init__(self,dayMonth,Month,year):

        self.dayMonth = dayMonth
        self.Month = Month
        self.year = year

    def calcDays(self):
        if(year2 > year1):
            day = 365 - day1

            print("Number of days from day1 to End of year: ",day)

            if(year2 > year1 + 1):
                tempYr = year1 
                
                while(year2 > tempYr + 1):
                    newDate = tempYr + day

                    tempYr +=1
            global days
            days = day + (365 - day2)
            print("Total number of Days: ", days)

        else:
            if(year1 == year2):
                print("")

                days = 0

            if(month1 == month2):
                days = day2 - day1

            else:
                counter = 0
                
                lst1 = []
                
                while(month1 > counter):
                    
                    counter += 1
                    
                    lst1.append(counter)
                    if counter == month1:
                        print(lst1)
                days = len(lst1) - (day1 + 1) 

                for days in range(month1 + 1, month2 - 1):
                    days = days + len(lst1)

                days = days + day2

                print("Days Are between year1 and year2 : ", days)

                    
info1 = OurDate(23,12,2000)
info2 = OurDate(14,12,2000)

day1 = info1.dayMonth
day2 = info2.dayMonth

month1 = info1.Month
month2 = info2.Month

year1 = info1.year
year2 = info2.year

print( "Day1: ", day1,"Day2: ", day2,"Month1: ", month1,"Month2: ", month2 ,"Year1: ", year1,"Year2: ", year2)

OurDate.calcDays(OurDate)

class BankAccount(OurDate):
    def __init__(self,accountNo,Balance,accountHolder,dateOpened):
        self.accountNo = accountNo
        self.Balance = Balance
        self.accountHolder = accountHolder
        self.dateOpened = dateOpened    
   
    def SavingsAccountInt(self):

            interest = (Balance*(days/365))*days
       
            totalwithInt = Balance + interest
            
            return print(" Interest: ","R",interest,"\n","Total with Interest: ","R", totalwithInt ,"\n", "Account Holder: ", accountholder)
        
    def NoticeDepositAccount(self):
        
        keep = input("Withdraw or Leave or Deposit: ")
        
        if(keep == "Leave"):
            return interest1.SavingsAccountInt()
        
        else:
            #return print("Deducted Amount: ","R", Balance - 250)
            
            if( keep == "Withdraw"):
                amount = float(input("Enter amount to withdraw: "))
                
                print("Your Balance Now: ","R",Balance)
                
                if (amount > Balance):
                    return print("Amount Greater than Balance")
                
                if(amount <= Balance):
                    return print("Current Balance: ","R", Balance - amount)
            
            
            
            
            else:
                
                deposit = float(input("Enter Amount to Deposit: "))
                
                print("Your Balance Now: ","R", Balance)
                
                return print("Amount Deposited: ","R",deposit,"\n","Your Balance After Deposit: ","R",self.Balance + deposit)

accountNo = int(input("Account No: "))
BalanceAm = float(input("Balance: "))
AccH = input("Account Holder: ")


interest1 = BankAccount(accountNo,BalanceAm,AccH,12042019)
Balance = interest1.Balance
accountholder = interest1.accountHolder

print("_______________________________________________________________________")
print("TRANSACTION DETAILS FOR ", AccH)
print("_______________________________________________________________________")

interest1.NoticeDepositAccount()

print("_________________________________________")
print("THANK YOU FOR BANKING WITH US")
print("________________________________________")



