#odev1
asal_sayi_liste=[]
asil_list=[]
list1=[]
list2=[]
list3=[]
for sayi in range(3,100):
       for i in range(2,sayi):
           if (sayi % i) == 0:
               break
       else:
           asal_sayi_liste.append(sayi)

print(asal_sayi_liste)
sum=0

for i in range(9):
  if sum<3:
    list1.insert(i,liste[i])
    sum+=1
  elif 3<= sum <6:
    list2.insert(i,liste[i])
    sum+=1
  else:
    list3.insert(i,liste[i])

asil_list=[list1,list2,list3]        

print(asil_list)        

for i in asil_list:
  for j in i:
   print(j)
