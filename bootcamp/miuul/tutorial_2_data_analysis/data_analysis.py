###############################################
# PYTHON İLE VERİ ANALİZİ (DATA ANALYSIS WITH PYTHON)
###############################################
# - NumPy
# - Pandas
# - Veri Görselleştirme: Matplotlib & Seaborn
# - Gelişmiş Fonksiyonel Keşifçi Veri Analizi (Advanced Functional Exploratory Data Analysis) - özel bir bölüm
# son bölüm gerçek hayata uygun, sadece dökümantasyonlarda olan bilgiler, özel çözecemeyeceğimiz problemler için

#############################################
# NUMPY
#############################################

# Neden NumPy? (Why Numpy?)
"""bilimsel hesaplamalar için kullanılır, arraylar, çok boyutlu arrayler ve matrisler üzerinde yüksek performanslı çalışma
imkanı sağlar. matematik ve istatistik konularının daha kolay kodlanabilmesi için oluşturulmuştur. Python dünyasını
veri analitiğine açan temel kütüphanesidir.
Listelerden farklı olarak verimli veri saklama ve vektörel operasyonlarıdır (yüksek seviyeli işlemler).
Numpy içersinde veri tutarken fix-type (sabitplenmiş tip) ile tutarak listelere kıyasla çok daha hızlı bir şekilde işlem
yapma imkanı sağlar. Listeler her bir elemanın tip ve boyut bilgilerini için ayrı ayrı tutarken, numpy sabit bir tipte
veri tutarak verimli veri saklama imkanı sağlayarak hızlı bir şekilde array'ler üzerinde çalışma imkanı sağlar.
Döngü yazmaya gerek olmadan array'lere yüksek seviyeli işlemler yapmamıza olanak sağlar. (örn elemanlarını görmek için
her defasında for loop yazmaya gerek yoktur). Genel olarak daha az çabayla daha fazla işlem yapmamıza olanak sağlar.
"""
# NumPy Array'i Oluşturmak (Creating Numpy Arrays)
# NumPy Array Özellikleri (Attibutes of Numpy Arrays)
# Yeniden Şekillendirme (Reshaping)
# Index Seçimi (Index Selection)
# Slicing
# Fancy Index
# Numpy'da Koşullu İşlemler (Conditions on Numpy)
# Matematiksel İşlemler (Mathematical Operations)

#############################################
# Neden NumPy?
#############################################
import numpy as np
a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

for i in range(0, len(a)): #listenin elemanlarını çarpmak için for döngüsüne ihtiyacımız vardır
    ab.append(a[i] * b[i])

ab

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
a * b #for döngüsüne gerek kalmadan çarpma işlemi (numpy avantajı)




#############################################
# NumPy Array'i Oluşturmak (Creating Numpy Arrays)
#############################################
import numpy as np

np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5])) #dtype: numpy.ndarray
np.zeros(10, dtype=int) # 0'lardan 10 elemanlı bir ndarray oluşturur
np.random.randint(0, 10, size=10) # 0 ile 10 arasında random değerlerden 10 elemanlı bir ndarray oluşturur
np.random.normal(10, 4, (3, 4)) #10 ortalamalı 4 standart sapmalı (3,4)'lük 2 boyutlu ndarray
"""
random.normal(1,2,3) 3 adet argümanı vardır.
1: oluşturulmak istenen normal dağılımlı kitlenin ortalamasını gir.
2: argümanı (standart sapması)
3: boyut bilgisi
"""

#############################################
# NumPy Array Özellikleri (Attibutes of Numpy Arrays)
#############################################
import numpy as np

# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

a = np.random.randint(10, size=5) # 0'dan 10'a kadar 5 elemanlı ndarray oluştur
a
a.ndim # 1
a.shape # (5,) her boyuttaki eleman sayısını getirir (5, ) -> 2.boyut olmadığı için yok
a.size # 5
a.dtype # int32

#############################################
# Yeniden Şekillendirme (Reshaping)
#############################################
import numpy as np

np.random.randint(1, 10, size=9) # 1'den 10'a kadar 9 elemanlı ndarray
np.random.randint(1, 10, size=9).reshape(3, 3) # 2 boyutlu (3 satır x 3 sütun) yap

ar = np.random.randint(1, 10, size=9)
ar.reshape(3, 3)

#dikkat: ndarray 10 elemanlı olsaydı 3x3 yapamazdık, hata verir

#############################################
# Index Seçimi (Index Selection)
#############################################
import numpy as np
a = np.random.randint(10, size=10) #0'dan 10'a kadar random 10 elemanlı ndarray
a[0] # 0.indis
a[0:5] # 0'dan 5'e kadar olan elemanları getir (slicing - dilimleme)
a[0] = 999 # 0.ncı indisteki elemanı 999 yap


# 2 boyutlu ndarray'lerde seçim işlemi

m = np.random.randint(10, size=(3, 5)) # (satır,sütun)
m

m[0, 0] # 0.satırdaki 0.sütun (eleman)
m[1, 1] # 1.satırdaki 1.eleman
m[2, 3] # 2.satırdaki 3.eleman

m[2, 3] = 999 #2.satırdaki 3.elemanı 999 yap

m[2, 3] = 2.9 # fix type olduğu için sadece 2 değeri alınır

m

m[:, 0] # tüm satırlardaki 0.elemanını seç
m[1, :] # 1.satırdaki tüm elemanları seç
m[0:2, 0:3] # 0'dan 2.satıra kadar (0 ve 1.satır) 0'dan 3'e kadar elemanını seç (ilk 3 eleman)

#############################################
# Fancy Index
#############################################
import numpy as np

v = np.arange(0, 30, 3) # 0'dan 30'a kadar 3'er 3'er artacak şekilde ndarray oluştur
v
v[1]
v[4]

#elimizdeki birden fazla indexleri aynı anda alabilmek için fancy-index kavramı vardır.
#index no veya True-False ifadeleri tutabilir (liste formatında)

catch = [1, 2, 3]

v[catch] #fancy index ile elemanları getirdik

#############################################
# Numpy'da Koşullu İşlemler (Conditions on Numpy)
#############################################
import numpy as np
v = np.array([1, 2, 3, 4, 5])

#amacımız 3'den küçük değerlere erişmek

#######################
# Klasik döngü ile
#######################
ab = []
for i in v:
    if i < 3:
        ab.append(i)

#######################
# Numpy ile
#######################
v < 3

#fancy index ile liste ve sayısal değerlerin yanı sıra boolean tipte array alabiliyor, seçim işlemi sağlanabiliyor

v[v < 3] #boolean değer gönderip istediğimiz değerlere erişebiliriz (true olanlar döndü)
v[v > 3]
v[v != 3] # eşit değildir ifadesi -> java'da sadece ! şeklindeydi
v[v == 3]
v[v >= 3]

#############################################
# Matematiksel İşlemler (Mathematical Operations)
#############################################
import numpy as np
v = np.array([1, 2, 3, 4, 5])

v / 5 # her bir elemanı 5'e böl
v * 5 / 10
v ** 2 # karesini al
v - 1

np.subtract(v, 1) #çıkarma
np.add(v, 1) # toplama
np.mean(v) # ortalama
np.sum(v) # toplam alma
np.min(v)
np.max(v)
np.var(v) # varyans
v = np.subtract(v, 1)

#######################
# NumPy ile İki Bilinmeyenli Denklem Çözümü
#######################

# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

# katsayılar ve sonuçlar ayrı array'de olacak şekilde;
a = np.array([[5, 1], [1, 3]]) #1. ve 2. değişkenin kat sayıları
b = np.array([12, 10]) # 1. 2. değişkenin sonuçları

np.linalg.solve(a, b) # x1 ve x2 değerleri

"""
Numpy bitti. Neden NumPy tekrardan ele alalım.
1. Hız. Hızın sebebi verimli veri saklamadır. (fix type)
2. Vektörel düzeyde yüksek seviyede kolaylıklar sağlar. (örn for döngüsü yazmadan elemanlarına erişebiliriz)

0'dan numpy arrayleri oluşturulabilir ama genellikle pratikte var olan veri setleri üzerinden numpy array'lerine gidilir.
Bunların üzerinde çalışıyor olunur.

Neler yaptık?
-ndim,shape.. özelliklerine erişmeyi, tip bilgisine erişmek
reshape ile yeniden şekillendirme
index işlemleri - slice işlemleri (slice: belirli aralıktaki indeksleri almak) (en önemlisi)
fancy index (birden fazla index bilgisi girerek toplu şekilde seçimler yapabilmek)
numpy koşullu işlemler (yüksek seviyeli erişim)
numpy matematiksel işlem (ortalama,toplam,varyans gibi metodları gördük)(iki bilinmeyenli denklem)
"""

#############################################
# PANDAS
#############################################

"""
Veri manipülasyonu, veri analizi dendiğinde akla gelen ilk python kütüphanesidir.
Öncelikle ekonometrik ve finansal çalışmalar için doğmuş sonrasında veri analitiğinde en sık kullanılan kütüphane haline gelmiş
Veri analitiği genel anlamda;
Makine öğrenmesinden -> Veri bilimine
Veri analizinden -> Derin öğrenmeye kadar değerlendirilebilir.
"""

# Pandas Series
# Veri Okuma (Reading Data)
# Veriye Hızlı Bakış (Quick Look at Data)
# Pandas'ta Seçim İşlemleri (Selection in Pandas)
# Toplulaştırma ve Gruplama (Aggregation & Grouping)
# Apply ve Lambda
# Birleştirme (Join) İşlemleri

#############################################
# Pandas Series
# series: tek boyutlu index bilgileri barındıran veri tipidir.
# dataframe: çok boyutlu index bilgileri barındıran veri tipi.
# dataframe daha önemli ama series bilmek lazım
# numpy'da ve listelerde index bilgilerine erişebiliyorduk ama verinin index bilgilerini göstermiyordu
#############################################
import pandas as pd

s = pd.Series([10, 77, 12, 4, 5])
s # sol tarafta index , sağ tarafta değerleri var.
type(s) # veri tipini bilmek önemlidir, fonksiyonların bizden beklediği ihtiyaçları doğru bir şekilde yerine getirmek için
#karşılaşabileceğimiz hataları daha iyi çözme imkanı sağlar. -> Series
s.index # Serinin index bilgisi
s.dtype # elemanların veri tipi (int64)
s.size # 5 (eleman sayısı)
s.ndim # 1 (boyut bilgisi) - pandas serileri tek boyutludur ve index bilgileri vardır.
s.values # serinin değerlerine erişmek için
type(s.values) # değerlerin tipi ndarray imiş. yani ndarray return ediyor
s.head(3) # ilk 3 gözlemi
s.tail(3) # sondan 3 gözlemi

"""
pandas serileri matematiksel, istatistiksel işlemler yapabileceğimiz, index isimlendirmelerini değiştirebileceğimiz vb. birçok
farklı imkan sağlamaktadır.
"""
#############################################
# Veri Okuma (Reading Data)
# dış kaynakları verileri okuma
#############################################
import pandas as pd
#bulunduğu dizini almak için; sol tarafta advertising.csv dataset'e sağ tıkla copy path -> path from content room (eğer aynı klasördeyse)

df = pd.read_csv("dataset/advertising.csv")
df.head()

#farklı veri seti okumak için; pd ifadesine ctrl tuşu ile tıkla (json bile okuyabiliyormuşum) -> ctrl+f -> read_x

# pandas cheatsheet

#############################################
# Veriye Hızlı Bakış (Quick Look at Data)
#############################################
import pandas as pd
import seaborn as sns # yaygın hazır verilerle kolay çalışmak için;

"""
survived değişkeni veri setinin ana odağıdır, bağımlı (hedef) değişkendir.
1: hayatta, 2: hayatta değil
"""

df = sns.load_dataset("titanic")
df.head() # ilk 5 gözlem
df.tail() # son 5 gözlem
df.shape # boyut bilgisi
df.info() # değişkenler hakkında bilgi almak isersek -> 891 gözlem , age değişkeninde eksik gözlemler var
#object ve category tipi bizim için kategorik değişkenlerdir. aralarında genel bir fark yoktur. ama bazı fonksiyonlar için
#dönüştürmemiz gerekiyordu (udemy'den hatırladığım)
df.columns # değişkenlerin isimleri
df.index # değişkenlerin index bilgisi
df.describe().T # hızlı bir şekilde sayısal olan değişkenlerin özet istatistikleri (betimsel istatistikleri)
df.isnull().values.any() # veri setinde en az 1 tane bile eksiklik var mı?
df.isnull().values # ndarray döndü
df.isnull().sum() # her değişkenin eksik değer sayısnı getirir (true: 1 - false: 0)
df["sex"].head() # önce gözlemleyelim
df["sex"].value_counts() # cinsiyet kategorik değişkeninin kaç tane sınıf olduğu ve kaçar tane olduğu


#############################################
# Pandas'ta Seçim İşlemleri (Selection in Pandas) ***********************************(yıldız)
# veri analizi veri manipülasyonu dediğimizde aklımıza seçim işlemleri gelmelidir.
#############################################
import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")
df.head()

df.index
df[0:13] # 0'dan 13'e kadar olan satırları getir
df.drop(0, axis=0).head() # axis = 0 (satırlardan siler), 0.satırı sildi (kalıcı değil)

delete_indexes = [1, 3, 5, 7] # birden fazla index gönderip buna göre silme işlemi yapmak (fancy-index)
df.drop(delete_indexes, axis=0).head(10) # 1, 3, 5, 7 satırları silinir

# df = df.drop(delete_indexes, axis=0) #kalıcı silmek için 1.yol
# df.drop(delete_indexes, axis=0, inplace=True) # 2.yol, inplace çok yaygın kullanılan argümandır, kalıcılığı sağlar birçok metod ile kullanılmaktadır

"""
birçok senaryoda elimizdeki dataframe'lerin indeksini değişkene yada değişkeni index'e çevirme ihtiyacı olmaktadır.
"""

#######################
# Değişkeni Indexe Çevirmek
#######################

#age değişkenini -> index'e   ,  index değerini de bir değişken olarak değişkenlerin arasına alalım

df["age"].head()
df.age.head()

df.index
df.index = df["age"] # yaş değişkenini index değerine atamak istiyoruz
df.index # yaş değişkeni index olarak eklenmiş oldu

#age değişkenini index'e atadığımız için değişken olarak ihtiyacımız kalmadı
df.drop("age", axis=1).head()  # age değişkenini siler

df.drop("age", axis=1, inplace=True) # kalıcı olarak siler
df.head()

#######################
# Indexi Değişkene Çevirmek
#######################

df.index

#girmiş olduğumuz age değişkeni df'de yoksa yeni değişken olarak algılar varsa o değişkeni günceller
df["age"] = df.index #age değişkenini index değerlerinden oluşturuldu (1.yol)

df.head()
df.drop("age", axis=1, inplace=True) # 2.yol'u göstermek için tekrar siliyoruz

df.reset_index().head() #1.si index'te yer alan değeri silecektir, 2.si bunu sütun olarak yeni bir değişken olarak ekleyecektir
# indexlerde artık age diye bir değişken yok, sütunlarda ise age değişkeni gelmiş oldu
df = df.reset_index() # kalıcı yapmak için atayabiliriz
df.head()

#######################
# Değişkenler Üzerinde İşlemler (Sütun bazında işlemler)
#######################
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None) # çıktımızdaki ... 'lardan kurtulmak istersek, değişkenlerin tamamını yansıtmak için
df = sns.load_dataset("titanic")
df.head()

"age" in df # age değişkeni var mı

df["age"].head()
df.age.head()

df["age"].head()
type(df["age"].head()) #değişkenin tipi series (burası çokomelli)

#eğer series formatında değilde df formatında döndürmek istiyorsak;

df[["age"]].head() # burası çokomelli
type(df[["age"]].head()) #değişken tipi dataFrame

df[["age", "alive"]] # dataframe içerisinden birden fazla değişken seçmek istersek (fancy index)

col_names = ["age", "adult_male", "alive"]
df[col_names]

#dataFrame'e yeni bir değişken eklemek
df["age2"] = df["age"]**2 # yaşların karesi
df["age3"] = df["age"] / df["age2"]

df.drop("age3", axis=1).head() #değişkeni silmek için (sütunlara göre) (kalıcı değil)

df.drop(col_names, axis=1).head() # birden fazla değişkeni silmek için

#veri setinde belirli bir string ifadeyi barındıran değişkenleri silmek istersek;
df.loc[:, ~df.columns.str.contains("age")].head() # tüm age değişkenlerini siler, loc seçim yapmak için kullanılır
#tüm satırları seç, df columns'larına contains metodunu kullanarak age değişkenini kolonlarda arar, (age değişkenlerini yakalar)
# tilda ila bunun dışındakileri seçme işlemi yaptırıyoruz ve df içerisinde age değişkenlerini bu şekilde kaldırmış oluyoruz


#######################
# iloc & loc
# dataframe'lerde seçim işlemi için kullanılan özel yapılardır
# iloc: alışık olduğumuz index bilgisi vererek seçme işlemi (integer based selection)
# loc: indekslerde label'lara göre seçim yapar (label based selection)
#######################
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

# iloc: integer based selection
df.iloc[0:3] # 0'dan 3'e kadar satırları seç - çıktıdaki ters \ ifadesi kodun aşağıda devam ettiğni gösterir
df.iloc[0, 0] # 0.satır 0.sütundaki elemanı getir

# loc: label based selection
df.loc[0:3] # 0'dan 3'e kadar (ama 3 de dahil) satırları seç

df.iloc[0:3, 0:3] # 0'dan 3.satıra kadar , ilk 3 sütunu getir
#df.iloc[0:3, "age] # hata verir, integer based yani index ile yapabilirsin
df.loc[0:3, "age"] # loc ile yapılabiliyor (sütun ismini string vererek aldık)

col_names = ["age", "embarked", "alive"] # fancy index ile çoklu değişken seçimi (liste yardımı ile)
df.loc[0:3, col_names] # col_names değişkenlerin ilk 3 satırını getir (3 dahil)

#loc: label based selection: sütunlarını string girebiliyoruz ve dahilide getirir ('e dahil)
#iloc: index based selection: sütunları mutlaka index olacak ve dahil olan indeksi getirmez ('e kadar)

#######################
# Koşullu Seçim (Conditional Selection)
# dataframe'lerde koşullu işlemler
#######################
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df[df["age"] > 50].head() # yaşı 50'den büyük olanların ilk 5 gözlemi
#df[df["age"] > 50].count() # bütün değişkenlere count atar istediğimiz gibi çalışmadı
df[df["age"] > 50]["age"].count() # yaşı 50'den büyük olanların sayısı (64)

#yaşı 50'den büyük olan değişkenler hakkında araştırma yapmak istiyoruz, değişken ismi gireceğimiz için loc

df.loc[df["age"] > 50, ["age", "class"]].head() # yaşı 50'den büyük olan değişkenlerin yaşını ve class sınıfını getir

df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"]].head() # yaşı 50'den büyük olan erkeklerin yaş ve class sınıfını getir
#birden fazla koşul girdiğimiz için () içine almak zorundayız

df["embark_town"].value_counts() # yolculuk için gemiye bininen liman sayısını getir

df_new = df.loc[(df["age"] > 50) & (df["sex"] == "male") # yaşı 50'den büyük erkeklerin Cherbourg yada Southampton'dan binilen
       & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")), # yaş , sınıf ve liman bilgilerini getir
       ["age", "class", "embark_town"]]

#df.loc[(df["age"] > 50) & (df["embark_town"].isin(["Southampton", "Cherbourg"])), ["sex", "age", "embark_town"]] (bu şekilde de olur)

df_new

df_new["embark_town"].value_counts() # yeni dataFramedeki limanların sayısını getir


#############################################
# Toplulaştırma ve Gruplama (Aggregation & Grouping)
# bu bölüm udemy'den güzel ayrılmış ve tekrara değer bir bölüm olmuş
# bu ve bundan sonraki bölümler udemy'den çok daha iyi ve anlaşılır.
#############################################
"""toplulaştırma: bir veri yapısının içerisinde barınan değerleri toplu bir şekilde temsil etmek 
toplulaştırma bize özet istatistikler veren betimleme fonksiyonlarıdır. 
Gruplama ile beraber düşündüğümüzde hep bir arada olur.
"""

# TOPLULAŞTIRMA FONKSİYONLARI (groupby ile sık kullanılır)
# - count() # array içerisindeki elemanları saydırmak
# - first() # ilk değer
# - last() # son değer
# - mean() # ortalama
# - median() #
# - min()
# - max()
# - std()
# - var()
# - sum()
# - pivot table (groupby ile kullanılmaz)

# aggregtion fonk dict yapısını kullanarak toplulaştırma fonk. uygulayabiliriz
# groupby aldıktan sonra agg fonksiyonlarını sayısal değişkenlere uygulamak daha mantıklı olacaktır
# birden fazla seviyeli groupby yapacaksak [] liste yardımı ile yapılır
# class değişkeni kategorik formda , pclass ise integer formunda

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df["age"].mean() # yaş ortalamaları

#cinsiyete göre yaş ortalaması
df.groupby("sex")["age"].mean() # önce sex'e göre grupla sonra yaş mean() aggregation fonksiyonu uygula (ort al)

df.groupby("sex").agg({"age": "mean"}) # aggregtion fonk dict yapısını kullanarak toplulaştırma fonk. uygulayabiliriz
df.groupby("sex").agg({"age": ["mean", "sum"]}) # önce sex'e göre grupla sonra yaş değişkeninin hem mean hem sum al

#dict yapısı ile birden fazla agg fonks uygulayabiliyoruz, sex'e göre kır
df.groupby("sex").agg({"age": ["mean", "sum"], # önce sex'e göre grupla sonra yaş değişkenin mean ve sum uygula
                       "survived": "mean"}) # aynı şekilde survived değişkenine mean uygula


#sex'e ve embark_town'a göre kır (grupla), age değişkenine mean survived değişkenine mean fonk. uygula
df.groupby(["sex", "embark_town"]).agg({"age": ["mean"],
                       "survived": "mean"})

#sex embark_town ve class'a göre kır (grupla) ve age ve survived değişkenine mean fonk uygula
df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean"],
                       "survived": "mean"})

df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean", "count"], #bunu ek olarak ben yaptım
                       "survived": "mean"})


#sex, embark_town, class' göre kır (grupla) age ve survived değişkeninin mean uygula sex'e count uygula
df.groupby(["sex", "embark_town", "class"]).agg({
    "age": ["mean"],
    "survived": "mean",
    "sex": "count"})

#değişkenlerin (frekans) :) bilgilerine erişmiş olduk

#######################
# Pivot table
#######################
#veri setini kırılımlar açısından değerlendirmek ve ilgilendiğimiz özet istatistiği bu kırılımlar açısından
#görme imkanı sağlar.

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

#pivot_table("values", satırda hangi değişken olsun, sütunda hangi değişken olsun)
#values: kesişimlerde neyi görmek istiyorsan onu ver (default: mean() uygular, biçimlendirilebilir)

# sex: satır embarked: sütun da olmak üzere survived ortalamaları var.
df.pivot_table("survived", "sex", "embarked")
df.pivot_table("survived", "sex", "embarked", aggfunc="std") # survived artık std değerleri olacak

#groupby'a benzer şekilde daha basit şekilde daha fazla boyut bilgisi ekleyebiliriz [] liste ile

# satır: sex, sütun: embarked,class olacak şekilde survived mean() değerlerini getir
df.pivot_table("survived", "sex", ["embarked", "class"])
#sütunlarda 2 seviye, satırda 1 seviye (satır içinde birden fazla seviyeyi [] yardımı ile verebiliriz


# yaşlara göre kırılım kırılım yapmak istediğimizde hayatta kalma durumlarını analiz etmek istiyoruz
# öyle birşey yapmalıyız ki bir boyuta yaş değişkenini ekleyebilelim.
# yaş sayısal değişkenini kategorik değişkene çevirmemiz gerekiyor.
# cut ve qcut fonksiyonları elimizdeki sayısal değişkenleri kategorik değişkene çevirmek için en yaygın şekilde kullanılır
# sayısal değişkeni hangi kategoriler aralığına bölmek istiyorsanız (belirtmek isterseniz) cut
# sayısal değişkeni tanımadığımızda dolayısıyla çeyreklik değerlerine göre bölünsün istersek qcut

df.head()

df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])

df.pivot_table("survived","sex","new_age")

#satır: sex, sütun: new_age ve class olmak üzere survived ortalamalarını getir (çıktı biraz kalabalık)
# \ ifadesi çıktının (out) aşağıda devam edeceğini gösteriyor
df.pivot_table("survived", "sex", ["new_age", "class"])

pd.set_option('display.width', 500) # çıktıyı daha kolay görmek için
# pd.set_option('display.max_columns', None) # veya bunu dene

#############################################
# Apply ve Lambda
#############################################

#apply satır veya sütunlarda otomatik olarak fonksiyon çalıştırma imkanı sağlar.
#bir dataFrame'a apply ile istediğimiz bir fonksiyonu uygulayabiliriz.
#lambda bir fonksiyon tanımlama şeklidir tıpkı def gibi ama farkı kullan at şeklindedir (kod akışı esnasında 1 kere kullanılır, daha sonra işim olmaz)


import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df["age2"] = df["age"]*2
df["age3"] = df["age"]*5

(df["age"]/10).head()
(df["age2"]/10).head()
(df["age3"]/10).head()

#her bir age değişkenini 10'a bölecek fonksiyona ihtiyacımız var. (amaç; değişkenlere metod uygulamak istiyorum)
#öncelikle normal loop ile

for col in df.columns:
    if "age" in col: #age ifadesini içeren kolonları getir
        print(col)

for col in df.columns:
    if "age" in col:
        print((df[col]/10).head()) #yakaladığın age kolonunu /10'a böl ve gözlemleri getir

for col in df.columns:
    if "age" in col:
        df[col] = df[col]/10 #yakaladığın age kolononu /10'a böl ve ilgili kolona kaydet

df.head()

# with apply & lambda
df[["age", "age2", "age3"]].apply(lambda x: x/10).head() # değişkenleri seç ve apply ile şunu uygula demiş oluyoruz
#lambda fonksiyonunu apply içerisinde tanımlıyoruz
#yaş değişkenini globalleştirelim, burda manuel hepsini girmişiz

#bütün satırları seç ve bütün yakalamış olduğun age içeren değişkenleri lambda fonksiyonunu uygula
df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head()
#bir döngü yazmadan apply fonksiyonu bize değişkenlerde gezme imkanı sağladı

#amaç; uygulandığı dataframe'deki değerleri standartlaştırsın (standartlaştırma,normalleştirme fonk.)
df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()
#feature scaling için önemli - standart scaler - before ML modelling
#feature scaling before machine learning modeling

#apply fonksiyonu bize satırlarda-sütunlarda elimizdeki belirli bir fonksiyonu satır-sütunlara uygulama imkanı
#sağlıyor.

#normal def ile yapmak istersek;
def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

# df.loc[:, ["age","age2","age3"]] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)
# yaptığımız işlemleri kaydetmek için (age değişkenlerini globalleştirelim)

df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)
#yaptığımız işlemleri kaydetmek için (sol taraf; istediğimiz değişkenlerde değişikliği uygulayacak kısım)

#apply fonksiyonu satırlarda ve sütunlarda fonksiyon uygulama şansı sağlar,
#istersek aggregation fonksiyonları ile istersek de kullan at lambda fonksiyonları ile yapabiliyoruz

df.head()

#############################################
# Birleştirme (Join) İşlemleri
#############################################
import numpy as np
import pandas as pd
m = np.random.randint(1, 30, size=(5, 3)) # 1 ile 30 arasında (5,3)'lük 2 boyutlu ndarray
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"]) #ndarray ile dataframe oluşturma
df2 = df1 + 99

#hızlı, seri, basit: concat() fonk
pd.concat([df1, df2]) # alt alta birleştirir (indexler biraz sıkıntılı)

pd.concat([df1, df2], ignore_index=True) # index sorununu çözmek için

#sütun bazında da birleştirme işlemleri yapabiliriz (ctrl ile bakabilirsin veya stackoverflow)
#yan yana yapmak için axis = 1 sütunlara göre yapılır

#######################
# Merge ile Birleştirme İşlemleri
#######################
#daha detaylı birleştirme işlemleri


#df1; çalışanlar ve departmanları
df1 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})

#df2; çalışanlar ve işe başlangıç yılları
df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})

# Amaç: Her çalışanın işe başlangıç yıllarına erişmek istiyoruz
pd.merge(df1, df2) #employess vermedik ama fonk bunu kendisi anladı
pd.merge(df1, df2, on="employees") #özellikle belirtmek istersek

# Amaç: Her çalışanın müdürünün bilgisine erişmek istiyoruz.
df3 = pd.merge(df1, df2) #önceki birleştirme işlemlerini kaydediyoruz

#müdürler dataFrame'i
df4 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
                    'manager': ['Caner', 'Mustafa', 'Berkcan']})

pd.merge(df3, df4) #group'a göre birleştireceğini anladı

#Genellikle birleştirme işlemleri veritabanlarında yapılır ve python tarafına aggregate edilmiş ve tekilleştirilmiş
#tablolar getirilir. Bazen Python'da pratikte tabloları birleştirme ihtiyacı doğabilir. (merge-concat)


#############################################
# VERİ GÖRSELLEŞTİRME: MATPLOTLIB & SEABORN
#############################################

#############################################
# MATPLOTLIB
#############################################
"""
veri görselleştirme araçlarının atasıdır. Low level veri görselleştirme aracıdır.
Seaborn'a kıyasla daha fazla çaba ile görselleştirmek anlamına geliyor.
Python veri görselleştirme için en uygun yer olmayabilir. Veri tabanına bağlı olan veri görselleştirme aracı,
iş zekası aracı daha uygundur. (Power BI, tableau, qlik view araçlar veri tabanına bağlı araçlardır.)
"""

# hangi değişkeni hangi grafiklerle göstermeliyiz?
# Kategorik değişken: sütun grafik. countplot bar (pie chart: exel)
# Sayısal değişken: hist, boxplot (verinin dağılımı, boxplot aykırı değerleride gösterir)



#############################################
# Kategorik Değişken Görselleştirme
#############################################
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None) #output'un güzel olması ile alakalı (... göstermemesi için)
pd.set_option('display.width', 500) #output'un aşağı kaymaması için (güzel olması için)
df = sns.load_dataset("titanic")
df.head()

#cinsiyet kategorik değişkenini görselleştirelim (with matplotlib)
#value_counts() kategorik değişkenlerin görselleştirilmesinde ilk aklımıza gelmelidir
df['sex'].value_counts().plot(kind='bar') # bar (sütun) tipinde-türünde
plt.show()

#eğer görselleştirmede sıkıntı çıkarsa matplotlib güncellenmeli pip install matplotlib
#yada pip install --upgrade matplotlib

#############################################
# Sayısal Değişken Görselleştirme
#############################################
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

plt.hist(df["age"]) #age sayısal değişkeninin dağılımı (with hist)
plt.show()

plt.boxplot(df["fare"]) #fare sayısal değişkenin dağılımı (with boxplot) - fare: bilet ücreti
plt.show()

"""
Kutu grafiği (boxplot) açıklama:
Veri setindeki aykırı değerleri çeyreklik değerler üzerinden gösterebiliyor olmasıdır. Veri ön işleme konusudur.
Verinin kendi içindeki dağılımı göz önünde bulundurarak genel dağılımın dışındaki gözlemleri yakalar.
"""

"""
Birçok farklı veri görselleştirme tekniği vardır ama bu 2 grafik istatistiksel 2 grafiktir. Yani bir veriyi
tanımaya çalışırken asıl amacımız değişkenlerin dağılım yapılarını gözlemleyebilmektir.
Bu sebeple histogram ve boxplot hem sayısal değişkenin hangi aralıklarında hangi frekanslarda gözlemler var
bunu gösterir hemde veri setinin içindeki bu değişkenin kendi içindeki dağılım bilgisini ve bu dağılıma göre
ne kadar aykırı değer olabileceği bilgisini gösterir.
Bir sürekli değişkeni anlamak için histogram ve boxplot tamamen işlerimizi görecektir.
"""

#############################################
# Matplotlib'in Özellikleri
#############################################
"""
katmanlı şekilde veri görselleştirme imkanı sağlar. bir katmanda bir görsel diğer katmanda ayrı bir görsel
diğer katmanda bir title (isimlendirme), diğer katmanda eksenleri hakkında bilgi vermek gibi çeşitli başlıklarda
çalışma imkanı sağlar. (sadece biliyor olmak yeterli olacaktır)
Amacımız daha yüksek seviyeden büyük ölçekli işler yapmak için ihtiyaçlarımızı görebilmektir.
Bütün veri görselleştirme yöntemlerini görmek değildir.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

#######################
# plot - veriyi görselleştirmek için kullandığımız fonk'lardan biri
#######################


x = np.array([1, 8]) # x ekseni
y = np.array([0, 150]) # y ekseni

plt.plot(x, y) # çizgi çeker
plt.show()

plt.plot(x, y, 'o') # çizgi uçları üzerine nokta koyar (sadece bu satırı çalıştırırsak çizgi gözükmeyecek)
plt.show()

"""
gelen görselleri kapatmadan başka bir grafik görselleştirme kodu çalıştırırsak aynı grafiğin üzerine atar
"""

#daha fazla nokta verirsek neler olur
x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])

plt.plot(x, y)
plt.show()

plt.plot(x, y, 'o') #noktalar liste içerisindeki eleman kadar olacaktır
plt.show()



#######################
# marker - işaret özellikleri
#######################

y = np.array([13, 28, 11, 100])

plt.plot(y, marker='o') # y noktalarını işaretlemek istiyoruz (içi dolu daire ile)
plt.show()

plt.plot(y, marker='*') # yıldız koyar
plt.show()

#uygulanabilecek farklı marker'lar
markers = ['o', '*', '.', ',', 'x', 'X', '+', 'P', 's', 'D', 'd', 'p', 'H', 'h']

"""
bu tip konuda uzmanlaşmak için gereksinim;
dökümantasyon okuma
cheetshet bulma
ilgili kütüphanelerin yazarlarının github (kaynak) sayfalarına ulaşma
hatalarla,problemlerle uğraşabilme kültürü (problem çözme kabiliyeti)
araştırma kabiliyeti (uygun kütüphane kullanım yaklaşımları gibi)
"""

#######################
# line - çizgi özelliği, çizgi oluşturma işlemleri
#######################

y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle="dashdot", color="r") #dashed: kesikli, dashdot: hem nokta hem kesikli çizgi, dotted:noktalar
plt.show()

#######################
# Multiple Lines - çoklu özellik girmek istersek; peş peşe çalıştırarak görebiliriz
#######################

x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])
plt.plot(x)
plt.plot(y)
plt.show()

#######################
# Labels - detayında bilgiler vermek için etiketler (labels) kullanırız
#######################

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
# Başlık
plt.title("Bu ana başlık")

# X eksenini isimlendirme
plt.xlabel("X ekseni isimlendirmesi")

plt.ylabel("Y ekseni isimlendirmesi")

plt.grid() # grid: ızgara, okunabilirlik artması için
plt.show()

#######################
# Subplots - birden fazla görselin gösterilmesi çabaları
#######################

# plot 1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 2, 1) # 1 satırlık 2 sütunluk grafik'in 1.grafiğini oluşturuyorum
plt.title("1")
plt.plot(x, y)

# plot 2
x = np.array([8, 8, 9, 9, 10, 15, 11, 15, 12, 15])
y = np.array([24, 20, 26, 27, 280, 29, 30, 30, 30, 30])
plt.subplot(1, 2, 2)
plt.title("2")
plt.plot(x, y)
plt.show()


# 3 grafiği bir satır 3 sütun olarak konumlamak.
# plot 1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 1) # 1'e 3'lük bir grafik oluştur ve bu 1.bölümü
plt.title("1")
plt.plot(x, y)

# plot 2
x = np.array([8, 8, 9, 9, 10, 15, 11, 15, 12, 15])
y = np.array([24, 20, 26, 27, 280, 29, 30, 30, 30, 30])
plt.subplot(1, 3, 2) # 1'e 3'lük bir grafik oluştur ve bu 2.bölümü
plt.title("2")
plt.plot(x, y)

# plot 3
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 3)
plt.title("3")
plt.plot(x, y)

plt.show()



#############################################
# SEABORN - high level - daha az çaba, daha çok iş
#yaygınca ihtiyacımız olabilecek 2 görselleştirme türünü göreceğiz
#############################################
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
df = sns.load_dataset("tips")
df.head()

#kategorik görselleştirme
df["sex"].value_counts() #sex değişkeninin sınıf frekansları
sns.countplot(x=df["sex"], data=df)
plt.show()

#matplotlib ile nasıl görselleştiriyorduk
df['sex'].value_counts().plot(kind='bar')
plt.show()


#############################################
# Sayısal Değişken Görselleştirme
#matplotlib kıyasla daha çok seaborn'u tercih edeceğiz
#############################################
#sayısal değişkenin dağılım bilgisi
#with boxplot
sns.boxplot(x=df["total_bill"])
plt.show()

#with histogram (hist pandas'ın içindedir)
df["total_bill"].hist() #pandas func
plt.show()

#3 temel yaklaşım
#1: value_counts ve countplot
#2: histogram
#3: boxplot
#bu üçünü kullanarak veri anlama değişken anlama açısından birçok ihtiyacımızı karşılayabiliriz.

#############################################
# GELİŞMİŞ FONKSİYONEL KEŞİFÇİ VERİ ANALİZİ (ADVANCED FUNCTIONAL EDA)
#bu bölüm çok değerli; udemy'den ayrılan kısım ve güzel detaylar içeriyor
#toy data setlerinde ihtiyaç gözükmeyen ama gerçek veri setleriyle ilgilendiğimizde ihtiyacımız olan bölüm
#############################################
"""
amaç; elimize veri geldiğinde bu verileri ölçeklenebilir (fonksiyonel tarzda işleyebilmeyi), hızlı bir şekilde
veriyle ilgili iç görüler elde edinebilmeyi amaçlamaktadır. Hızlı bir şekilde genel fonksiyonlar ile elimize
gelen verileri analiz etmek.
"""
# 1. Genel Resim
# 2. Kategorik Değişken Analizi (Analysis of Categorical Variables)
# 3. Sayısal Değişken Analizi (Analysis of Numerical Variables)
# 4. Hedef Değişken Analizi (Analysis of Target Variable)
# 5. Korelasyon Analizi (Analysis of Correlation)

"""
İlk 4 bölüme odaklanarak elimize gelen verileri her açıdan değerlendirip anlama imkanı yakalayabiliriz.
"""
#############################################
# 1. Genel Resim
#############################################
"""
Veri setinin dış ve iç özelliklerinin genel hatlarını edinmek. Kaç gözlem var? Kaç değişken var? İlk gözlemlere
bakalım. Değişkenlerin tiplerine bakalım. Hızlı bir şekilde eksik değer var mı? Varsa hangi değişkende kaçar
tane var?
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head() # ilk 5 gözlem

df.tail() # son 5 gözlem
df.shape #satır - sütun bilgisi
df.info() #verilerin tipleri
df.columns # kolon isimleri
df.index # index bilgisi
df.describe().T # sayısal değşikenlerin betimlemeleri
df.isnull().values.any() # hiç eksik veri var mı?
df.isnull().sum() # eksik veri hangi kolonlarda toplam kaç tane var?

"""
Amaç; Sık kullanılan bazı metotları ihtiyaçlarımıza göre bir fonk. olarak tanımlayacağız ve bu fonksyionu
veri üzerinde çalışırken kod akışı esnasında işimize yarayacak bir şekilde biçimlendirip kullanıyor olacağız. 
"""

"""
Konsol ekranını sağ tarafa getirmek için;
konsol -> sağ tık -> move to -> right top or bottom left
"""

#fonksiyonun amacı; gönderilen veriyi genel resmi vermesi için

def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape) # gözlem-değişken sayısı
    print("##################### Types #####################")
    print(dataframe.dtypes) # değişkenlerin tip bilgileri
    print("##################### Head #####################")
    print(dataframe.head(head)) # ilk 5 (ön tanımlı) gözlem
    print("##################### Tail #####################")
    print(dataframe.tail(head)) # son 5 (ön tanımlı) gözlem
    print("##################### NA #####################")
    print(dataframe.isnull().sum()) # eksik değerlerin sayısı
    print("##################### Quantiles #####################") #çeyreklikler
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T) # sayısal değişkenlerin dağılım bilgisi

"""
Neden check_df diye isimlendirdik?
Örneğin bir değişiklik yaptığımızda tekrar bir kontrol etmek istediğimizde kullanacağız
"""


check_df(df)

#yeni bir veri setini gözlemleyelim
df = sns.load_dataset("flights")
check_df(df)

#daha farklı veri setlerine incelemek için ctrl + load_dataset -> github adresi

#############################################*************************************
# 2. Kategorik Değişken Analizi (Analysis of Categorical Variables)
#############################################*************************************
""""
veri bilimi, makine öğrenmesi modelleme süreçlerinde geliştirmeler yaparken göz yordamıyla değil de programatik
olarak bazı tanımalamaları yapabiliyor ve takip edebiliyor olmamız lazım.
tek bir değişkeni analiz etmek istiyorsak örneğin value_counts'ı kullanarak analiz edebiliriz fakat çok fazla
sayıda değişken olduğunda tek tek yakalamak zor olacaktır.
Bu bölümde fonksiyonel şekilde genellenebilirlik kaygısıyla değişken tiplerini yakalamayı ve bunların özelinde
analiz yapacak fonksiyon yazma işlemini gerçekleştirmiş olacağız.
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df["survived"].value_counts() # survived değişkeninin sınıfları ve frekansları
df["sex"].unique() # sex değişkeninin benzersiz (eşsiz) değerlerine erişmek istersek
df["class"].nunique() # toplamda kaç eşsiz değer var (sayısal)

#öyle birşey yapmalıyız ki veri setinin içerisinden otomatik şekilde bütün olası kategorik değişkenleri seçsin
#aşama1: tip bilgisine göre seçme
#aşama2: başka tipte gözüken ama aslında kategorik olan değişkenleri bulabilme

"""
örneğin; adult_male bool gözükmesine rağmen kategorik bir değişkendir.
örneğin; embark_town object gözükmesine rağmen kategorik bir değişkendir.
örneğin; survived değişkeni int64 gözükmesine rağmen kategorik bir değişkendir (tip bilgisine göre yakalanamaz)
örneğin; pclass değişkeni int64 gözükmesine rağmen kategorik bir değişkendir (tip bilgisine göre yakalanamaz)
örneğin; parch ve sibsp int64 gözüküyor acaba kategorik değişken olabilirler mi?
kategorik değişkeni göz yordamıyla değil de programatik olarak yakalayacağız.
"""

#aşama1: kategorik değişkenleri yakalama
cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

#str(df["alone"].dtypes) in ["bool"] # ilgili değişkenin tip bilgisini string'e çevirerek liste içerisinde var mı kontrolü.

#aşama2: sinsi kategorik tipte olmayanları yakalama
df["survived"].value_counts() #görüldüğü üzere 2 sınıfı var
#tip bilgisi int veya float olup eşsiz sınıf sayısı belirli bir değerden küçük olanları yakala
#10'dan küçük eşsiz sınıf sayısına sahip olan değişkenleri yakala ve kategorik değişken olarak değerlendir
#num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and (str(df[col].dtypes).startswith(('int' or 'float')))]
"""
"int" in "int64" #true
"int64" in "int" #false
"""

"""object-category tipindedeğişkenlerin sınıf sayısı çok fazla olabilir. Örneğin name değişkeni için 891 tane
unique değer olabilir. Bu kategorik değişken DEĞİLDİR. Bunlara kardinalitesi yüksek değişkenler denir. Yani
ölçülemeyecek kadar, açıklanabilirlik taşımayacak kadar fazla sınıfı vardır. Bir kategorik değişkenin 50 sınıfı
olması yüksek ihtimalle onun bilgi taşımadığı anlamına gelir.

Öyle bir kod yazalım ki; kategorik tipte olduğu halde özünde kategorik olmayan değişkenleri yakalayalım.
""" #cat but cardinal

#20'den büyük category veya object veri tiplerini al (bunlar cardinal değişkenler - ölçülebilir olmayan değişkenler)
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]

cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
#cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and (str(df[col].dtypes).startswith(('category' or 'object')))]
#her iki durumda da boş geliyor demek ki numerik görünümlü kategorik değişken yokmuş. (20 sayısı isteğe göre değişebilir)

#yakalamış olduğumuz kategorik değişkenleri birleştirelim
cat_cols = cat_cols + num_but_cat

#cat_but_car'dan gelen değişkenleri sorgulayalım (gelmiş olsaydı) kategorik değişkenlerin içerisinden çıkarmamız gerekirdi
cat_cols = [col for col in cat_cols if col not in cat_but_car]

#yaptığımız işlemler gerçek datasetleri üzerinden veri görselleştirme-analizi için önemlidir.
#toy datasetleri ilgilenirken bu tarz problemlerle çok fazla karşı karşıya gelinmez.

df[cat_cols] # seçtiğimiz kategorik değişkenleri görelim
df[cat_cols].nunique() #seçtiğimiz değişkenlerin eşsiz sınıf sayısına bakarak kontrolümüzü yapalım

#cate_cols içinde olmayanları seçelim
[col for col in df.columns if col not in cat_cols]

#şimdi yapmış olduğumuz işlemlerin fonksiyonlarını yazalım. (bu bölüm gerçekten özel bir bölüm olmuş)
# kategorik değişkenlerin özel seçimlerinin fonksiyonları

df["survived"].value_counts() # survived değişkenin frekansı (hangi sınıfından kaçar tane var?)
100 * df["survived"].value_counts() / len(df) # sınıfların yüzdelik bilgisi

#bu fonksiyon sınıfların yüzdelik bilgisini verir
def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

cat_summary(df, "sex")

#bütün değişkenleri cat_summary fonksiyonuna tabii tutalım
for col in cat_cols:
    cat_summary(df, col)

"""
Sürdürülebilirlik kavramı:
Yapısal noktalara dokunup, genellenebilirlik-ölçeklenebilirlik kaygısıyla ilerlediğimizde (daha yüksek seviyeden
olaya baktığımızda) genel bir eğilimde olunması tavsiye ediliyor. Yani; basitlik.. Yüksek seviyeden basit bir bilgiye
ihtiyacımız olduğunda bunu en basit, en işe yarar şekilde ortaya konulmalıdır. Çok fazla derine inmeden sürdürebilirlik
kavramının öneminin farkına varılacaktır.
"""

#cat-summary fonksiyonuna grafik özelliğini ekleyelim..
def cat_summary(dataframe, col_name, plot=False): #ön tanımlı değeri false @Overloading
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True) #birden fazla döngüye girdiğimizde görsel olacağından dolayı sağlıklı değerlendirmek adına block=True

cat_summary(df, "sex", plot=True) #sadece cinsiyet değişkeninin görselleştirilmesi

#bütün değişkenleri görselleştirelim (bool hariç)
for col in cat_cols:
    if df[col].dtypes == "bool": #adult_male bool tipte ve bu görselleştirilemez
        print("sdfsdfsdfsdfsdfsd") #bir nevi exception yakaladık
    else:
        cat_summary(df, col, plot=True)


#bool tipteki verileri nasıl görselleştirebiliriz -> (casting işlemi)

df["adult_male"].astype(int) #true->1 , false->0 adult_male elemanlarını int'e çeviriyor
#amaç sadece adult_male değil global olarak bool içeren değişkenleri çevirelim

#bu döngüyü fonk. içinde yazamayız, do one thing prensibi; birden fazla değişken uygulanacaksa fonksiyon dışına yazılır (yaygın olan budur)
for col in cat_cols:
    if df[col].dtypes == "bool": #bool değişkenleri yakal
        df[col] = df[col].astype(int) #bool değişkenlerin elemanını int'e çevir
        cat_summary(df, col, plot=True) #görselleştir, burada patlasaydık, loc yapısını kullanıp ilgili değişkeni değiştirecektik

    else:
        cat_summary(df, col, plot=True) #yakalamadıklarını direkt görselleştir


#pekala, şimdi fonksiyon haline dökelim. (özellik,eklemeler arttıkça beraberinde başka riskleri getiriyor)
#küçük değişikler için kod yapısı baya değişebilir

def cat_summary(dataframe, col_name, plot=False):

    if dataframe[col_name].dtypes == "bool": # tip eğer bool tipindeyse
        dataframe[col_name] = dataframe[col_name].astype(int) # int tipine çevir

        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        print("##########################################")

        if plot: #grafik özelliği True gelmişse görselleştir (default=False) @overloading
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show(block=True)
    else: # bool tipinde değilse
        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        print("##########################################")

        if plot:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show(block=True)

cat_summary(df, "adult_male", plot=True) #tek bir değişkeni görselleştirdik
#eğer diğer bütün değişkenleri görmek istersek yine aynı şekilde for yapısıyla metoda gönderebiliriz



#amacımız hızlı bir şekilde analiz etme imkanı sağlamaksa bunu kullanalım..
def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

cat_summary(df, "sex")



#############################################
# 3. Sayısal Değişken Analizi (Analysis of Numerical Variables)
#############################################

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df[["age", "fare"]].describe().T #sayısal değişkenlerin özet istatistikleri

#programatik olarak sayısal verileri nasıl seçebiliriz?

#kategorik değişkenleri önceki bölümden alalım..
cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and (str(df[col].dtypes).startswith(('int' or 'float')))]
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
cat_cols = cat_cols + num_but_cat
cat_cols = [col for col in cat_cols if col not in cat_but_car]

#numerik, sayısal değişkenler (fakat içerisinde survived,pclass gibi gizli kategorik değişkenler olabilir)
num_cols = [col for col in df.columns if df[col].dtypes in ["int","float"]]

#num cols içerisinde olup cat_cols'da olmayan değişkenleri seç ile sadece sayısal değişkenleri alıyoruz
num_cols = [col for col in num_cols if col not in cat_cols] # özü sayısal değişkenleri almış alıyoruz

"""
Ölçeklenebilirlik ve genellenebilirlik kavramının asıl zorluğu bu veri yapılarını analiz edecek fonksiyonu yazmak değil, bu veri yapılarını
seçebilmektir. Programatik olarak genellenebilirlik kaygılarıyla seçebilmek.
"""

#yaptığımız işlemleri fonksiyona dökelim..
def num_summary(dataframe, numerical_col):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99] #çeyreklikler
    print(dataframe[numerical_col].describe(quantiles).T)

num_summary(df, "age") #sadece age değişkenine bakalım

#bütün değişkenleri gönderelim
for col in num_cols:
    num_summary(df, col)

#ek olarak fonksiyon içerisinde görselleştirebiliriz..
def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist() #histogram dağılım grafiği
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)


num_summary(df, "age", plot=True) #age değişkeninin özet istatistiği ve görsel hali

#bütün sayısal değişkenlerin özet istatistikleri ve görselleştirilmesi
for col in num_cols:
    num_summary(df, col, plot=True)


#############################################
# Değişkenlerin Yakalanması ve İşlemlerin Genelleştirilmesi ************ Önemli bir bölüm ************
#############################################

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()
df.info()

#öyle bir işlem yapacağızki kategorik ve nümerik değerleri ayrı ayrı getirsin.. (kategorik ama kardinal değişkenlerde gelsin)

# docstring: kullanmak istediğimiz fonksiyonları bizden başka kişiler kullanmak istediğinde bu fonksiyonların ne görev yaptığını ve tanımını oluşturmak

#ön tanımlı docstring yöntemini değiştirmek için;
# file -> settings -> docstring (search) -> docstring format -> NumPy

#cat_th: nümerik ama aslında kategorik olan değişkenler (default:10) categorical threshold, default: eşsiz değer sayısı < 10 ise kategorik değişken
#car_th: kategorik ama aslında nümerik olan değişkenler (default:20) cardinal threshold, default: eşsiz değer sayısı > 20 ise cardinal değişken
def grab_col_names(dataframe, cat_th=10,  car_th=20):
    """
    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.

    Parameters
    ----------
    dataframe: dataframe
        değişken isimleri alınmak istenen dataframe'dir.
    cat_th: int, float
        numerik fakat kategorik olan değişkenler için sınıf eşik değeri
    car_th: int, float
        kategorik fakat kardinal değişkenler için sınıf eşik değeri

    Returns
    -------
    cat_cols: list
        Kategorik değişken listesi
    num_cols: list
        Numerik değişken listesi
    cat_but_car: list
        Kategorik görünümlü kardinal değişken listesi

    Notes
    ------
    cat_cols + num_cols + cat_but_car = toplam değişken sayısı
    num_but_cat cat_cols'un içerisinde.

    """

    # cat_cols, cat_but_car (daha önceki bölümde yaptığımız kategorik ve nümerik değişken seçimlerini alalım..
    cat_cols = [col for col in dataframe.columns if str(dataframe[col].dtypes) in ["category", "object", "bool"]]

    #num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < 10 and dataframe[col].dtypes in ["int", "float"]]
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < 10 and (str(dataframe[col].dtypes).startswith('int' or 'float'))]
    #int32 ve int64 verileri bir arada bulunmaması için 1.yol

    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > 20 and str(dataframe[col].dtypes) in ["category", "object"]]

    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    #nümerik değişkenleri alalım..
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes in ['int', 'float']]
    #num_cols = [col for col in dataframe.columns if (str(dataframe[col].dtypes).startswith('int' or 'float'))] #neden boş dönüyor, anlamadım?

    num_cols = [col for col in num_cols if col not in cat_cols]

    #gönderilen dataFrame ile ilgili raporları sunalım..
    print(f"Observations: {dataframe.shape[0]}") #f String
    print(f"Variables: {dataframe.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')

    return cat_cols, num_cols, cat_but_car

help(grab_col_names) # fonksiyonun docstring'e (dökümantasyonuna) ulaşmak için

cat_cols, num_cols, cat_but_car = grab_col_names(df)

#bütün fonksiyonları getirip bütün öğrendiklerimizi uygulayalım..

def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

cat_summary(df, "sex") # tek bir değişken

#bütün değişken
for col in cat_cols:
    cat_summary(df, col)


#numerik değişkenler için
def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)


for col in num_cols:
    num_summary(df, col, plot=True)



# BONUS - en son yazmış olduğumuz cat_summary fonksiyonunu görselleştirmeye çalışalım..
df = sns.load_dataset("titanic")
df.info()

#bool tipleri int'e çevir -> fonksiyon içerisinde yapmak yerine burda kullanıyoruz, fonksiyon daha da zor okunabilir hale getirmek istemiyoruz
#veri setini hemen okuduktan sonra tip dönüşümünü yapmak daha mantıklı olacaktır
for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int) #int64 diyerek direkt int32 int64 verilerinin bir arada bulunmaması için 2.yol

cat_cols, num_cols, cat_but_car = grab_col_names(df) # kategorik ve nümerik değişkenleri yakal

def cat_summary(dataframe, col_name, plot=False): # yüzde oranlarını ver ve görselleştir
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

#tüm kategorik değişkenleri fonksiyona gönderelim..
for col in cat_cols:
    cat_summary(df, col, plot=True)

#tüm nümerik değişkenleri fonksiyona gönderelim
for col in num_cols:
    num_summary(df, col, plot=True)



#############################################
# 4. Hedef Değişken Analizi (Analysis of Target Variable)
#############################################
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")


#bool casting -> int
for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int) #direkt int64 dönüşümü yaparak int32-int64 verilerinin bir arada olmasını engelleyebilirsin

#veri setinin görselleştirilmesi
def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

#veri setinin değişkenlerinin kategorik-numerik analizi
def grab_col_names(dataframe, cat_th=10,  car_th=20):
    """
    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.

    Parameters
    ----------
    dataframe: dataframe
        değişken isimleri alınmak istenen dataframe'dir.
    cat_th: int, float
        numerik fakat kategorik olan değişkenler için sınıf eşik değeri
    car_th: int, float
        kategorik fakat kardinal değişkenler için sınıf eşik değeri

    Returns
    -------
    cat_cols: list
        Kategorik değişken listesi
    num_cols: list
        Numerik değişken listesi
    cat_but_car: list
        Kategorik görünümlü kardinal değişken listesi

    Notes
    ------
    cat_cols + num_cols + cat_but_car = toplam değişken sayısı
    num_but_cat cat_cols'un içerisinde.

    """
    # cat_cols, cat_but_car
    cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

    num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]] #muhtemelen çalışmayacak alttakini dene
    #num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < 10 and (str(dataframe[col].dtypes).startswith('int' or 'float'))]
    #int32 ve int64 verileri bir arada bulunmaması için 1.yol

    cat_but_car = [col for col in df.columns if
                   df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]

    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')

    return cat_cols, num_cols, cat_but_car

cat_cols, num_cols, cat_but_car = grab_col_names(df)


#Amacımız hedef survived değişkenini kategorik-sayısal değişkenler açısından analiz etmek; (hedef değişkeni genelde biliyor oluruz)
#Genelde hedef değişkenimizin ortaya çıkış sebeplerini merak ederiz. Titanic veri seti için; insanların hayatta kalma durumunu etkileyen şey nedir?
#Çaprazlamalar.. Çaprazlamaları hedef değişken üzerinden yapmalıyız.

df.head()

df["survived"].value_counts()
cat_summary(df, "survived")

#######################
# Hedef Değişkenin Kategorik Değişkenler ile Analizi
#######################


#kadın olmak survived değişkenini direkt etkileyen bir faktör olabilir (hedef değişken analizi)
df.groupby("sex")["survived"].mean() #cinsiyet değişkenine göre gruplayıp survived ortalamalarını al

#bütün kategorik değişkenleri hedef değişken üzerinden analiz etmeye çalışacağız
def target_summary_with_cat(dataframe, target, categorical_col):
    print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(categorical_col)[target].mean()}), end="\n\n\n") #gelen kategorik değişkeni önce grupla ve target değişkenine göre ortalamasını al


target_summary_with_cat(df, "survived", "pclass") #pclass ile survived değişkeni analizi (first class'lar belirgin şekilde daha fazla hayatta kalmış)

#tüm kategorik değişkenlerini gönderelim
for col in cat_cols:
    target_summary_with_cat(df, "survived", col) #(yalnızlar üzdü)



#######################
# Hedef Değişkenin Sayısal Değişkenler ile Analizi
#######################

#bu sefer survived'a göre grupla (sayısal değişkenler için böyle)
df.groupby("survived")["age"].mean() #önce survived ile grupla sonra yaş ortalamalarını al
#hayatta kalanların ve kalmayanların yaş ortalamaları

df.groupby("survived").agg({"age":"mean"}) #agg (toplulaştırma fonk.) ile kullanabilirz, çıktı daha düzgün

#hedef değişkeni sayısal değişkenlerle açıklama
def target_summary_with_num(dataframe, target, numerical_col):
    print(dataframe.groupby(target).agg({numerical_col: "mean"}), end="\n\n\n") #dikkat; sayısal değişkenlerde hedef değişkene göre gruplanır!


target_summary_with_num(df, "survived","age")

#tüm sayısal değişkenleri gönderelim..
for col in num_cols:
    target_summary_with_num(df, "survived", col)


#############################################
# 5. Korelasyon Analizi (Analysis of Correlation)
#############################################
#Amacımız;
#hızlı bir şekilde ısı haritası oluşturma
#birbiriyle yüksek korelasyona sahip değişkenlerden birisini nasıl silebiliriz? (bazen ihtiyaç durumunda dışarıda bırakma durumları gerekebilir, analiz aracı olarak kullanabiliriz)

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = pd.read_csv("dataset/breast_cancer.csv")
df = df.iloc[:, 1:-1] #sıkıntılı değişkenleri dışarıda bırakmak için (id, unnamed)
df.head()

"""
Korelasyon Nedir?
Değişkenlerin birbirleriyle ilişkisini ifade eden istatistiksel ölçümdür. -1 ile +1 arasında değer alır. 
-1'e veya +1'e yaklaştıkça ilişkinin şiddeti kuvvetlenir.
Arasındaki ilişki pozitif ise pozitif korelasyon denir ve bir değişkenin değeri arttıkça diğerinin de değeri artar. 1'e yakınsar.
Arasındaki ilişki negatif ise negatif korelasyon denir ve bir değişkenin değeri arttıkça diğerinin azalır. -1'e yakınsar.
Değer 0'a ne kadar yakınsı ilişkinin olmadığı gözlemlenir.
Düşür korelasyon 0 ile 0.50 arasında veya 0 ile -0.50 değerleri arasındadır.
Analitik çalışmalarda birbiriyle yüksek korelasyona sahip olan değişkenlerin çalışmalarda bulunmamasını isteriz. Çünkü ikiside aynı şeyi ifade ediyor.
"""

"""
Hayat kurtaranlardan;
Bazı senaryolarda birçok değişken olabilir ve bu değişkenler birbirleri arasında yüksek korelasyonlu olması model optimizasyonlarını, çalışmanın sürdürülebiliğini
çalışmanın el değiştirmesini, model deployment, development süreçlerini özetle negatif etkileyebilir. Bu durumda öyle birşey yapmak gerekir ki yüksek korelasyonlu
değişkenlerden kurtulalım. Bu ihtiyaç doğrultusunda (her zaman ihtiyaç duyulmayabilir) bir analiz aracı olarak görebiliriz.
"""


#sayısal değişkenleri alalım..
num_cols = [col for col in df.columns if df[col].dtype in [int, float]]

#veri setimiz, meme kanseri ile ilgili ölçüm değerleri var, ve biz bu ölçüm değerleri arasındaki korelasyonu görmek istiyoruz..
#önce ısı haritasını oluşturacağız, sonra birbirleriyle yüksek korelasyonu olanları elemeye çalışacağız..

#sayısal değişkenlerin korelasyonları
corr = df[num_cols].corr()

#ısı haritasında gösterelim..
sns.set(rc={'figure.figsize': (12, 12)})
sns.heatmap(corr, cmap="RdBu")
plt.show()


#######################
# Yüksek Korelasyonlu Değişkenlerin Silinmesi
#######################

#pozitiflik-negatiflik durumlarıyla ilgilenmiyoruz, korelasyon değerlerinin mutlak değerini alalım..
cor_matrix = df.corr().abs()


#4 değişkenli veri setinin korelasyon çıktısı (aynı bilgiler tekrar ediyor) (çoklama, birbirini tekrar eden bilgiler var)
#           0         1         2         3
# 0  1.000000  0.117570  0.871754  0.817941
# 1  0.117570  1.000000  0.428440  0.366126
# 2  0.871754  0.428440  1.000000  0.962865
# 3  0.817941  0.366126  0.962865  1.000000

#matristeki gereksiz elemanları silelim.. (istenilen hale getirme - varmak istediğimiz hedef)
#     0        1         2         3
# 0 NaN  0.11757  0.871754  0.817941
# 1 NaN      NaN  0.428440  0.366126
# 2 NaN      NaN       NaN  0.962865
# 3 NaN      NaN       NaN       NaN

#1'lerden oluşan ve oluşturmuş olduğumuz matris boyutunda numpy array'i oluşturuyoruz ve bool tipine çeviriyoruz daha sonra istenen formata çevirmek için triu fonk. kullanıyoruz
upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(bool)) # bu şekilde birbirini tekrar eden bilgilerden kurtulabiliyoruz
#köşegen 1.00 değerlerinden kurtulduk..

#şimdi yüksek korelasyon değerine sahip değişkenleri çıkarmamız lazım (onu ifade eden başka bir değişken var) (thresh (eşik) değerimiz 90 olsun)
drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col]>0.90)] # #değerlerden herhangi birisi: any()
#0.90'dan büyük korelasyon değişkenleri drop_list'de.

cor_matrix[drop_list] #yüksek korelasyonları seçelim
df.drop(drop_list, axis=1) #31 değişkenli olan veri seti yüksek korelasyona sahip değişkenlerden arındırıyoruz. ve 21 tane değişken kalıyor (10 tanesi uçtu)


#yaptığımız işlemleri fonksiyonlaştıralım..
def high_correlated_cols(dataframe, plot=False, corr_th=0.90):
    corr = dataframe.corr()
    cor_matrix = corr.abs()
    upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(bool))
    drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > corr_th)]
    if plot: #ısı haritası
        import seaborn as sns
        import matplotlib.pyplot as plt
        sns.set(rc={'figure.figsize': (15, 15)})
        sns.heatmap(corr, cmap="RdBu")
        plt.show()
    return drop_list


high_correlated_cols(df) #veri setimizi fonksiyona gönderelim. drop_list ile drop etmemiz gereken ilgili değişkenlerin listesini verecek
drop_list = high_correlated_cols(df, plot=True) #koyu mavileri ve koyu kırmızıları silmeye çalışıyoruz
df.drop(drop_list, axis=1) #korelasyonu yüksek verilerin silinmiş hali
high_correlated_cols(df.drop(drop_list, axis=1), plot=True) #silinmiş halini fonksiyona gönderelim (birçok bölümdeki yoğunluklar gitti)

# Yaklaşık 600 mb'lık 300'den fazla değişkenin olduğu bir veri setinde deneyelim.
# https://www.kaggle.com/c/ieee-fraud-detection/data?select=train_transaction.csv

df = pd.read_csv("datasets/fraud_train_transaction.csv")
len(df.columns)
df.head() #394'tane değişken var

"""
Veri setindeki problem; fraud -> sahtekarlık projesi olduğundan dolayı ve bir ticari yönü olduğundan dolayı veri setini paylaşan şirket değişkenlerin isimlerini
girmemiş. O kadar fazla birbirleriyle ilişkili korelasyon var ki bunun üzerine çalışmak neredeyse imkansız.
"""

drop_list = high_correlated_cols(df, plot=True) #ilgili fonksiyonumu uyguluyoruz, görselin çirkinliği :D (dikkat 10 dakikada açılıyor)

len(df.drop(drop_list, axis=1).columns) # yakalamış olduğumuz drop_list'i veri setimiz içerisinden silelim ve sildikten sonraki değişken sayısı 198

"""
Yazmış olduğumuz high_correlated_cols fonksiyonumuzun önemi;
Değişkenleri bu şekilde silmek, meziyet değil. Bu veri setinde el yordamıyla gözlemlemenin ve yapmanın mümkün olmayacağı kadar fazla sayıda yüksek korelasyonlu
değişken olduğunu ifade etmek asıl amaç.
"""
#type(adsa)

"""
grab_col_names fonksiyonu içerisinde num_but_cat değişkeni tanımlanırken dikkat!
windows ortamında int32 ve int64 verilerinin bir arada bulunmasına yol açıyor. Buda nümerik değerleri çekerken bazı problemlere yol açabiliyor.
ilk yol: grab_col_name startswith('int','float') kombinasyonlarını alabilirsin.
ikinci yol: zaten asıl sıkıntı bool tipindeki verileri int'e çevirirken yaşanıyordu. hem int32 hemde int64 verileri oluyor. direkt int64 astype yapılabilir.
"""

"""
İlgili bölümü toparlayacak olursak;
Artık şunları yapabiliyor olmamız bekleniyor..
- Elimize bir veri seti geldiğinde check_df ile o verinin genel yapısını değerlendirebiliyor oluruz.
- Veri setinin kategorik değişkenlerini sinsirelllalar dahil (kategorik gözüküp nümerik olan veya nümerik olup kategorik olan) her senaryodan yakalayabiliyor
olmalı ve bunların üzerinde gezecek olan bir fonksiyonumuz olmalı. (cut_summary fonk)
- grab_col_names fonk ile zaten yapmış olduğumuz bütün kategorik ve nümerik analizi için yapmış olduğumuz işlemleri ele almıştık. Burdan gelen çıktılarla
kolay bir şekilde target değişkenimizi kategorik ve nümerik değişkenler açısından değerlendirebiliyor olmamız bekleniyor.
- Son olarakta korelasyon analizi bölümüyle sadece analiz yapmak maksadıyla yüksek korelasyonlu değişkenlere erişebiliyor olmamız bekleniyor.
(Bu bölüm fazlasıyla udemy'den ayrılıyor. Çok şey öğrendim..)
"""