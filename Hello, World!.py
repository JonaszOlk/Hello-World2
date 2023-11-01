#W3schoolsnauka
print("Hello, World!")
x = 4
y = 5
z = 6 #to jest komentarz this is a comment
print(x)
#to jest komentarz pomiedzy 6 a 7 linią, ma się nie wyswietlic
print(y)
print(z)
#This
#is
#a
#comment
"""
this
is 
a 
comment
as
well
"""
a = 1
b = "jhon"
print(a)
print(b)
c = str(7) 
d = float(7)
e = int(7)
print(c)
print(d)
print(e)
print(type(a))#pokazuje rodzaj zmiennej zamiast jej wartości
print(type(b))
C = 8 #Duze C nie nadpisze małego c i beda traktowane jako inne zmienne
print(c)
print(C)
#ta sama nazwa ale inna wielkość liter czy podkreślenia w trakcie
mojeimie = 'Jonasz'
mojeImie = 'Jonasz'
MojeImie = 'Jonasz'
_moje_imie = 'Jonasz'
Moje_Imie = 'Jonasz'
print(mojeImie)
print(mojeImie)
print(MojeImie)
print(_moje_imie)
print(Moje_Imie)
#zmienne odzdzielone przcinkiem ta sama ilość co wartości
X, Y, Z = 'blue', 'red', 'black'
print(X)
print(Y)
print(Z)
F = G = H = 'White'#tworzenie wspólnej wartości dla różnych zmiennych
print(F)
print(G)
print(H)
owoce = ['jabłko', 'banan', 'wiśnia']#odpakowanie zbiorów
U , I, O = owoce
print(U)
print(I)
print(O)
print(U, I, O)
print(U + I + O)#można użyć przecinków lub plusów
#dla liczb plus będzie działał jako zadanie w przeciwieństwie do słów
print(x + y + z)
def myfunc():
    print("mam na imię " + mojeimie)#spacje prze drugim '' bo się zleje 
myfunc()
def imiona():
    mojeimie = 'nikodem'
    print('mam na imię ' + mojeimie)
imiona()
print('mam na imię ' + mojeimie)
def brat():
    global mlody
    #global wyciąga poza zamkniętą funkcje wartość przypisaną 
    # i nadpisuje zmieną
    mlody = 'Miłosz'
brat()
print('Mój młodszy brat ma na imię ' + mlody)
zx = 1 #int\integer plus minus znak, bez limitu znakow i bez przecinka
zxc = 2.4 #float plus minuz znak, z liczbami po przecniku,naukowa liczba"e" co oznacza do 10 potęgi
zxcv = 2j  #complex oznacz się z literą j co oznacza liczby wyobrazone, np.urojone
print (type(zx))
print(type(zxc))
print(type(zxcv))
#zmiana z int do float
xz = float(zx)
#zmiana z float do int
cxz = int(zxc)
#zmiana z int do complex
vcxz = complex(zx)
print(xz)
print(cxz)
print(vcxz)
print(type(xz))
print(type(cxz))
print(type(vcxz))
import random#tworzy pseudo funkcje losowości
print(random.randrange(1, 10))#kontynuacja funkcji 
dxs = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(dxs)#dzięki użyciu potrojnego znaku string złamania w teksćie bedą w 
#tym samym miejscu co w kodzie 
#string są liczone jak arrays, dzięki czemu można wyciągnąć 
# element wnętrza np
dfg = 'Wyviąganie zawartości'
print(dfg[4])#arrays zaczymaja sie od 0 i ida o jeden w gore 
#dzieki str bedacym arrays mozna je loopowac np
#uzywamy dla tego funkcji "for smth in 'smth': "
for asdf in 'jabłko':
    print(asdf)
#zeby poznac dlugosc zawarosci str uzywamy opcji len()
agfh = 'konieckraju'
print(len(agfh))
#korzystąjac z funkcji "in" mozna sprawdzic czy dany element w niej występuje 
txt = 'dawno, dawno temu za górami i lasami'
print("lasami" in txt)
print("smoki" in txt)
print('smoki' not in txt)
#zamiast komunikatu ture or false mozemy uzyc funkcji "if" ktora pozwoli nam zmienic odpowiedzi
if "lasami" in txt:
    print('Tak, w tekście znajduje się "lasami"')
if "smoki" not in txt:
    print('nie ma słowa "smoki" w tekście')
print(3 + 5)
print('Iron'+ 'Man')
fyt = 'basket' #strings można dodawac do siebie jako wartości
tyf = 'ball'
print(fyt + tyf)
print('360'+ '360')#kiedy zapiszemy liczby jako string data nie mozna wykonac matematyki
#nie można dodawać liczb ze string 
print(type(fyt))#samo type sprawdz rodzaj zmiennej z komendą print daje output z info
city = "Berlin"
age = 42
balance = 820.31
print(type(city))
print(type(age))
print(type(balance))
djk = 6 #dzielenie wartości zawsze bedzie traktowane jako float, nawet gdy wynik moglbybyc str
jdk = 2
csdf = 6/2
print(type(djk))
print(type(jdk))
print(type(csdf))
#input() zawsze zapisuje wartości wpisane przez użytkownika jako string data 
# birth_year = input()
# print(type(birth_year))
#komenda int() zamieni kazdy rodzaj data w int 
ghjs = "567"
kjsl = int(ghjs)
print(type(ghjs))
print(type(kjsl))
#można od razu modyfikować str data w input na int data
# x = int(input())
#to samo dotyczy się innych converts
aert = 13
trea = float(aert)
print(trea)
port = 13.7
trop = int(port)
print(trop)
#te komendy są ręcznym zmienianiem danych, jednak w kodzie mogą wystąpić naturalne zmiany struktury wartości
A1 = 2
A2 = 4
A3 = A2/A1 
print(type(A1))
print(type(A3))
posd = "asodjiwnppqnwdi"
print(posd[2:5])#pozwala wyciągnąć część string data nie licząc pierwszego elementu opisanego w komendzie
print(posd[:5])#zostawiając pusty pierwszy człon wyciągamy wszystko od 0 do podanego zamknięcia
print(posd[5:])#zostawiając ostatni człon pusty możemy wyciągnąć od zaznaczonego do końca
klao = posd[:5]#tworzenie nowej zmiennej z częsciowązawartością string i ponowne lączenie w całość
aolk = posd[5:]
print(klao + aolk)
klar = 'Samara to nie imię' 
print(klar[-7:-4])#negative indexing w slicingu pozwala zrobić to samo tylko od tyłu
#modyfikacja string value
kolin = 'Hello, world!'
print(kolin.upper())#po zmiennej używamy .upper() zeby calosc pojawiła się w upercase
print(kolin.lower())#.lower() powoduje odwrotność czyli całość jest w lowercase
#ze wzgledu na to ze python traktuje string dosłownie z przestrzenia przed i po tekscie mozna to łatwo edytowac
porty = ' Hello, world! '
print(porty)
print(porty.strip())#komenda .strip() usuwa whitespaces przed i po tekscie 
#wewnętrzne zmienianie string
print(kolin)
print(kolin.replace('H', 'J'))#komeda .replace() zamienia w stringu dane na wybrane przez nas ale tez trzeba uzyc ""
#.split() pozwala nam wybrać seperator, który rozdzieli nam fragmenty w tym miejscu
print(kolin.split(","))
#strin concatenation czyli combination
pal = 'Hello'
lap = 'world'
papa = pal + lap
print(papa)
#zeby stworzyc przerw mozna zostawic spacje przed drugim zamknięciem lub uzyc " " ze spacją w środku
papa2 = pal + " " + lap
print(papa2)
#nie mozna łączyć string z numbers(int,float,complex) przez plus za to można użyc format() gdzie w stringu 
#umieszczamy {} zeby wskazac miejsce 
lata3 = 34
txt47 = 'mam {} lata'
print(txt47.format(lata3))
#.format() nie ma limitu ilosci argumentow i umiesza je w kolejnosci przedstawionej 
cena7 = 49.99
ilosc34 = 5
przedmiot_nr = 437
txt33 = "chcę kupić {}, w ilości {} sztuk, za {} złotych"
print(txt33.format(przedmiot_nr, ilosc34, cena7))#mozna uzyc index numbers w {} zeby miec pewnosc co do kolejności
#\ <- tego znaku uzywamy zeby uzyc nielegalnych znakow w string przykładowo wewnatrz "" uzycie ""
txt485 = "Bardzo mi się podobał serial o tytul \"Gra o tron\" na Hbo"
print(txt485)
#znaki ktore mozemy dzieki temu uzyc 
#\' -> '
#\\ -> \
#\n -> new line
#\r -> carriage return
#\t -> tab
#\b -> backspace
#\f -> form feed
#\ooo -> octal value 
#\xhh -> hex value
X47 = txt485.count("o") #liczy ilość występowań
print(X47)
X48 = txt485.endswith("o") #sprawź czy kończy się na o
print(X48)
print(txt485)
X49 = txt485.find("o")
print(X49)
#Boolean values czyli True or False
print(10 > 9)
print(10 == 9)
print(10 < 9)
#korzystając z if and else możemy zmenić True od False na wybrane przez nas odpowiedzi
ASDFG = 35
GFDSA = 197
if GFDSA > ASDFG:
    print('GFDSA jest większe od ASDFG')
else:
    print('GFDSA nie jest większe od ASDFG')
#bool() to opcja do oceniania wartości 
print(bool('Hello'))
print(bool(15))
XDD = 'Hello'
XDDD = 15
print(bool(XDD))
print(bool(XDDD))#większość wartości bedzie prawdziwa
#jedynie puste zbiory będą wyskakiwać jako fałyszywe np.
print(bool())
#jeszcze w przypadku opcji class gdy wynik bedzie wracal do zera tez mamy fałsz
class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))
#funkcje mogą wrócic jako boolean Value
def myFunction():
    return True
print(myFunction())
#mozna stworzyc kod oparty o boolean answers
if myFunction():
    print('Yes')
else:
    print('NO')
#istnieją wbudowane opcje opierające się o boolean
XD37 = 456
print(isinstance(XD37, int))#sprawda czy wartosc jest zapisana jako integer
#Python Operators
#arythmetics
#składa się na to +, -, *, /, **(potęgi), %(reszta z dzielenia), //(zaokrągla do najbliższej liczby całkowitej w dół)
print(1 + 2)#addition
print(5 - 2)#substraction
print(3 * 5)#multiplication
print(8 / 2)#division
print(2 ** 5)#exponentiation
print(7 % 2)#modulus
print(7 // 2)#floor division
#Assigment operations
XE = 5 #operator =
XE += 3 # +=, co znaczy XE = XE + 3
print(XE)
XE -= 3 # -=, co znaczy XE = XE - 3
print(XE)
#XE *= 3 # *=, co znaczy XE = XE * 3
#XE /= 3 # /=, co znaczy XE = XE / 3
#XE %= 3 # %=, co znaczy XE = XE % 3
#XE **= 3 # **=, co znaczy XE = XE ** 3
#XE &= 3 # &=, co znaczy XE = XE & 3
#XE |= 3 # |=, co znaczy XE = XE |= 3 
#XE ^= 3 # ^=, co znaczy XE = XE ^= 3
#XE >>= 3# >>=, co znaczy XE = XE >>= 3
#XE <<= 3# <<=, co znaczy XE = XE <<= 3
#Comparison operators
A_2 = 7
A_3 = 10
print(A_2==A_3)#równe ==
print(A_2!=A_3)#nierówne !=
print(A_2>A_3)#wiekszę >
print(A_2<A_3)#mniejsze <
print(A_2>=A_3)#większe lub równe >=
print(A_2<=A_3)#mniejsze lub równe <=
#logical operators "and", "or", "not"
print(A_2>5 and A_2<9)#oba są prawdziwe więć true
print(A_2>6 or A_2>9)#wystarczy że jedno jest prawdziwe jak tutaj
print(not(A_2>5 and A_2<9))#pokazuje wynik przeciwny do realnego 
print(2.5/11*100)
