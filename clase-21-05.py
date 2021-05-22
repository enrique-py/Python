# for anidados
for i in range(1, 3):
    for j in range (1, 10):
        print(f"i={i}, j={j}")

for i in range(1, 3):
    for j in range (2, 5):
        for k in range (1, 3):
            print(f"i={i}, j={j}, k={k}")

# A prime number (or a prime) is a natural number greater than 1 that has no positive divisors 
# other than 1 and itself. A natural number greater than 1 that is not a prime number 
# is called a composite number.

# Based on this definition, if we consider the first 10 natural numbers, we can see that 2, 3, 5, 
# and 7 are primes, while 1, 4, 6, 8, 9, 10 are not. In order to have a computer tell you 
# if a number N is prime, you can divide that number by all natural numbers in the range [2, N ). 
# If any of those divisions yields zero as a remainder, then the number is not a prime.

# Write a program to find all the primes numbers from 1 to N, where N is an integer given by the user.
# Write two scripts, one using while and other one using for

n = int(input("Escriba el numero N: "))
primes = []
for number in range(2, n): # for number
    is_prime = True
    for divisor in range (2, number): # for divisor
        if number % divisor == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(number)
print(primes)

#for i in reversed(range(1, 7)):
#    print("*" * i)

#for i in range (2, 7):
#    print("*" * i)

i = 6
while i > 0:
    print("*" * i)
    i -= 1

i = 1
while i <= 6:
    print("*" * i)
    i += 1
people = ["jonas", "julio", "mike", "mez"]
ages = [25, 30, 31, 39]
length = len(people)

for i in range (0, length): # buscar indice de cada elemento de lista
    name = people[i]
    age = ages[i]
    print(f"{name} {age}")

for nombre, edad in zip(people,ages): # solo sirve en python
    print(f"{nombre} {edad}")
