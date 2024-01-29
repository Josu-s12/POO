def primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5)+1):
        if numero % i==0:
            return False
        return True
        
numero=int(input("ingrese un numero para saber si es primo o no"))
if primo(numero):
        print(f"{numero} es primo")
else:
        print(f"{numero} no es primo")



    