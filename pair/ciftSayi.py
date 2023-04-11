#Kullanıcının vereceği üst limit ile 0'dan bu üst limite kadar olan tüm 'çift' sayıları ekrana yazdıralım.

maxLimit = int(input("Üst limit giriniz:"))

for i in range(0,maxLimit):
  if i % 2 == 0:
    print(i, end=" ")
    
