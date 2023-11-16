


def hey_user():
      print( "Welcome, make an account! " )

hey_user()


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
  

    user_name = input("Create a Username: ")

while user_name == "":
        user_name = input("Create a Username: ")

else:

    pass_word = input("Create a 6 digit password:")
if len(pass_word) == 6:
       thislist = [pass_word[0]+'-'+pass_word[1]+'-'+pass_word[2]+'-'+pass_word[3]+'-'+pass_word[4]+'-'+pass_word[5]]
    
       print(thislist)
print("Congrats you've made an account! ")

while pass_word == "":
      pass_word = input("Create a 6 digit password: ")

  