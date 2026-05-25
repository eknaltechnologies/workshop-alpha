num = int(input("Enetr a number: "))

fact = 1

if num >= 0:
    for val in range(1, num + 1):
        fact = fact * val

print(fact)
