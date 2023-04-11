
def sum(firstNum:float,secondNum:float):
    sum = firstNum+secondNum
    print(f"{firstNum} + {secondNum} = {sum}")
    
def subtract (firstNum: float, secondNum=float):
    subtract = firstNum - secondNum
    print(f"{firstNum} - {secondNum} = {subtract}")

def multiplication (firstNum: float, secondNum=float):
    multiplication = firstNum * secondNum
    print(f"{firstNum} * {secondNum} = {multiplication}")

def divide (firstNum: float, secondNum=float):
    divide = firstNum / secondNum
    if secondNum != 0:
        print(f"{firstNum} / {secondNum} = {divide}")
    else: 
        print("Please enter a valid number!")

def mod (firstNum: float, secondNum=float):
    mod = firstNum%secondNum
    print(f"{firstNum} % {secondNum} = {mod}")

def calculator (fNum:float, sNum:float, operation:str):
    if operation == "+":
        sum(firstNum=fNum, secondNum=sNum)
    elif operation == "-":
        subtract(firstNum=fNum, secondNum=sNum)
    elif operation == "*":
        multiplication(firstNum=fNum, secondNum=sNum)
    elif operation == "/":
        divide(firstNum=fNum, secondNum=sNum)
    elif operation == "%":
        mod(firstNum=fNum, secondNum=sNum)
    else:
        print("Please choose valid operation!")
while True:
    print("----------------------\n")
    firstNum= float(input("Please enter a first number: "))
    secondNum= float(input("Please enter a second number: "))
    operation= str(input("Please choose your operation (+,-,*,/,%): "))

    calculator(firstNum, secondNum, operation)
    isContinue = input("If you want to quick press 'q' or continue for enter!")

    if isContinue == "q":
        print("Finished operation.")
        break
    else:
        pass
    