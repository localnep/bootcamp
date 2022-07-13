#Görev1: Verilen değerlerin veri yapılarını inceleyiniz.Type() metodunu kullanınız.
x = 8
y = 3.2
z = 8j + 18
a = "Hello World"
b = True
c = 23 < 22
l = [1, 2, 3, 4]
d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
t = ("Machine Learning", "Data Science")
s = {"Python", "Machine Learning", "Data Science"}

result = x, y, z, a, b, c, l, d, t, s

list(map(lambda x: type(x), result)) # functional

[[type(i) for i in result]] # list comprehension


########################################################################################################################
#Görev2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz.Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız. String metodlarını kullanınız.

# text = "The goal is to turn data into information, and information into insight."
# output = ['THE', 'GOAL', 'IS', 'TO', 'TURN', 'DATA', 'INTO', 'INFORMATION', 'AND', 'INFORMATION', 'INTO', 'INSIGHT']

text = "The goal is to turn data into information, and information into insight."

def test(text):
     text = text.upper()
     text = text.replace(",", " ")
     text = text.replace(".", " ")
     text = text.split()
     return text

print(test(text))


########################################################################################################################
#Görev3: Verilen listeye şu adımları uygulayın.

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

#Adım1: Verilen listenin eleman sayısına bakınız.
len(lst)

#Adım2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
lst[0]
lst[10]

#Adım3: Verilen liste üzerinden["D", "A", "T", "A"] listesi oluşturunuz.
new_list = lst[0:4]

#Adım4: Sekizinci indeksteki elemanı siliniz.
lst.pop(8) #indeks sileceksek pop
#lst.remove(value)

#Adım5: Yeni bir eleman ekleyiniz
lst.append(25)

#Adım6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.
lst.insert(8, "N") #indekse eleman eklerken insert

########################################################################################################################
#Görev4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.

dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}

#Adım1: Key değerlerine erişiniz
dict.keys()

#Adım2: Value değerlerine erişiniz
dict.values()

#Adım3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
dict['Daisy'][1] = 13

#Adım4: Antonio'yu dictionary'den siliniz.
dict.pop('Antonio')
#dict.del(key)

########################################################################################################################
#Görev5: Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden fonksiyon yazın.
#Liste elemanlarına tek tek erişmeniz gerekmektedir. Her bir elemanın çift veya tek olma durumunu kontrol etmek için % yapısını kullanabilirsiniz.

l = [2, 13, 18, 93, 22]

def func(values):
    even_list = []
    odd_list = []
    groups = [even_list, odd_list]
    for index, value in enumerate(values):
        if index % 2 == 0:
            groups[0].append(value)
        else:
            groups[1].append(value)
    print(groups)
    return groups

even_list, odd_list = func(l)

########################################################################################################################
#Görev6: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz
#Numeric olmayan değişkenlerin de isimleri büyümeli. Tek bir list comprehension yapısı kullanılmalı.

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns


df.columns = ["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]
df.columns

########################################################################################################################
#Görev7: List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan değişkenlerin isimlerinin sonuna "FLAG" yazınız.
#Tüm değişkenlerin isimleri büyük harf olmalı. Tek bir list comprehension yapısı ile yapılmalı

df.columns = [col + "_FLAG" if "NO" in col else col for col in df.columns]
df.columns

########################################################################################################################
#Görev8: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
#önce verilen listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
#sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz ve adını new_df olarak isimlendiriniz.

import seaborn as sns
df = sns.load_dataset("car_crashes")
df

og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df