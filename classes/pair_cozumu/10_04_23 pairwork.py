
#kullanıcı sürekli konsolda tutan >> sonsuz döngü
#hesap makinesi
#4 işlem +mod alma işlemi
#q girdiğinde sonsuz döngü kırılacak 
#fonksiyon


def getNumberFromUser():
    return float(input("Lütfen sayı giriniz: "))
def calculateSum():
    num1=getNumberFromUser()
    num2=getNumberFromUser()
    print(f"Toplama işleminin sonucu: {num1 + num2}")
def calculateMinus():
    num1=getNumberFromUser()
    num2=getNumberFromUser()
    print(f"Çıkarma işleminin sonucu: {num1 - num2}")
def calculateMultiply():
    num1=getNumberFromUser()
    num2=getNumberFromUser()
    print(f"Çarpma işleminin sonucu: {num1 * num2}")
def calculateDivide():
    num1=getNumberFromUser()
    num2=getNumberFromUser()
    print(f"Bölme işleminin sonucu: {num1 / num2}")
def calculateMod ():
    num1=getNumberFromUser()
    num2=getNumberFromUser()
    print(f"Mod işleminin sonucu: {num1 % num2}")
    
while True:
    userInput = input("Yapmak istediğiniz işelmi seçiniz: ")
    if userInput == "q":
        break
    elif userInput == "+":
        calculateSum()
    elif userInput == "-":
        calculateMinus()
    elif userInput == "*":
        calculateMultiply()
    elif userInput == "/":
        calculateDivide()
    elif userInput == "%":
        calculateMod()
    else:
        print("Yanlış işlem girdiniz!")

