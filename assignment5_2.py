"""Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
 Once 'done' is entered, print out the largest and smallest of the numbers. 
 If the user enters anything other than a valid number catch it with a try/except 
 and put out an appropriate message and ignore the number.
 Enter 7, 2, bob, 10, and 4 and match the output below."""
 
"""largest = None
smallest = None

while True:
    x = input("Enter a number: ")
    if x == "done" : break
    try:
        num = int(x)
    except:
       
        print("Invalid input")
        continue
    if smallest is None:
        smallest = num 
    if (num) > (largest) :
        largest = num
    elif (num) < (smallest) :
        smallest = num


print("Maximum is", int(largest))
print("Minimum is", int(smallest))
"""
largest = None
smallest = None
while True:
   
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        #print (num)
        num = int(num)
        if largest is None or largest < num :
            largest = num
        elif smallest is None or smallest > num :
            smallest = num
    except:
        print("Invalid input")

print ("Maximum is", largest)
print ("Minimum is", smallest)
#https://www.coursera.org/account/accomplishments/verify/X4KPFSUV5V8X?utm_source=link&utm_campaign=copybutton_certificate

