# 1. 程式包裝
# 1.1 把 99 乘法表包裝成函式，可做 n*n 乘法   
def multiple():
    for x in range(1,10):      
      for y in range(1,10): 
        print("%d*%d=%d"%(x,y,x*y))

# 1.2 把四則運算機包裝成函式
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

# 1.3  將以上兩個函式包裝進模組 core.py 中
# import core
# core.multiple()
# core.caculator()

# 1.4 將模組 core.py 包裝進封包 lib 中，並在主程式中正確呼叫運用。
# import lib.core
# lib.core.multiple()
# lib.core.caculator()

# 2. 使用系統內建的模組 random 產生 1~100 間的亂數 （練習到官網找文件 - The Python Standard Library 9.6）
lib.random.random(1,101)
