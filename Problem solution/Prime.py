""" This Program for Internship 2020"""
import math
def main():
    while(True):
        unkown_number = input()
        unkown_prime = ""
        isprime = "FALSE"
        if(float(unkown_number) == 0.0):
            break
        for i in unkown_number:
            if(isprime == "TRUE"):
                break
            if(i == "."):
                continue
            else:
                unkown_prime  += i
                isprime = IsEven(int(unkown_prime))
        print(isprime)
        


def IsPrime(unkown_number, number_d2):
    if(number_d2 == 1):
        return True
    elif(unkown_number%number_d2 == 0):
        return False
    else:
        return IsPrime(unkown_number, number_d2-1)

def IsEven(unkown_number):
    if(unkown_number == 2.0):
        return "TRUE"
    elif(unkown_number == 1.0):
        return "FALSE"
    elif(unkown_number % 2 == 0.0):
        return "FALSE"
    elif(IsPrime(unkown_number, math.floor(unkown_number**0.5))):
        return "TRUE"
    else:
        return "FALSE"

main()