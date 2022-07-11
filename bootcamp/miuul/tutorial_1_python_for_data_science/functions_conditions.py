###############################################
# FONKSİYONLAR, KOŞULLAR, DÖNGÜLER, COMPREHENSIONS
###############################################
# - Fonksiyonlar (Functions)
# - Koşullar (Conditions)
# - Döngüler (Loops)
# - Comprehesions


###############################################
# FONKSİYONLAR (FUNCTIONS)
###############################################

#######################
# Fonksiyon Okuryazarlığı
#######################

"""
parametre fonksiyon tanımlanması esnasında ifade edilen değişkenlerdir
argüman ise bu fonksiyonlar çağrıldığında parametre değerlerine karşılık girilen değerlerdir
sık sık birbirlerinin yerine kullanılabilirler (argüman diyerek ifade edeceğiz)
argümanlar bir özellik belirtebileceği gibi fonksiyonun genel amacını biçimlendirmek üzere kullanılan alt görevcilerdir.
print fonksiyonun sep argümanı; iki değer arasına string koymak istersek
"""

"""
Dökümanyasyon: docstring
?print
help(print)
"""

print("a", "b")

print("a", "b", sep="__") #iki değer arasına string '__' koyar, default olarak "" boşluktur.


#######################
# Fonksiyon Tanımlama
#PEP8: kod yazarken boşluk yazma kuralı, böyle yazarsanız daha iyi dediği kod yazma örnekleri
#######################

def calculate(x): #girilen sayıları 2 ile çarpacak
    print(x * 2)


calculate(5)


# İki argümanlı/parametreli bir fonksiyon tanımlayalım.

def summer(arg1, arg2):
    print(arg1 + arg2)


summer(7, 8)

summer(8, 7)

summer(arg2=8, arg1=7) #argümanlara bu şekilde de değer verilebilir


#######################
# Docstring
#######################

"""
Docstring: fonksiyonlarımıza herkesin anlayabileceği ortak bir dil ile bilgi notu ekleme yoludur. Tıpki şuanki yaptığım gibi (:
oluşturmanın birden fazla yolu vardır; en yaygın kullanılan yol numpy ve google'dır. Docstring formatı istendiği taktide değiştrilebilir.
File->settings->search(docstring) -> in tools -> Docstring format
bir fonksiyona docstring eklediğimizde temel olarak 3 bölümü vardır.
1:fonksiyonun ne yaptığı (tek bir cümle, basit anlaşılır)
2: argümanları
3: return ne olacağı
ek olarak: Examples ve Notes bölümlerinide ekleyebiliriz
"""

def summer(arg1, arg2):
    print(arg1 + arg2)


def summer(arg1, arg2):
    """
    Sum of two numbers    -> (fonksiyonun ne yaptığı bilgisi yazılır)

    Args:                   -> (argümanların tipleri belirtilir)
        arg1: int, float
        arg2: int, float

    Returns:            -> (return bilgisi verilir)
        int, float

    """
    #Fonksiyonumuza dökümantasyon eklemiş oluyoruz.

    print(arg1 + arg2)


summer(1, 3)


#######################
# Fonksiyonların Statement/Body Bölümü
#######################

# def function_name(parameters/arguments):
#     statements (function body)

def say_hi(): #argümanı olmayan fonks
    print("Merhaba")
    print("Hi")
    print("Hello")


say_hi()


def say_hi(string):
    print(string)
    print("Hi")
    print("Hello")


say_hi("miuul")


def multiplication(a, b): #girilen 2 sayısı çarpan fonksiyon
    c = a * b
    print(c)


multiplication(10, 9)

# girilen değerleri bir liste içinde saklayacak fonksiyon.

list_store = [] #boş liste


def add_element(a, b):
    c = a * b
    list_store.append(c) #uygulandığı listeye kalıcı değişiklik yapar
    print(list_store)

#bütün çalışma içerisinden erişebilen değişkenlere global scope -> global etki alanındaki değişkenler
#sadece ilgili fonksiyon, döngü, if yapıları içerisinde oluşturulan değişkenlere local scope

add_element(1, 8)
add_element(18, 8)
add_element(180, 10)


#######################
# Ön Tanımlı Argümanlar/Parametreler (Default Parameters/Arguments)
#######################

def divide(a, b):
    print(a / b)


divide(1, 2)


def divide(a, b=1): #b'nin ön tanımlı değeri girilmiş
    print(a / b)


divide(10)


def say_hi(string="Merhaba"):
    print(string)
    print("Hi")
    print("Hello")


say_hi("mrb") #kullanıcı hiçbirşey girmezse default merhaba yazar, mrb diyerek girersek ön tanımlı değer değilde mrb yazacaktır.

#######################
# Ne Zaman Fonksiyon Yazma İhtiyacımız Olur?
#-birbirini tekrar eden görevler söz konusu olduğunda fonksiyon yazma ihtiyacı doğacaktır.
#######################

#belediyenin akıllı sokak lambaları sinyalleri için (ısı,nem,pil) hesaplamalar yapmak istiyoruz.
# varm, moisture, charge

(56 + 15) / 80
(17 + 45) / 70
(52 + 45) / 80


# DRY

def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)


calculate(98, 12, 78)


#######################
# Return: Fonksiyon Çıktılarını Girdi Olarak Kullanmak
######################

def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)


# calculate(98, 12, 78) * 10 ->izin verdirmez çünkü return olmayan (NoneType) bir metot'un tipi belli değildir.

def calculate(varm, moisture, charge):
    return (varm + moisture) / charge #return'dan sonraki alt satırlardaki kod çalışmaz


calculate(98, 12, 78) * 10

a = calculate(98, 12, 78)


def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge
    return varm, moisture, charge, output #birden fazla return verebiliyoruz (java'da çok zorlanmıştım yoktu böyle seçenek)

#bir fonksiyonun çıktısını kullanmak istiyorsak return kullanmalıyız
#birden fazla çıktı verebiliyoru ve bu çıktıları birden fazla değişkene aynı anda atayabiliyoruz


type(calculate(98, 12, 78)) #tuple şeklinde dönüş yapar

varma, moisturea, chargea, outputa = calculate(98, 12, 78) #her bir dönen değeri değişkene atadık (bu python'ı sevmeye başladım)


#######################
# Fonksiyon İçerisinden Fonksiyon Çağırmak
######################

def calculate(varm, moisture, charge):
    return int((varm + moisture) / charge)


calculate(90, 12, 12) * 10


def standardization(a, p): #buradaki a argümanı calculate'in sonucu olacak
    return a * 10 / 100 * p * p


standardization(45, 1)

#bu fonksiyonda başka fonksyionları çağıracağımız için ve argümanlar üzerinde işlemler yapacağımız için biçimlendirmek istediğimiz argümanları tanımladık
def all_calculation(varm, moisture, charge, p):
    a = calculate(varm, moisture, charge) #a calculate'in sonucu
    b = standardization(a, p)
    print(b * 10)


all_calculation(1, 3, 5, 12)


def all_calculation(varm, moisture, charge, a, p): #burada biçimlendirmek istediğimzden a'yı da dahil ettik
    print(calculate(varm, moisture, charge)) #a değişkeni yok
    b = standardization(a, p)
    print(b * 10)


all_calculation(1, 3, 5, 19, 12)

#######################
# Lokal & Global Değişkenler (Local & Global Variables)
#######################


list_store = [1, 2] #list_store: global scope -> Her yerden erişilebilir

def add_element(a, b):
    c = a * b #c: local scope -> Sadece fonksiyon içerisinden erişilir
    list_store.append(c)
    print(list_store)

add_element(1, 9)

###############################################
# KOŞULLAR (CONDITIONS)
###############################################

# True-False'u hatırlayalım.
1 == 1
1 == 2

# if
if 1 == 1:
    print("something")

if 1 == 2:
    print("something")

number = 11

if number == 10:
    print("number is 10")

number = 10
number = 20


def number_check(number):
    if number == 10:
        print("number is 10")

number_check(12)

#######################
# else
#######################

def number_check(number):
    if number == 10:
        print("number is 10")

number_check(12)


def number_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")

number_check(12)

#######################
# elif
#######################

def number_check(number):
    if number > 10:
        print("greater than 10")
    elif number < 10:
        print("less than 10")
    else:
        print("equal to 10")

number_check(6)

###############################################
# DÖNGÜLER (LOOPS)
###############################################
# for loop

students = ["John", "Mark", "Venessa", "Mariam"] #liste

students[0]
students[1]
students[2]

for student in students: #her bir elemanı yazdırma işlemi
    print(student)

for student in students: #her bir elemanı büyük harflerle yazdıracak
    print(student.upper())

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(salary)

#değerlere zam uygulamak istiyoruz
for salary in salaries: #%20 zam
    print(int(salary*20/100 + salary))

for salary in salaries:
    print(int(salary*30/100 + salary))

for salary in salaries:
    print(int(salary*50/100 + salary))

def new_salary(salary, rate): #hem maaşları hemde zam miktarı argümanı
    return int(salary*rate/100 + salary)

new_salary(1500, 10) #1500 değerin %10 zam yap
new_salary(2000, 20) #2000 değerin %20 zam yap

for salary in salaries: #tüm maaşlara yüzde 20 zam yapar
    print(new_salary(salary, 20))

#BU KISMI BEĞENDİM, GÜZEL ÖRNEK
salaries2 = [10700, 25000, 30400, 40300, 50200]

for salary in salaries2: #tüm değerlere %15 zam yap
    print(new_salary(salary, 15))

for salary in salaries:
    if salary >= 3000:
        print(new_salary(salary, 10))
    else:
        print(new_salary(salary, 20))



#######################
# Uygulama - Mülakat Sorusu
#######################

# Amaç: Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz.

# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

#çift olan index'leri büyütüyor, küçük olan index'leri küçültüyor

range(len("miuul")) #(0,5) -> 0'dan 5'e kadar
range(0, 5)

for i in range(len("miuul")):
    print(i)

# 4 % 2 == 0
# m = "miuul"
# m[0]

def alternating(string):
    new_string = ""
    # girilen string'in index'lerinde gez.
    for string_index in range(len(string)):
        # index çift ise büyük harfe çevir.
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        # index tek ise küçük harfe çevir.
        else:
            new_string += string[string_index].lower()
    print(new_string)

alternating("miuul")

#######################
# break & continue & while
#######################

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    if salary == 3000:
        break
    print(salary)


for salary in salaries:
    if salary == 3000:
        continue
    print(salary)


# while

number = 1
while number < 5:
    print(number)
    number += 1

#######################
# Enumerate: Otomatik Counter/Indexer ile for loop
#######################

#Bir iteratif nesne içerisinde gezip elemanlarına birşey yaparken aynı zamanda o elemanların index bilgilerini takip etmek istediğimizde


students = ["John", "Mark", "Venessa", "Mariam"]

for student in students:
    print(student)

for index, student in enumerate(students):
    print(index, student)

#Amaç: tek indeksteki öğrencileri ve çift indeksteki öğrencileri farklı liselere almak
A = []
B = []

for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)


#######################
# Uygulama - Mülakat Sorusu
#######################
# divide_students fonksiyonu yazınız.
# Çift indexte yer alan öğrencileri bir listeye alınız.
# Tek indexte yer alan öğrencileri başka bir listeye alınız.
# Fakat bu iki liste tek bir liste olarak return olsun.

students = ["John", "Mark", "Venessa", "Mariam"]


def divide_students(students):
    groups = [[], []] #2 alt listeyi içeren groups listesini return edeceğiz
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups

st = divide_students(students)
st[0]
st[1]


#######################
# alternating fonksiyonunun enumerate ile yazılması
#######################

def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)

alternating_with_enumerate("hi my name is john and i am learning python")

#######################
# Zip
#######################

#farklı listeleri, eşlemek, birbiriyle değerlendirmek istiyoruz

students = ["John", "Mark", "Venessa", "Mariam"]

departments = ["mathematics", "statistics", "physics", "astronomy"]

ages = [23, 30, 26, 22]

list(zip(students, departments, ages)) #bir liste içerisinde tuple formunda

###############################################
# lambda, map, filter, reduce - Fonksiyonel Programlama - Vektör Seviyesinde İşlemler
###############################################

#lambda özellikle apply fonk. ile birlikte kullanılır
#lambda kullan at fonks,

def summer(a, b):
    return a + b

summer(1, 3) * 9

new_sum = lambda a, b: a + b #sol taraftaki a ve b argümanlar : şu işi yapar (ifadeleri topluyor), fonksiyonları tanımlama şeklidir, apply ve map ile birlikte sık kullanılır

new_sum(4, 5)

# map - fonksiyon verilerek döngü yazmaktan kurtarır
salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x

new_salary(5000)

for salary in salaries:
    print(new_salary(salary))

list(map(new_salary, salaries)) #foreach gibi düşünülebilir
#map(fonksiyon, gezilecek nesne)


# del new_sum
list(map(lambda x: x * 20 / 100 + x, salaries)) #salaries listesindeki elemanların %20 zam yapar
list(map(lambda x: x ** 2 , salaries)) #salaries listesindeki elemanların karesini alır

# FILTER - belirli koşulu sağlayanları seçmek istediğimizde
list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x % 2 == 0, list_store)) # list store'daki elemanların 2 ile bölümünden kalanları seçme işlemi

# REDUCE - indirgemek, elemanlara işlem uygulamak için
from functools import reduce
list_store = [1, 2, 3, 4]
reduce(lambda a, b: a + b, list_store) #list store'daki elemanları toplar (1+2) = 3 -> (3+3) = 6 -> (6+4) = 10

###############################################
# COMPREHENSIONS
###############################################

#######################
# List Comprehension - Not asıl açıklamalar github hesabımda list comprehension'da
# çıktı list tipindedir, amaç daha az kod yazıp daha çok şey yapmak
#######################

salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x

for salary in salaries:
    print(new_salary(salary))

null_list = []

for salary in salaries:
    null_list.append(new_salary(salary))

null_list = []

for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2))

[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries] #

#kademe kademe neler olduğunu görelim
[salary * 2 for salary in salaries]
[salary * 2 for salary in salaries if salary < 3000]
[salary * 2 if salary < 3000 else salary * 0 for salary in salaries] #if-else birlikte kullanılacaksa sol tarafta olmalıdır
[new_salary(salary * 2) if salary < 3000 else new_salary(salary * 0.2) for salary in salaries]

students = ["John", "Mark", "Venessa", "Mariam"]
students_no = ["John", "Venessa"]

#Amaç: students listesinde stundes_no elemanları varsa isimlerini küçük harflere, yoksa büyük harflerle dönüştür
#2 farklı şekilde gerçekleştirebiliriz
[student.lower() if student in students_no else student.upper() for student in students]
[student.upper() if student not in students_no else student.lower() for student in students]

#######################
# Dict Comprehension
#######################

dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}

dictionary.keys()
dictionary.values()
dictionary.items()

{k: v ** 2 for (k, v) in dictionary.items()}

{k.upper(): v for (k, v) in dictionary.items()}

{k.upper(): v*2 for (k, v) in dictionary.items()}



#######################
# Uygulama - Mülakat Sorusu
#######################

# Amaç: çift sayıların karesi alınarak bir sözlüğe eklenmek istemektedir
# Key'ler orjinal değerler value'lar ise değiştirilmiş değerler olacak.


numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2

{n: n ** 2 for n in numbers if n % 2 == 0}

#######################
# List & Dict Comprehension Uygulamalar
#######################

#######################
# Bir Veri Setindeki Değişken İsimlerini Değiştirmek
#######################

# before:
# ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

# after:
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

for col in df.columns:
    print(col.upper()) #kalıcı değil


A = []

for col in df.columns:
    A.append(col.upper())

df.columns = A

df = sns.load_dataset("car_crashes")

df.columns = [col.upper() for col in df.columns]

#######################
# İsminde "INS" olan değişkenlerin başına FLAG diğerlerine NO_FLAG eklemek istiyoruz.
#######################

# before:
# ['TOTAL',
# 'SPEEDING',
# 'ALCOHOL',
# 'NOT_DISTRACTED',
# 'NO_PREVIOUS',
# 'INS_PREMIUM',
# 'INS_LOSSES',
# 'ABBREV']

# after:
# ['NO_FLAG_TOTAL',
#  'NO_FLAG_SPEEDING',
#  'NO_FLAG_ALCOHOL',
#  'NO_FLAG_NOT_DISTRACTED',
#  'NO_FLAG_NO_PREVIOUS',
#  'FLAG_INS_PREMIUM',
#  'FLAG_INS_LOSSES',
#  'NO_FLAG_ABBREV']

[col for col in df.columns if "INS" in col]

["FLAG_" + col for col in df.columns if "INS" in col]

["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

df.columns = ["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

#######################
# Amaç key'i string, value'su aşağıdaki gibi bir liste olan sözlük oluşturmak.
# Sadece sayısal değişkenler için yapmak istiyoruz.
#######################

# Output:
# {'total': ['mean', 'min', 'max', 'var'],
#  'speeding': ['mean', 'min', 'max', 'var'],
#  'alcohol': ['mean', 'min', 'max', 'var'],
#  'not_distracted': ['mean', 'min', 'max', 'var'],
#  'no_previous': ['mean', 'min', 'max', 'var'],
#  'ins_premium': ['mean', 'min', 'max', 'var'],
#  'ins_losses': ['mean', 'min', 'max', 'var']}

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

num_cols = [col for col in df.columns if df[col].dtype != "O"]

soz = {}
agg_list = ["mean", "min", "max", "sum"]

for col in num_cols:
    soz[col] = agg_list

# kısa yol
new_dict = {col: agg_list for col in num_cols}

df[num_cols].head()

df[num_cols].agg(new_dict)

