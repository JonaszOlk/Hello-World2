#BroCode 12H kurs
print('hello, world2!')
#data types and ways of reading them
"""first_name = 'Jonasz'
last_name = 'Olkowski'
full_name = first_name + " " + last_name
print('Hello ' + first_name)
print(type(first_name))
print('hello ' + full_name)
age = 23
age = age + 1
print(age)
print(type(age))
print('Your age is: ' + (str(age)))
height = 176.6
print('Your height is ' + (str(height)) + 'cm')
print(type(height))
human = False
print(human)
print(type(human))
print('Are you a human? ' + (str(human)))
name = 'Jonasz'
age = 23
attractive = True
name, age, attractive = 'Jonasz', 23, True
print(name)
print(age)
print(attractive)"""

#zapisywanie zmiennych z tymi samymi danymi w celu zaoczedzenia miejsca i pracy
"""spongebob = 30
patrick = 30
sandy = 30
squidward = 30

spongebob = patrick = sandy = squidward = 30

print(spongebob)
print(patrick)
print(sandy)
print(squidward)"""

#obsługa string data
"""name = 'Jonasz'
name1 = 'jonasz'
print(name) #output
print(len(name)) #długość
print(name.find("a")) #znajdz pierwszą lokalizacje a
print(name1.capitalize()) #zacznij dużą literą
print(name.upper()) #uzyj capslocka
print(name.lower()) #wszystko małymi
print(name.isdigit()) #sprawddz czy jest liczbą
print(name.isalpha()) #sprawdz czy jest literami
print(name.count('o')) #policz ilość występowań znaku
print(name.replace('o', 'p')) #zastąp znak innym znakiem
print(name*3) #output 3 razy"""

#laczenie str i int i float data
"""x = 1 #int
y = 2.0 #float
z = '3' #str

print('X is ' + str(x)) #zmiana int w str zeby moc polaczyc z innym str
print('Y is ' + str(y)) #zmiana float w str zeby moc polaczyc z innym str
print("Z is " + z*3) #nie wymaga zmiany bo jest juz str ale zamiast pomozyc razy 3 pojawi sie 3 razy po sobie"""

#input próby
"""name = input("What is your name?: ") #zmienna okreslona przez input uzytkownika zawsze jest w str
age = int(input('How old are you?: ')) # -||- i transformajca w int
age = age + 1 #nadpisanie data z zwiekszeniem o 1 bo wczesniej zmienilismy str w int
height = float(input('How tall are you?: ')) #nadpisanie str na float
print('Hello ' + name) #mozna tak bo oba są str
print('Your age is: ' +str(age)) #zmiana int na str ponownie by działało
print('You are ' + str(height) +"cm tall") #zmiana float na str zeby dzialalo"""

#math
"""import math 
pi = 3.14
x = 1
y = 2 
z = 3
print(round(pi)) #zaokrąglenia 
print(math.ceil(pi)) #zaokrąglenie w górę do całych
print(math.floor(pi)) #zaokrąglenie w dół do całych
print(abs(pi)) #absolutna wartość czyli odległość od zera
print(pow(pi,2)) #power do potęgi
print(math.sqrt(pi)) #squareroot pierwiastek drugiego stopnia
print(max(x, y, z)) #znajdź największą wartość ze zbioru
print(min(x, y, z)) #znajdź najmniejszą wartość ze zbioru"""

#Wyciąganie danych ze str
"""name = 'Jonasz Olkowski'

first_name = name[0:6] #pierwszy indeks jest włącznie a drugi bez ostatniej
first_name_2 = name[:6] #brak indeksu oznacza indeks 0 na początku
last_name = name[7:15] #tak jak wyżej
last_name_2 = name[7:] #oznacza że do końca
print(first_name)
print(first_name_2)
print(last_name)
print(last_name_2)
funky_name = name[0::2] # start/stop/step można też zapisać [::2]
print(funky_name)
reversed_name = name[::-1] #-1 powoduje ze liczy od końca zamiast od początku, tez mogloby byc [0:15:-1]
print(reversed_name)

website = "htpp://google.com"
slice = slice(7,-4)#slice w przeciwienstwie do indeksow dzielą ',' zamiat ':'
#dodatkowo wartości od konca liczy sie od 1 zamiast zera i uzywa znaku minus
print(website[slice])
website_2 = "http://wikipedia.com"
print(website_2[slice])"""

#if statements
"""age = int(input("how old are you?: "))
#mamy "if" i "elif" ktore oznaczaja kolejnosc az do ostatniego gdzie zamykamy "else"
if age == 100:
    print("You're a century old")
elif age >= 18:
    print("You are an adult!")
elif age == 100:
    print("You're a century old")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are a child!")"""

#logical operators
"""temp = int(input("What is the temperature outside?"))
#and oba muszą byc prawdziwe, or jedno musi byc prawdziwe, not zmienia True w False i viceversa
if not(temp >= 0 and temp <= 30):
    print("the temperature is good outside")
    print('go outside')
elif not(temp < 0 or temp > 30):
    print("the temperature is bad outside")
    print("stay in home")"""
#while loop
"""#while loop trwa tak długo jak warunki statement są prawdziwe
name = "" #name jest jakims str
while len(name) == 0: #kiedy lenght of name is equal 0 działa loop
    name = input("Enter your name:") #miejsce na input imienia, jezeli len>0 wyjdz z loop
print("Hello " + name) #output hello + str

name = None #imie nie ma wartosci
while not name: #to samo co wyzje czyli poki imie nie ma wartosci to pokazuj enter your name
    name = input("enter your name: ") #input imienia jesli imie sie pojawi zrywa loop bo false
print("hello " + name) #po wyjsciu z loopa output hello + str"""

#forloops
"""#a statement that will execute it's block a limited amount of type, when while loop is unlimited

for index in range(10): #inex popularnie uzywa się i
    print(index + 1) #output 0 1 2 3 4 5 6 7 8 9 10(bo +1 range)

for i in range(90,100): #index zastapione 'i' oraz ze wzgledu na okreslenie poczatku nie leci od zera
    print(i)

for i in range(50,100,10): # step to ostatnie i co tyle liczy(start,stop,step)
    print(i) #output 50 60 70 80 90

for i in "Jonasz Olkowski": #po koleji kazda litera
    print(i)
import time #import time for time def bo nie ma jej automatycznie
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1) #co sekundę zmiana w  programie
print("Happy New Year!") #print po odliczaniu"""

#nested loops
# wewnętrzny loop zakonczy działanie zanim zakonćży swoje działanie zewnętrzny loop, nie ma znaczenia
#czy jest to for loop czy while loop zanim zakonczy się jeden zewnetrzny loop wykona się w nim cały wewnętrzny loop
"""rows = int(input("How many rows?: ")) #transforms input number in string to number in int
columns = int(input("How many columns?: ")) #transforms input number in string to number in int
symbol = input("Enter a symbol to use: ") #input of symbol
#create outer loop and then create inside loop
for i in range(rows): #loop zewnetrzny dla rzedów
    for j in range(columns): #loop wewnętrzny dla kolumn oraz uzywamy zazwyczaj "j" poniewaz jest po i(index)
        print(symbol, end="") #bez dopisku " end='' " bylby problem z przejsciem do kolejnej lini poniewz print działa jako /n
    print()#daje finalny efekt gdyby zrobic to dzielac loop wyszdłby ciąg symboli zamiast założonego sensu"""

#loop control statements in python, czyli zmiany ich tradycyjnych zachowań w realizacji
#break = używamy do całkowitego zakońćzenia loopa
#continue = używamy do przejścia do kolejnego powtórzenia loopa
# pass = nie robi nic działa jako placeholder

#break
"""while True: #loop ciągłości podczas prawdy/ zawsze prawda
    name = input("Enter your name: ") #wpisz swoje imie, jesli pominiesz wracamy do prawdy czyli wpisz swoje imie itd
    if name != "": #jednak kiedy name nie jest dłuzej równe pustej przestrzeni przechodzi do kolejnego elementu czyli
        break #break, przerywamy loopa

while True:
    haslo = input("Podaj haslo: ")
    if haslo == "Armor":
        break

rows = int(input("podaj ilość rzedow: "))
columns = int(input("podaj ilość kolumn: "))
symbol = input("Podaj symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()"""

#continue

"""phone_number = "123-456-7890" #uzylismy tutaj "-"

for i in phone_number: #loop czytający kazdy elemt string data z phone_number
    if i == "-": #"wewnętrzny warunek jezeli czytajac znajdzie '-' ma za zadanie
        continue #uzyc kolejnego elementy pomijac '-' poniewaz uzylismy "continue"
    print(i, end="") #na koniec print pozwala nam pokazac odczyt i z pomineciem "-", jednak bez end wyjdzie kolumna"""

#pass
"""for i in range(1,21): #od 1 do 20

    if i == 13: #jezeli odczyta 13
        pass #to ma zrobic pass tego numeru czyli pominąć
    else: #w przypadku innych ma printowac output
        print(i) #output 123(...)121415(...)20"""

#lists
#used to store multiple items in single variable

"""food_1 = "pizza" #zmienna trzyma jedną wartość
food_2 = ["pizza","hamburger","hotdog","spaghetti"] #nie trzyma dłużej tylko jednej zmiennej ale staje się listą 
food_2[0] = "sushi" #powoduje zmiane elementu w liście z indexem 0 co mozemy robic w dowolnym momencie

#ważne elemnty działań na listach
food_2.append("ice cram") #dodaje na koniec listy wpisany element
food_2.remove("hotdog") #usuwa wpisany element z listy
food_2.pop() #usuwa osatni element bez wpisywania go
food_2.insert(0, "cake") #dodaje element w wybrane element przez index na liscie bez usuwanie niczego
food_2.sort() #ułoży liczbę alfabetycznie
#food_2.clear() #usuwa wszystkie elementy listy

print(food_2) #printuje całą listę w "['x', 'c', 'v', 'f']"
print(food_2[0]) #print element listy z indexem 0

for x in food_2: #po koleji print całej listy w kolumnie
    print(x)"""

#2D lists
#inaczej a list of lists / multidimentional list

"""drinks = ["coffe", "soda", "tea"] #3 listy
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "icecream"]

food = [drinks, dinner, dessert] #2D list / list of lists

print(food) #print wszystkie listy 
print(food[0][0]) #print [która lista][który index z tej listy]"""

#tuples
"""#zbiór uporządkowana i niezmienna uzywana do grupowania danych, są jak listy tylko brak zmian i są uporządkowane

student = ("Jonasz",23,"male")
print(student.count("Jonasz")) #count how many times data apears in tuple
print(student.index("male")) #count in which place data is putted

for x in student: #print all datas in tuple
    print(x)

if "Jonasz" in student: #check if X apears in datas inside tuple
    print("Jonasz is here")"""

#sets
#sets -> collection that's unordered and unindexed, no duplicate values
"""utensils = {"fork", "spoon", "knife"}
dishes = {"bowl","plate","cup","knife"}

utensils.add("napkin") #add to set
utensils.remove("fork") #remove from set
utensils.clear() #clear the set
#utensils.update(dishes) #update utensils o dishes
dinner_table = utensils.union(dishes)

for x in utensils: #output zawartości zbioru w randomowej kolejności
    print(x)

for x in dinner_table:
    print(x)

print(dishes.difference(utensils)) #pokaz roznice miedzy setami
print(dishes.intersection(utensils)) #pokaz co sety mają ze sobą wspólnego""" 

#dictionary 
# a changeable, unordered collection of unique key:values paires
#fast because they use hashing, allow us to access a value quickly

"""capitals = {'USA': 'Washington DC',   #dicitionary konstrukcja zmienna = {Key: value,}
            'India':'New Dheli',
            'China':'Beijing',
            'Russia':'Moscow',
            'Poland':'Warsaw'}

print(capitals['Russia']) #prints value of the key but gives us error when there is no key in dict
print(capitals.get('Russia')) #safer cuz prints none if there is no key in dict
print(capitals.keys()) #prints only keys from dictionary
print(capitals.values()) #prints only values from dictionary
print(capitals.items()) #prints both keys and values from dictionary

for key,value in capitals.items(): #prints every key and value asigned to one 
    print(key,value)

capitals.update({"Germany":"Barlin"}) #update dictionary with this key and value ({"x":"y"})
print(capitals.items())

capitals.update({"USA":"NY"}) #update value of the key
print(capitals.items())

capitals.update({"Unia":"Warsaw"}) #update key conected to the value
print(capitals.items())

capitals.pop("China") #delete Key and value asigned to it, there is no {}
print(capitals.items())

capitals.clear() #clear dict completly
print(capitals.items())"""

#indexing
#index operator -> [] = gives access to a sequence's element (str,list,tuples)

"""name = "Jonasz Olkowski"
if(name[0].isupper()): #isupper or is lower sprawdz czy pierwsza litera jest duża/mała if true
    name = name.lower()                                                           #zamień na małą

print(name)                                                                       #print everything in lowercase

first_name = name[0:3].upper() #nowa zmienna powstaje z częscie wyznaczonej przez indexy, wszystko zostaje capslock
print(first_name)

last_name = name[7:].lower() #nowa zmienna powstaje z wyznaczonego indexem, wszystko z małej
print(last_name)

name_2 = "Jonasz Olkowski!" #nowa zmienna
last_character = name_2[-1] #tworzy z ostatniego znaku bo -1
print(last_character)"""

# functions 
# a block of code which is executed only when it is called

"""def hello(): #start with def of function and naming to call it use its name and "()"
    print("hello!")
    print("Have a nice day!")

hello()
hello()
hello()

def hello_2(name): #name a argument in function name so later u can use it to fill the argument
    print("hello " + name)
    print("Have a nice day!")

hello_2("Bro") #name in function is changed with "Bro"
hello_2("Jonasz") #name in function is changed with "Jonasz"

my_name = "bro" #diffrent option insted of giving info to the brackets in called function we can give
                #value to the argument and then give this argument to called function

hello_2(my_name)

# hello_2("Bro","Code") wouldn't work cuz there is only one argument function not two

def hello_3(first_name, last_name): #two parameters and updated places for them in function
    print("hello " + first_name + last_name)
    print("Have a nice day!")

hello_3("Bro ", "Code") #filling for two parameters in function

def hello_4(first_name, last_name, age): #function with 3 parameters
    print("Hello " + first_name + last_name)
    print("You are", age ,"years old") #can't use + cuz str and int

hello_4("Jonasz", "Olkowski", 23) #filling of 3 parameters"""

#return statement
#functions send Python values/objects bacl to the caller
#These values/objects are known as function's return data

"""def multiply(number1, number2): #option 1 where result is returned to the caller
    result = number1 * number2
    return result

x = multiply(11,22) #n1 and n2 is 11 and 22 and is stored as x
print(multiply(6,8)) #is alredy printing a result od function for 6 * 8
print(x) # is printing a value stored for x

def multiply_2(number_3,number_4): #2nd option of function with return in less lines
    return number_3 * number_4

y = multiply_2(70,72) #same like x
print(y)"""

#keyword arguments
# these are arguments that are proceed by identifier, when we pass them to a function
# order doesn't matter, unlike positional arguments
# Python knows the name of the arguments that are recevied by function
# example of positional arguments are in functions, every position is important for correct output of the function
#in case of keywords argument positioning won't matter

"""def hello(first,middle,last):
    print("Hello "+ first + " " +middle+ " " + last)

hello(first="Jonasz",middle="Nikodem",last="Olkowski") #when arguments are preceded with identifier 
#                                                       they order doesn't matter"""

#nested function calls
#function calls inside other function calls 
#innermost function calls are resolved first; work in -> out
#returned value is used as argument for the next outter function

"""num = input("entera whole positive number") #mozemy uprosicic te działania za pomocą nested function 
num = float(num)
num = abs(num)
num = round(num)
print(num)

print(round(abs(float(input("Enter a whloe positive number"))))) #nested function"""

#variable scope
# The region that a variable is recognized
# A variable is only avaible from inside the region it is created
# A global and locally scoped version of a variable can be created

"""def display_name():
    name = "Code" #Here is a variable that is inside function thats local scope variable(only inside avaible)
    print(name)

#print(name) #name isn't defined cuz name before was created inside function and it is local scope, but we can
# can create global variable by putting it outsied function "name = BRO" amd it is global scope
#                                                             avaible inside and outsie function
#it is possible to have global and local variable of the same name but then print function with inside version
# is going to be first and then print global variable
#for ex.
number = 9

def display_number():
    number = 7
    print(number)

display_number() #output 7 9 if we are going to delete local scoop in function output is gonna be 9 9
print(number)    #Python is following the rule named LEGB (L)ocal (E)nclosing (G)lobal (B)uilt-in 
                                                            #in a way of using ordered variables"""

#*args
#parameter that will pack all arguments into a tuple
#useful so that a function can accept a varying amount of arguments

"""def add(num1, num2): #it works only when we want to add two parameters
    sum = num1 + num2
    return sum

print(add(1,2))

#to resolve the issue we can use *args

def add_2(*args): #you can name args however you want but you have to remember about asterik "*"(but it is often called args)
    sum2 = 0      #thanks to that we are packing all arguments into a tuple(ordered and unchangeable) 
    for i in args:#then thanks to that we are not limited aslike in example above
        sum2 += i #so we can sum more of the arguments
    return sum2

#to change arguments in tuples we have to transform them into list for ex
def add_3(*pack): #create tuple with *x
    sum3 = 0      #sum for beggining
    pack = list(pack) #transform tuple into list
    pack[0] = 0       #now we can change values inside list by indexing
    for i in pack:    #works like in ex above but now we can transform them
        sum3 += i
    return sum3

print(add_2(1,2,3,4,5,6,7))
print(add_3(1,2,3,4,5,6,7))"""

#**kwargs = *args packed everything int tuple, but **kwargs will pack everything into dictionary
#useful so that a function can acccept a varying amount of keywords arguments

"""def hello(first,last): #here is a function that will work for two arguments only
    print("hello " + first + " " + last ) #this function will print hello f l

hello(first="Bro",last="Code") #we gave values to arguments for function two work with
#in case someone has a middle name we would like to use hello(first="x",middle="dude",last="code") but it won't work

def hello2(**kwargs):#kwarg = keywords arguments but you can name them however but remember about "**" it is the name 
#of dictionary
    print("Hello " + kwargs['first_2'] + " " + kwargs["last_2"]) #This will work as above byt wont show error for 
#more arguments like function above
hello2(first_2="bro",middle="dude",last_2="bro")
#now to display full name usin kwargs
def hello3(**kwargs2): #now for unlimited amount of key arguments
    print("Hello",end=" ") #we use "end=' ' " to display it on the same lane as print below
    for key,value in kwargs2.items(): #for every key in kwargs2 print value for that keys
        print(value,end=" ")

hello3(title="mister",name3="Jonasz",middle3="Nikodem",last="Olkowski")"""

#strin.format() = str.format(), optional method that gives users more control when displaying output

"""animal = "cow" #data stored in variables
item = "moon"
print("The "+animal+" jumped over the "+item) #connecting string as output
#using format method
print("The {} jumped over the {}".format("cow","moon"))#the brackets works as placeholders that are explained by 
#format(value1,value2) We can replace values with variables
print("The {} jumped over the {}".format(animal,item))#the first bracket/placeholder'll dispaly first thing in format
#next option in positional arguments
print("The {0} jumped over the {1}".format(animal,item)) # using index we can change order, we can reuse index
#last way at given format field is keyword arguments
print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))#now we wouldn't need our variables at top,and
#we are still able to use indexes to change order of format input, we can reuse variables

#another way to write it
text = "The {} jumped over the {}" #The format method
print(text.format(animal,item))

#adding padding
name = "Bro"

print("Hello, my name is {}".format(name)) #we can add some padding before or after our placeholder
#padding example
print("Hello, mu name is {:10} x".format(name))#we just added ten spaces here,it is 10 to the right 
print("Hello, mu name is {:<10} x".format(name))#left align <,(no visable example, cuz it is by default)
print("Hello, mu name is {:>10} x".format(name))#right align >, our name moved ten spaces to the right
print("Hello, mu name is {:^10} x".format(name))#center align ^, both ways four spaces
#what if we nned to add positional argument or keywords argument to our format field, but there is some txt?
#add before a collin example {0:10} ->psotional, {name:10} -> keyword argument, and follow by whatever you want
#now changing format of number variable
number=3.14159
print("The number pi is {}".format(number))#it will display full floatin number
print("The number pi is {:.2f}".format(number)) #f is for floating points numbers, .2 -> is for two numbers after dot
print("The number pi is {:.3f}".format(number)) #It will display 3 digits after dot and it will round the number for us

number_2=1000
print("The number is {}".format(number_2)) #it will display number
print("The number is {:,}".format(number_2))#it will display number with the come before 3 zeros to make it easy 
print("The number is {:b}".format(number_2))#it will display a binary number as 0=0 1=01 2=10 3=11, 4=100
print("The number is {:o}".format(number_2))#it will display octal number
print("The number is {:x}".format(number_2))#hexadecimal number, lower for lowercase,upper fo uppercase 
print("The number is {:X}".format(number_2))
print("The number is {:e}".format(number_2))#scientific notation with lower upper
print("The number is {:E}".format(number_2))"""

#random numbers =random module which is pseudo 
"""import random #now we have access to every option of random module 

x = random.randint(1,6) #with described limits it will generate random number between 1 to 6 in int,
#without it is jus any random
print(x)
y = random.random() #generate random floating number, it takes no arguments
print(y)
my_list = ["rock","paper","scissors"]
z = random.choice(my_list)#now it gives us an option to randomly choice something from the list
print(z)
#shuffle to randomly shuffle list or other collection
cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"] #deck of cards
random.shuffle(cards) #randomly shuffle list
print(cards[0]) #print first value of shuffled list
print(cards) #print all values of shuffled list"""

#exception handling = event detected during execution that interrupt the flow of it

# numerator = int(input("Enter a number to divide: ")) #it will work as long as we work inside mathematicly correct 
# denominator = int(input("Enter a number to divide by: ")) #statements, we will interrupt flow of program with divide
# result = numerator / denominator #by 0 for example 
# print(result)

#for any code that is risky with exceptions we can put it inside "try:"

"""try: #It will try to run a program but instead of the error msg and interruption of the flow 
    numerator_2 = int(input("Number to divide: ")) #It will show us a given by us output
    denominator_2= int(input("Number to divide by: ")) #We have to end a try: block with except
    result_2 = numerator_2 / denominator_2
    print(result_2)
except ZeroDivisionError: #here is precise error as exception when someone is trying to divide by 0
    print("You can't divide by 0!")
except ValueError: #here is another problem where someone tried to use letters instead of numbers
    print("Enter only numbers")
except Exception: #It will work on all exceptions but it is better to be precise like above
    print("something went wrong") #of course you can use at the end if someone would do something you didn't anticipate

#Another way of showing someone what they did wrong is using except xxx as e:
#It will print what exceptions someone did insted of only a msg from us
#at the end we can py else: print(result) so it will work only if there is no exceptions we named
try:
    numerator_3 = int(input("Number to divide: ")) 
    denominator_3= int(input("Number to divide by: ")) 
    result_3 = numerator_3 / denominator_3
except ZeroDivisionError as e:
    print(e) 
    print("You can't divide by 0!")
except ValueError as e:
    print(e) 
    print("Enter only numbers")
except Exception as e:
    print(e) 
    print("something went wrong")
else:
    print(result_3)
#Here we can put our finally block that will always execute whatever error will be at the time
finally:
    print("It will always work!")#remember it when open and close file in future"""

#file detection
#we will be looking for files 

"""import os
#we will be checking if file exists somewhere on computer

path = "C:\\Users\\jonas\\OneDrive\\Pulpit\\Gry\\League of Legends.lnk" #that's a path value

if os.path.exists(path): #if path exists print msg and if path is to the file print msg
    print("that location exist")
    if os.path.isfile(path):
        print('That location is a file')
    elif os.path.isdir(path): #if path isn't to a file but to dir print msg
        print("That is a directory")
else: #if path doesn't exist print msg
    print("That location doesn't exist")"""

#reading files
#how to read a context of a file reading python

"""with open("C:\\Users\\jonas\\OneDrive\\Pulpit\\Gry\\test.txt.txt") as file: #now if this file would be inside
# project folder with this python code(visable on left) i would be able to just give a name of file
    print(file.read())#this will close files automaticly after using them so it is convenient

print(file.closed)#It will tell us if the file is closed but using with open("dir") it always close the file """

#The code above with close files after using them automaticly but usually you have to close files by hand after
#using them, as well it won't work when exceptions occur

"""try:
    with open("C:\\Users\\jonas\\OneDrive\\Pulpit\\Gry\\test.txt.txt") as file: #if we misspelled the name or path
#it won't work for us that's why we will use try: block from above
        print(file.read())
except FileNotFoundError as e:
    print(e)
    print("The file was not found :<")"""

#write file we will be writing files in python and append
"""text = "This is some text\nHave a good one\n" #this is a text that we will have in a file
with open("C:\\Users\\jonas\\OneDrive\\Pulpit\\Gry\\test.txt.txt" , 'w') as file: #wit open(path, 'w') to edit
    file.write(text) #edited text from previous version to new with text value from above
with open("C:\\Users\\jonas\\OneDrive\\Pulpit\\Gry\\test.txt.txt") as file: #path to open file
    print(file.read()) #read and close a file

#append file
text_2 = "This is text added insted of replacing old one\ngood job!" #new text to add
with open("C:\\Users\\jonas\\OneDrive\\Pulpit\\Gry\\test.txt.txt" , 'a') as file: #when we use 'a' insted of 'w' we
    file.write(text_2) #can add text to the end of file insted of changing it
with open("C:\\Users\\jonas\\OneDrive\\Pulpit\\Gry\\test.txt.txt") as file: #path to open file
    print(file.read()) #read new edited file"""

#copy a file
"""#shutil import gives us 3 options
# copyfile() = copies contents of a file, it works inside a project cuz you don't need permision
# copy() = copyfile() + permisson mode + destination can be a directory
# copy2() = copy() + copies metadata(file's creation and modifications times)
import shutil

shutil.copy("C:\\Users\\jonas\\OneDrive\\Pulpit\\Gry\\test.txt.txt" , "C:\\Users\\jonas\\OneDrive\\Pulpit\\copy.txt")
#here are two arguments source and destination with ',' between them"""

#moving a file
"""import os #we have to import os from library

source = "C:\\Users\\jonas\\OneDrive\\Pulpit\\copy.txt" #path for source
destination = "C:\\Users\\jonas\\OneDrive\\Pulpit\\naukakodowania\\copy.txt" #path for destination

try: #using try: block with exception for errors
    if os.path.exists(destination): #if path alredy exists inform me about it
        print("There is alredy a file there")
    else: #if path didn't exist
        os.replace(source,destination) #change location from source to destination
        print(source+" was moved") #inform me about it
except FileNotFoundError: #exception is file not found error
    print(source+ " was not found") #inform me about making an error in source path 
#You can do the same with folders insted of naming file in source and on directory and this folder will be moved
#to destination you have given and its name will change accordingly to the name you have given in dest"""

#delate a file in python
"""import os #import os from library
path = 'test.txt' #path argument with value == name of file or path to the file if it isn't in our project
try:
    os.remove(path) #commend to remove path in that case test.txt
except FileNotFoundError as e:
    print(e)
    print("that file was not found")
#now if there is no file that we decided to remove it is a good idea to use try: block
#next step is removing folders
path_2 ="empty_folder"
try:
    os.rmdir(path_2) #instead of remove we use rmdir(ReMoveDIRectory) to delete an empty folder
except FileNotFoundError:
    print("that file was not found")
except PermissionError:
    print("You do not have permission to delete that")
else:
    print(path_2+"was deleted") #but this option won't delete a folder with files

#to remove folder with files we'll use this one:
path_3 = 'folderxd'
import shutil
try:
    shutil.rmtree('folderxd') #ReMoveTREE is to delete a folder with files, it is dangerous 
except FileNotFoundError:
    print("that file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError: #error if we used os.rmdir cuz there are files inside
    print("You can't delete that cuz there are files inside")
else:
    print(path_3+"was deleted")"""

#modules
"""#a file containing python code. May contain functions, classes, etc.
#used with modular programming, which is to separate a program into parts
#we can import a file with python code to use functions from it for example
import messages as msg #import [name of the file} as [nickname]. 
#without the nickname we have to use full name to use functions and diffrent things
#instead of importing everything from messages we can import targeted elements
#from messages import hello,bye
#instead of giving arguents we can use args* to get them all but it is not the best with bigger programs
#cuz of naming conflict

msg.hello() #impotred functions
msg.bye()

help("modules") #will list all modules in terminal
#u can find them in python official documentation online"""

#game of rock,papper, scissors in python projects folder
#quiz game in python projects folder

#object oriented programing(OOP)
"""#is instance of the class, using programing we can create representations of real-life objects
#we can create a class in main module or in file in the project to make it look cleaner using import
#objects need 
# attributes = is/has(name, age, height)
#methods = actions(eat,sleep,record video)
#class is like blueprints that sghow what attributes and methods our object will have
#to impor class we have to write "from [file] import [name of the class]"

class Car: #it's good practice to use capital letter for classes

    def __init__(self,make,model,year,color):#we need 5 argumentts there cuz of self attached to the object
        self.make = make #Attributes of car
        self.model = model 
        self.year = year
        self.color = color
    def drive(self):#self refer to the object using method we need to pass self here in method
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped") #self is replaced with the name of the object

car_1 = Car("Chevy","Corvette",2021,"blue") #when we are using class we only need 4 arguments cuz self
# is passed automaticlly in python 

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
car_1.drive() #self is passed automaticlly like in using class above
car_1.stop() #self is replaced with name that is car_1.model insted of self.model

car_2 = Car("Ford","Mustang",2022,"red")

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)
car_2.drive()
car_2.stop()"""

#class variables
#class and instance variables dif
"""class Car:
    #class variable is declared inside class but outside constructor(in con are insta variables)
    wheels = 4 #class variable it will be assigned to every object created by this class
    def __init__(self,make,model,year,color): #constructor
        self.make=make #instance variable
        self.model=model #instance variable
        self.year=year #instance variable
        self.color=color #instance variable each object can have their own uniqe values assigned  to each variable

car_1 = Car("Chevy","Corvette",2021,"blue") #there are their instance variables declared
car_2 = Car("Ford","Mustang",2022,"red")
car_1.wheels = 2 #U can change class variable outside a class
print("---------------------------")
print(car_1.wheels)#changed class variable above
print("---------------------------")
print(car_2.wheels)#constant class variable from class Car

Car.wheels = 2 #in car_1.wheels we changed class variables for only car_1 object but now we changed class variables 
#for everything
print("---------------------------")
print(Car.wheels)#print new class variable value
print("---------------------------")
print(car_1.wheels)#new value for class variable in object car_1
print("---------------------------")
print(car_2.wheels)#-||- in object car_2
print(car_1.color)"""

#inheritance
"""#its kinda like parents and children parent class can give some of their variables to their children class
class Animal: #parent class

    alive = True #class variable

    def eat(self): #function
        print("This animal is eating")
    
    def sleep(self): #function #you can make change in parent classes and it will change in all child classes
        print("This animal is sleeping")

class Rabbit(Animal):#child class class NewClass(ParenClass): it will inheritance all of variables and functions
    def run(self):
        print("This rabbit is running")#their own atributes by def x(self)

class Fish(Animal):
    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit() #1st object assigned to class Rabbit
fish = Fish() #2nd object -||-
hawk = Hawk() #3rd object -||-

print(rabbit.alive) #even when class Rabbit to which rabbit isassigned is empty, it still have access to 
#parent(Animal) functions like alive or eat() and sleep()
fish.eat()
hawk.sleep()
rabbit.run()
fish.swim()
hawk.fly()"""

#multilevel inheritance
"""#when a derived child class inherits another derived child class

class Organism: #paren class
    alive = True

class Animal(Organism):#child class
    def eat(self):
        print("This animal is eating")

class Dog(Animal): #child's child class
    def bark(self):
        print("This dog is barking")

dog = Dog() #dog is an object of Dog class

print(dog.alive) #inheritance form parent class
dog.eat() #inheritance from child class
dog.bark() #from child's child class"""

#multiple inheritance

