print('hello, world2!')
#first_name = 'Jonasz'
#last_name = 'Olkowski'
#full_name = first_name + " " + last_name
#print('Hello ' + first_name)
#print(type(first_name))
#print('hello ' + full_name)
#age = 23
#age = age + 1
#print(age)
#print(type(age))
#print('Your age is: ' + (str(age)))
#height = 176.6
#print('Your height is ' + (str(height)) + 'cm')
#print(type(height))
#human = False
#print(human)
#print(type(human))
#print('Are you a human? ' + (str(human)))
# name = 'Jonasz'
# age = 23
# attractive = True
# name, age, attractive = 'Jonasz', 23, True
# print(name)
# print(age)
# print(attractive)

#spongebob = 30
#patrick = 30
#sandy = 30
#squidward = 30

# spongebob = patrick = sandy = squidward = 30

# print(spongebob)
# print(patrick)
# print(sandy)
# print(squidward)

#name = 'Jonasz'
#name1 = 'jonasz'
# print(name)
# print(len(name))
# print(name.find("a"))
#print(name1.capitalize())
#print(name.upper())
#print(name.lower())
#print(name.isdigit())
#print(name.isalpha())
#print(name.count('o'))
# print(name.replace('o', 'p'))
# print(name*3)

#x = 1
#y = 2.0
#z = '3'

#print('X is ' + str(x))
#print('Y is ' + str(y))
#print("Z is " + z*3)

#name = input("What is your name?: ")
#age = int(input('How old are you?: '))
#age = age + 1
#height = float(input('How tall are you?: '))
#print('Hello ' + name)
#print('Your age is: ' +str(age))
#print('You are ' + str(height) +"cm tall")

#import math 
#pi = 3.14
#x = 1
#y = 2 
#z = 3
#print(round(pi)) #zaokrąglenia 
#print(math.ceil(pi)) #zaokrąglenie w górę do całych
#print(math.floor(pi)) #zaokrąglenie w dół do całych
#print(abs(pi)) #absolutna wartość czyli odległość od zera
#print(pow(pi,2)) #power do potęgi
#print(math.sqrt(pi)) #squareroot pierwiastek drugiego stopnia
#print(max(x, y, z)) #znajdź największą wartość ze zbioru
#print(min(x, y, z)) #znajdź najmniejszą wartość ze zbioru

#name = 'Jonasz Olkowski'

#first_name = name[0:6] #pierwszy indeks jest włącznie a drugi bez ostatniej
#first_name_2 = name[:6] #brak indeksu oznacza indeks 0 na początku
#last_name = name[7:15] #tak jak wyżej
#last_name_2 = name[7:] #oznacza że do końca
#print(first_name)
#print(first_name_2)
#print(last_name)
#print(last_name_2)
#funky_name = name[0::2] # start/stop/step można też zapisać [::2]
#print(funky_name)
#reversed_name = name[::-1] #-1 powoduje ze liczy od końca zamiast od początku
#print(reversed_name)

#website = "htpp://google.com"
#slice = slice(7,-4)#slice w przeciwienstwie do indeksow dzielą , zamiat :
#dodatkowo wartości od konca liczy sie od 1 zamiast zera i uzywa znaku minus
#print(website[slice])
#website_2 = "http://wikipedia.com"
#print(website_2[slice])

#age = int(input("how old are you?: "))

#if age == 100:
    #print("You're a century old")
#elif age >= 18:
    #print("You are an adult!")
#elif age == 100:
    #print("You're a century old")
#elif age < 0:
    #print("You haven't been born yet!")
#else:
    #print("You are a child!")


#temp = int(input("What is the temperature outside?"))
#and oba muszą byc prawdziwe, or jedno musi byc prawdziwe, not zmienia True w False i viceversa
#if not(temp >= 0 and temp <= 30):
    #print("the temperature is good outside")
    #print('go outside')
#elif not(temp < 0 or temp > 30):
    #print("the temperature is bad outside")
    #print("stay in home")

#while loop trwa tak długo jak warunki statement są prawdziwe
#name = ""
#while len(name) == 0:
#    name = input("Enter your name:")

#print("Hello " + name)

#name = None
#while not name:
#    name = input("enter your name: ")
#print("hello " + name)

#forloops
#a statement that will execute it's block a limited amount of type, when while loop is unlimited

#for index in range(10):
#    print(index + 1)

#for i in range(90,100):
#    print(i)

#for i in range(50,100,10): # step to ostatnie i co tyle liczy
    #print(i)

#for i in "Jonasz Olkowski": po koleji kazda litera
#    print(i)
# import time #import time for time def 
#for seconds in range(10,0,-1):
#    print(seconds)
#    time.sleep(1) #co sekundę zmiana w  programie
#print("Happy New Year!") #print po odliczaniu

