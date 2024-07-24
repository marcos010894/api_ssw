def calc(num1, num2):

    print(num1)
    print(num2)

    while num2 <= 100:
        result = num1 + num2
        print(result)
        num1 = num2 
        num2 = result 

#calc(0, 1)  

arrresult = []
def calcAms(num):
    quantie_num = len(num)
    result = 0
    for unicNumber in num:
        unic = int(unicNumber)
 
        result += unic ** quantie_num 
    if(result == int(num)):
        return result
    return False

def countLimit():
    limited = 10000000
    count = 0
    while count <= limited:
        result = calcAms(str(count))
        if(result):
            arrresult.append(result)
            print(result)
        count = count + 1
countLimit()