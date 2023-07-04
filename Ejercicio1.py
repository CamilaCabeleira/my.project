#ejercicio 1:
# varHola = 'Hola mundo!'
#print (varHola)

#ejercicio 2:
# print(((3 + 2) / (2 * 5)) ** 2)

#ejercicio 3
for num in range(101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
