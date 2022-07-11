###############################################
# VERİ YAPILARI (DATA STRUCTURES)
###############################################
# - Veri Yapılarına Giriş ve Hızlı Özet
# - Sayılar (Numbers): int, float, complex
# - Karakter Dizileri (Strings): str
# - Boolean (TRUE-FALSE): bool
# - Liste (List)
# - Sözlük (Dictionary)
# - Demet (Tuple)
# - Set


###############################################
# Veri Yapılarına Giriş ve Hızlı Özet
##############################################

# Sayılar: integer
x = 46
type(x)

# Sayılar: float
x = 10.3
type(x)

# Sayılar: complex
x = 2j + 1
type(x)

# String
x = "Hello ai era"
type(x)

# Boolean
True
False
type(True)
5 == 4
3 == 2
1 == 1
type(3 == 2) #bool

# Liste
x = ["btc", "eth", "xrp"]
type(x)

# Sözlük (dictionary)
x = {"name": "Peter", "Age": 36}
type(x)

"""
Sözlükler (key,value) değerlerinden oluşur -> Java'da hashmap gibi ama çok daha basiti
name: key
Peter: value
"""

# Tuple - listenin aksi huysuz kardeşidir
x = ("python", "ml", "ds")
type(x)

# Set
x = {"python", "ml", "ds"}
type(x)

# Not: Liste, tuple, set ve dictionary veri yapıları aynı zamanda Python Collections (Arrays) olarak geçmektedir.


###############################################
# Sayılar (Numbers): int, float, complex
###############################################

a = 5 #int
b = 10.5 #float

a * 3
a / 7 #result float
a * b / 10
a ** 2 #kare alma işlemi

#######################
# Tipleri değiştirmek, Tip dönüşümü, python casting
#######################

int(b)
float(a)

int(a * b / 10)

c = a * b / 10

int(c)


###############################################
# Karakter Dizileri (Strings)
###############################################

print("John")
print('John')

"John"
name = "John"
name = 'John'

#######################
# Çok Satırlı Karakter Dizileri
#######################

"""Veri Yapıları: Hızlı Özet, 
Sayılar (Numbers): int, float, complex, 
Karakter Dizileri (Strings): str, 
List, Dictionary, Tuple, Set, 
Boolean (TRUE-FALSE): bool"""

long_str = """Veri Yapıları: Hızlı Özet, 
Sayılar (Numbers): int, float, complex, 
Karakter Dizileri (Strings): str, 
List, Dictionary, Tuple, Set, 
Boolean (TRUE-FALSE): bool"""

#######################
# Karakter Dizilerinin Elemanlarına Erişmek
#######################

name
name[0]
name[3]
name[2]

#######################
# Karakter Dizilerinde Slice İşlemi
#######################

name[0:2] #0'dan 2'ye kadar (2 hariç)
long_str[0:10]

#######################
# String İçerisinde Karakter Sorgulamak
#######################

long_str

"veri" in long_str #false

"Veri" in long_str #true

"bool" in long_str

#/n alt satıra geçer

###############################################
# String (Karakter Dizisi) Metodları
###############################################

dir(str) #ilgili değişkenin metotları

#######################
# len -> stringlerde boyut bilgisini söyler, len fonksiyondur len(value)
#######################

name = "john"
type(name)
type(len)

len(name)
len("vahitkeskin")
len("miuul")

"""
bir fonksiyon class yapısı içerisinde tanımlandıysa buna metot denir
eğer bir class yapısı içerisinde değilse fonksiyondur
fonksiyonlar bağımsızdır, metotlar class içerisinde tanımlanmış olmasıdır.
"""

#######################
# upper() & lower(): küçük-büyük dönüşümleri
#######################

"miuul".upper() #class yapısının içersinde o yüzden metot (ctrl) ile bakılabiliyor .upper()
"MIUUL".lower()

# type(upper)
# type(upper())


#######################
# replace: karakter değiştirir
#######################

hi = "Hello AI Era"
hi.replace("l", "p")

#######################
# split: böler
#######################

"Hello AI Era".split() #liste döner

#######################
# strip: kırpar
#######################

" ofofo ".strip() #boşlukları siler
"ofofo".strip("o") #baştaki ve sondaki o'lar uçtu


#######################
# capitalize: ilk harfi büyütür
#######################

"foo".capitalize()

dir("foo") #bu şekilde de string veri tipinin metotlarına erişebiliyoruz

"foo".startswith("f")

###############################################
# Liste (List)
###############################################

# - Değiştirilebilir
# - Sıralıdır. Index işlemleri yapılabilir.
# - Kapsayıcıdır.

#type() metoduna aşinalık önemlidir, sık sık kullanılmalıdır. Hatalar karşısında mücadele etmek için önemli yeri vardır. (print de öyle, dir() de)


notes = [1, 2, 3, 4]
type(notes)
names = ["a", "b", "v", "d"]
not_nam = [1, 2, 3, "a", "b", True, [1, 2, 3]] #bütün değişkenleri farklı bir liste oluşturulabiliyor (kapsayıcılık), birden fazla veri yapısını aynı anda tutabilir

not_nam[0]
not_nam[5]
not_nam[6]
not_nam[6][1] #liste içerisindeki listenin elemanına erişmek (index işlemleri)

type(not_nam[6])

type(not_nam[6][1])

notes[0] = 99 #elemanları değiştirilebilir

not_nam[0:4]


###############################################
# Liste Metodları (List Methods)
###############################################

dir(notes) #listenin kullanılabilir metotları  __ifadeler kullanılamaz__

#######################
# len: builtin python fonksiyonu, boyut bilgisi.
#######################

len(notes)
len(not_nam)

#######################
# append: eleman ekler (çok iyi bilmemiz gerekiyor)
#######################

notes
notes.append(100)

#######################
# pop: indexe göre siler
#######################

notes.pop(0)

#######################
# insert: indexe ekler
#######################

notes.insert(2, 99) #2.index'e 99 değerini ekle (diğer elemanlara sağa kayar)


###############################################
# Sözlük (Dictonary)
###############################################

# Değiştirilebilir.
# Sırasız. (3.7 sonra sıralı.)
# Kapsayıcı.

# key-value çiftleri

dictionary = {"REG": "Regression",
              "LOG": "Logistic Regression",
              "CART": "Classification and Reg"}

dictionary["REG"] #Regression value değerini döndürür


dictionary = {"REG": ["RMSE", 10], #value değerleri bir liste
              "LOG": ["MSE", 20],
              "CART": ["SSE", 30]}

dictionary["CART"][1] #CART key'inin 30 değerini getirir

dictionary = {"REG": 10,
              "LOG": 20,
              "CART": 30}

dictionary["CART"]


#######################
# Key Sorgulama
#######################

"YSA" in dictionary

#######################
# Key'e Göre Value'ya Erişmek
#######################

dictionary["REG"]
dictionary.get("REG") #.get metodu ile de elemanlarına erişebiliriz, aynı şey

#######################
# Value Değiştirmek
#######################

dictionary["REG"] = ["YSA", 10]

#######################
# Tüm Key'lere Erişmek
#######################
dictionary.keys()

#######################
# Tüm Value'lara Erişmek
#######################

dictionary.values()


#######################
# Tüm Çiftleri Tuple Halinde Listeye Çevirme
#######################

dictionary.items() #hem key hemde value değerlerine erişebiliyoruz (bir liste içerisinde key ve value'ları tuple cinsinden döner)

#######################
# Key-Value Değerini Güncellemek
#######################

dictionary.update({"REG": 11})

#######################
# Yeni Key-Value Eklemek
#######################

dictionary.update({"RF": 10}) #olmayan birşeyi update ettiğimizde ekleme işlemi yapar

###############################################
# Demet (Tuple)
###############################################

# - Değiştirilemez.
# - Sıralıdır.
# - Kapsayıcıdır.

t = ("john", "mark", 1, 2)
type(t)

t[0]
t[0:3]

t[0] = 99

#Değiştirmek için önce listeye çevrilir sonra elemanı değiştirilir sonra tekrardan tuple'a dönüştürülür.
t = list(t)
t[0] = 99
t = tuple(t)



###############################################
# Set -> hızlı ve küme işlemlerinde çok kullanılır
###############################################

# - Değiştirilebilir.
# - Sırasız + Eşsizdir.
# - Kapsayıcıdır.

#######################
# difference(): İki kümenin farkı
#######################

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

# set1'de olup set2'de olmayanlar.
set1.difference(set2)
set1 - set2 #küme farkı işlemi

# set2'de olup set1'de olmayanlar.
set2.difference(set1)
set2 - set1

#######################
# symmetric_difference(): İki kümede de birbirlerine göre olmayanlar
#######################

set1.symmetric_difference(set2)
set2.symmetric_difference(set1)

#######################
# intersection(): İki kümenin kesişimi
#######################

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

set1.intersection(set2)
set2.intersection(set1)

set1 & set2 #iki kümenin kesişimi


#######################
# union(): İki kümenin birleşimi
#######################

set1.union(set2)
set2.union(set1)


#######################
# isdisjoint(): İki kümenin kesişimi boş mu? -> kullanılacak olan metotların başında is varsa genelde true-false döner
#######################

set1 = set([7, 8, 9])
set2 = set([5, 6, 7, 8, 9, 10])

set1.isdisjoint(set2)
set2.isdisjoint(set1)


#######################
# isdisjoint(): Bir küme diğer kümenin alt kümesi mi?
#######################

set1.issubset(set2)
set2.issubset(set1)

#######################
# issuperset(): Bir küme diğer kümeyi kapsıyor mu?
#######################

set2.issuperset(set1)
set1.issuperset(set2)