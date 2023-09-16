import random

score = 0
intentos = 10


while(intentos != 0):
    num = random.randint(0, 9)
    if num == 0:
        intentos -=1
        print ("# de intentos: ", intentos)
    else:
        score +=1
        print ("score: ", score)