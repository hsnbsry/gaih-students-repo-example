#proje

class YemekTarifleri():
  isim=""
  def __init__(self,yemekisim,pisirmesuresi,pisirmederecesi):
      self.isim=yemekisim
      self.sure=pisirmesuresi
      self.derece=pisirmederecesi
      self.malzemeler=[]
      self.baharatlar=[]

  def __init__(self,yemekisim):
      self.isim=yemekisim
      self.sutmalzemeler=[]
      self.yapilis=[]  

  def sutlacmalzeme(self,new_malzeme):
      self.sutmalzemeler.append(new_malzeme)

  def  sutyapilisi(self,yap):
      self.yapilis.append(yap)     

  def sutlacinfo(self):
      print("{}'in tarifi".format(self.isim))
      for i in  self.yapilis:
        print(i)   

  def eklemalzeme(self,new_malzeme):
      self.malzemeler.append(new_malzeme)    

  def eklebaharat(self,new_baharat):
      self.baharatlar.append(new_baharat)

  def showName(self):
      print(self.isim)  

  def showInfo(self):
      print("Yemeginizin  ismi:{}".format(self.isim))
      print("Kullandiginiz  malzemeler:")
      for i in self.malzemeler:
        print(i)
      print("Kullandiginiz baharatlar:")
      for i in self.baharatlar:
        print(i)  

  def firinda(self):
      print("Butun malzemelerimizi kucuk kucuk dogruyoruz. ")
      print("Baharatlarini {},{},{} ve salcayi bir bardak  suda karistiriyoruz ".format(self.baharatlar[0],self.baharatlar[1],self.baharatlar[2]))
      print("sonra {} nun ustune  dokuyoruz. firinda {} derecede {} dakika pisiriyoruz.".format(self.isim,self.derece,self.sure))
      print("Yemegimiz  hazir.Afiyet olsun")      

  def ocakta(self):
      print("Önce {} lari pisiriyoruz sonra  {} ve diger malzemeleri katip {} derecede yavas  yavas {} dakika pisiriyoruz".format(self.malzemeler[0],self.malzemeler[1],self.derece,self.sure))
      print("Yemegimiz  hazir.Afiyet olsun") 
      
      
      
      

class Turlu(YemekTarifleri):
  def __init__(self,yemekisim,pisirmesuresi,pisirmederecesi):
    super().__init__(isim)

print("Yemek tariflerine Hosgeldiniz")

yemekisim=str(input("Lutfen yemek  ismini giriniz:   ").upper())
pisirmesuresi=str(input("Lutfen pisirme suresini giriniz:    "))
pisirmederecesi=str(input("Lutfen pisirme derecesini giriniz:   "))

yemek=YemekTarifleri(yemekisim,pisirmesuresi,pisirmederecesi)

print(yemek.isim)

secim=str(input("Lutfen  secim yapiniz:Malzeme_Ekleme=1,Baharat_Ekleme=2,Cikis=3 --> "))

while secim!="3":
  
  if secim=="1":
    print("lutfen  5  Malzeme giriniz:  ")
    sum=0
    while sum!=5:
      new_malzeme=str(input("Lutfen  malzeme giriniz:   ").upper())
      yemek.eklemalzeme(new_malzeme)
      sum+=1
  elif secim=="2":
    print("lutfen  3  Malzeme giriniz:  ")
    sum=0
    while sum!=3:
      new_baharat=str(input("Lutfen  baharat giriniz:   ").upper())
      yemek.eklebaharat(new_baharat)
      sum+=1
  else:
    break    
  
  secim=str(input("Lutfen  secim yapiniz:Malzeme_Ekleme=1,Baharat_Ekleme=2,Cikis=3 --> "))

yemek.showInfo()

pisirme_sekli=str(input("Lutfen nasil  pisireceginizi  secin:Sefin secimi  firinda pisirmek.  Firinda=1,Ocakta=2 -->  "))
if pisirme_sekli=="1":
   yemek.firinda()
else:
   yemek.ocakta()

    
    

    
class Fasulye(YemekTarifleri):
  def __init__(self,yemekisim,pisirmesuresi,pisirmederecesi):
    super().__init__(isim)

print("Yemek tariflerine Hosgeldiniz")

yemekisim="Kuru Fasulye"
pisirmesuresi=str(input("Lutfen pisirme suresini giriniz:    "))
pisirmederecesi=str(input("Lutfen pisirme derecesini giriniz:   "))

yemek=YemekTarifleri(yemekisim,pisirmesuresi,pisirmederecesi)

print(yemek.isim)

secim=str(input("Lutfen  secim yapiniz:Malzeme_Ekleme=1,Baharat_Ekleme=2,Cikis=3 --> "))

while secim!="3":
  
  if secim=="1":
    print("lutfen  5  Malzeme giriniz:  ")
    sum=0
    while sum!=5:
      new_malzeme=str(input("Lutfen  malzeme giriniz:   ").upper())
      yemek.eklemalzeme(new_malzeme)
      sum+=1
  elif secim=="2":
    print("lutfen  3  Malzeme giriniz:  ")
    sum=0
    while sum!=3:
      new_baharat=str(input("Lutfen  baharat giriniz:   ").upper())
      yemek.eklebaharat(new_baharat)
      sum+=1
  else:
    break    
  
  secim=str(input("Lutfen  secim yapiniz:Malzeme_Ekleme=1,Baharat_Ekleme=2,Cikis=3 --> "))

yemek.showInfo()

pisirme_sekli=str(input("Lutfen nasil  pisireceginizi  secin:KuruFasulye en  guzel ocakta piser.  Firinda=1,Ocakta=2 -->  "))
if pisirme_sekli=="1":
   yemek.firinda()
else:
   yemek.ocakta()
    
    
    
    
    
    

class Sutlac(YemekTarifleri):
   def __init__(self,yemekisim,pisirmesuresi,pisirmederecesi):
    super().__init__(isim)

print("Yemek tariflerine Hosgeldiniz")

malzemeler=["Su","Pirinc","Süt","Seker","Vanilya","Nisasta"]
yemekisim="Sütlac"

yemek=YemekTarifleri(yemekisim)
for i in malzemeler:
  yemek.sutlacmalzeme(i)

def pisme(malzeme1,malzeme2,derece,sure):
    print(malzeme1+"  ile "+malzeme2+" i "+derece+"  derecede "+sure+" dakika arada  karistirarak yavas  yavas  kaynatiniz")

print("Sutlac da  kullancaginiz  malzemeler: ",malzemeler)
secim=str(input("Sutlaci yapmaya baslayalim. Devam  etmek icin:1 ,Cikmak  icin:2 tiklayin  -->  "))

while secim != "2":
  if secim=="1":
    sure=str(input("Lutfen pisirme suresini giriniz:    "))
    derece=str(input("Lutfen pisirme derecesini giriniz:   "))
    #yemek=YemekTarifleri(yemekisim,pisirmesuresi,pisirmederecesi)
    malzeme1=str(input("Tencereye ne  ekleyelim:-->"))
    malzeme2=str(input("Neyle  devam edelim:-->"))
    x=pisme(malzeme1,malzeme2,derece,sure)
    yemek.sutyapilisi(x)
  else:
    break

  secim=str(input("Devam  etmek icin:1 ,Cikmak  icin:2 tuklayin  -->  "))   

print("-------------------------------------------------------")
print("Sutlac da  kullancaginiz  malzemeler: ",malzemeler)
yemek.sutlacinfo()   


