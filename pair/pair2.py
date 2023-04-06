#kullanıcıdan vize ve final notları alacak.
#vize %40  final %60 etkili olacak
#vize ve final notları 50.5 gibi ondalıklı sayılar olabilir
#uygulama ortalamayı hesaplayacak ve ortalamaya göre
#0-49 FF
#50-59 DD
#60-69 CC
#70-79 BB
#80-100 AA
#not ortalamasını ve not harfini kullanıcıya gösterecek programı kodlayınız.


vize =float(input("Lütfen vize notunuzu giriniz: "))
final = float(input("Lütfen final notunuzu giriniz:"))
ortalama = (vize*0.4) + (final*0.6)

if ortalama<=49 :
    print("Harf notunuz FF.")
elif  50<= ortalama <=59:
    print("Harf notunuz DD.")
elif  60<= ortalama <=69:
    print("Harf notunuz CC.")
elif  80 <= ortalama <=89:
    print("Harf notunuz BB.")
else:
    print("Harf notunuz AA.")
    
   