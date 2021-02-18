#Explain your work

#Question 2
notlar=[]
isim_soyisim=[]
d={}
for i in range(3):
  isim=str(input("Lutfen isim  ve soyisminizi giriniz:"))
  isim_soyisim.append(isim)
  vize=int(input("Vize notunu giriniz:"))
  final=int(input("Final notunu giriniz:"))
  odev=int(input("Odev notunu giriniz:"))
  ortalama=(vize+final+odev)/3
  notlar.append(ortalama)
  d[isim_soyisim[i]]=notlar[i]
  
print(notlar)
print(isim_soyisim)
print(d)
maxx=0
for v in d.values():
  if maxx<v:
    maxx=v

for k,v in d.items():

  if maxx==v:
    print("en  yuksek notu alan ogrenci:",k,"notu:",v)


 

  

