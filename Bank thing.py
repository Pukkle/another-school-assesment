import random

def lottery():
    lotto = random.randint(1,4000000)
    print("The lottery number was {}".format(lotto))
try:
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
    credit_card_1 = 0
    credit_card_2 = 0
    credit_card_3 = 0
    credit_card_4 = 0
    credit_card_5 = 0
    credit_card_6 = 0
    credit_card_7 = 0
    credit_card_8 = 0
    credit_card_9 = 0
    credit_card_10 = 0
    credit_card_11 = 0
    credit_card_12 = 0
    credit_card_13 = 0
    credit_card_14 = 0
    credit_card_15 = 0
    credit_card_16 = 0
    name_list = ["Account_1", "Account_2", "Account_3", "Account_4", "Account_5", "Account_6", "Account_7", "Account_8", "Account_9", "Account_10", "Account_11", "Account_12", "Account_13", "Account_14", "Account_15", "Account_16"]
    account = input("Which account would you like to access? ")
    if account == "Account_1":
        code_1 = input("Please input the access code. ")
        if code_1 == "1234":
            choice_1 = input("would you like to withdraw, deposit, borrow, or gamble? ")
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
            elif choice_1 == "borrow":
                if credit_card_1 > 0:
                    print("You cannot borrow money if you owe money to the bank.")
                    payback_1 = input("would you like to pay it back?")
                    if payback_1 == "yes":
                        user_1 -= (credit_card_1 * 1.1)
                        print("{} has been deducted from your account".format(credit_card_1 * 1.1))
                        print("Your balance is ${}".format(user_1))
                    else:
                        print("Okay, but keep in mind you're going to have to pay it back sometime.")
                else:
                    def borrow1():
                        borrow_1 = int(input("How much would you like to borrow?"))
                        user_1 += borrow_1
                        credit_card_1 += borrow_1
                        print("You now owe ${}".format(borrow_1))
                        print("Your balance is ${}".format(user_1))
            elif choice_1 == "gamble":
                if user_1 < 20:
                    print("You don't have enough money.")
                    gamble_borrow_1 = input("Would you like to borrow some money? ")
                    if gamble_borrow_1 == "yes":
                        borrow1()
                gamble_1 = int(input("What do you think the number will be? "))
                lottery()
                if lotto = gamble_1:
                    print("congratulations!")
                    user_1 += 1000000
                else:

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
            elif choice_2 == "borrow":
                if credit_card_2 > 0:
                    print("You cannot borrow money if you owe money to the bank.")
                    payback_2 = input("would you like to pay it back?")
                    if payback_2 == "yes":
                        user_2 -= (credit_card_2 * 1.1)
                        print("{} has been deducted from your account".format(credit_card_2 * 1.1))
                        print("Your balance is ${}".format(user_2))
                    else:
                        print("Okay, but keep in mind you're going to have to pay it back sometime.")
                else:
                    borrow_2 = int(input("How much would you like to borrow?"))
                    user_2 += borrow_2
                    credit_card_2 += borrow_2
                    print("You now owe ${}".format(borrow_2))
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
            elif choice_3 == "borrow":
                if credit_card_3 > 0:
                    print("You cannot borrow money if you owe money to the bank.")
                    payback_3 = input("would you like to pay it back?")
                    if payback_3 == "yes":
                        user_3 -= (credit_card_3 * 1.1)
                        print("{} has been deducted from your account".format(credit_card_3 * 1.1))
                        print("Your balance is ${}".format(user_3))
                    else:
                        print("Okay, but keep in mind you're going to have to pay it back sometime.")
                else:
                    borrow_3 = int(input("How much would you like to borrow?"))
                    user_3 += borrow_3
                    credit_card_3 += borrow_3
                    print("You now owe ${}".format(borrow_3))
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
                withdraw_4 = int(input("How much would you like to withdraw? "))
                user_4 -= withdraw_4
                print("{} has been deducted from your account".format(withdraw_4))
                print("Your balance is ${}".format(user_4))
            elif choice_4 == "deposit":
                deposit_4 = int(input("How much would you like to deposit? "))
                user_4 += deposit_4
                print("{} has been added to your account".format(deposit_4))
                print("Your balance is ${}".format(user_4))
            elif choice_4 == "borrow":
                if credit_card_4 > 0:
                    print("You cannot borrow money if you owe money to the bank.")
                    payback_4 = input("would you like to pay it back?")
                    if payback_4 == "yes":
                        user_4 -= (credit_card_4 * 1.1)
                        print("{} has been deducted from your account".format(credit_card_4 * 1.1))
                        print("Your balance is ${}".format(user_4))
                    else:
                        print("Okay, but keep in mind you're going to have to pay it back sometime.")
                else:
                    borrow_4 = int(input("How much would you like to borrow?"))
                    user_4 += borrow_4
                    credit_card_4 += borrow_4
                    print("You now owe ${}".format(borrow_4))
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
            elif choice_5 == "borrow":
                if credit_card_5 > 0:
                    print("You cannot borrow money if you owe money to the bank.")
                    payback_5 = input("would you like to pay it back?")
                    if payback_5 == "yes":
                        user_5 -= (credit_card_5 * 1.1)
                        print("{} has been deducted from your account".format(credit_card_5 * 1.1))
                        print("Your balance is ${}".format(user_5))
                    else:
                        print("Okay, but keep in mind you're going to have to pay it back sometime.")
                else:
                    borrow_5 = int(input("How much would you like to borrow?"))
                    user_5 += borrow_5
                    credit_card_5 += borrow_5
                    print("You now owe ${}".format(borrow_5))
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
            elif choice_6 == "borrow":
                if credit_card_6 > 0:
                    print("You cannot borrow money if you owe money to the bank.")
                    payback_6 = input("would you like to pay it back?")
                    if payback_6 == "yes":
                        user_6 -= (credit_card_6 * 1.1)
                        print("{} has been deducted from your account".format(credit_card_6 * 1.1))
                        print("Your balance is ${}".format(user_6))
                    else:
                        print("Okay, but keep in mind you're going to have to pay it back sometime.")
                else:
                    borrow_6 = int(input("How much would you like to borrow?"))
                    user_6 += borrow_6
                    credit_card_6 += borrow_6
                    print("You now owe ${}".format(borrow_6))
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
            elif choice_7 == "borrow":
                if credit_card_7 > 0:
                    print("You cannot borrow money if you owe money to the bank.")
                    payback_7 = input("would you like to pay it back?")
                    if payback_7 == "yes":
                        user_7 -= (credit_card_7 * 1.1)
                        print("{} has been deducted from your account".format(credit_card_7 * 1.1))
                        print("Your balance is ${}".format(user_7))
                    else:
                        print("Okay, but keep in mind you're going to have to pay it back sometime.")
                else:
                    borrow_7 = int(input("How much would you like to borrow?"))
                    user_7 += borrow_7
                    credit_card_7 += borrow_7
                    print("You now owe ${}".format(borrow_7))
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
            elif choice_8 == "borrow":
                if credit_card_8 > 0:
                    print("You cannot borrow money if you owe money to the bank.")
                    payback_8 = input("would you like to pay it back?")
                    if payback_8 == "yes":
                        user_8 -= (credit_card_8 * 1.1)
                        print("{} has been deducted from your account".format(credit_card_8 * 1.1))
                        print("Your balance is ${}".format(user_8))
                    else:
                        print("Okay, but keep in mind you're going to have to pay it back sometime.")
                else:
                    borrow_8 = int(input("How much would you like to borrow?"))
                    user_8 += borrow_8
                    credit_card_8 += borrow_8
                    print("You now owe ${}".format(borrow_8))
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
            elif choice_9 == "borrow":
                if credit_card_9 > 0:
                    print("You cannot borrow money if you owe money to the bank.")
                    payback_9 = input("would you like to pay it back?")
                    if payback_9 == "yes":
                        user_9 -= (credit_card_9 * 1.1)
                        print("{} has been deducted from your account".format(credit_card_9 * 1.1))
                        print("Your balance is ${}".format(user_9))
                    else:
                        print("Okay, but keep in mind you're going to have to pay it back sometime.")
                else:
                    borrow_9 = int(input("How much would you like to borrow?"))
                    user_9 += borrow_9
                    credit_card_9 += borrow_9
                    print("You now owe ${}".format(borrow_9))
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
            elif choice_10 == "borrow":
                if credit_card_10 > 0:
                    print("You cannot borrow money if you owe money to the bank.")
                    payback_10 = input("would you like to pay it back?")
                    if payback_10 == "yes":
                        user_10 -= (credit_card_10 * 1.1)
                        print("{} has been deducted from your account".format(credit_card_10 * 1.1))
                        print("Your balance is ${}".format(user_10))
                    else:
                        print("Okay, but keep in mind you're going to have to pay it back sometime.")
                else:
                    borrow_10 = int(input("How much would you like to borrow?"))
                    user_10 += borrow_10
                    credit_card_10 += borrow_10
                    print("You now owe ${}".format(borrow_10))
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
            elif choice_11 == "borrow":
                if credit_card_11 > 0:
                    print("You cannot borrow money if you owe money to the bank.")
                    payback_11 = input("would you like to pay it back?")
                    if payback_11 == "yes":
                        user_11 -= (credit_card_11 * 1.1)
                        print("{} has been deducted from your account".format(credit_card_11 * 1.1))
                        print("Your balance is ${}".format(user_11))
                    else:
                        print("Okay, but keep in mind you're going to have to pay it back sometime.")
                else:
                    borrow_11 = int(input("How much would you like to borrow?"))
                    user_11 += borrow_11
                    credit_card_11 += borrow_11
                    print("You now owe ${}".format(borrow_11))
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
            elif choice_12 == "borrow":
                if credit_card_12 > 0:
                    print("You cannot borrow money if you owe money to the bank.")
                    payback_12 = input("would you like to pay it back?")
                    if payback_12 == "yes":
                        user_12 -= (credit_card_12 * 1.1)
                        print("{} has been deducted from your account".format(credit_card_12 * 1.1))
                        print("Your balance is ${}".format(user_12))
                    else:
                        print("Okay, but keep in mind you're going to have to pay it back sometime.")
                else:
                    borrow_12 = int(input("How much would you like to borrow?"))
                    user_12 += borrow_12
                    credit_card_12 += borrow_12
                    print("You now owe ${}".format(borrow_12))
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
            elif choice_13 == "borrow":
                if credit_card_13 > 0:
                    print("You cannot borrow money if you owe money to the bank.")
                    payback_13 = input("would you like to pay it back?")
                    if payback_13 == "yes":
                        user_13 -= (credit_card_13 * 1.1)
                        print("{} has been deducted from your account".format(credit_card_13 * 1.1))
                        print("Your balance is ${}".format(user_13))
                    else:
                        print("Okay, but keep in mind you're going to have to pay it back sometime.")
                else:
                    borrow_13 = int(input("How much would you like to borrow?"))
                    user_13 += borrow_13
                    credit_card_13 += borrow_13
                    print("You now owe ${}".format(borrow_13))
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
            elif choice_14 == "borrow":
                if credit_card_14 > 0:
                    print("You cannot borrow money if you owe money to the bank.")
                    payback_14 = input("would you like to pay it back?")
                    if payback_14 == "yes":
                        user_14 -= (credit_card_14 * 1.1)
                        print("{} has been deducted from your account".format(credit_card_14 * 1.1))
                        print("Your balance is ${}".format(user_14))
                    else:
                        print("Okay, but keep in mind you're going to have to pay it back sometime.")
                else:
                    borrow_14 = int(input("How much would you like to borrow?"))
                    user_14 += borrow_14
                    credit_card_14 += borrow_14
                    print("You now owe ${}".format(borrow_14))
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
            elif choice_15 == "borrow":
                if credit_card_15 > 0:
                    print("You cannot borrow money if you owe money to the bank.")
                    payback_15 = input("would you like to pay it back?")
                    if payback_15 == "yes":
                        user_15 -= (credit_card_15 * 1.1)
                        print("{} has been deducted from your account".format(credit_card_15 * 1.1))
                        print("Your balance is ${}".format(user_15))
                    else:
                        print("Okay, but keep in mind you're going to have to pay it back sometime.")
                else:
                    borrow_15 = int(input("How much would you like to borrow?"))
                    user_15 += borrow_15
                    credit_card_15 += borrow_15
                    print("You now owe ${}".format(borrow_15))
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
            elif choice_16 == "borrow":
                if credit_card_16 > 0:
                    print("You cannot borrow money if you owe money to the bank.")
                    payback_16 = input("would you like to pay it back?")
                    if payback_16 == "yes":
                        user_16 -= (credit_card_16 * 1.1)
                        print("{} has been deducted from your account".format(credit_card_16 * 1.1))
                        print("Your balance is ${}".format(user_16))
                    else:
                        print("Okay, but keep in mind you're going to have to pay it back sometime.")
                else:
                    borrow_16 = int(input("How much would you like to borrow?"))
                    user_16 += borrow_16
                    credit_card_16 += borrow_16
                    print("You now owe ${}".format(borrow_16))
                    print("Your balance is ${}".format(user_16))
            else:
                print("Please enter a valid option.")
        else:
            print("That code is incorrect.")
    else:
        print("Please enter a valid account.")
