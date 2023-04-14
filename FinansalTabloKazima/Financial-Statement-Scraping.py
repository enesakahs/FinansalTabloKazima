import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By #xpath yapıları icin
import time
import pandas as pd

url="https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse=ACSEL"
r=requests.get(url)
s=BeautifulSoup(r.text,"html.parser") # html kodlarını oku s degiskenine ata

s1=s.find("select",{"id":"ddlAddCompare"}) # s degiskeninedeki html kodlarından select yapısında id si ddlAddCompare olanları getir

s2=s1.find("optgroup").find_all("option") #find ile yakaldıgı ilk optgroup u getirttik onun icinden de optionsları aldık

hisseler=[]
for i in s2:
    hisseler.append(i.text) # s2 de yakaladıgımız hisselerin text kısmını teker teker alıp hisselerin icine attık

def site():

    #terminaldeki hata mesajından kurtulmak icin
    option=webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches",["enable-logging"])

    #SELENIUM CALISIRKEN PENCEREYİ GÖRMEMEK İCİN
    option.add_argument("--headless")

    driver=webdriver.Chrome(options=option)

    driver.get("https://www.halkyatirim.com.tr/skorkart/bize-ulasin") # sayfaya ulastı
    time.sleep(5)
    driver.maximize_window()
    
    sec=driver.find_element(By.XPATH,"//*[@id='DropDownEnstrumanKodu']") # acılır pencereyi actı
    sec.click()
    time.sleep(5)

    s=Select(sec)
    s.select_by_value(HisseAdi)
    time.sleep(5)
    return driver

def PazarEndeks():
    page=site().page_source
    soup=BeautifulSoup(page,"html.parser")
    tablo=soup.find("table",{"id":"TBLPAZARENDEKSLERI"})
    tablo=pd.read_html(str(tablo),flavor="bs4")[0]

    #Tablo Baslıklarına İsim Vermek İcin
    tablo=tablo.rename(columns={"Unnamed 0":"Özellikler","Unnamed: 1":"Bilgiler"})
    print(tablo)

def FiyatPerformans():
    page=site().page_source
    soup=BeautifulSoup(page,"html.parser")
    tablo=soup.find("table",{"id":"TBLFIYATPERFORMANSI"})
    tablo=pd.read_html(str(tablo),flavor="bs4")[0]
    tablo=tablo.rename(columns={"Unnamed 0":"Kalemler"})
    print(tablo)

def PiyasaDegeri():
    page=site().page_source
    soup=BeautifulSoup(page,"html.parser")
    tablo=soup.find("table",{"id":"TBLPIYASADEGER"})
    tablo=pd.read_html(str(tablo),flavor="bs4")[0]
    tablo=tablo.rename(columns={"Unnamed 0":"Kalemler","Unnamed: 1":"Degerler"})
    print(tablo)

def TeknikVeriler():
    page=site().page_source
    soup=BeautifulSoup(page,"html.parser")
    tablo=soup.find("table",{"id":"TBLTEKNIKVERI"})
    tablo=pd.read_html(str(tablo),flavor="bs4")[0]
    tablo=tablo.rename(columns={"Unnamed 0":"Teknik","Unnamed: 1":"Degerler","Unnamed 2":"Yorumlar"})
    print(tablo)

def TemelAnalizVerileri():
    page=site().page_source
    soup=BeautifulSoup(page,"html.parser")
    tablo=soup.find("table",{"id":"TBLTEMELANALIZ"})
    tablo=pd.read_html(str(tablo),flavor="bs4")[0]
    tablo=tablo.rename(columns={"Unnamed 0":"Kalemler","Unnamed: 1":"Degerler"})
    print(tablo)

def FiyatOzeti():
    page=site().page_source
    soup=BeautifulSoup(page,"html.parser")
    tablo=soup.find("table",{"id":"TBLFIYATOZET"})
    tablo=pd.read_html(str(tablo),flavor="bs4")[0]
    tablo=tablo.rename(columns={"Unnamed 0":"Kalemler","Unnamed: 1":"Degerler"})
    print(tablo)

def Finansallar():
    page=site().page_source
    soup=BeautifulSoup(page,"html.parser")
    tablo=soup.find("table",{"id":"TBLFINANSALVERİLER3"})
    tablo=pd.read_html(str(tablo),flavor="bs4")[0]
    print(tablo)

def Karlılık():
    page=site().page_source
    soup=BeautifulSoup(page,"html.parser")
    tablo=soup.find("table",{"id":"TBLFINANSALVERİLER2"})
    tablo=pd.read_html(str(tablo),flavor="bs4")[0]
    print(tablo)

def Carpanlar():
    page=site().page_source
    soup=BeautifulSoup(page,"html.parser")
    tablo=soup.find("table",{"id":"TBLFINANSALVERİLER1"})
    tablo=pd.read_html(str(tablo),flavor="bs4")[0]
    print(tablo)

print("------Finansal Tablo Kazıma------\n")

while True:
    HisseAdi=input("Bilgilerini Görmek İstediginiz Hisse Adını Giriniz: ")
    HisseAdi=HisseAdi.upper() #inputu degerini büyük harflere cevirdi

    if HisseAdi in hisseler:
        print("Devam Ediliyor..")
        time.sleep(3)
        s=["PazarEndeks","FiyatPerformans","PiyasaDegeri","TeknikVeriler","TemelAnalizVerileri",
           "FiyatOzeti","Finansallar","Karlılık","Carpanlar"]
        print("1-{}\n2-{}\n3-{}\n4-{}\n5-{}\n6-{}\n7-{}\n8-{}\n9-{}\n"
        .format(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8]))

        while True: #1-9 arası deger girmezse
            giris=input("Lütfen İstediginiz Tablo Kodunu Giriniz: ")

            if giris in ["1","2","3","4","5","6","7","8","9"]:
                print("Devam Ediliyor..")
                time.sleep(3)
                print("\033c") #terminal ekranını temizlemek icin

                if giris == "1":
                    PazarEndeks()
                    break

                elif giris == "2":
                    FiyatPerformans()
                    break

                elif giris == "3":
                    PiyasaDegeri()
                    break

                elif giris == "4":
                    TeknikVeriler()
                    break

                elif giris == "5":
                    TemelAnalizVerileri()
                    break

                elif giris == "6":
                    FiyatOzeti()
                    break

                elif giris == "7":
                    Finansallar()
                    break

                elif giris == "8":
                    Karlılık()
                    break

                elif giris == "9":
                    Carpanlar()
                    break
            else:
                print("Lütfen Gecerli Bir Tablo Kodu Giriniz..\n")
        break

    else:
        print("Hisse Adı Bulunamadı..\n\n")
        time.sleep(3)
