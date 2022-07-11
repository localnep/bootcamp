# Sayılar (Numbers) ve Karakter Dizileri (Strings)

print("Hello World")
print("Hello AI Era")

"""
Python'da kullanılan 3 tip sayı veri tipi;
Integer: 9
Float: 9.2
Kompleks
"""

# Atamalar ve Değişkenler (Assignments & Variables)

##########################################################################
# Virtual Environment (Sanal Ortam) ve (Package Managment) Paket Yönetimi
##########################################################################

#Sanal ortamların listelenmesi (in terminal)
#conda env list      --> bilgisayaramızda yüklü olan sanal ortamlar listelenmiş olacaktır. (*) simgesi bulunduğumuz sanal ortam
#conda info --envs

#Sanal Ortam Oluşturma
#conda create -n myenv     --> kendi istediğimiz isimlendirme ile sanal ortam oluşturma (myenv oluşturulacka isim) [y]

#Sanal ortamı aktif etme, Oluşturulan sanal ortamın içine girmek istersek
#conda activate myenv

#Yüklü paketlerin listelenmesi; Ortam içerisindeki paketleri görmek için;
#conda list

#Sanal ortama paket yüklemek istediğimizde
#conda install (numpy)

#Aynı anda birden fazla paket yüklemek istersek
#conda install numpy scipy pandas

#paket silme (bağımlılıklarını da kaldırır)
#conda remove package_name

#Özel olarak belirli bir numpy versiyonunu kullanmak istersek - belirli bir versiyona göre paket yükleme
#(pip -> == (çift), conda -> = (tek) kullanılır
#conda install numpy=1.20.1 (python'un 3.9'dan daha az sürümlerinde çalışır)

#paket yükseltme
#conda upgrade (numpy)
#conda upgrade conda

#tüm paketlerin yükseltilmesi
#conda upgrade -all

#python package index: paket yönetim aracı (pipy)
#pip kullanarak paket (pandas) yükleme
#pip install paket_adi

#paket yükleme versiyona göre (önceki sürümü otomatik siler)
#pip install pandas==1.2.1
#bağımlılık (paket) yönetimi aracının işlevlerinden birisi zorluk çıkarmadan versiyon bilgisini indirmesi (öncekini sildi)

"""
conda list içerisindeki kütüphaneleri başka bir çalışma ortamına aktarma işlemi
paket sayısı arttıkça aktarmak zor olacaktır, bunu aktarmanın yolu requirements txt dosyası yada yaml file dosyası
oluşturularak yapılır. (yml şeklinde de olabilir)
yaml yaparak conda aracılığıyla gerçekleştirelim. (pip ile de gerçekleştirilebilir (requirements.txt ile))
conda env export > environment.yaml 
sonra dir komutu ile çalışma dizinine bakalım (ios için ls)
projemize environment.yaml dizini geldiği için yakından inceleyebiliriz (her kütüphane versiyon bilgileri ile önümüze gelmiş oldu)
bu şekilde yeni bir environment oluşturduğumuzda kolay bir şekilde dahil edebiliriz
"""

"""
dahil etme işlemi;
conda deactivate (bulunduğumuz myenv enviremont'dan çıktık, şuan base'deyiz)
conda env remove -n myenv ile silmiş oluruz
şimdi elimizde var olan sanal ortam bilgi setini ismini,paketlerini,versiyonlarını barındıran dosyayı kullanarak
aynı enviroment'ı oluşturalım
conda env create -f environment.yaml (-f environment.yaml ile dosyadan bilgilerimizi aktarabiliyoruz, myenv ismini kendisi oto aldı create ile oluşturmadık)
ortamı aktif etmek için conda activate myenv
"""
