user_1 = 10
user_2 = 0
user_3 = 0
user_4 = 0
user_5 = 0
user_6 = 0
user_7 = 0
user_8 = 0
user_9 = 0
user_10 = 0
user_11 = 0
user_12 = 0
user_13 = 0
user_14 = 0
user_15 = 0
user_16 = 0
name_list = ["Account_1", "Account_2", "Account_3", "Account_4", "Account_5", "Account_6", "Account_7", "Account_8", "Account_9", "Account_10", "Account_11", "Account_12", "Account_13", "Account_14", "Account_15", "Account_16"]
def code():
 account = input("Which account would you like to access? ")
 if account == "Account_1":
     code_1 = input("Please input the access code. ")
     if code_1 == "1234":
         choice_1 = input("would you like to withdraw, deposit, or borrow money? ")
         if choice_1 == "withdraw":
             withdraw_1 = int(input("How much would you like to withdraw? "))
             user_1 -= withdraw_1
             print("{} has been deducted from your account".format(withdraw_1))
             print("Your balance is ${}".format(user_1))
         elif choice_1 == "deposit":
             deposit_1 = int(input("How much would you like to deposit? "))
             user_1 += deposit_1
             print("{} has been added to your account".format(deposit_1))
             print("Your balance is ${}".format(user_1))
         else:
             print("Please enter a valid option.")
     else:
         print("That code is incorrect.")

 elif account == "Account_2":
     code_2 = input("Please input the access code. ")
     if code_2 == "2345":
         choice_2 = input("would you like to withdraw, deposit, or borrow money? ")
         if choice_2 == "withdraw":
             withdraw_2 = int(input("How much would you like to withdraw? "))
             user_2 -= withdraw_2
             print("{} has been deducted from your account".format(withdraw_2))
             print("Your balance is ${}".format(user_2))
         elif choice_2 == "deposit":
             deposit_2 = int(input("How much would you like to deposit? "))
             user_2 += deposit_2
             print("{} has been added to your account".format(deposit_2))
             print("Your balance is ${}".format(user_2))
         else:
             print("Please enter a valid option.")
     else:
         print("That code is incorrect.")
 elif account == "Account_3":
     code_3 = input("Please input the access code. ")
     if code_3 == "3456":
         choice_3 = input("would you like to withdraw, deposit, or borrow money? ")
         if choice_3 == "withdraw":
             withdraw_3 = int(input("How much would you like to withdraw? "))
             user_3 -= withdraw_3
             print("{} has been deducted from your account".format(withdraw_3))
             print("Your balance is ${}".format(user_3))
         elif choice_3 == "deposit":
             deposit_3 = int(input("How much would you like to deposit? "))
             user_3 += deposit_3
             print("{} has been added to your account".format(deposit_3))
             print("Your balance is ${}".format(user_3))
         else:
             print("Please enter a valid option.")
     else:
         print("That code is incorrect.")
 elif account == "Account_4":
     code_4 = input("Please input the access code. ")
     if code_4 == "4567":
         choice_4 = input("would you like to withdraw, deposit, or borrow money? ")
         if choice_4 == "withdraw":
             withdraw_3 = int(input("How much would you like to withdraw? "))
             user_4 -= withdraw_4
             print("{} has been deducted from your account".format(withdraw_4))
             print("Your balance is ${}".format(user_4))
         elif choice_4 == "deposit":
             deposit_4 = int(input("How much would you like to deposit? "))
             user_4 += deposit_4
             print("{} has been added to your account".format(deposit_4))
             print("Your balance is ${}".format(user_4))
         else:
             print("Please enter a valid option.")
     else:
         print("That code is incorrect.")
 elif account == "Account_5":
     code_5 = input("Please input the access code. ")
     if code_5 == "5678":
         choice_5 = input("would you like to withdraw, deposit, or borrow money? ")
         if choice_5 == "withdraw":
             withdraw_5 = int(input("How much would you like to withdraw? "))
             user_5 -= withdraw_5
             print("{} has been deducted from your account".format(withdraw_5))
             print("Your balance is ${}".format(user_5))
         elif choice_5 == "deposit":
             deposit_5 = int(input("How much would you like to deposit? "))
             user_5 += deposit_5
             print("{} has been added to your account".format(deposit_5))
             print("Your balance is ${}".format(user_5))
         else:
             print("Please enter a valid option.")
     else:
         print("That code is incorrect.")
 elif account == "Account_6":
     code_6 = input("Please input the access code. ")
     if code_6 == "6789":
         choice_6 = input("would you like to withdraw, deposit, or borrow money? ")
         if choice_6 == "withdraw":
             withdraw_6 = int(input("How much would you like to withdraw? "))
             user_6 -= withdraw_6
             print("{} has been deducted from your account".format(withdraw_6))
             print("Your balance is ${}".format(user_6))
         elif choice_6 == "deposit":
             deposit_6 = int(input("How much would you like to deposit? "))
             user_6 += deposit_6
             print("{} has been added to your account".format(deposit_6))
             print("Your balance is ${}".format(user_6))
         else:
             print("Please enter a valid option.")
     else:
         print("That code is incorrect.")
 elif account == "Account_7":
     code_7 = input("Please input the access code. ")
     if code_7 == "7891":
         choice_7 = input("would you like to withdraw, deposit, or borrow money? ")
         if choice_7 == "withdraw":
             withdraw_7 = int(input("How much would you like to withdraw? "))
             user_7 -= withdraw_7
             print("{} has been deducted from your account".format(withdraw_7))
             print("Your balance is ${}".format(user_7))
         elif choice_7 == "deposit":
             deposit_7 = int(input("How much would you like to deposit? "))
             user_7 += deposit_7
             print("{} has been added to your account".format(deposit_7))
             print("Your balance is ${}".format(user_7))
         else:
             print("Please enter a valid option.")
     else:
         print("That code is incorrect.")
 elif account == "Account_8":
     code_8 = input("Please input the access code. ")
     if code_8 == "8910":
         choice_8 = input("would you like to withdraw, deposit, or borrow money? ")
         if choice_8 == "withdraw":
             withdraw_8 = int(input("How much would you like to withdraw? "))
             user_8 -= withdraw_8
             print("{} has been deducted from your account".format(withdraw_8))
             print("Your balance is ${}".format(user_8))
         elif choice_8 == "deposit":
             deposit_8 = int(input("How much would you like to deposit? "))
             user_8 += deposit_8
             print("{} has been added to your account".format(deposit_8))
             print("Your balance is ${}".format(user_8))
         else:
             print("Please enter a valid option.")
     else:
         print("That code is incorrect.")
 elif account == "Account_9":
     code_9 = input("Please input the access code. ")
     if code_9 == "9101":
         choice_9 = input("would you like to withdraw, deposit, or borrow money? ")
         if choice_9 == "withdraw":
             withdraw_9 = int(input("How much would you like to withdraw? "))
             user_9 -= withdraw_9
             print("{} has been deducted from your account".format(withdraw_9))
             print("Your balance is ${}".format(user_9))
         elif choice_9 == "deposit":
             deposit_9 = int(input("How much would you like to deposit? "))
             user_9 += deposit_9
             print("{} has been added to your account".format(deposit_9))
             print("Your balance is ${}".format(user_9))
         else:
             print("Please enter a valid option.")
     else:
         print("That code is incorrect.")
 elif account == "Account_10":
     code_10 = input("Please input the access code. ")
     if code_10 == "1011":
         choice_10 = input("would you like to withdraw, deposit, or borrow money? ")
         if choice_10 == "withdraw":
             withdraw_10 = int(input("How much would you like to withdraw? "))
             user_10 -= withdraw_10
             print("{} has been deducted from your account".format(withdraw_10))
             print("Your balance is ${}".format(user_10))
         elif choice_10 == "deposit":
             deposit_10 = int(input("How much would you like to deposit? "))
             user_10 += deposit_10
             print("{} has been added to your account".format(deposit_10))
             print("Your balance is ${}".format(user_10))
         else:
             print("Please enter a valid option.")
     else:
         print("That code is incorrect.")
 elif account == "Account_11":
     code_11 = input("Please input the access code. ")
     if code_11 == "1112":
         choice_11 = input("would you like to withdraw, deposit, or borrow money? ")
         if choice_11 == "withdraw":
             withdraw_11 = int(input("How much would you like to withdraw? "))
             user_11 -= withdraw_11
             print("{} has been deducted from your account".format(withdraw_11))
             print("Your balance is ${}".format(user_11))
         elif choice_11 == "deposit":
             deposit_11 = int(input("How much would you like to deposit? "))
             user_11 += deposit_11
             print("{} has been added to your account".format(deposit_11))
             print("Your balance is ${}".format(user_11))
         else:
             print("Please enter a valid option.")
     else:
         print("That code is incorrect.")
 elif account == "Account_12":
     code_12 = input("Please input the access code. ")
     if code_12 == "1213":
         choice_12 = input("would you like to withdraw, deposit, or borrow money? ")
         if choice_12 == "withdraw":
             withdraw_12 = int(input("How much would you like to withdraw? "))
             user_12 -= withdraw_12
             print("{} has been deducted from your account".format(withdraw_12))
             print("Your balance is ${}".format(user_12))
         elif choice_12 == "deposit":
             deposit_12 = int(input("How much would you like to deposit? "))
             user_12 += deposit_12
             print("{} has been added to your account".format(deposit_12))
             print("Your balance is ${}".format(user_12))
         else:
             print("Please enter a valid option.")
     else:
         print("That code is incorrect.")
 elif account == "Account_13":
     code_13 = input("Please input the access code. ")
     if code_13 == "1314":
         choice_13 = input("would you like to withdraw, deposit, or borrow money? ")
         if choice_13 == "withdraw":
             withdraw_13 = int(input("How much would you like to withdraw? "))
             user_13 -= withdraw_13
             print("{} has been deducted from your account".format(withdraw_13))
             print("Your balance is ${}".format(user_13))
         elif choice_13 == "deposit":
             deposit_13 = int(input("How much would you like to deposit? "))
             user_13 += deposit_13
             print("{} has been added to your account".format(deposit_13))
             print("Your balance is ${}".format(user_13))
         else:
             print("Please enter a valid option.")
     else:
         print("That code is incorrect.")
 elif account == "Account_14":
     code_14 = input("Please input the access code. ")
     if code_14 == "1415":
         choice_14 = input("would you like to withdraw, deposit, or borrow money? ")
         if choice_14 == "withdraw":
             withdraw_14 = int(input("How much would you like to withdraw? "))
             user_14 -= withdraw_14
             print("{} has been deducted from your account".format(withdraw_14))
             print("Your balance is ${}".format(user_14))
         elif choice_14 == "deposit":
             deposit_14 = int(input("How much would you like to deposit? "))
             user_14 += deposit_14
             print("{} has been added to your account".format(deposit_14))
             print("Your balance is ${}".format(user_14))
         else:
             print("Please enter a valid option.")
     else:
         print("That code is incorrect.")
 elif account == "Account_15":
     code_15 = input("Please input the access code. ")
     if code_15 == "1516":
         choice_15 = input("would you like to withdraw, deposit, or borrow money? ")
         if choice_15 == "withdraw":
             withdraw_15 = int(input("How much would you like to withdraw? "))
             user_15 -= withdraw_15
             print("{} has been deducted from your account".format(withdraw_15))
             print("Your balance is ${}".format(user_15))
         elif choice_15 == "deposit":
             deposit_15 = int(input("How much would you like to deposit? "))
             user_15 += deposit_15
             print("{} has been added to your account".format(deposit_15))
             print("Your balance is ${}".format(user_15))
         else:
             print("Please enter a valid option.")
     else:
         print("That code is incorrect.")
 elif account == "Account_16":
     code_16 = input("Please input the access code. ")
     if code_16 == "1617":
         choice_16 = input("would you like to withdraw, deposit, or borrow money? ")
         if choice_16 == "withdraw":
             withdraw_16 = int(input("How much would you like to withdraw? "))
             user_16 -= withdraw_16
             print("{} has been deducted from your account".format(withdraw_16))
             print("Your balance is ${}".format(user_16))
         elif choice_16 == "deposit":
             deposit_16 = int(input("How much would you like to deposit? "))
             user_16 += deposit_16
             print("{} has been added to your account".format(deposit_16))
             print("Your balance is ${}".format(user_16))
         else:
             print("Please enter a valid option.")
     else:
         print("That code is incorrect.")
code()
