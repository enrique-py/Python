import random
#number = input("Escribe numero: ")

#if not number.lstrip("-").isdigit():
#    print("error, no escribio un numero")
#else:
#    number = float(number)

#    if number == 0:
#        print("Es cero")
#    if number < 0:
#        print("Es negativo")
#    if number > 0:
#        print("Es positivo")

#rand_number = random.randint(1, 9)
#random.choise solo trabaja sobre listas []
#number = input("Escribe un numero: ")

#result = print("You Win") if (rand_number == number) else print(f"You lose, the number is {rand_number}")
#print(f"{number==rand_number}")

my_dict = {"word-1":"piedra", "word-2":"papel", "word-3":"tijera"}

values = my_dict.values()
values = list(values)

#print(random.choice(values))
keys = my_dict.keys()
keys = list(keys)
key = random.choice(keys)

#print(random.choice(key))

list(my_dict.values())

my_dict2 = {1:"tijera", 2:"pock", 3:"papel", 4:"piedra", 5:"lagarto"}
values = my_dict2.values()
values = list(values)
#print(random.choice(values))