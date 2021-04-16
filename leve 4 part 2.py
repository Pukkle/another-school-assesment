name_list = ["Evi", "Madeline", "Dan", "Kelsey", "Cayden", "Hayley", "darian"]
print("The list of names is {}".format(name_list))
print("The list of names in alphabetical order is {}".format(sorted(name_list)))
username = input("What is your name? ")
if username in name_list:
    print("Your name is in the list")
else:
    print("Your name is not in the list")
    list_change = input("Would you like to add your name or replace an existing name? ")
    if list_change == "add":
          added_name = input("What name would you like to add? ")
          name_list.append(added_name)
          print(name_list)
    elif list_change == "replace":
      replaced_name = input("What name would you like to replace? ")
      if replaced_name in name_list:
          position = name_list.index(replaced_name)
          name_list[position] = username
          print(name_list)
      else:
        print("That name is not on the list.")
    else:
        print("Please choose between add or replace.")


