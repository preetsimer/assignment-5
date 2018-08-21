#question 1
year=int(input("Enter year "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))


#question 2
length=int(input("Enter length "))
breadth=int(input("Enter Breadth "))
if length==breadth:
    print("It's a square ")
else:
    print("It's a rectangle ")


#question 3
l=[]
print("Enter age of 3 peoples ")
for i in range(0,3):
    a=int(input())
    l.append(a)
l.sort()
print("The person with age {0} is youngest and with {1} is eldest ".format(l[0],l[2]))

#question 4
age=int(input("Enter age "))
gen=input("Enter gender M/F ")
stat=input("Enter marital status N/Y ")
if gen=="f" or gen=="F":
    print("She will work only in urban areas ")
elif (gen=="M" or gen=="m") and (age>=20 and age<=40):
    print("He may work anywhere")
elif (gen=="M" or gen=="m") and (age>40 and age<=60):
    print("He may work only in urban areas")
else:
    print("ERROR!")

#question 5
price=int(input("Enter Price of item "))
n=int(input("Enter number of item "))
cost=price*n
if cost>1000:
    dis=(1000*10)/100
    total=cost-dis
else:
    total=cost
print("Total Amount is :",total)

    
#LOOPS
#question 1
l=[]
print("Enter 10 integers ")
for i in range(1,11):
    a=input()
    l.append(a)
print("The integers are: ")
for i in range(0,10):
    print(l[i])

#question 2
while True:
    print("This is infinite loop")

#question 3
n=int(input("Enter the size of list: "))
l=[]
s=[]
print("enter list elements ")
for i in range(1,n+1):
    a=int(input())
    l.append(a)
    sq=a*a
    s.append(sq)
print("The square of elements of a list are: ")
print(s)
    
#question 4
n=int(input("Enter size of the list "))
l=[]
for i in range(0,n):
    a=input()
    l.append(a)
intL=[]
floatL=[]
stringL=[]
for i in range(0,n):
    if isinstance(l[i],int):
        intL.append(l[i])
    elif isinstance(l[i],str):
        stringL.append(l[i])
    else:
        floatL.append(l[i])    
    
print("The new lists are ")
print(intL)
print(floatL)
print(stringL)



#question 5
print("Prime numbers list between 1 to 101 are:")
l=[]
for num in range(1,102):
    k=0
    for i in range(2,num):
        if(num%i==0):
            k=k+1
    if(k<=0):
        l.append(num)
print(l)        


#question 6
for i in range(0,4):
    for j in range(0,i+1):
        print("* ",end="")
    print("")


 
#question 7
n=int(input("Enter list size "))
l=[]
for i in range(1,n+1):
    a=input()
    l.append(a)
ele=input("Enter element to delete from list: ")
for i in range(0,n):
    if l[i]==ele:
        del l[i]
        break
print("The updated list is ")
print(l)





    
    






