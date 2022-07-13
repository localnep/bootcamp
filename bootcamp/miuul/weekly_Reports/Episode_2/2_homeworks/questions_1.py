"""
Görev: cat_summary() fonksiyonuna 1 özellikekleyiniz. Bu özellik argümanla biçimlendirilebilir olsun.
Var olan özelliğide argümanla kontroledilebilir hale getirebilirsiniz.Fonksiyona arguman ile biçimlendirilebilen bir özellik eklemek ne demek?
Örnek olarak aşağıdaki check_df fonksiyonuna argümanla biçimlendirilebilen 2 özellik eklenmiştir. Bu özellikler ile tail fonksiyonunun
kaç gözlemi göstereceği ve quantile değerlerinin gösterilip gösterilmeyeceği fonksiyona özellikolarak girilmiştir.
Bu özellikleri kullanıcı argümanlarla biçimlendirebilmektedir.
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")

#Cevap

def cat_summary(dataframe, col_name, plot = False, cat_names_list = []):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    if plot:
        print("################# Kırılımlar #########################")
        if(len(cat_names_list) == 1):
            sns.countplot(x=cat_names_list[0], data=dataframe)
            plt.show(block=True)
        elif(len(cat_names_list) == 2):
            sns.boxplot(x=cat_names_list[0], y= cat_names_list[1], data = dataframe)
            plt.show(block=True)
        elif(len(cat_names_list) == 3):
            sns.boxplot(x=cat_names_list[0], y=cat_names_list[1], hue=cat_names_list[2], data=dataframe)
            plt.show(block=True)
        else:
            print("liste boş veya 3'den fazla kolon bilgisi göndermeyin")


df.info()

cat_summary(df,"survived",True,["sex","age","survived"]) #sayısal değişkenleri gönderme

########################################################################################################################
#Görev: check_df(), cat_summary() fonksiyonlarına 4 bilgi(uygunsa) barındıra nnumpy tarzı docstring yazınız. (task, params, return, example)

#Cevap

def cat_summary(dataframe, col_name, plot = False, cat_names_list = []):
    #docstring
    """
        Veri setindeki gönderilen kolonun yüzdelik bilgisini verir ve Gönderilen liste istenilirse kırılımları grafikleştirilebilir.

        Parameters
        ----------
        dataframe: dataframe
            değişken isimleri alınmak istenen dataframe'dir.
        col_name: str
            yüzdelik oranını bilgisi verilecek olan kategorik kolon
        plot: bool
            görselleştirmek istenirse (default: False)
        cat_name_list:
            değişkenlerin kırılımları gösterilir (default: [])

        Returns
        -------


        Notes
        ------
        Lütfen kategorik değişken gönderin.
        cat_name_list listesi max 3 argüman alabilir.
        """
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    if plot:
        print("################# Kırılımlar #########################")
        if (len(cat_names_list) == 1):
            sns.countplot(x=cat_names_list[0], data=dataframe)
            plt.show(block=True)
        elif (len(cat_names_list) == 2):
            sns.boxplot(x=cat_names_list[0], y=cat_names_list[1], data=dataframe)
            plt.show(block=True)
        elif (len(cat_names_list) == 3):
            sns.boxplot(x=cat_names_list[0], y=cat_names_list[1], hue=cat_names_list[2], data=dataframe)
            plt.show(block=True)
        else:
            print("liste boş veya 3'den fazla kolon bilgisi göndermeyin")

def check_df(dataframe, head=5):
    #docstring
    """
        Gönderilen veriyi genel resmi vermesi için

        Parameters
        ----------
        dataframe: dataframe
            değişken isimleri alınmak istenen dataframe'dir.
        head: int
            gözlemlenecek dataframe'in ilk satırlarını getirir (default: 5)

        Returns
        -------

        Notes
        ------
        Bu metotu gönderilen nümrerik kolonlar ile ilgili genel bilgileri edinmek için kullanın.
    """
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