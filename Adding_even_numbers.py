# s = int(input("Enter first Value: "))
# l = int(input("Enter second Value: "))
# total = 0
# for i in range(s,l+1):
#   if(i%2==0):
#     total = i+total
#     print(total)



###### Adding of all even numbers
# n = int(input("starting value: "))
# s = int(input("Last number: "))
# evenSum = 0
# for i in range(n,s+1):
#  if(i%2==0):
    # print("The even numbers are : ",i)
    # evenSum = evenSum+i
# print(f'for the values in range {n} and {s} the sum of all even numbers is {evenSum}')




#####Adding of all odd numbers 
l = int(input("Enter the stating Value: "))
s = int(input("Enter the Last Value: "))
oddSum = 0
for i in range(l,s+1):
    if(i%2==1):
        print("Odd Numbers are: ",i)
        oddSum = i+oddSum
print(f'for the values in range {l} and {s} the sum of all even numbers is {oddSum}')
