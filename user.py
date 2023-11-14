
#import re
#raw_input= input()
NAME = "What is your full name? "

name = input (NAME)

while name == "":
        name = input(NAME)
else:
    print ("Hello " + name)
birth_year = input("Enter your year of birth: ")

while birth_year == "":
        birth_year = input(" Enter your year of birth: ")

else:
       #print("Create a username")
    #input_str = raw_input ("Create a username: ")
#if not re.match("^[a-z]*$", input_str):
      #print("Error! Only letters a-z allowed!")
    #sys.exit()
#elif len(input_str)>10:
    #print("Error! Only 10 characters allowed")

    user_name = input("Create a Username: ")

while user_name == "":
        user_name = input("Create a Username: ")

else:

    pass_word = input("Create a 6 digit password:")
if len(pass_word) == 6:
       digits = pass_word[0]+'-'+pass_word[1]+'-'+pass_word[2]+'-'+pass_word[3]+'-'+pass_word[4]+'-'+pass_word[5]
       #print("Password:", digits)
       print("Congrats you've succesfully made an account. ")

while pass_word == "":
      pass_word = input("Create a 6 digit password: ")

       #len(user) > 6:
      #pass_word = input("Creat a Password: ")