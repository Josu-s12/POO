# 1. fizz, buzz (multiplos 3, 5, ambos)
# 2. numero primo
# 3. 30 numeros pares despues del 100

## 1. 
for i in range(1,101):
    if i %3 == 0 and i %5 == 0:
        print("FizzBuzz")
    elif i %3==0:
        print("Fizz")
    elif i %5==0:
        print("Buzz")
    else:
        print(i)


    