
import random
random_number = random.randint(1,100)
answer = int(input("Diga um número de 1 a 100: "))
if answer == random_number:
    print("Você acertou na primeira tentativa!")
else:
    while answer != random_number:
        if answer > random_number:
            print("Muito alto")
        else:
          print("Muito baixo")
        answer = int(input("Tente novamente: "))
    else:
        print("você acertou!")


