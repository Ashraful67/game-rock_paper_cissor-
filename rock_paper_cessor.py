import random

def game(comp, you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return True
        if you == 'c':
            return False
    elif comp == 'p':
        if you == 'c':
            return True
        if you == 'r':
            return False
    elif comp == 'c':
        if you == 'r':
            return True
        if you == 'p':
            return False
        
ra = random.randint(1,3)        
if ra == 1:
    comp = 'r'
elif ra == 2:
    comp = 'p'
elif ra == 3:
    comp = 'c'

you = input("enter your choice rock(r) paper(p) cessor(c) : ")

print(f"you chooose {you}")
print(f"computer choose {comp}")
a = game(comp,you)
if a == None:
    print("it's a tie")
elif a == True:
    print('you win')
elif a == False:
    print('you lose')