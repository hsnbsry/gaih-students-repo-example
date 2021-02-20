#proje

class YemekTarifleri():
  isim=""
  def __init__(self,yemekisim,pisirmesuresi,pisirmederecesi):
      self.isim=yemekisim
      self.sure=pisirmesuresi
      self.derece=pisirmederecesi
      self.malzemeler=[]
      self.baharatlar=[]

  def pisirme(self):
      print("{}  yemeginiz {} derece de {} dakika pisecektir.".format(self.isim,self.derece,self.sure))
      

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
      print("Önce soganlari pisiriyoruz sonra salca ve diger malzemeleri katip {} derecede yavas  yavas {} dakika pisiriyoruz".format(self.derece,self.sure))
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

pisirme_sekli=str(input("Lutfen nasil  pisireceginizi  secin:  Firinda=1,Ocakta=2 -->  "))
if pisirme_sekli=="1":
   yemek.firinda()
else:
   yemek.ocakta()













      
      
