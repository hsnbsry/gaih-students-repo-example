#ödev  3
def prime_first(num):
  sayac=0
  for i in range(2,num):
    if num%i==0:
      sayac+=1
      break
  if sayac == 0:    
    print(num ," asal sayidir")

def prime_second(num):
  sayac=0
  for i in range(2,num):
    if num%i==0:
      sayac+=1
      break
  if sayac==0:    
    print(num ," asal sayidir")        

#prime_first(21)
#prime_second(541)

for  i in range(2,1000):
  if i<500:
    prime_first(i)
  else:
    prime_second(i)  


