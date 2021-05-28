user_1 = 0
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
account = input("Which account would you like to access? ")
 if account == "Account_1":
     code_1 = int(input("Please input the access code. "))
     if code_1 == "1234":
         choice_1 = input("would you like to withdraw, deposit, or borrow money? ")
         if choice_1 == "withdraw":
             withdraw_1 = int(input("How much would you like to withdraw? "))
             user_1 -= withdraw_1
             print("{} has been deducted from your account".format(withdraw_1))
         elif choice_1 == "deposit":
             deposit_1 = int(input("How much would you like to deposit? "))
             user_1 += deposit_1
             print("{} has been added to your account".format(deposit_1))
         else:
             print("Please enter a valid option.")
     else:
         print("That code is incorrect.")


