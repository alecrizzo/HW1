# Alec Rizzo
# Python - HW 1

# Returns true for prime, false for composite
def isPrime(value):
    if value > 1:
        for i in range (2, value):
            if (value % i) == 0:
                #print("false")
                return False
    #print("true")
    return True

# Reverses the numerical value that is given
def reverse(value):
    result = 0
    while(value > 0):
        endVal = value % 10
        result = result * 10 + endVal
        value = value // 10     # integer division (floor division)
    return result

# Returns true if the value is emirp
def emirp(value):
    if isPrime(value) == True and isPrime(reverse(value)) == True:
        return True


userVal = 0
while True:
    try:
        userVal = int(input("Please enter a number for how many emirps you would like to calculate: "))
        if userVal < 0:
            print("Please enter only positive integers!")
            continue
        break
    except:
        print("Please enter only positive integers!")

Test = 2
emirpFound = 0
while emirpFound < userVal:
    if emirp(Test) == True:
        print(Test)
        emirpFound += 1
    Test += 1

input("Press Enter to Exit...")
