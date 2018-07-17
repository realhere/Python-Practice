print("作業一：四則運算")
n1=int(input("輸入第一個數字："))
n2=int(input("輸入第二個數字："))
op=input("選擇運算方式（ +, -, *, /）：")
if op=="+":
    print("數字相加為",n1+n2)
elif op=="-":
    print("數字相減為",n1-n2)
elif op=="*":
    print("數字相乘為",n1*n2)
elif op=="/":
    print("第一個數字除以第二個數字為",n1/n2)
    print("第二個數字除以第一個數字為",n2/n1)
else: 
    print("輸入的運算方式無效")

print("======================")
print("作業二：算整數平方根")
n=int(input("輸入一個正整數："))
for x in range(0,n):
    if x*x==n:
        print("n 的平方根為：%d" %(x))
        break
else:
        print("%d 的平方根不是整數" %(n))
print("======================")

import sys

while True:
    n=(input("要繼續嗎？（y/n）"))
    if n=="y":
        break
    else:
        print("Goodbye")
        sys.exit()

while True:
    n=(input("要印出九九乘法表嗎？（y/n）"))
    if n=="y":
        break
    else:
        print("Goodbye")
        sys.exit() 
             
print("作業三：印出九九乘法表")
for x in range(1,10):      
    for y in range(1,10): 
        print("%d*%d=%d"%(x,y,x*y))