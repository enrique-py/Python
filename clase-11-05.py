#number = 5
#if number == 5:
#    print("It is equals to 5")

# residuo 0 es par 

#number_user = float(input("write a number: "))

#if (number_user % 5) == False:
 #   print("Es divisible")
#else:
#   print("No es divisible")

# gender --> F, M; gender cannot be empty
# Email --> cannot be empty and @

gender = input("Your gender: ")
email = input("Your email: ")
gender = gender.upper()

print (type(email.find("@")))
if (gender == "" and email == ""):
    print("Invalido")
elif (gender == "F" or "M") and (email != "" and (email.find("@") != -1)):
    print("Valido")
else:
    print("Invalido")
# import re expresion regular
2 in range(2,5)
True

1 in range(2,5)
False

5 in range(2,5)
False

5 in range(2, 6)
True

