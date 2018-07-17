# 印出九九乘法表
def multiple():
    for x in range(1,10):      
      for y in range(1,10): 
        print("%d*%d=%d"%(x,y,x*y))

# 四則運算計算機
def caculator():
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