# s = int(input("Enter starting value: "))
# l = int(input("Enter Last value: "))
# num = 0
# for i in range(s,l+1):
#     print("numbers are : ",i)
#     num = num+i
# print("Total sum is : ",num)


# l = int(input("Enter the stating Value: "))
# s = int(input("Enter the Last Value: "))
# oddSum = 0
# for i in range(l,s+1):
#     if(i%2==1):
#         print("Odd Numbers are: ",i)
#         oddSum = i+oddSum
# print(f'for the values in range {l} and {s} the sum of all even numbers is {oddSum}')

# //print fibbonaci series?




n = int(input("Enter the value: "))
def fib(n):
  a = 0
  b = 1
  while b<n:
    print(b) 
    temp = a
    a = b
    b = temp+b
fib(n)




