"""
Bu bölüm bitirildiğinde;
Outliers (Aykırı Değerler)
Missing Values (Eksik Değerler)
Encoding
Feature Scaling (Özellik Ölçeklendirme)
Feature Extraction (Özellik Çıkarımı)
Feature Interactions (Özellik Etkileşimleri)
End to End App (Uçtan Uca Uygulama)
hakkında bilgi sahibi olacaksınız.

Ödev ve Projeler
Diyabet Verisi Özellik Mühendisliği
Telco Müşteri Terk Özellik Mühendisliği
"""

#Bu eğitim tamamlandığında bir script'i işletim seviyesinden çalıştırarak bütün veri ön işleme işlemlerini bitirebiliyor olmalıyız.
#Bu yüzden herşeyi programatik fonksiyonlarla script seviyesinde yapmak zorundayız.
#Yani çoğu şeyi fonksiyonlaştıracağız - dinamikleştireceğiz - globalleştireceğiz.

#############################################
# FEATURE ENGINEERING & DATA PRE-PROCESSING
#############################################

#Is your data is bad, your machine learning tools are useless. (by Thomas C.Redman) (2018)
#Sadece iyi veri ile ilgilenmiyoruz, potansiyel verilerle de ilgileniyoruz.
#The world's most valuable resource is no longer oil, but data (2017 The Economist)

"""
Uygulamalı makine öğrenmesi temel olarak değişken mühendisliğidir (feature engineering). (Andrew Ng)
Özellik Mühendisliği; Özellikler üzerinde gerçekleştirilen çalışmalar. Ham veriden değişken üretmek.
(Ön işleme, yeni değişkenler üretmek)
Veri Ön işleme; Çalışmalar öncesi verinin uygun hale getirilmesi sürecidir.

Büyük resmin özeti; Veri setini edindikten sonra veri seti üzerinde;
Data Processing & Wrangling (Veri Ön İşleme)
Feature Extraction & Engineering (Özellik-Değişken Mühendisliği)
Feature Scaling Selection (Ölçeklendirme ve Seçme)
işlemlerini gerçekleştirdikten sonra eğer amacımız makine öğrenmesi modeline sokmak ise ml modeline sokulur.
Sadece ml modeli için veri ön işleme, değişken özellik mühendisliği gerekmez. Birçok veri bilimi uygulaması 
kapsamında da bu basamaklar kullanılır.

Veri Ön işleme %80
ML modeli %20
"""

"""
Aykırı değer; 
Verideki genel eğilimin oldukça dışına çıkan değerler aykırı değer denir.
Aykırı değerler doğrunun ilişkisini, yönünü, şiddetini etkileyebilir. Özellikle doğrusal problemlerde aykırı değerlerin etkisi
daha şiddetlidir. Ağaç yöntemlerinde bu etki daha düşüktür.

Aykırı değerler neye göre belirlenir?
- Sektör Bilgisi (örn ev-fiyat tahmin modelinde 1000m^2'lik evler)
- Standart Sapma yaklaşımı (sapmanın altında ve üstünde kalan değerler kullanılmayabilir) (mean:10 std: 5 -> 15 üstü 5 altı - eşik değerler(threshold)) (x2 standart sapma olabilir)
- Z-Skoru Yaklaşımı (ilgili değişken standartlaştırılarak -2.5 0 +2.5 arasında değerler olur ve genel eğilimin dışına çıkanlar belirlenebilir) 
- Boxplot (interquartile range - IQR) Yöntemi (En Yaygın) -> tek değişkenli olarak.  (şunu demeyi çok seviyorum. Ayküar)
- LOF yöntemi -> çok değişkenli olarak 
"""

"""
Boxplot IQR YÖntemi (bunu kullanacağız); (Interquartile Range)
Q1: %25'lik çeyrek
Q3: %75'lik değer
Küçükten büyüğe doğru sıralandığında elde edilen değerler için eşik değer belirlenir.

IQR = Q3 - Q1 (ilgili değişkenin değişim aralığı) - robust dağılım ölçüsü
Üst Sınır = Q3 + 1.5 * IQR
Alt Sınır = Q1 - 1.5 * IQR

Üst-alt sınır belirlendikten sonra üst sınırın üstündeki değerler, alt sınırın altındaki değerler aykırı değer olarak tanımlanır.
Değişkenin değerleri hep pozitifse bu durumda alt sınır çalışmıyor olacaktır. Dolayısıyla genelde üst sınıra göre çalışılıyor olunur.
Yaş değişkeni için alt sınır -'li değerler olacaktır ve bu değerler silinmiyor olacaktır.
"""

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
# !pip install missingno #önce indir
import missingno as msno
from datetime import date
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import MinMaxScaler, LabelEncoder, StandardScaler, RobustScaler

#Görsel ayarlamalar
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 500)

#Büyük ölçeklikli örneklerimiz için app_train dataset'ini okuma işlemi (işlemciyi çok yoruyor fonk'lar ile birlikte)
def load_application_train():
    data = pd.read_csv("datasets/application_train.csv") #kaggle -> home credit default risk
    return data

df = load_application_train()
df.head()

#Küçük ölçekli örneklerimiz için titanic dataset'ini okuma işlemi
def load():
    data = pd.read_csv("datasets/titanic.csv")
    return data


df = load()
df.head()



#############################################
# 1. Outliers (Aykırı Değerler)
#############################################

#############################################
# Aykırı Değerleri Yakalama
#############################################

###################
# Grafik Teknikle Aykırı Değerler
###################

#Grafik teknik ile aykırı değerleri görmek istersek boxplot kutu grafik kullanılır. (boxplot: sayısal değişkenin dağılım bilgisini verir)
#sayısal değişkenleri görselleştirmek için en yaygın boxplot yönteminden sonra histogram grafiği kullanılır.

sns.boxplot(x=df["Age"]) # sağ taraktaki aykırı değerleri görebiliyoruz.
plt.show() # peki aykırı değerleri nasıl yakalayabiliriz?

###################
# Aykırı Değerler Nasıl Yakalanır?
###################

#önce eşik değerleri hesaplayalım. (üst sınır - alt sınır)
q1 = df["Age"].quantile(0.25) #küçükten büyüğe önce sıralar ve %25'lik değeri alır - 20.125
q3 = df["Age"].quantile(0.75) # 38.0
iqr = q3 - q1 # 17.875
up = q3 + 1.5 * iqr # üst limit - 64.8125
low = q1 - 1.5 * iqr # alt limit - -(6.6875)

df[(df["Age"] < low) | (df["Age"] > up)] # aykırılı değerlerin satırlarını görelim (hepsi üst limiti aşan değerler)

df[(df["Age"] < low) | (df["Age"] > up)].index # aykırı değerlerin index bilgisi

df[~(df["Age"] < low) | (df["Age"] > up)] # aykırı değer olmayanlar

###################
# Aykırı Değer Var mı Yok mu? - Hızlı bir şekilde değerlendirme
###################

#any fonk. içerisinde birşey olup olmama durumunu sorgular (True-False) (fonk yazarken ihtiyacımız olabilir)
df[(df["Age"] < low) | (df["Age"] > up)].any(axis=None) #hiç aykırı değer var mı? (True-False) (axis=None; hepsine göre bak)
df[(df["Age"] < low)].any(axis=None) # alt sınırdan küçük hiç aykırı değer var mı? - False yani yok

# 1. Eşik değer belirledik.
# 2. Aykırılara eriştik.
# 3. Hızlıca aykırı değer var mı yok diye sorduk.

###################
# İşlemleri Fonksiyonlaştırmak
###################

#gönderilen değişkenin eşik değerlerini hesaplayan fonksiyon
def outlier_thresholds(dataframe, col_name, q1=0.25, q3=0.75): #5-95, 1-99 şeklinde de kullanılıyor. Temel literatür 25-75
    quartile1 = dataframe[col_name].quantile(q1)
    quartile3 = dataframe[col_name].quantile(q3)
    interquantile_range = quartile3 - quartile1
    up_limit = quartile3 + 1.5 * interquantile_range
    low_limit = quartile1 - 1.5 * interquantile_range
    return low_limit, up_limit # alt ve üst limitler return ediliyor

outlier_thresholds(df, "Age") # yaş değişkeninin alt ve üst limitleri
outlier_thresholds(df, "Fare") # fare değişkeninin alt ve üst limitleri

low, up = outlier_thresholds(df, "Fare")

#fare değişkeninin low ve up threshold değerlerini belirledik, şimdi aykırı değerleri getirelim
df[(df["Fare"] < low) | (df["Fare"] > up)].head()


df[(df["Fare"] < low) | (df["Fare"] > up)].index # aykırı değerlerin index değerlerine erişelim

#gönderilen değişkenin aykırı değer olup olmadığını hızlıca cevaplamak için
def check_outlier(dataframe, col_name):
    low_limit, up_limit = outlier_thresholds(dataframe, col_name) #öncelikle eşik değerleri belirledik
    #if ile any fonk. kullanarak hiç aykırı değer olup olmadığını sorguluyoruz
    if dataframe[(dataframe[col_name] > up_limit) | (dataframe[col_name] < low_limit)].any(axis=None):
        return True
    else: #hiçbir değer yoksa
        return False

#DipNot: outlier_threshold ön tanımlı değerlerini check_outlier içerisinde biçimlendirmek istersek check_outlier'dan argümanla
#almamız gerekir. Örneğin 75-25 ön tanımlı değiri değiştirmek istiyorsak outlier_threshold'a göndermeden önce check_outlier
#fonk'dan argümanla almalıyız. (spesifik değil, genel fonksiyon yapılarına hakimim)

check_outlier(df, "Age") # true - aykırı değer var
check_outlier(df, "Fare") # true - aykırı değer var

#öyle bir fonksiyon yazalımki veri seti içerisindeki sayısal değişkenleri otomatik olarak seçiyor olsun..

###################
# grab_col_names
###################

#büyük veri seti
dff = load_application_train()
dff.head()

#öyle bir işlem yapalımki; otomatik olarak sayısal değişkenleri, kategorik değişkenleri, num_but_cat, cat_but_num, cardinal değişkenleri getirmiş olsun
#hayat kurtaran serisinden**********************************************************************************************************
#name değişkeni kategorik olamaz, cardinal değişkendir. (kategorik = ölçüm niteliği taşıyor)
#gözlem sayısı kadar sınıf olması (cardinal)
#bu fonksiyon aracılığıyla nümerik,kategorik değişkenleri
#kategorik gözüküp cardinalleri ve nümerik gibi gözüküp kategorik olan değişkenleri yakalamamızı sağlıyor.
def grab_col_names(dataframe, cat_th=10, car_th=20): # categorik threshold _ cardinal threshold (10 ve 20 değerleri) değişkendir.
    #bir sayısal değişkenin sınıf sayısı 10'dan azsa bu aslında sayısal görünümlü kategorik değişkendir.
    #Eğer bir kategorik değişkenin 20'den fazla bir sınıfı varsa cardinal değişkendir (ölçülebilirliği yok, çok sınıfı var)
    """

    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.
    Not: Kategorik değişkenlerin içerisine numerik görünümlü kategorik değişkenler de dahildir.

    Parameters
    ------
        dataframe: dataframe
                Değişken isimleri alınmak istenilen dataframe
        cat_th: int, optional
                numerik fakat kategorik olan değişkenler için sınıf eşik değeri
        car_th: int, optinal
                kategorik fakat kardinal değişkenler için sınıf eşik değeri

    Returns
    ------
        cat_cols: list
                Kategorik değişken listesi
        num_cols: list
                Numerik değişken listesi
        cat_but_car: list
                Kategorik görünümlü kardinal değişken listesi

    Examples
    ------
        import seaborn as sns
        df = sns.load_dataset("iris")
        print(grab_col_names(df))


    Notes
    ------
        cat_cols + num_cols + cat_but_car = toplam değişken sayısı
        num_but_cat cat_cols'un içerisinde.
        Return olan 3 liste toplamı toplam değişken sayısına eşittir: cat_cols + num_cols + cat_but_car = değişken sayısı

    """

    # cat_cols, cat_but_car
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"] #kategorik değişkenler seçildi
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and
                   dataframe[col].dtypes != "O"] #sayısal ama kategorik olanlar seçildi
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and
                   dataframe[col].dtypes == "O"] # kategorik görünümlü cardinaller
    cat_cols = cat_cols + num_but_cat # kategorik değişkenlerimizi güncelliyoruz
    cat_cols = [col for col in cat_cols if col not in cat_but_car] # kardinalleri dışarı alıyoruz

    # num_cols
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]
    num_cols = [col for col in num_cols if col not in num_but_cat] #num_but_cat içerisinde varsa o kolonu alma

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')
    return cat_cols, num_cols, cat_but_car

cat_cols, num_cols, cat_but_car = grab_col_names(df) #titanic veri seti için
#num_bat_cat: 4 sadece raporlamak için verilmiştir yani cat_cols'un içerisindedir.
#cat_cols + num_cols + cat_but_car = Variables olmasını bekleriz

num_cols = [col for col in num_cols if col not in "PassengerId"] #sayısal değişkenler içerisinden passangerId dışarı alıyoruz
#date değişkeni olsa oda geliyor olacaktı, fonksiyonun okunabilirliğini düşüreceğinden dolayı koymamayı tercih ettik.

for col in num_cols: #nümerik değişkenleri check_outlier fonk'na gönderelim
    print(col, check_outlier(df, col)) # True


cat_cols, num_cols, cat_but_car = grab_col_names(dff) # büyük veri seti üzerinde grab_col_names fonk'nu kullanalım

num_cols = [col for col in num_cols if col not in "SK_ID_CURR"] #SK_ID_CURR exception değişkenidir, date,name gibi değişkendir
#bu yüzden sayısal değişkenlerden dışladık.

for col in num_cols: # tüm sayısal değişkenler için aykırı değer olup olmadığını kontrol ediyor.
    print(col, check_outlier(dff, col))

#şimdi aykırı değerlerin satırlarına (kendilerine) erişelim..

###################
# Aykırı Değerlerin Kendilerine Erişmek
###################


# index bilgisi opsiyonel, bir değişkende aykırı değer sayısı 10'dan büyükse head atsın. 10'dan büyük değilse hepsini getirsin bakalım
def grab_outliers(dataframe, col_name, index=False):
    low, up = outlier_thresholds(dataframe, col_name) #öncelikle ilgili kolonun eşik (threshold) değerleri

    if dataframe[((dataframe[col_name] < low) | (dataframe[col_name] > up))].shape[0] > 10: #gözlem sayısı 10'dan büyükse
        print(dataframe[((dataframe[col_name] < low) | (dataframe[col_name] > up))].head())
        #demek ki çok fazla aykırı değer var sadece ilk 5 gözlemine bakalım
    else: #10'den küçükse hepsini getirsin
        print(dataframe[((dataframe[col_name] < low) | (dataframe[col_name] > up))])

    if index: #index true ise aykırı değerlerin index bilgisini return et
        outlier_index = dataframe[((dataframe[col_name] < low) | (dataframe[col_name] > up))].index
        return outlier_index

grab_outliers(df, "Age")

grab_outliers(df, "Age", True) # index bilgisi

age_index = grab_outliers(df, "Age", True)


outlier_thresholds(df, "Age") #outlier threshold hesaplama
check_outlier(df, "Age") #outlier var mı?
grab_outliers(df, "Age", True) #aykırı değerlerin kendisine eriştik

"""
Birçok ağaç yöntemi aykırı değerlere duyarsızdır, ve yaygınca ağaca dayalı yöntemler kullanırken eksik ve aykırı değerler
göz ardı edilir, edilmelidir.
"""

#############################################
# Aykırı Değer Problemini Çözme
#############################################

###################
# Silme
###################

#Fare değişkeni için aykırılıkları yakalayıp silelim..

low, up = outlier_thresholds(df, "Fare") #fare değişkeninin low-up (threshold) değerleri
df.shape # 891 gözlem

df[~((df["Fare"] < low) | (df["Fare"] > up))].shape #aykırı değer olmayanların boyutu (775 tanesi aykırı değilmiş)

# gönderilen kolonun aykırı olmayan değerlerini getirir
def remove_outlier(dataframe, col_name):
    low_limit, up_limit = outlier_thresholds(dataframe, col_name)
    df_without_outliers = dataframe[~((dataframe[col_name] < low_limit) | (dataframe[col_name] > up_limit))]
    return df_without_outliers


cat_cols, num_cols, cat_but_car = grab_col_names(df) #değişkenleri ayırt edelim.

num_cols = [col for col in num_cols if col not in "PassengerId"] #passengerId istemiyorduk

df.shape

#sayısal değişkenleri remove_outlier fonksiyonuna göndererek aykırı değerleri temizlemiş oluyoruz
for col in num_cols:
    new_df = remove_outlier(df, col)

df.shape[0] - new_df.shape[0] # 116 değer aykırı gözlem yakalanmış ve silinmiş

"""
Bir tanedeki hücrenin 1 kolonu aykırı değer olduğundan dolayı silme işlemi yaptığımızda diğer tam olan gözlemlerdeki verilerden de
oluyoruz. Bundan dolayı bazı senaryolarda silmek yerine baskılama yöntemini kullanabiliriz.
"""

###################
# Baskılama Yöntemi (re-assignment with thresholds)
###################

"""
Eşik değerlerin üzerinde kalan değerler eşik değerler ile değiştirilir. Veri kaybetmemek istediğimizde aykırılık bilgisi de taşınsın
diyerek aykırı değerler yakalandıktan sonra eşik değerler ile değiştirilir.
"""

low, up = outlier_thresholds(df, "Fare")

df[((df["Fare"] < low) | (df["Fare"] > up))]["Fare"] # fare değişkeninin aykırı değerleri

df.loc[((df["Fare"] < low) | (df["Fare"] > up)), "Fare"] # fare değişkeninin aykırı değerleri (loc yapısı ile)

# üst sınıra göre aykırı olan değerleri up eşik değer ile değiştirdik
df.loc[(df["Fare"] > up), "Fare"] = up

# alt sınıra göer aykırı olan değerleri low eşik değer ile değiştirme işlemi (alt sınıra göre aykırı değer zaten yok)
df.loc[(df["Fare"] < low), "Fare"] = low

#yaptığımız baskılama yöntemini fonksiyonlaştıralım..

def replace_with_thresholds(dataframe, variable):
    low_limit, up_limit = outlier_thresholds(dataframe, variable)
    dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit
    dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit

#Veri setini sıfırdan okuyalım.. (titanic)
df = load()

#değişken seçim işlemleri
cat_cols, num_cols, cat_but_car = grab_col_names(df)
num_cols = [col for col in num_cols if col not in "PassengerId"]

df.shape

#sayısal değişkenlerin aykırı değeri var mı? (eşik değerleri bu fonksiyonda belirlemiştik)
for col in num_cols:
    print(col, check_outlier(df, col))

# aykırı değerlerin yerine eşik değerleri veriyoruz (baskıla yöntemi fonksiyonumuz)
for col in num_cols:
    replace_with_thresholds(df, col)

# aykırı değer olup olmadığını tekrar sorguluyoruz
for col in num_cols:
    print(col, check_outlier(df, col))


###################
# Recap
###################

df = load()
outlier_thresholds(df, "Age")
check_outlier(df, "Age")
grab_outliers(df, "Age", index=True)

remove_outlier(df, "Age").shape
replace_with_thresholds(df, "Age")
check_outlier(df, "Age")

#outlier_threshold ve replace_with_thresholds ve grab_col_names fonksiyonları bizim için hayat kurtaran fonksiyonlardan.. **********************************************
#şu ana kadar tek bir değişken üzerinde aykırılığı inceledik. Şimdi çok değişkenli aykırı değer analizine geçiş yapalım..



#############################################
# Çok Değişkenli Aykırı Değer Analizi: Local Outlier Factor (How would you like to take wings and fly?) (Hayat kurtaran serisinden)
#############################################


"""
Çok değişkenli aykırı değer analizi nedir?
sadece 3 kez evlenen biri tek başına değerlendirildiğinde aykırı değer gözükmediği fakat işin içine yaş değişkeni girdiğinde
örneğin 21 yaşındaki birinin 3 kez evlenmiş olması aykırı değer olmasıdır.
Tek başına aykırı değer olamayacak bazı değerler birlikte ele alındığında bu durum aykırılık yaratıyor olabilir.

Hastalık bu futbol'dan alıntı yaparak bir orta saha oyuncusunun sadece pas atma becerisini tek başına değerlendirilemeyeceği
başarılı bir oyuncu sayılabilmesi için birçok metriği değerlindiririz. Şuan aynı şekilde çok değişkenli aykırı analizinde
aykırı değer olabilmesi için diğer metriklerle birlikte kıyaslandığında aykırı değer olup olmadığını sorgulayabiliyoruz.

(Görselde görmek istersen images içerisinde bulabilirsin.)

LOF Yöntemi:
Gözlemleri bulundukları konumda yoğunluk tabanlı skorlayarak buna göre aykırı değer olabilecek değerleri tanıma imkanı sağlar.
Bir noktanın lokal yoğunluğu; ilgili noktanın etrafındaki komşuluklar demektir. Eğer bir nokta komşularının yoğunluğundan
anlamlı bir şekilde düşük ise bu nokta daha seyrek bir bölgededir, aykırı değer olabilir. (görseldeki A noktası)
A noktası komşularının lokal yoğunluklarından oldukça farklıdır, bu nokta komşularının yoğunluğundan anlamlı bir şekilde
düşüktür, farklıdır. Bundan dolayı buna aykırı değer muamelesi yapılır.
Kısaca; komşuluklara göre uzaklık skoru hesaplama imkanı sağlar.
"""

"""
LOF yönteminde skorladıktan sonra bu skorları 1 değerine ne kadar yakın olup olmadığına göre inceleriz. 1'e ne kadar yakın olursa
o kadar iyidir. 1'den uzaklaştıkça ilgili gözlemin (nokta değil artık) outlier olma ihtimali artar.
(2.Resim)
Küçük noktalar inlier'dır. Skor değeri 1'den uzaklaştıkça çember büyüdükçe bu değerlerin outlier olasılığı artar. Threshold eşik
değerine müdahele edip aykırı değerliğe müdahele edebiliyoruz 
"""

"""
50-100 tane değişken olduğunda 2 boyutlu görselleştirip inceleyebiliyoruz. Nasıl? (Mülakat sorusu)
Elimizde 100 değişken olduğunda 2 boyutlu nasıl görselleştirebilirim?

Eğer elimizdeki 100 değişkenin taşıdığı bilginin büyük miktarını 2 boyuta indirgeyebilirsek görselleştirilebilir.
Bunu PCA (TEMEL BİLEŞEN YÖNTEMİ) ile gerçekleştirebiliriz.
"""

"""
Üst sınır için aykırı değer olmama durumu olabilir mi? Yani ilk düşününce eşik değerler bunu en çok etkileyen durum olarak
gözüküyor. Standart sapmanın çok düşük olduğu durumda aykırı değerlerin azalacağını düşünüyorum.

***
Literatürde outliers threshold 25-75 olduğu durumda tabiki de 95-5 threshold değerlerine göre daha fazla aykırı
gözlem yakalayacaktır. Konuya tek değişkenli yaklaşıp silseydik ciddi bir veri kaybı olacaktı, baskılama yöntemi ile
doldursaydık gürültüye sebep olacaktır. Ağaç yöntemleri kullanacaksak aykırı değerlere hiç dokunulmaması tercih edilir.
(çok uç aykırılıklar yakalanabilir)
***
"""


# 17, 3

#aykırılıkları diamonds veri setinde incelersek
df = sns.load_dataset('diamonds')
df = df.select_dtypes(include=['float64', 'int64'])
df = df.dropna()
df.head()
df.shape
for col in df.columns:
    print(col, check_outlier(df, col))


low, up = outlier_thresholds(df, "carat")

df[((df["carat"] < low) | (df["carat"] > up))].shape

low, up = outlier_thresholds(df, "depth")

df[((df["depth"] < low) | (df["depth"] > up))].shape

#buraya kadar tek değişkenliği yaklaştığımızda ve 75-25 eşik değerlere göre çok fazla aykırılıklar yakaladık.
#şimdi çok değişkenli yaklaştığımızda neler olacağına bakalım.
#komşuluk sayısı değişebilir. Problem şu ki; Denemeler sonucu komşuluk sayısının hangisinin daha iyi olacağı yorumu yapılamayacak.
#Dolayısıyla ön tanımlı 20 değerini kullanmak tercih edilmeli.
clf = LocalOutlierFactor(n_neighbors=20)
clf.fit_predict(df)

df_scores = clf.negative_outlier_factor_ #skorları değişkene atadık.
df_scores[0:5]
# df_scores = -df_scores # - değerlere göre değerlendirmek istemediğimiz zaman bunu kullanabiliriz (biz negatif değerlerle ilgileneceğiz)
#eşik değere karar vermek için **elbow method** (dirsek yöntemi) grafik tekniğinde daha rahat okunabilirlik açısından skorları - olarak alıyoruz.
#değerlerin -1'e yakın olması inlier olması durumunu gösteriyor. (-1'e ne kadar yakınsa o kadar aykırı değer olma ihtimaline uzaktır)
np.sort(df_scores)[0:5] # en kötü 5 gözlem

#eşik değer belirlememiz gerekiyor, eşik değer manuel veya programatik olarak belirlenebilir.
#elbow method (her yerde bulunmayan serisinden PCA elbow method)
scores = pd.DataFrame(np.sort(df_scores))
scores.plot(stacked=True, xlim=[0, 50], style='.-')
plt.show()
# en dik eğim değişikliği -5 (3.indeks) noktası. Dolayısıyla bu noktayı eşik değer olarak belirleyebiliriz.

th = np.sort(df_scores)[3] #sıralama işleminden sonra 3.indeksteki değeri eşik değer olarak aldık (-4.98)

df[df_scores < th] # belirlediğimiz eşik değere göre aykırı gözlemleri bul

df[df_scores < th].shape # 3 tane

"""
tek değişken bazında aykırılıkları incelediğimizde çok fazla sayıda aykırı değer bulmuşken, çok değişkenli incelediğimizde
sadece 3 tane aykırı değer gözlemledik. Nedenini incelemek için 3 gözlemi inceleyelim..

Aykırı değerlerimizi Describe fonksiyonu ile değerleri kıyaslayacağız;
1.gözlemin depth değeri max çok yakın ama 79 varken 79 aykırı gözlemi gelmemiş. Bu nasıl olabiliyor? (Çok değişkenli aykırı değer
analizinin önemi burada)
Çünkü çok değişkenli yaklaşarak depth değeri bu olup price değeri olma durumları etki göstermiş olabilir. (HAZİNE BİLGİ)
max depth değerinin price değişkeni normal olmuş ki aykırı değer olarak gelmemiş, fakat 78 olanın price değişkeni veya
daha farklı değişkeni de aykırılığa sebep olmuş olabilir.
2.gözlemde z değeri 31.800 max değeri olmuş ve potaya yakalanmış. (ama tek değişkenli olarak baz almıyoruz diğer değişkenlerde de
etkileyen faktörler olmuş)
"""

df.describe([0.01, 0.05, 0.75, 0.90, 0.99]).T

df[df_scores < th].index #aykırı değerlerin indeks bilgileri

#df[df_scores < th].drop(axis=0, labels=df[df_scores < th].index) # aykırı değerleri silme işlemi (kalıcı değil) #buranın aşağıdaki satırla değişmesi gerekiyor
df.drop(axis=0, labels=df[df_scores < th].index)

"""
silme işlemini gerçekleştirdik. Baskılama yöntemiyle de yapabilirdik. Fakat 3 gözlem olduğundan dolayı silmeyi tercih ettik.
Çok değişkenli aykırı değer analizinde fazla sayıda aykırı gözlem yakalasaydık eşik değer belirleyip baskılama yöntemini
kullanabilirdik. Artık değişkene göre değil bir gözlem birimine göre baskılama yapmamız gerektiğinden aykırılığı barındıran
gözlemi komple kaldırıp yerine başka bir gözlem koymamız lazım. Bu da verimizi zorla bozacağımız anlamına gelir (duplicate).
çok değişkenli aykırı değer analizinde (ağaç yöntemleri ile çalışıyorsak aykırılıklara gerekiyorsa hiç dokunma) 
tek değişkenli aykırı değer analizinde eşik değerler 95-5 ile ucundan dokunabiliriz. (önerilir).
Kırpılacak gözlem sayısını aza indirgemiş oluruz.
Birçok aykırı değerin yerine yeni duplicate kayıtları üretmek yerine daha faydalı bir çözüm olabilir.
Doğrusal yöntemlerde aykırılıklar çok önemlidir. (az sayıda ise silinmesi önerilir, doldurmak yerine de tek değişkenli yaklaşıp baskılamak tercih edilebilir)
Çok değişkenlide komple baskılamak mümkünitesi düşük. Onun yerine yukarıdaki alternatif tercih edilir.
Ağaç yöntemlerinde aykırılıkla göz ardı edilmesi önerilir.
"""


#############################################
# Missing Values (Eksik Değerler)
#############################################

"""
Eksik veri problemi nasıl çözülür?
-Silme
-Değer atama yöntemleri (ort,mod,median) (basit atama yöntemleri)
-Tahmine dayalı yöntemler (makine öğrenmesi, istatistiksel yaklaşımlar)
The idea of imputation is both seductive and dangerous (R.J.A Little & D.B. Rubin)
Eksik veri ile çalışırken göz önünde bulundurulması gereken önemli konulardan birisi: Eksik verinin rassallığı.
Eksikliğin rastgele ortaya çıkıp-çıkmadığı durumun bilinmesi gerekir.

Eksik değere sahip gözlemlerin veri setinden direkt çıkarılması ve rassallığın incelenmemesi, yapılacak istatistiksel çıkarımların
ve modelleme çalışmalarının güvenilirliğini düşürecektir. (Alpar, 2011) (Çok değişkenli istatistiksel yöntemler)

Eksik gözlemlerin veri setinden direkt çıkarılabilmesi için veri setindeki eksikliğin bazı durumlarda kısmen bazı durumlarda
tamamen rastlantısal olarak oluşmuş olması gerekmektedir.
Eğer eksiklikler değişkenler ile ilişkili olarak ortaya çıkan yapısal problemler ile meydana gelmiş ise bu durumda yapılacak silme
işlemleri ciddi yanlılıklara sebep olabilecektir. (Tabachnick ve Fiddel, 1996)

Yani eksik değerler rastgele ortaya çıktıyda isteğe bağlı silip doldurabiliriz. Eksik değerlerin rastgele olmaması durumu;
bir değişkendeki eksikliğin başka bir değişken etkisinde ortaya çıkması durumunda olabilir. Örneğin kredi kartı olmayan birinin
kredi kartı borcu da olamaz. Kredi kartı borcu olmaması rastgele eksiklik değildir. Eksikliğin başka bir değişkenle ilişkili
olup olmaması durumu önemlidir.
Eksiklikler rastgele ise kafa rahat
Rastgele değil ise yapısallığın nereden kaynaklandığını bulmalıyız, incelemeliyiz.
Eksik değerler ağaç yöntemlerinde dallara ayırmalı şeklinde çalışıyor olduğundan dolayı aykırılıklar ve eksik verilerin etkisi
neredeyse yoka yakındır. 1 istisna durum vardır. Eğer ilgilendiğimiz problem regresyon problemi ise ve bağımlı değişken sayısal
bir değişken ise bu durumda aykırılık olması durumunda sadece sonuca gitme süresi uzayabilir. (optimizasyon işlemlerinde)
Doğrusal yöntemlerde ve gradient descent temelli yöntemlerde aykırı ve eksik değerler çok hassas iken ağaca dayalı yöntemlerde
bunların etkisi çok çok daha düşüktür.
"""

#############################################
# Eksik Değerlerin Yakalanması (analiz edilmesi)
#############################################

df = load() #titanic veri setini baştan tanımlıyoruz
df.head()

# eksik gozlem var mı yok mu sorgusu
df.isnull().values.any()

# degiskenlerdeki eksik deger sayisi
df.isnull().sum()

# degiskenlerdeki tam deger sayisi
df.notnull().sum()

# veri setindeki toplam eksik deger sayisi
df.isnull().sum().sum() # (1 satırda en az 1 tane bile eksiklik varsa getirir)

# en az bir tane eksik degere sahip olan gözlem birimleri (yukarıda 866 tane sayılan gözlem birimlerine erişmek)
df[df.isnull().any(axis=1)]

# tam olan gözlem birimleri
df[df.notnull().all(axis=1)] #hepsi tam olan gözlem birimleri (eksik gözlemlere göre tam olan gözlemler az sayıda)

# Azalan şekilde sıralamak
df.isnull().sum().sort_values(ascending=False)

#değişkenlerdeki eksikliğin bütün veri setine göre oranı
#her bir değişkendeki eksiklik / veri setinin toplam gözlem sayısı * 100
(df.isnull().sum() / df.shape[0] * 100).sort_values(ascending=False)

#eksik değere sahip olan değişkenlerin isimlerini değişkende tutmak için
na_cols = [col for col in df.columns if df[col].isnull().sum() > 0]

#yaptığımız işlemleri fonksiyonlaştıralım..
def missing_values_table(dataframe, na_name=False): #na_name opsiyonel
    na_columns = [col for col in dataframe.columns if dataframe[col].isnull().sum() > 0] #eksikliğe sahip olan değişken isimleri

    n_miss = dataframe[na_columns].isnull().sum().sort_values(ascending=False) #eksik gözlem değişkenlerini sırala
    ratio = (dataframe[na_columns].isnull().sum() / dataframe.shape[0] * 100).sort_values(ascending=False) #yüzdelik oranlar
    #yakalamış olduğun eksik gözlemlerle ilgili bilgileri missing_df'de concat et
    missing_df = pd.concat([n_miss, np.round(ratio, 2)], axis=1, keys=['n_miss', 'ratio']) #
    print(missing_df, end="\n")

    if na_name:
        return na_columns


missing_values_table(df) #eksikliklerin değişken isimleri, frekansı, oranları

missing_values_table(df, True)


#############################################
# Eksik Değer Problemini Çözme
#############################################

#3 değişkende eksik gözlemlerimiz var
missing_values_table(df)

###################
# Çözüm 1: Hızlıca silmek
###################
df.dropna().shape #gözlem sayısı baya azalacaktır (1 satırda en az 1 tane eksik değer varsa silecektir)
#gözlem sayımız çok fazlaysa direk silmek tercih edilebilir (veri boyutu yeterli olduğundan dolayı)

###################
# Çözüm 2: Basit Atama Yöntemleri ile Doldurmak
###################

df["Age"].fillna(df["Age"].mean()).isnull().sum() # yaş değişkenindeki eksiklikleri ortalama ile doldurma
df["Age"].fillna(df["Age"].median()).isnull().sum() # median ile doldurma
df["Age"].fillna(0).isnull().sum() # 0 sabit bir değer ile doldurma

#yaptığımız işlemleri fonksiyonlaştıralım..

#axis=0 ile aşağıya doğru bütün satırları almış oluyoruz (sütun bazında satırlara bakmak) (udemy'de bu durumu karıştırıyordum)

# df.apply(lambda x: x.fillna(x.mean()), axis=0) # hata verir; sadece sayısal değişkenleri göndermemiz lazım

#hayat kurtaran serisinden , else ile ilgili değişkenin tipi object'den farklı değilse olduğu gibi kalsın demiş oluyoruz
df.apply(lambda x: x.fillna(x.mean()) if x.dtype != "O" else x, axis=0).head()

dff = df.apply(lambda x: x.fillna(x.mean()) if x.dtype != "O" else x, axis=0)

dff.isnull().sum().sort_values(ascending=False) # cabin ve embarked kategorik değişken eksiklikleri

"""
Kategorik değişkenler için en mantıklı doldurulabilecek yöntemlerinden birisi modunu almaktır. 
"""

df["Embarked"].fillna(df["Embarked"].mode()[0]).isnull().sum() #isnull().sum() sadece görmek için

df["Embarked"].fillna("missing") #embarked değişkenindeki eksiklikleri str 'missing' ifadesi ile doldurur.

#yaptığımız eksik veri kategorik mode işlemini fonksiyonlaştıralım..

#if tipi object ise ve eşsiz değer sayısı <= 10 ise (kardinal değişken olup olmadığını kontrol etmiş oluyoruz) (10 threshold, yoruma açık)
df.apply(lambda x: x.fillna(x.mode()[0]) if (x.dtype == "O" and len(x.unique()) <= 10) else x, axis=0).isnull().sum() #isnull().sum sadece gözlemleyebilmek adına

###################
# Kategorik Değişken Kırılımında Değer Atama
###################

#kategorik değişkenleri kırılımlayarak neticesindeki ilgili değerleri eksik değerlerin yerine atamak.

df.groupby("Sex")["Age"].mean() #cinsiyete göre yaş değişkenin ortalaması

df["Age"].mean() # yaş ortalaması 29.69

#gruplama (kırılım) işlemi sonrası ortalama değeri ayrı ayrı farklı cinsiyetlere vermek daha doğru olacaktır.

#yaş değişkenini cinsiyet kırılımında yaş değişkenini kırarak ortalama değeri ver
df["Age"].fillna(df.groupby("Sex")["Age"].transform("mean")).isnull().sum()


#yaptığımız işlemi adım adım ele alalım
df.groupby("Sex")["Age"].mean()["female"] #kadınlara göre yaş değişkeninin ortalaması

#yaş eksik değerlerini ve cinsiyeti kadın olanların yaş değişkenini = kadınların yaş ortalamasını ata
df.loc[(df["Age"].isnull()) & (df["Sex"]=="female"), "Age"] = df.groupby("Sex")["Age"].mean()["female"]

#yaş eksik değerlerini ve cinsiyet erkek olanların yaş değişkenini seç = erkeklerin yaş ortalamasını ata
df.loc[(df["Age"].isnull()) & (df["Sex"]=="male"), "Age"] = df.groupby("Sex")["Age"].mean()["male"]

df.isnull().sum() #yaş değişkenini doldurduk

#kırılımlar ile daha sağlıklı eksik değer analizi yapabiliriz.

"""
#burası bağımsız alan, benim alanım
df = load() #titanic veri setini baştan tanımlıyoruz
df.head()
df.isnull().sum()
def func(df, missing_value_column, grouping_column, choice="mean", all_grouping_column=False):
    df[missing_value_column].fillna(df.groupby(grouping_column)[missing_value_column].transform(choice), inplace = True)
    if all_grouping_column:
        cat_cols, num_cols, cat_but_car = grab_col_names(df)
        print(cat_cols)
        #print(list(map(lambda x: df.groupby(cat_cols[x])[missing_value_column].transform(choice), cat_cols)))
        df.groupby("Sex")["Age"].mean()["female"]

func(df,"Age","Sex", "mean", True)
"""""

#############################################
# Çözüm 3: Tahmine Dayalı Atama ile Doldurma
#############################################

"""
eksikliğe sahip olan değişkeni bağımlı değişken, diğer değişkenleri bağımsız değişkenlermiş gibi kabul edip, bir modelleme
işlemi gerçekleştireceğiz. Modelleme işlemine göre eksik değerlere sahip olan noktaları tahmin etmeye çalışacağız.
1- Kategorik değişlenleri -> one hot encoding işlemine tabii tutmamız lazım (modelin bizden beklediği standart)
2- KNN uzaklık temelli algoritma olduğundan dolayı değişkenleri standartlaştırmamız lazım.
"""

df = load() # titanic veri seti

cat_cols, num_cols, cat_but_car = grab_col_names(df) # değişkenlerimizi yakalayalım
num_cols = [col for col in num_cols if col not in "PassengerId"] #passengerId istemiyoruz
#kategorik değişken olan cat_cols'lara bir dönüşüm (encoder) yapmamız lazım.
#label encoding ve one hot encoding işlemini aynı anda yapabilmek için get_dummies metodunu kullanabiliriz.
dff = pd.get_dummies(df[cat_cols + num_cols], drop_first=True) #drop_first ile kategorik değişkeni binary bir şekilde temsil edebiliyor olacağız
#get_dummies'e bütün değişkenleri birlikte verseniz dahi sadece kategorik değişkenlere bir dönüşüm işlemi uygulamaktadır.
#Kullanacak olduğumuz değişkenleri bir arada görmek istediğimizden dolayı aynı anda gönderdik

"""
get_dummies metodu bize sadece tipi kategorik,object olan veri tiplerini binary hale getirir. Nümerik gözüken fakat
kategorik değişkenlerine girmedik. şuan için sıkıntı yok. encoding bölümünde onlara da değinilecek.
"""

dff.head() #kategorik değişkenleri binary hale dönüştürdük

# değişkenlerin standartlatırılması
scaler = MinMaxScaler() #değerleri 0 ile 1 arasına dönüştür
dff = pd.DataFrame(scaler.fit_transform(dff), columns=dff.columns) #scaler işlemini veri tipimize uyguluyoruz ve df veri tipine dönüştürüyoruz
dff.head()


#knn ile makine öğrenmesi algoritmasını kullanarak eksik değerleri dolduracağız.
#knn bana arkadaşını söyle sana kim olduğunu söyleyim.

# knn'in uygulanması.
from sklearn.impute import KNNImputer
imputer = KNNImputer(n_neighbors=5) # eksik veriyi en yakın 5 gözleme göre ortalama alarak dolduracağız
dff = pd.DataFrame(imputer.fit_transform(dff), columns=dff.columns) #modeli uygulayıp dataframe formatına çevirdik
dff.head()

#amacımız doldurduğumuz değerleri görmek istiyoruz..
#hayat kurtaran serisinden

#standartlaştırma işlemini geri alalım (incelemek için) (1-0 değerleri değil gerçek değerleri görmek istiyoruz)
dff = pd.DataFrame(scaler.inverse_transform(dff), columns=dff.columns) #(sadece standartlaştırma işlemini geri alır, eksik verileri doldurduk)

#eksik verileri doldurduk, doldurulmadan önce kıyas yapmak, analiz etmek istersek..

df["age_imputed_knn"] = dff[["Age"]] #yeni oluşturulan age değişkenini ilk df'ye age_imputed_knn şeklinde kolon oluşturduk

df.loc[df["Age"].isnull(), ["Age", "age_imputed_knn"]] #age değişkenindeki null olan satırları ve doldurulmuş hallerini birlikte getir
df.loc[df["Age"].isnull()] #genel değerlendirmek istersek


###################
# Recap (neler yaptık?)
###################

df = load()
# missing table
missing_values_table(df)
# sayısal değişkenleri direk median ile oldurma
df.apply(lambda x: x.fillna(x.median()) if x.dtype != "O" else x, axis=0).isnull().sum()
# kategorik değişkenleri mode ile doldurma
df.apply(lambda x: x.fillna(x.mode()[0]) if (x.dtype == "O" and len(x.unique()) <= 10) else x, axis=0).isnull().sum()
# kategorik değişken kırılımında sayısal değişkenleri doldurmak
df["Age"].fillna(df.groupby("Sex")["Age"].transform("mean")).isnull().sum()
# Tahmine Dayalı Atama ile Doldurma



#############################################
# Gelişmiş Analizler
#############################################

###################
# Eksik Veri Yapısının İncelenmesi
###################

df = load()

msno.bar(df) #veri setinin değişkenlerdeki tam olan gözlemlerin sayısını göstermektedir
plt.show()

msno.matrix(df) # değişkenlerdeki eksikliğin birlikte bir araya çıkıp çıkmadığı durumunu incelemek için görsel bir araç (udemy)
plt.show()

#eksik değerlerin belirli bir korelasyonla ortaya çıkıp çıkmadığı durumla ilgileniyorduk. (rassallık)
#eksiklikler birlikte veya belirli bir değişkene bağlı olarak çıkması senaryosu var. İkiside bağımlılık durumudur.
msno.heatmap(df) # eksiklikler üzerine nullity correlation değerlerini hesaplar.
plt.show()
#grafiği incelediğimizde değişkenler arasında anlamsız bir korelasyon olduğu gözlemleniyor.

###################
# Eksik Değerlerin Bağımlı Değişken ile İlişkisinin İncelenmesi ********************************************************
###################

#amacımız; eksikliklerin bağımlı değişken tarafında karşılığını, ilişkisini incelemek.


missing_values_table(df, True)
na_cols = missing_values_table(df, True) #eksik değere sahip gözlemlerimi çekiyoruz

#eksik değerlere odaklanıp bağımlı değişkenin ortalamasını alarak, aynı şekilde dolu değerlere odaklanıp bağımlı değişkenin
#ortalaması alınarak kıyaslama yapıyor. Ana odağımız bağımlı değişkene göre etkileyen şeyi bulmak.

def missing_vs_target(dataframe, target, na_columns): #target: bağımlı değişken
    temp_df = dataframe.copy() #temp_df ile df kopyası oluşturuldu

    for col in na_columns:
        temp_df[col + '_NA_FLAG'] = np.where(temp_df[col].isnull(), 1, 0)
        #seçmiş olduğun değişken eksik değere sahipse 1, dolu olan yerlere 0

    na_flags = temp_df.loc[:, temp_df.columns.str.contains("_NA_")].columns
    #içerisinde _NA_ ifadesi olan bütün satırları getir ve na_flags değişkeninde tut

    for col in na_flags:
        print(pd.DataFrame({"TARGET_MEAN": temp_df.groupby(col)[target].mean(), #na_flags içerisinden gelen kolona göre grupla ve target değişkeninin ort al
                            "Count": temp_df.groupby(col)[target].count()}), end="\n\n\n") #na_flags içerisinden gelen kolona göre grupla ve target değişkenin ort al


missing_vs_target(df, "Survived", na_cols)

#age ve cabin değişkeninde gözüktüğü gibi eksik değerlerin (1) survived ortalamaları dolu değerlere göre belirlgin şekilde düşük.

"""
Gerçekten; o gemide çalışan kişilerin kabin numaralarının olmaması, kabinlerde kalmıyor olması durumundan cabine değişkeninde
eksik veriler yaratmıştır ve çalışanların çoğu hayatta kalamamıştır (sadece çalışanlar değil ama çoğunluğu).
Count sayılarıda incelemek için yeterli (ama embarked için denilemez) (count'da bunun için aldık frekans bilgisi)

Bu konuda verinin ilk başta bize vermek istemediği ince noktalara erişebiliyoruz ve böyle bir durum iş bilgisi içinde geçebilir.
İş bilgisi olmadan verinin ince detaylarına erişerek bu bilgiye eriştik.

Cabine değişkenini silmek yerine Cabin_NA_FLAG değişkenini oluşturabiliriz. (feature extraction)

"""


###################
# Recap
###################

df = load()
na_cols = missing_values_table(df, True)
# sayısal değişkenleri direk median ile oldurma
df.apply(lambda x: x.fillna(x.median()) if x.dtype != "O" else x, axis=0).isnull().sum()
# kategorik değişkenleri mode ile doldurma
df.apply(lambda x: x.fillna(x.mode()[0]) if (x.dtype == "O" and len(x.unique()) <= 10) else x, axis=0).isnull().sum()
# kategorik değişken kırılımında sayısal değişkenleri doldurmak
df["Age"].fillna(df.groupby("Sex")["Age"].transform("mean")).isnull().sum()
# Tahmine Dayalı Atama ile Doldurma
missing_vs_target(df, "Survived", na_cols)





#############################################
# 3. Encoding (Label Encoding, One-Hot Encoding, Rare Encoding)
#############################################

#Encoding; değişkenlerin temsil şekillerinin değiştirilmesi

"""
Senaryo 1;
Ordinal kategorik değişken olduğunda label encoding ve one hot encoding işlemlerini gerçekleştirebiliriz. Örneğin; (label encoding)
Pre-School -> 0
Secondary School -> 1
High School -> 2
Graduate -> 3
Master -> 4
PhD -> 5
Ordinal kategorik sıralama ordinal şekilde binary olarak da bilgisi tutulabilir.

Senaryo 2;
Nominal kategorik değişkenler olduğunda direkt label encoding işlemi uyguladığımızda binary halini büyüklük olarak algılayacak ve
ordinal sıralama yapacaktır.
GS -> 0
FB -> 1
BJK -> 2
TS -> 3
BC -> 4
RM -> 5
Bundan dolayı label encoding nominal kategorik değişkenlerde kullanılmamalıdır. (büyüklük - küçüklük algısı oluşacaktır)
Burada yapılması gereken işlem One-hot encoder'dan geçirmektir. One-Hot encoding değişkenin her bir sınıfını bir sütun olarak
değişkene dönüştürecektir.


Neden encoding işlemlerine ihtiyaç vardır?
Makine Öğrenmesi yöntemlerinde kullanmak için standartlaştırma ve kategorik değişkenin bağımlı değişken üzerindeki etkisini görebilmek.
"""

#############################################
# Label Encoding & Binary Encoding
#############################################

#Eğer bir kategorik değişkenin 2 sınıfı varsa 1-0 olarak kodlanırsa binary encoding denir.
#Eğer bir kategorik değişkenin 2'den fazla sınıfı varsa bu durumda label encoding yapılmış olur.
#Label Encoding > Binary Encoding - Temel fark böyle olsada sürekli birbiri yerine kullanılıyor.

#Male -> 0
#Female -> 1


df = load()
df.head()
df["Sex"].head()

le = LabelEncoder() # labelEncoder nesnesi oluşturuldu
le.fit_transform(df["Sex"])[0:5] #önce nesneyi sex değişkenine fit et (encoder uygula) sonra transform ile değerlerini dönüştür.
#fit: ilgili dönüştürme işlemi yap, transform: binary hale dönüştür
"""
0-1 Dönüştürme İşlemini yaparken alfabetik sıraya dikkat ediyor.
[F]emale -> 0
[M]ale -> 1
"""
#Binary halin hangi sınıfı temsil ettiğini unuttuğumuzda..
le.inverse_transform([0, 1])


#yaptığımız işlemleri fonksiyonlaştıralım..
def label_encoder(dataframe, binary_col):
    labelencoder = LabelEncoder()
    dataframe[binary_col] = labelencoder.fit_transform(dataframe[binary_col])
    return dataframe

#verimizi baştan tanımlayalım ve ilgili fonksiyonu kullanalım.
df = load()

"""
Elimizde 100'lerce değişken olduğunda binary_cols kolonları seçilebilir veya one-hot encoder işlemi uygulanabilir. (2 farklı şekilde ele alabiliyoruz)
Köşede kalsın;
One-hot encoding ile get dummies metodunu kullanarak (drop_First=True) iki sınıflı kategorik değişkenleride aslında label
encoderden geçirmiş oluruz.
"""

#değişkenin sütunları int-float değilse ve nunique sayısı 2 olanları seç
#len(unique) yaparsak değişkenin içerisindeki eksik değerleri de sınıf olarak görecektir, cinsiyet değişkeninde eksiklik varsa len 3 çıkacaktır
#nunique eksik değeri sınıf olarak görmez
df.info()
binary_cols = [col for col in df.columns if df[col].dtype not in ["int64", float]
               and df[col].nunique() == 2]

#yakalamış olduğumuz tüm binary_cols değişkenlerini fonksiyona gönderelim
for col in binary_cols:
    label_encoder(df, col)

df.head() # sex değişkeni encoding edildi (yakalanan tek sex değişkeni idi)

#fonksiyonumuzu daha büyük veri setinde görmek için (bilgisayarıma acıdığım için bu bölümü execute etmedim)
df = load_application_train()
df.shape #122 değişken var

binary_cols = [col for col in df.columns if df[col].dtype not in [int, float]
               and df[col].nunique() == 2]
#4 değişken yakalandı (binary_cols type list)

df[binary_cols].head() #yakalanan binary_cols değişkenlerini inceleyelim

#yakalamış olduğumuz binary_cols listesindeki değişkenleri fonksiyonumuza tabii tutalım.
for col in binary_cols:
    label_encoder(df, col)

df[binary_cols].head()
"""
Dikkat! EMERGENCYSTATE_MODE 3 sınıflı.
2 sınıfına sahip olan değerler eksik olan değerlerdir. nunique kullanmıştık fakat eksik değerleri bir sınıf olarak gördü.
Bunun farkındalığı önemlidir. Eksik gözlemler uçurulabilir. Yada kullanılacak olan diğer encoding yöntemleri kullanılabilir.
LabelEncoder fonk uyguladığımızda eksik değerleride görerek 3 sınıflı olarak gördü.
"""

#nunique - unique arasındaki fark
df = load()
df["Embarked"].value_counts()
df["Embarked"].nunique() # 3
len(df["Embarked"].unique()) # 4 (eksik değerleride göz önünde bulundurmak istiyorsak kullanılabilir)

#############################################
# One-Hot Encoding
#############################################

"""
Nominal kategorik değişkenlerde sınıflar arası fark yokken label encoding yaptığımızda sınıflar arası fark oluşturuyor.
Doğrusal ve fonksiyonel yöntemlerde hissedilirken ağaç yöntemlerinde değişkenlerde bir sıralama ve dallara bölme işlemi
olduğu için orada bir etkisi olmayabilir.

Nominal Kategorik değişkeninin sınıfları -> binary ifade etme (One-hot encoding)

Team    GS      FB      BJK     TS      BC      RM
GS      1       0       0       0       0       0  
FB      0       1       0       0       0       0
BJK     0       0       1       0       0       0
TS      0       0       0       1       0       0
BC      0       0       0       0       1       0
RM      0       0       0       0       0       1

One-hot encoding uygularken dummy variable (değişken) durumu söz konusu. One-hot encoding uygularken kullanacak olduğumuz
metotlarda drop first diyerek ilk sınıfı drop ederek ortaya çıkabilecek olan dummy değişken tuzağından kurtuluruz.

dummy değişken tuzağı; kolonlara taşınan değişkenlerin birbiri üzerinden oluşturulabilir olursa bu durumda ortaya ölçme
problemi ortaya çıkarır. Birbiri üzerinden oluşturulabilen değişkenler yüksek bir korelasyona sebep oluyor olacaktır.
Bundan dolayı dummy değişken oluştururken ilk sınıf drop edilir (GS) ve birbiri üzerinden oluşturulma durumu kaldırılmaya
çalışılır.
"""

df = load()
df.head()
df["Embarked"].value_counts() # 3 sınıfı var (nominal) -> one-hot encoding

pd.get_dummies(df, columns=["Embarked"]).head()

pd.get_dummies(df, columns=["Embarked"], drop_first=True).head() #değişkenlerin birbirleri üzerinden oluşturulmasını engellemek için drop_first (yüksek korelasyon etkisi yaratmasın)
#embarked_C uçtu

#eğer ilgili değişkendeki eksik değerleri de bir sınıf olarak gelsin istersek;
pd.get_dummies(df, columns=["Embarked"], dummy_na=True).head() #embarked değişkeninde 2 eksik değer için sınıf oluşturdu

#label encoder uygulamaya gerek kalmadan direkt 2 sınıflı kategorik değişkenlerde binary encode edilebilir
pd.get_dummies(df, columns=["Sex", "Embarked"], drop_first=True).head()
#gelen değişken Sex_male, Embarked_Q, Embarked_S ve birbirleri üzerinden oluşturulamıyorlar

"""
** get_dummies ** metodunu kullanarak hem label encoding (2 sınıflı) hem de one-hot encoding işlemini yapabiliyoruz 
"""

#yaptımız işlemleri fonksiyonlaştıralım..
def one_hot_encoder(dataframe, categorical_cols, drop_first=True):
    dataframe = pd.get_dummies(dataframe, columns=categorical_cols, drop_first=drop_first)
    return dataframe

df = load() #veri setimizi baştan tanımlayalım

# cat_cols, num_cols, cat_but_car = grab_col_names(df) # örneğin survived bağımlı değişkenini cat_cols'da istemeyebiliriz (yoruma açık)

"""
Yoruma açık noktalar;
Veri setindeki tüm kategorik değişkenlere one_hot_encoder uygulayabiliriz
Özel olarak kullandığımız değişken seçimi grab_col_names'den sonra kategorik değişkenlere uygulayabiliriz
"""

# one hot encoder'dan geçecek olan sütunları özel olarak seçilebilir (önerilir)
ohe_cols = [col for col in df.columns if 10 >= df[col].nunique() > 2] # 10>threshold(nunique)>2 ise o kolonu seç
# gelen değişkenler: Pclass, SibSp, Parch, Embarked
#Sex ve survived 2 değişkenlilerden kurtulduk (sex'i zaten önce label_encoder'dan geçirmiştik, survived bağımlı değişkenimiz, uygulama bölümünde sex'i alacağız)
#(yoruma açık, keyfi seçilim, keyfi threshold aralığı)

#yakaladığımız ohe_cols değişkenlerini fonksiyona gönderelim (liste formunda gönderiyoruz)
one_hot_encoder(df, ohe_cols).head() #kalıcı olsun istersen df =

df.head()

#############################################
# Rare Encoding
#############################################

""" 
Genelde model geliştirme süreçlerinde karmaşıklık ile değil basitlik ve genellenebilirlik ile ilgileniyor oluruz.
Genellenebilirlik herşeyi kapsayalım değil büyük çoğunlu temsil edilmesi gibi düşünülebilir.  

Kategorik değişkenin gözlenme frekansları incelendiğinde çok az sayıda (rare) gözlemlenen sınıfın taşıdığı bilgi ve
ayırt edici özelliği çok çok düşüktür. Dolayısıyla tüm değişkenleri one hot encoding işlemine tabii tuttuktna sonra 
oluşan yeni değişken (kolonların) ölçüm kalitesi, bağımlı değişkene olan etkileri ihtimallerininden gitmek istiyoruz.
Gereksiz birçok değişken oluşturmak istemediğimizden dolayı gereksiz değişkenlerden kurtulmak için rare encoding kullanabiliriz.
(Bütün işlemlerde mutlaka yapılması gereken bir işlem değildir.)

Belirlenen eşik (threshold) değere göre eşik değerin altında olan sınıflar işaretlenir ve bütün bu sınıflar bir araya
getirilir.

CITY    CITY_COUNT          -->         CITY            CITY_COUNT
A       56                              A               56
B       84                              B               84
C       54                              C               54
D       2 (flag)                        F               60
E       12 (flag)                       K               25
F       60                              M               36
G       3 (flag)                        Z               45
H       5 (flag)                        RARE(D,E,G,H,L) 23 (birleştirildi)
K       25
L       1 (flag)
M       36
Z       45
"""

# 1. Kategorik değişkenlerin azlık çokluk durumunun analiz edilmesi.
# 2. Rare kategoriler ile bağımlı değişken arasındaki ilişkinin analiz edilmesi.
# 3. Rare encoder yazacağız.

###################
# 1. Kategorik değişkenlerin azlık çokluk durumunun analiz edilmesi.
###################

df = load_application_train() #büyük veri seti
df["NAME_EDUCATION_TYPE"].value_counts() # sınıflarından Academic degree çok az (164)

#veri setinin değişkenlerini ele alalım..
cat_cols, num_cols, cat_but_car = grab_col_names(df)

# kategorik değişkenlerinin sınıflarını ve oranlarını getirelim..
def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")
    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show()


#kategorik değişkenleri fonksiyona gönderelim
for col in cat_cols:
    cat_summary(df, col)

"""
Fonksiyona gönderdiğimizde;
CODE_GENDER değişkenini incelediğimizde;
XNA sınıfı Ç-Ö-P. Bu sınıf direkt silinmeli, bilgi taşımamaktadır. Değişkene dönüştürülmemelidir.
NAME_INCOME_TYPE sınıfında Unemployed,Student,Businessman,Maternity leave Ç-Ö-P (Rare encoding oluşturabiliriz)
FLAG_MOBIL 0.sınıfı Ç-Ö-P silinmeli gibi..

Çok fazla değişken ve çok fazla sınıf olduğunu gözlemledik. Böyle durumda %100 rare_analyser fonksiyonunu kullanmalısınız.
"""

###################
# 2. Rare kategoriler ile bağımlı değişken arasındaki ilişkinin analiz edilmesi.
###################

df["NAME_INCOME_TYPE"].value_counts()

df.groupby("NAME_INCOME_TYPE")["TARGET"].mean() #ilgili değişken sınıflarına göre target değişkeninin ortalaması (üzerindeki etkisi)
# 1'e yakın olması durumu krediyi ödeyememe, 0'a yakın olması krediyi ödeyebilmeyi ifade ediyor.
#Businessman: Ort 0 yani krediyi ödüyor.
#Unemployed: 0.36 ödeyememe durumuna daha yakın
#Bu iki değişken sayısı az ve ort birbirine çok uzak. Bu yüzden RARE encoding ile birleştirilmeli midir? Buralar yorumlara açıktır.
#Biz bir araya getireceğiz ama seçim ve tercihler yorumlara açıktır, farklı kararlar alınabilir.

#yaptığımız işlemleri fonksiyonlaştıralım.. (hayat kurtaran serisinden)
def rare_analyser(dataframe, target, cat_cols):
    for col in cat_cols:
        print(col, ":", len(dataframe[col].value_counts()))
        print(pd.DataFrame({"COUNT": dataframe[col].value_counts(),
                            "RATIO": dataframe[col].value_counts() / len(dataframe),
                            "TARGET_MEAN": dataframe.groupby(col)[target].mean()}), end="\n\n\n")

rare_analyser(df, "TARGET", cat_cols)
#bütün kategorik değişkenler için rare analizi gerçekleştirdik (DEF_60_CNT_SOCIAL_CIRCLE sınıfındaki son 5 veri birleştirilebilir)

#analiz ettiğimize göre artık rare encoding fonk uygulamasını yazalım..

#############################################
# 3. Rare encoder'ın fonksiyonun yazılması.
#############################################

#rare_perc: rare eşik değer. Değerin altında kalan kategorik değişken sınıflarını bir araya getirecek.
#Not: Oranın altında kalan 1 tane sınıf olursa onu da Rare birleştirme yapacak.
def rare_encoder(dataframe, rare_perc):
    temp_df = dataframe.copy() #öncelikle gönderilen df'in kopyası alınıyor

    #fonksiyona gönderilen rare_perc değerinden daha düşük sayıda herhangi bir kategorik değişkenin sınıf oranı varsa ve kategorik değişkense rare_columns'a al.
    rare_columns = [col for col in temp_df.columns if temp_df[col].dtypes == 'O'
                    and (temp_df[col].value_counts() / len(temp_df) < rare_perc).any(axis=None)]
    #rare sınıflara sahip olan değişkenler seçildi

    #rare yakalanan kolonlarda gez
    for var in rare_columns:
        tmp = temp_df[var].value_counts() / len(temp_df) # temp_df içerisindeki ilgili rare değişkenleri için sınıf oranları hesaplanıyor
        rare_labels = tmp[tmp < rare_perc].index # rare_perc verilen oranından daha düşük orana sahip olan sınıflarları indirgeyerek (eşik orandan daha düşük olan sınıfların) indeks bilgilerini al
        temp_df[var] = np.where(temp_df[var].isin(rare_labels), 'Rare', temp_df[var])
        #temp_df[var].isin(rare_labels) -> rare kolon içerisinde rare_labels'lardan 1 tanesini görürsen bunların yerine Rare yaz değilse olduğu gibi kalsın

    return temp_df

new_df = rare_encoder(df, 0.01)
#örneğin NAME_TYPE_SUITE için 5 tane sınıfı var ve 2907 Rare count sayıda gözlem birimini bir araya getirmiş.

"""
rare_encoder fonksiyonumuz veri seti içerisinde seyrek sınıflı kategorik değişkenlerin seyrek sınıflarını toplayıp bir araya
getirerek bunlara RARE isimlendirmesi yapmaktadır. Bir araya getirme, toplulaştırma işlemlerini kuralları iş bilgisi ile de
oluşturulabilir. Rare encoding yoruma açıktır.
"""

rare_analyser(new_df, "TARGET", cat_cols)

df["OCCUPATION_TYPE"].value_counts()


#############################################
# Feature Scaling (Özellik Ölçeklendirme)
#############################################

"""
Özellik ölçeklendirmedeki amaçlarımızdan birisi değişkenler arasındaki ölçüm farklılığını gidermektir. Kullanılacak olan modellerin
değişkenlere eşit şartlar altında yaklaşmasını sağlamaya çalışmak.

dağılımları farklı olan aynı etkiler açısından bir modelleme yapamamaktayız. (ağaç yöntemleri etkilenmez, göz ardı edilebilir)
Değişkenlerin ölçekleri arasındaki farklılıklar kullanılacak olan algoritmaların değerlendirilmesinde yanlılıklara sebep 
olmaktadır. Dolayısıyla değişkenler scaling (ölçeklendirilir) edilir.

1 - Tüm değişkenleri eşit şartlar altında değerlendirebilmek adına ölçeklendirmektir.
2 - Özellikle 'gradient descent' kullanan algoritmaların train sürelerini kısaltma durumu.

Scale edilmiş feature'lar söz konusu olduğunda ölçeklendirilmiş feature'ların üreteceği error'ların boyutları ve bunların iteratif
olarak azaltılması çabası değişkenler standart olduğunda daha hızlı olmaktadır. Dolayısıyla ölçeklerin birbirinden farklı olması
(standartlılaştırılmaması) değişkenler üzerinden minimum noktaya erişecek şekilde gradient descent kullandığımızda süresi uzamaktadır.
Çünkü her iterasyonda ölçek farklılıklarından kaynaklanan error'ların boyutları büyük olacaktır ve daha uzun sürede min noktaya erişiliyor olacaktır.  

3 - Uzaklık temelli yöntemlerde büyük değerlere sahip değişkenler dominantlık sergilemektedir. yani ezicilik sergilemektedir.
(1.maddeye benzer). Özellikle knn,k-means, PCA gibi uzaklık temelli yada benzerlik temelli bazı yöntemler kullandığımızda 
ölçeklerin birbirinden farklı olması durumu yapılacak olan uzaklık-benzerlik hesaplamalarında yanlılığa sebep olur.

Ağaca dayalı yöntemlerin birçoğu eksik değerden, aykırı değerden, standartlılaştırmalardan etkilenmez. Bunun sebebi dallara
ayırma işlemleri için değişkenlerin değerleri küçükten büyüğe sıralama işlemine tabii tutulur ve noktalardan bölünerek dallanmalar
neticesinde entropiler, heterojenlikler, homojenlikler hesaplanır.
"""

#Yaygınca kullanılan standartlaştırma,ölçeklendirme yöntemlerine bakalım..

###################
# StandardScaler: Klasik standartlaştırma, normalleştirme, z standartlaştırılması. Ortalamayı çıkar, standart sapmaya böl. z = (x - u) / s
#bütün gözlem değerlerinden ortalama çıkarılır ve bu sonuç standart sapmasına bölünür.
###################

df = load() #titanic veri seti
ss = StandardScaler()
df["Age_standard_scaler"] = ss.fit_transform(df[["Age"]]) #yaş değişkenini standartlaştırıyoruz
df.head()

"""
Standart scaler; tüm gözlem birimlerinden ortalamayı çıkarıp standart sapmaya böler. Dikkat! Standart sapma da ortalama da aslında
veri setindeki aykırı değerlerden etkilenen metriklerdir. Tüm gözlem birimlerinden medyanı çıkartırsak bölme işlemini de aykırılıklardan
etkilenmeyen IQR 'a böldüğümüzde merhaba --> Robust Scaler 
"""

###################
# RobustScaler: Medyanı çıkar iqr'a böl.
###################

"""
RobustScaler -> StandartScaler'a göre aykırı değerlere karşı dayanıklı olduğundan dolayı daha tercih edilebilir olabilir. Fakat
daha çok standartScaler, minmaxScaler kullanılır.
"""

rs = RobustScaler()
df["Age_robuts_scaler"] = rs.fit_transform(df[["Age"]])
df.describe().T #dağılımın yapısında değil de temsil noktasında değişiklik var. (max değer daha aşağıda min değer daha yukarıda)

###################
# MinMaxScaler: Verilen 2 değer arasında değişken dönüşümü (default 0 - 1 arasında aralık veriyor)
###################

"""
Dönüştürmek istediğimiz özel bir aralık olduğunda bu durumda sıklıkla kullanılır.
"""

# X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
# X_scaled = X_std * (max - min) + min

mms = MinMaxScaler()
df["Age_min_max_scaler"] = mms.fit_transform(df[["Age"]])
df.describe().T

df.head()

age_cols = [col for col in df.columns if "Age" in col] # yaş içeren değişkenlerini aldık
# ['Age, 'Age_standard_scaler', 'Age_robust_scaler', 'Age_min_max_scaler']

#sayısal değişkeni çeyreklik değerler ile göstererek görselleştirir (histogram)
#amacımız age değişkenini önce ilk haliyle sonra scaler ettiğimiz değişkenlerle arasındaki farkı incelemek
def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist(bins=20)
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)

#age ve yapmış olduğumuz age_scaler değişkenlerini metodumuza uyguluyoruz ve değişim analizini görsel üzerinden inceleyebiliriz.
for col in age_cols:
    num_summary(df, col, plot=True)

#dağılımlar aynı sadece ölçek ifade ediliş tarzları farklı. Yapılarını koruyacak şekilde ifade ediliş tarzlarını değiştirdik.

###################
# Numeric to Categorical: Sayısal Değişkenleri Kateorik Değişkenlere Çevirme
# Binning
###################

df["Age_qcut"] = pd.qcut(df['Age'], 5) #yaş değişkeni çeyrek değerlere göre böldük (5 parçaya böl)
#dönüştürecek olduğumuz değişkeni hangi sınıflara dönüştürmek istediğimizi biliyorsak label argümanını kullanabiliriz.
#qcut fonk'nu bir değişkenin değerlerini küçükten büyüğe doğru sıralar ve çeyrek değerlere göre 5 parçaya böler.
df.head()

#############################################
# Feature Extraction (Özellik Çıkarımı)
#############################################

"""
Özellik Çıkarımı; ham veriden değişken üretmek
1-Yapsıal verilerden değişken türetmek
Mevcut değişkenler üzerinden veri türetilir.

Timestamp           -->       Year    Month    Day    Hour    DayName
2021-02-05 07:45              2021    2        5      7       Friday
2021-02-04 21:05              2021    2        4      21      Thursday
2019-05-17 09:51              2019    5        17     9       Friday         

Timestamp değişkeninden 5 adet anlamlı yeni değişken türetildi. Anlamlılık; hedef bağımlı değişken açısından bir ayırt edicilik
oluşturup oluşturmama durumu ifade edilmektedir.

2-Yapısal olmayan verilerden değişken türetmek
Görüntü,ses,yazı gibi verilerden özellik türetilir. Yapısal olmayan şeyleri nümerik temsil etmeye çalışıyoruz.

Yapısal olmayan text metinlerinden örneğin yüzlerce film açıklamalarını ele alıp eşsiz unique kelimeleri sütunlara koyarız,
filmlerde geçen unique kelimeleri sütunlara koyarak vektörleştirebiliriz. (Düz bir metni matematiksel gösterime dökmeye çalışılıyor)

Türettiğimiz her bir değişken özellik çıkarımıdır (feature extraction). Düz bir film açıklaması örneğinde her bir kelimenin
ilgili film açıklamasında kaç defa geçtiği bilgisi türetilmiştir.

Hayvan resimleriyle makine öğrenmesini kullanarak bir sınıflandırıcı yapılmak isteniyor. Örneğin bir kedi resmini lineer cebir
olarak nasıl gösterebiliriz. Matematiksel formu nedir? Piksellerin yoğunlukları belirli bölgelerdeki belirli yoğunluk farklılaşmaları
belirli bölgelerdeki piksellerin renk dağılımları gibi özellikler türetilebilir (derin öğrenme). Örneğin kedinin kulağı özelliği
eklenerek kulağı ifade eden piksel yoğunluklarını türetilebilir. (kedi örneğini images içerisinde)
Üreteceğimiz feature'ların ayırt edicilikleri birçok veri ile beslendiğinde ortaya çıkacaktır.

Özetle makine öğrenmesi, derin öğrenme, zaman serisi problemleri ve bununla ilişkili birçok modelleme sürecinin temelini feature'lar
türetilerek yapılır.    
"""

#############################################
# Binary Features: Flag, Bool, True-False
#############################################

#Hedefimiz var olan değişkenler üzerinden özellik çıkarımında bulunmak

df = load() # titanic
df.head() #Cabin değişkeninde NaN değerlere 1 NaN olmayan değerlere 0 yazılmak isteniyor

#hedefimiz Cabin değişkeninin bağımlı değişken üzerindeki etkisini incelemek.

df["NEW_CABIN_BOOL"] = df["Cabin"].notnull().astype('int') #NaN olan yere 0 yazar, dolu ise 1 yazar
#notnull() ile NaN değerler True-False ile yakalanır ve bu değerleri astype ile int'e çevirerek 0-1 binary değerlere çevirebiliriz.

df.groupby("NEW_CABIN_BOOL").agg({"Survived": "mean"}) #yeni değişkenimizi gruplayarak survived ortalamalarına bakalım
#kabini olanların hayatta kalma oranları %67
#kabini olmayanların hayatta kalma oranları %30
#daha öncesinde çöp gibi gözüken bu değişken çok değerli bir bilgi taşıdığını gördük.

#iki grubun oranını kıyaslayarak istatistiki test uygulayalım. Yeni oluşturduğumuz feature'un bağımlı değişken üzerindeki etkisi merak ediliyor, bunun için oran testi yapılıyor.

from statsmodels.stats.proportion import proportions_ztest
#count başarı sayısı (başarı hayatta kalmaktır), nobs gözlem sayısı
test_stat, pvalue = proportions_ztest(count=[df.loc[df["NEW_CABIN_BOOL"] == 1, "Survived"].sum(), #kabin numarası olup hayatta olanların sayısı
                                             df.loc[df["NEW_CABIN_BOOL"] == 0, "Survived"].sum()], #kabin numarası olmayıp hayatta olanların sayısı (sum edebileceği sadece 1'ler var zaten), kaç tane 1 olduğunu sayar ve buda hayatta kalma sayısını ifade eder

                                      nobs=[df.loc[df["NEW_CABIN_BOOL"] == 1, "Survived"].shape[0], #kabin numarası olanlar kaç kişi
                                            df.loc[df["NEW_CABIN_BOOL"] == 0, "Survived"].shape[0]]) #kabin numarası olmayanlar kaç kişi

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
"""
proportion_ztest testinin hipotezi; p1 ve p2 oranları arasında fark yoktur der. p1 ve p2 oranları kabin numarası olan ve olmayanların
hayatta kalıp kalmama durumunu ifade ediyor. ikisi arasında fark yoktur diyen h0 hipotezi p<0.05 olduğu için red edilir. Yani aralarında
istatistiki olarak anlamlı bir farklılık vardır.
"""

"""
Çok değişkenli etki bilinmiyor. İki tane değişkenin sanki sadece ikisi birlikte oluşmuş gibi değerlendirerek inceledik. Bu yapılar tek başına oluşmadı.
Yani survived değişkeninin ortaya çıkışını sadece new_cabin_bool değişkenine göre baktık. Dolayısıyla istatistiki test olarak anlamlılığı kanıtlasakta
çok değişkenli incelenmediği için henüz bu değişkenin bizim için çok önemlidir genellemesini söyleyemeyiz, en azından kayda değerdir.
(Kırılımın öneminden söz ediliyor heralde)
"""

#yakın ve uzak olan akrabalık ilişkisini ifade eden değişkenlerine bakalım.

#NEW_IS_ALONE değişkeni bu şekilde oluşturulabilir. (sol taraf istenen koşul, sağ taraf oluşturduğumuz değişken, eşitliğin sağ tarafı gözlemlerin değeri)
df.loc[((df['SibSp'] + df['Parch']) > 0), "NEW_IS_ALONE"] = "NO" #yakınlık_uzaklık toplamı > 0 ise yalnız değildir
df.loc[((df['SibSp'] + df['Parch']) == 0), "NEW_IS_ALONE"] = "YES" #yakınlık_uzaklık toplamı > 0 değil ise yalnızdır.

df.groupby("NEW_IS_ALONE").agg({"Survived": "mean"})
# yalnız olmayanların hayatta kalma şansı %50
# yalnız olanların hayatta kalma şansı %30

#bu etkiyi istatistiki olarak inceleyelim
test_stat, pvalue = proportions_ztest(count=[df.loc[df["NEW_IS_ALONE"] == "YES", "Survived"].sum(),
                                             df.loc[df["NEW_IS_ALONE"] == "NO", "Survived"].sum()],

                                      nobs=[df.loc[df["NEW_IS_ALONE"] == "YES", "Survived"].shape[0],
                                            df.loc[df["NEW_IS_ALONE"] == "NO", "Survived"].shape[0]])

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

#p-value < 0.05 olduğu için anlamlı farklılık vardır. h0 hipotezi red edilir. İki oran arasında anlamlı bir farklılık yoktur hipotezi red edildi.

"""
binary feature'ları var olan değişkenlerin üzerinde birden fazla değişkeni etkileşime sokarak yada var olan tek bir değişken üzerinde
çeşitli dönüşümler gerçekleştirerek oluşturabiliyoruz.
"""


#############################################
# Text'ler Üzerinden Özellik Türetmek
#############################################

df = load()
df.head()

#Name metinlerinden değişken türetmeye çalışacağız. Name değişkeni tek başına kardinalitesi yüksek çöp bir değişkendir.

###################
# Letter Count -> Harfleri saydır, bir isimde kaç tane harf olduğunu çıkaralım..
###################

df["NEW_NAME_COUNT"] = df["Name"].str.len() #Name değişkenindeki harfleri say

###################
# Word Count - harfleri saydık, kelimeleri sayalım
###################

df["NEW_NAME_WORD_COUNT"] = df["Name"].apply(lambda x: len(str(x).split(" "))) # boşluk karaktere göre split et (kelimeleri al)
df.head()

###################
# Özel Yapıları Yakalamak
###################

"""
Bakış açısı; 
Olası tüm feature'ları türeterek modelleyerek yeni değerlendirmeler kazanabiliriz.
Diğer yandan feature'ları sadeleştirerek mümkün olduğunca az sayıda değişkenle yüksek başarılara erişmeye çalışıyoruz. (RARE encoding gibi)
Ama feature engineering bölümünde öyle değişkenler türeyebilir ki bunlar bir şekilde hataları düşürerek başarılı tahminler elde edilme imkanı sağlar.
"""

# İsimlerin içerisinde doktor ifadelerini yakalayalım.

df["NEW_NAME_DR"] = df["Name"].apply(lambda x: len([x for x in x.split() if x.startswith("Dr")])) #ilgili değişkeni split et ve Dr ile başlayanları al ve len'ni al

#gözlemleyebilmek için doktora göre gruplayıp Survived için mean ve count değerlerine bakalım
df.groupby("NEW_NAME_DR").agg({"Survived": ["mean","count"]}) # 10 tane doktor varmış ve doktor olanların hayatta kalma oranları daha yüksek

###################
# Regex ile Değişken Türetmek
###################

#Name değişkeninde Mr,Miss. gibi title'ları veriler nasıl yakalanabilir?
#örüntü yakalamaya çalışıyoruz. Solunda boşluk sağında nokta var büyük küçük harfler var, Miss. - Mr. - Mrs. ...

df = load()
df.head()

df['NEW_TITLE'] = df.Name.str.extract(' ([A-Za-z]+)\.', expand=False) #extract fonk. ile istediğimiz örüntü tanımlıyoruz
#Önünde boşluk var, sonunda nokta var, büyük yada küçük harflerden oluşacak şekilde ifadeleri yakala

df.head()

#3 değişkeni al - NEW_TITLE ile grupla - SURVIVED -> mean , AGE -> count mean uygula
df[["NEW_TITLE", "Survived", "Age"]].groupby(["NEW_TITLE"]).agg({"Survived": "mean", "Age": ["count", "mean"]})

#frekansları (count) yükske olanlar kayda değerdir. frekansları az olanlar RARE encoding edilebilir.
#master 36 kişi var ve yaş ortalaması sadece 4


"""
Değerli yorum;
Veri setinde daha önce olmayan bir değişken türeterek yaşların ortalamasını aldığımızda kategorik değişken kırılımında eksiklikleri
atayabilmek adına hizmet edebilecek değişken türettik. Bu sınıflar kırılımında eksiklikleri doldurabiliriz.
"""

#############################################
# Date Değişkenleri Üretmek
#############################################

"""
Veri seti hikayesi;
Bir kursa yapılan puanlamalar var. Puanlamaların tarihleri, kişilerin üye olma tarihleri, ilerleme durumu, sorduğu sorular, yanıtlanan
sorular gibi değişkenleri var. Amacımız timestamp değişkeninden yeni değişkenler türetmek.
"""

dff = pd.read_csv("datasets/course_reviews.csv")
dff.head()
dff.info() #timestamp değişkeninin tipi object -> olması gereken datetime

#timestamp değişkenini formatını datetime yapalım. Format sırası year-month-day
dff['Timestamp'] = pd.to_datetime(dff["Timestamp"], format="%Y-%m-%d")

# year
dff['year'] = dff['Timestamp'].dt.year #timestamp değişkeninden yılları çek ve year değişkenine ata

# month
dff['month'] = dff['Timestamp'].dt.month #ayı çek

# year diff
dff['year_diff'] = date.today().year - dff['Timestamp'].dt.year #bugünün tarihinden değişkenlerin yılını çıkar (geçen yılların farkını al)

# month diff (iki tarih arasındaki ay farkı): yıl farkı + ay farkı
dff['month_diff'] = (date.today().year - dff['Timestamp'].dt.year) * 12 + date.today().month - dff['Timestamp'].dt.month
#öncelikle yıl farkını hesaplayarak 12 ile çarparak ay cinsine çevirmeliyiz ardından iki tarih arasındaki ay farkını alabiliriz.


# day name
dff['day_name'] = dff['Timestamp'].dt.day_name()

dff.head()

# date
#date fonk içerisinde olası birçok ihtiyaç için uygun metotlar vardır.

#############################################
# Feature Interactions (Özellik Etkileşimleri)
#############################################

"""
Özellik etkileşimi;
Değişkenlerin birbirleri ile ilişkisi. İki değişkenin çarpılması, toplanması, karesinin alınamsı gibi değişkenlerle etkileşim kurulur.
"""

df = load() #titanic
df.head()

#yaş değişkeni ile pclass'ı çarpıyoruz. Tabiki boş bir çarpım işlemi yapılmamalı. Çarpım sonucu birşey ifade etmeli. Olmasa da olur mu olurmuş xD.
df["NEW_AGE_PCLASS"] = df["Age"] * df["Pclass"]
#amacımız yaşı küçük-büyük olup yolculuk sınıflarının kalitesine göre farkları görmek (refah seviyesi açısından)
#yaş değişkeninin standarlaştırılmaya [0-3] arasında gibi gereksinim vardır. Amacımız sadece kavramaya çalıştırmak için standartlaştırmaya girmeyeceğiz.


df["NEW_FAMILY_SIZE"] = df["SibSp"] + df["Parch"] + 1 #akrabalık seviyesi + kişinin kendisi ailede boyutunu görebiliriz

#Değişken olarak yaş aralığına göre bir değer verelim
df.loc[(df['SEX'] == 'male') & (df['Age'] <= 21), 'NEW_SEX_CAT'] = 'youngmale'

df.loc[(df['SEX'] == 'male') & (df['Age'] > 21) & (df['Age'] < 50), 'NEW_SEX_CAT'] = 'maturemale'

df.loc[(df['SEX'] == 'male') & (df['Age'] >= 50), 'NEW_SEX_CAT'] = 'seniormale'

df.loc[(df['SEX'] == 'female') & (df['Age'] <= 21), 'NEW_SEX_CAT'] = 'youngfemale'

df.loc[(df['SEX'] == 'female') & (df['Age'] > 21) & (df['Age'] < 50), 'NEW_SEX_CAT'] = 'maturefemale'

df.loc[(df['SEX'] == 'female') & (df['Age'] >= 50), 'NEW_SEX_CAT'] = 'seniorfemale'


df.head()

df.groupby("NEW_SEX_CAT")["Survived"].mean() #oluşturmuz değişkene göre gruplayıp Survived ortalamalarına bakalım.
#seniorfemale 0.73
#seniormale 0.128 (dedeler için yakılır)


#############################################
# Titanic Uçtan Uca Feature Engineering & Data Preprocessing
#############################################

#Amacımız; bağımlı değişkenimiz survived'ı bu veri seti üzerinden modellemek. Modelleme öncesinde gereken bütün basamakları değerlendirelim..

df = load()
df.shape
df.head()

df.columns = [col.upper() for col in df.columns] #bütün değişkenlerin harflerini büyült

#############################################
# 1. Feature Engineering (Değişken Mühendisliği)
#############################################

#bazen yeni üretilen değişkenleri daha sonr ön işleme alınır bazen de önce ön işleme yapıp sonra yeni değişken türetilebilir.

# Cabin bool
df["NEW_CABIN_BOOL"] = df["CABIN"].notnull().astype('int')
# Name count
df["NEW_NAME_COUNT"] = df["NAME"].str.len()
# name word count
df["NEW_NAME_WORD_COUNT"] = df["NAME"].apply(lambda x: len(str(x).split(" ")))
# name dr
df["NEW_NAME_DR"] = df["NAME"].apply(lambda x: len([x for x in x.split() if x.startswith("Dr")]))
# name title
df['NEW_TITLE'] = df.NAME.str.extract(' ([A-Za-z]+)\.', expand=False)
# family size
df["NEW_FAMILY_SIZE"] = df["SIBSP"] + df["PARCH"] + 1
# age_pclass
df["NEW_AGE_PCLASS"] = df["AGE"] * df["PCLASS"]
# is alone
df.loc[((df['SIBSP'] + df['PARCH']) > 0), "NEW_IS_ALONE"] = "NO"
df.loc[((df['SIBSP'] + df['PARCH']) == 0), "NEW_IS_ALONE"] = "YES"
# age level
df.loc[(df['AGE'] < 18), 'NEW_AGE_CAT'] = 'young'
df.loc[(df['AGE'] >= 18) & (df['AGE'] < 56), 'NEW_AGE_CAT'] = 'mature'
df.loc[(df['AGE'] >= 56), 'NEW_AGE_CAT'] = 'senior'
# sex x age
df.loc[(df['SEX'] == 'male') & (df['AGE'] <= 21), 'NEW_SEX_CAT'] = 'youngmale'
df.loc[(df['SEX'] == 'male') & (df['AGE'] > 21) & (df['AGE'] < 50), 'NEW_SEX_CAT'] = 'maturemale'
df.loc[(df['SEX'] == 'male') & (df['AGE'] >= 50), 'NEW_SEX_CAT'] = 'seniormale'
df.loc[(df['SEX'] == 'female') & (df['AGE'] <= 21), 'NEW_SEX_CAT'] = 'youngfemale'
df.loc[(df['SEX'] == 'female') & (df['AGE'] > 21) & (df['AGE'] < 50), 'NEW_SEX_CAT'] = 'maturefemale'
df.loc[(df['SEX'] == 'female') & (df['AGE'] >= 50), 'NEW_SEX_CAT'] = 'seniorfemale'

df.head()
df.shape # 22 tane değişken oldu

cat_cols, num_cols, cat_but_car = grab_col_names(df)

#num_cols'da PASSENGERID istemiyoruz
num_cols = [col for col in num_cols if "PASSENGERID" not in col]

#############################################
# 2. Outliers (Aykırı Değerler)
#############################################

#sayısal değişkenler için aykırı değerlerin yakalanması
for col in num_cols:
    print(col, check_outlier(df, col)) # aykırı değerler hepsi için True

#eşik değerleri aykırı değerlerin yerine verirsek
for col in num_cols:
    replace_with_thresholds(df, col)

#tekrar aykırı değerlere bakalım
for col in num_cols:
    print(col, check_outlier(df, col)) # hepsi false

#############################################
# 3. Missing Values (Eksik Değerler)
#############################################

missing_values_table(df) #değişkenlerdeki eksik değerler ve oranları
#NEW_SEX_CAT fazlalık? Vahit hocanın videosunda NEW_SEX_CAT eksiklik gözlemlenmiyor

"""
yeni türetmiş olduğumuz değişkenlerdeki eksiklikler nereden geldi?
- türetmiş olduğumuz değişkenler yaşa bağlı olduğu için yaştaki eksik değer sayısı yeni türettiğimiz değişkenlere de yansımış
"""

#cabin değişkeninden kurtulalım..
df.drop("CABIN", inplace=True, axis=1)

#ticket ve name değişkenlerinden de kurtulalım.. (kurtulmak istediğimiz bu değişkenlerin yerine zaten yeni değişkenler türetmiştik)
remove_cols = ["TICKET", "NAME"]
df.drop(remove_cols, inplace=True, axis=1)

missing_values_table(df)

# oluşturulan NEW_TITLE değişkenine göre gruplayıp age değişkeninin eksik değerlerini median ile dolduralım..
df["AGE"] = df["AGE"].fillna(df.groupby("NEW_TITLE")["AGE"].transform("median"))
#yaş değişkenindeki eksiklik gider..

#yaş değişkeni üzerinden oluşturulan diğer değişkenleri tekrar baştan oluşturalım..
#yaşa bağlı tüm nümerik değişkenleri tekrar oluşturuyoruz..

df["NEW_AGE_PCLASS"] = df["AGE"] * df["PCLASS"]

df.loc[(df['AGE'] < 18), 'NEW_AGE_CAT'] = 'young'
df.loc[(df['AGE'] >= 18) & (df['AGE'] < 56), 'NEW_AGE_CAT'] = 'mature'
df.loc[(df['AGE'] >= 56), 'NEW_AGE_CAT'] = 'senior'

df.loc[(df['SEX'] == 'male') & (df['AGE'] <= 21), 'NEW_SEX_CAT'] = 'youngmale'
df.loc[(df['SEX'] == 'male') & (df['AGE'] > 21) & (df['AGE'] < 50), 'NEW_SEX_CAT'] = 'maturemale'
df.loc[(df['SEX'] == 'male') & (df['AGE'] >= 50), 'NEW_SEX_CAT'] = 'seniormale'
df.loc[(df['SEX'] == 'female') & (df['AGE'] <= 21), 'NEW_SEX_CAT'] = 'youngfemale'
df.loc[(df['SEX'] == 'female') & (df['AGE'] > 21) & (df['AGE'] < 50), 'NEW_SEX_CAT'] = 'maturefemale'
df.loc[(df['SEX'] == 'female') & (df['AGE'] >= 50), 'NEW_SEX_CAT'] = 'seniorfemale'

missing_values_table(df) #embarked değişkeni hariç eksiklik kalmadı

#embarked değişkeni için eksiklikleri doldurma işlemi programatik şekilde yapmıştık..
#tipi object olan ve unique sayısı <= 10 olan kategorik değişkenleri modları ile doldur
df = df.apply(lambda x: x.fillna(x.mode()[0]) if (x.dtype == "O" and len(x.unique()) <= 10) else x, axis=0)

missing_values_table(df) #embarked değişkeni hariç eksiklik kalmadı

#veri setimizde hiçbir eksiklik kalmadı..
#kullanacak olduğumuz modellere göre kurtulmamayı da tercih edebilirdik (örn: ağaç yöntemleri)

#############################################
# 4. Label Encoding
#############################################

#2 sınıflı kategorik değişkenleri 0-1 olarak binary hale dönüştüreceğiz.

#iki sınıflı kategorik değişkenleri yakalayalım..
#df.info()
binary_cols = [col for col in df.columns if df[col].dtype not in ['int64', 'int32', 'float']
               and df[col].nunique() == 2]


#yakalamış olduğumuz değişkenleri label_encoder fonk'na gönderelim
for col in binary_cols:
    df = label_encoder(df, col)


#############################################
# 5. Rare Encoding
#############################################

#olası indirgemeleri yaptıktan sonra one-hot encoding uygulamak için öncelikle rare encoding analyser bakalım.

rare_analyser(df, "SURVIVED", cat_cols)

# bütün az sayıda sınıflara değişkenlere aynı muameleyi yapmış oluyoruz (iş problemine göre birleştirme işlemleri mantıklı olmayabilir)
df = rare_encoder(df, 0.01)
#0.01 eşik değerine göre değişkenlerin sınıflarını rare encoding ile birleştirelim..

df["NEW_TITLE"].value_counts() #belirlenen eşik değere göre az rastlanılan sınıflar Rare olarak birleştirilmiş
#frekansı yüksek olanlar one-hot-encoding bölümünde önemini taşıyor olacak.

#############################################
# 6. One-Hot Encoding
#############################################

#bütün kategorik değişkenleri one-hot-encoding uygulayacağız..

#one-hot-encoding işlemine tabii tutacağımız kolonları seçelim..
#yeni türettiğimiz değişkenlerden dolayı bunu tekrar seçmemiz lazım..
ohe_cols = [col for col in df.columns if 10 >= df[col].nunique() > 2]
#2'den fazla 10'dan eşit veya küçük eşsiz değer sayısı olan değişkenleri seç

df = one_hot_encoder(df, ohe_cols) #drop_first ön tanımlı default değeri True (kategorik değişkenlerin ilk sınıfları uçar, dummy_encoding)

#bütün olası kategoriler değişkenlere dönüştü..
df.head()
df.shape #yeni veri setindeki değişken sayımız 52

"""
Rare analyser fonk. tekrar çağıralım sebebi yeni oluşan değişkenlerde 1 ve 0 olan sınıfların sayısı dağılımında çok düşük rastlanılan
sınıflar var mı? One hot encoder'dan geçti ama acaba gereksiz değişkenler mi, bilgi taşıyorlar mı? (akışı kesip tekrar geriye doğru gidiyoruz)
"""

#değişkenlerimizi tekrar yakalayalım..
cat_cols, num_cols, cat_but_car = grab_col_names(df)

#passangerid uçsun
num_cols = [col for col in num_cols if "PASSENGERID" not in col]

#kategorik değişkenleri rare_anlyser fonk'na gönderelim
rare_analyser(df, "SURVIVED", cat_cols)

"""
yeni oluşan değişkenlerin frekanslarına bakarak değer taşıyıp taşımadığını ve hedef target değişken üzerindeki etkisini görebiliyoruz.
NEW_FAMILY_SIZE_11 olan değişkenin bir bilgi taşımıyor. 1 sınıfından sadece 7 tane var.
Şu yorum yapılabilir;
Eğer birkaç tane daha aile sayısı ile oluşturulmuş dummy değişkende bu durumu gözlemlersek aile sayısını olduğu gibi bırakmayı tercih edebiliriz.
NEW_FAMILY_SIZE_8 -> ÇÖP
NEW_NAME_WORD_COUNT_14,_9,.. -> ÇÖP

Dolayısıyla 2 sınıflı olup sınıflarından herhangi birisi ratio < 0.01'den olan sınıflar var ve bunları yakalayalım..
"""
#hayat kurtaran serisinden
useless_cols = [col for col in df.columns if df[col].nunique() == 2 and
                (df[col].value_counts() / len(df) < 0.01).any(axis=None)]

#bunları silmeyi-silmemeyi tercih edebiliriz

# df.drop(useless_cols, axis=1, inplace=True) #silmek için

#############################################
# 7. Standart Scaler
#############################################

#bu problemde gerekli değil ama standartlaştırmaya ihtiyacımız olursa diye.. (standart,robust,minMax scalers)

scaler = StandardScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

df[num_cols].head() #sayısal değişkenler standartlılaştırıldı (dağılım aynı, değerler standartlaşıyor)

df.head()
df.shape

# Veri ön işleme bölümleri bitti. Artık herhangi bir makine öğrenmesi modeline gönderebiliriz..

#############################################
# 8. Model
#############################################



y = df["SURVIVED"] # bağımlı değişken
X = df.drop(["PASSENGERID", "SURVIVED"], axis=1) # bağımsız değişkenler passengerid ve survived dışındakilerin hepsi

#Veri seti train-test ayırmı
#train seti üzerinde model kurulacak
#test seti ile kurulan bu modeli test ediyor olacağız
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=17)

#Ağaç temelli random forest modelini kullanalım..
from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(random_state=46).fit(X_train, y_train) #modelling (train seti üzerinden kuruldu)
y_pred = rf_model.predict(X_test) # tahmin değerlerimiz, x test bağımsız değişkenlerini modele gönderdik ve y_pred'e atadık.
accuracy_score(y_pred, y_test) # tahmin edilen değerlerle gerçek değerleri kıyasla

"""
accuracy_score: %80

Bu gemiye binen kişilerin verilerine bakarak kimin hayatta kalıp kalamayacağını %80 doğru tahminledi.
"""

#############################################
# Hiç bir işlem yapılmadan elde edilecek skor?
#############################################

dff = load()
dff.dropna(inplace=True) # eksik değerleri silmeden gönderirsek modelleme yapılamaz.
dff = pd.get_dummies(dff, columns=["Sex", "Embarked"], drop_first=True) # 2 sınıflıları binary encoding yaptık
y = dff["Survived"]
X = dff.drop(["PassengerId", "Survived", "Name", "Ticket", "Cabin"], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=17)
rf_model = RandomForestClassifier(random_state=46).fit(X_train, y_train)
y_pred = rf_model.predict(X_test)
accuracy_score(y_pred, y_test)

#model_accuracy_score: %70

"""
Random Forest aykırı ve eksik gözlemlere duyarsız demiştik ama bu eksik değerlere birşey yapılmayacağı anlamına gelmez.
Random Forest programı uygulamak anlamında duyarlı davrandı.

One-hot encoding uygulamadan da veri setine modelleme yapılamıyor. Algoritma bizden binary değerler beklerken string değerinde 
value gönderemiyoruz.
"""

# Yeni ürettiğimiz değişkenler ne alemde?

#çalıştırmadan önce model başarısı %80 olan modeli tekrar kur.

#fonksiyon yeni türettiğimiz ve var olan bütün değişkenlerin bağımlı değişken üzerindeki etki oranını gösteriyor
def plot_importance(model, features, num=len(X), save=False):
    feature_imp = pd.DataFrame({'Value': model.feature_importances_, 'Feature': features.columns})
    plt.figure(figsize=(10, 10))
    sns.set(font_scale=1)
    sns.barplot(x="Value", y="Feature", data=feature_imp.sort_values(by="Value",
                                                                      ascending=False)[0:num])
    plt.title('Features')
    plt.tight_layout()
    plt.show()
    if save:
        plt.savefig('importances.png')


plot_importance(rf_model, X_train)

"""
En önemli değişkenler;
NEW_NAME_COUNT
FARE 
NEW_AGE_PCLASS
NEW_TITLE_Mr
"""

"""
Gözlemleneceği üzere;
andrew ng ifade ettiği gibi pratik makine öğrenmesi temelinde değişken-özellik mühendisliğine dayanmaktadır. Veri ön işleme
ve özellik mühendisliği işlemleriyle hem algoritmaların bizden beklediği uygun formata verileri getirebiliriz hem de kullanmış
olduğumuz yöntemlerin başarı değerlerini arttırabiliriz.
"""