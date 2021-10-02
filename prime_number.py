number = int(input("Enter a number please: "))


def isPrime(number):
    flag = True
    for i in range(2,number):
        if number % i == 0:
            flag = False
            break
        i+=1            
    if flag == True:
         print(str(number) + " is a prime number")
    else:
         print(str(number) + " is not a prime number")


isPrime(number)


   