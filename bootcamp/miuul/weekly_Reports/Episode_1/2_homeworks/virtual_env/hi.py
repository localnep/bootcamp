#Komut Satırında Python Kodu Çalıştırma

#PyCharm'da"hi.py"isminde python dosyası oluşturunuz
#Aşağıdaki kodu yazın.
print("Merhaba, ben Ozan Erdoğan !")
"""Konsoldan üzerinden "hi.py" dosyasının olduğu dizien (klasöre) gidiniz. PyCharm'da sol tarafta yer alan menüde hi.py dosyası
hangi klasördeyse o klasöre sağ tuş ile tıklayıp şu seçimi yapınız. "open in > terminal".
PyCharm'ın alt tarafınad terminal ekranı açılacak. Şu anda hi.py dosyası ile aynı dizindesiniz. (klasörde)
"""
#Konsola python hi.py yazarak, python kodunuzu çalıştırın.


########################################################################################################################
#Virtual Environment
########################################################################################################################

#documentation://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

# Kendi isminizde bir virtual environment oluşturunuz, oluşturma esnasında python 3 kurulumu yapınız
# conda create -n ozan python=3.0
# conda env list

# Oluşturduğunuz environment'ı aktif ediniz.
# conda activate ozan

# Yüklü paketleri listeleyin
# conda list

# Environment içerisine Numpy'ın güncel versiyonunu ve Pandas'ın 1.2.1 versiyonunu aynı anda indirin.
# conda install numpy pandas=1.2.1

# İndirilen Numpy'ın versiyonu nedir?
# conda list

# Pandas'ı upgrade ediniz. Yeni versiyonu nedir?
# conda upgrade pandas

# Numpy'ı environment'dan siliniz.
# conda remove numpy

# Seaborn ve matplotlib kütüphanesinin güncel versiyonlarını aynı anda indiriniz.
# pip install seaborn matplotlib

# Virtual environment içindeki kütüphaneleri versiyon bilgisi ile beraber export ediniz ve yaml dosyasını inceleyiniz.
# conda env export > environment.yaml

# Oluşturduğunuz environment'ı siliniz. (Önce environment'i deactivate ediniz)
# conda deactivate
# conda env remove -n ozan

# environment.yaml projemize dahil etmek için
#conda env create -f environment.yaml