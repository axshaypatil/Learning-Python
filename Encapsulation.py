'''

__    (Double underscore is used to private variable)


'''


# class BankAccount:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

#     def readpass(self):
#         print(self.__acc_pass)



# acc = BankAccount(1234,6789)
# print(acc.acc_no)
# # print(acc.acc_pass)  #this will give error because it is private
# acc.readpass()




class BankAccount:
    def __init__(self, Balance):
        self.__Balance = Balance
      

    def credit(self,amount):
        self.__Balance += amount
        print(f"Balance after adding {amount} is {self.__Balance}")
   
    def debit(self,amount):
        if self.__Balance > amount:
            self.__Balance -= amount
            print(f"Balance after withdraw {amount} is {self.__Balance}")
        else:
            print("low balance to debit paisa kama")


acc = BankAccount(500)
acc.credit(500)
acc.debit(20000)