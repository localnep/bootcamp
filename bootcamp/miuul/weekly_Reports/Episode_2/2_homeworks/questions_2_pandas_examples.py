#####################################################################################################################################################################
# Pandas Alıştırmalar

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

#####################################################################################################################################################################

# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.

df = sns.load_dataset("titanic")
df.head()

#####################################################################################################################################################################

# Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.

df["sex"].value_counts()

#####################################################################################################################################################################

# Görev 3: Her bir sütuna ait unique değerlerin sayısını bulunuz.

df.nunique()
for columns in df:
    print(str(columns), "değişkeninin unique değerleri: ", df[columns].unique(), "unique sayısı " ,len(df[columns].unique()), "\n")

#####################################################################################################################################################################

# Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.

df["pclass"].nunique()
len(df["pclass"].unique())

#####################################################################################################################################################################

# Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.

df["pclass"].nunique()
df["parch"].nunique()

#####################################################################################################################################################################

# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.

str(df["embarked"].dtype)
df["embarked"] = df["embarked"].astype("category")
str(df["embarked"].dtype)

#####################################################################################################################################################################

# Görev 7: embarked değeri C olonların tüm bilgilerini gösteriniz.

df[df["embarked"] == "C"]
#df["embarked"] == "C" elemanlarının True-False değerini getirir. O elemanları almak istiyorsak çerçeveletmemiz gerekir. df[df[]]

#####################################################################################################################################################################

# Görev 8: embarked değeri S olmayanların tüm bilgilerini gösteriniz.

df[df["embarked"] != "S"]

#####################################################################################################################################################################

# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.

df[(df["age"] < 30) & (df["sex"] == "female")]

#####################################################################################################################################################################

# Görev 10: Fare'i 500'den büyük veya yaşı 70'den büyük yolcuların bilgilerini gösteriniz.

df[(df["fare"] > 500) | (df["age"] > 70)]

#####################################################################################################################################################################

# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.

df.isnull().sum()

#####################################################################################################################################################################

# Görev 12: who değişkenini dataframe'den çıkarınız.

df.drop("who", axis = 1) # kalıcı değil (inplace)
"who" in df.columns # True

#####################################################################################################################################################################

# Görev 13: deck değişkenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.

df["deck"].value_counts() #deck değişkeninin sınıfların sayıları
(df["deck"].value_counts()).index[0] #deck değişkenin en çok tekrar eden değeri 'C' index'ni alma

#df["deck"].mode() # en çok tekrar eden sınıfı bulmak için mode alma işlemini de uygulayabiliriz

df[df["deck"].isnull()]["deck"] # doldurmadan önceki NaN değerlerini görelim
df["deck"] = df["deck"].fillna((df["deck"].value_counts()).index[0]) # en global yöntem ile dolduruyoruz

#####################################################################################################################################################################

# Görev 14: age değişkenindeki boş değerleri age değişkenin medyanı ile doldurunuz.

df[df["age"].isnull()]["age"] # age değişkenin NaN değerleri
df["age"] = df["age"].fillna(df["age"].median()) # NaN değerleri median ile doldurma

#####################################################################################################################################################################

# Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımında sum, count, mean değerlerini bulun.

list = ["sum", "count", "mean"]
df.groupby(["sex","pclass"]).agg({"survived": list})

#####################################################################################################################################################################

# Görev 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 verecek bir fonksiyon yazın. Yazdığınız fonksiyonu kullanarak titanik veri
#setinde age_flag adında bir değişken oluşturunuz. (apply ve lambda yapılarını kullanınız)

def func(df, column):
    return df[column].apply(lambda x: 1 if x < 30 else 0)

func = lambda df, column: df[column].apply(lambda x: 1 if x < 30 else 0)

df["age"] = func(df, "age")
df["age"]

#####################################################################################################################################################################

#Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.

df = sns.load_dataset("tips")
df.head()

#####################################################################################################################################################################

#Görev 18: Time değişkeninin kategorilerine (Dinner,Lunch) göre total_bill değerinin sum, min, max ve mean değerlerini bulunuz.

list = ["sum", "min", "max", "mean"]
df["time"].value_counts()
df.groupby(["time"]).agg({"total_bill": list}) #önce time'ın sınıflarına göre gruplar ve list içerisindeki toplulaştırma fonksiyonlarını uygular

#####################################################################################################################################################################

#Görev 19: Day ve time'a göre total_bill değerlerinin sum,min,max ve mean değerlerini bulunuz.

list = ["sum", "min", "max", "mean"]
df.groupby(["day", "time"]).agg({"total_bill": list})

#####################################################################################################################################################################

#Görev 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'a göre sum, min, max ve mean değerlerini bulun.


list = ["sum", "min", "max", "mean"]
df[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby(["day"]).agg({"total_bill": list,
                                                                        "tip": list})

#####################################################################################################################################################################

# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)

df.loc[(df["size"] < 3) & (df["total_bill"] > 10)].mean()

#####################################################################################################################################################################

# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.

#df.loc[:,["total_bill", "tip"]].sum()
sum = df["total_bill"] + df["tip"]
df["total_bill_tip_sum"] = sum
df["total_bill_tip_sum"]

#df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]

#####################################################################################################################################################################

#Görev 23:
"""
Total_bill değişkeninin kadın ve erkek için ayrı ayrı ortalamasını bulunuz. Bulduğunuz ortalamaların altında olanlara 0, üstünde ve eşit olanlara 1
verildiği yeni bir total_bill_flag değişkeni oluşturunuz.
Kadınlar için Female olanlarının ortalamaları, erkekler için ise Male olanların ortalamaları dikkate alınacaktır. Parametre olarak cinsiyet ve total_bill
alan bir fonksiyon yazarak başlayınız. (if-else koşulları içerecek)
"""

#Adım adım ele alayım..
df[df["sex"] == "Female"] #cinsiyeti kadın olanları getir
df[df["sex"] == "Female"].mean() #cinsiyeti kadın olanların sayısal değişkenlerinin ortalaması
df[df["sex"] == "Female"]["total_bill"].mean() #cinsiyeti kadın olanların 'total_bill' değişkeninin ortalaması
df[df["sex"] == "Male"]["total_bill"].mean() #cinsiyeti erkek olanların 'total_bill' değişkeninin ortalaması


#df.groupby("sex").agg({"total_bill": "mean"})

#df[df["sex"] == "Male"]["total_bill"] > df[df["sex"] == "Male"]["total_bill"].mean()


def func(sex_column, total_bill_column):
    male_mean = df[df["sex"] == "Male"]["total_bill"].mean()
    #male_mean = df.groupby("sex").total_bill.mean()[0]
    female_mean = df[df["sex"] == "Female"]["total_bill"].mean()
    #female_mean = df.groupby("sex").total_bill.mean()[1]

    if ((sex_column == "Male") & (total_bill_column > male_mean)):
        return 1

    elif ((sex_column == "Female") & (total_bill_column > female_mean)):
        return 1

    else:
        return 0

df["total_bill_flag"] = df.apply(lambda column: func(column["sex"], column["total_bill"]), axis=1)
df.groupby("sex").agg({"total_bill": "mean"})
df.head(50)

#####################################################################################################################################################################

#Görev 24: total_bill_flag değişkenini kullanarak cinsiyetlere göre ortalamanın altında ve üstünde olanların sayısını gözlemleyiniz.

df.groupby("sex")["total_bill_flag"].value_counts()

#####################################################################################################################################################################

#Görev 25: Veriyi total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.

high_tbts_df = df["total_bill_tip_sum"].sort_values(ascending=False)[0:30]
high_tbts_df[0:30]

#####################################################################################################################################################################