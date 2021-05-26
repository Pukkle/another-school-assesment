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
name_list = ["User_1", "User_2", "User_3", "User_4", "User_5", "User_6", "User_7", "User_8", "User_9", "User_10", "User_11", "User_12", "User_13", "User_14", "User_15", "User_16"]
username = input("What is your name? ")
if username in name_list:

else:
  replaced_name = input("Where would you like to add your name? ")
  if replaced_name in name_list:
        position = name_list.index(replaced_name)
        name_list[position] = username
        print(name_list)
        if replaced_name == "User_1":
            user_1 = username

