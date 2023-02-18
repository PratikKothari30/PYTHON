#153 = 1 **3  + 5**3 + 3**3




def Armstrong_Num(num, count):

    sum = 0
    temp = num

    while temp > 0:

        last_digit = temp % 10       #     --> Returns last digit
        sum = sum + last_digit**count
        temp = temp // 10            # --> Returns integer value of QUOTIENT

    if sum ==  num :

        print("Is Armstrong Number")

    else:

        print("is NOT an Armstrong Number")


num  = int(input("Enter a number: "))
# length = str(num)
# power = len(length)
x = num
count = 0
while x != 0:    #--> Finding the number of digits in given INTEGER number
    x = x//10
    count = count + 1    #--> COUNT gives the total no. of digits 

Armstrong_Num(num,count)