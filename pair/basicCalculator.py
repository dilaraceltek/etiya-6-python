#Bir hesap makinesi kodladığımızı varsayalım, 
#kullanıcı ilk olarak sırayla 2 adet sayı girecek ve bu sayılar arasında 
#yapmak istediği dört işlemi seçecek. Seçerken verdiği değerler dört işlemden birisi değil ise 
#kullanıcı uyarılacak ( + - * / ). Girilen işleme göre bu iki sayı arasında ilgili işlem yapılarak 
#kullanıcıya sonuç gösterilecek. 


sayi1= float(input("1.sayıyı giriniz: "))
sayi2= float(input("2.sayıyı giriniz: "))
islem = input("Yapmak istediğiniz işlemi seçiniz ( +,-,*, /) :")

if islem== "+":
    print(sayi1+sayi2)
elif islem == "-":
    print(sayi1-sayi2)
elif islem == "*":
    print(sayi1*sayi2)
elif islem == "/":
    print(sayi1/sayi2)
else:
    print("Uygun işlemi seçmediniz!. Lütfen uygun işlemlerden birini seçiniz.")
