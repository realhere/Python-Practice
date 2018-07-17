# function 函式基礎
# 建立函式 > 呼叫函式
# 建立函式：函式的名字、參數、回傳值

# 以下為函式格式
# def 函式的名字(參數列表):
#     函式內部的程式碼
#     return 回傳值

# 建立一個函式
# def test(): # 參數列表可以不用寫
#     print("Hello") # 所有學過的程式碼都可以寫在這裡
#     return # 回傳值可以不用寫
# test() # 函式呼叫（從呼叫函式的地方、跳進函式裡面）
# test() # 建立函式的目的、是可以重複呼叫函式 

# def test(msg): # 代表在函式裡面可以使用這名字（參數）來工作 
#     print(msg)  
#     return 15 # 只有在函式內可用此命令（與函式搭配），把資料帶出來。若是空的，則會帶出空值 
# data=test("Hello") # 給相對應的資料
# test("world")
# print(data) # 印出資料內容（return 的結果）

# 呼叫這個函式，是為了做加法
# def add(n1,n2): # 可以有很多參數，以逗號隔開
#     print(n1+n2)
#     return n1-n2 # 可以回傳任何「資料」Ex. "hello"
# result=add(4,3)*add(3,2)
# print(result)

# 函式將程式包裝，可以重複使用

# sum=0
# for x in range(1,11): # (列表 1 到 10) / range(1,11) 等於 [1,2,3,4,5,6,7,8,9,10]
#     sum=sum+x
# print(sum)

# # 函式的實際範例使用
# def calSum(max):  
#     sum=0
#     for x in range(1,max+1):
#         sum=sum+x
#     print(sum)
# data=calSum(10) # 1 加到 10
# calSum(50) # 1 加到 50


# 函式參數變化：參數預設值
# def add(n1,n2=5):
#     print(n1+n2)
# add(4,8) # n1 & n2 都有給資料
# add(3) # n2 沒有給資料，用預設值（5）

# 函式參數變化：參數名稱對應
# def add(n1,n2=5):
#     print(n1-n2)
# add(n2=4,n1=8) # 原本是依照順序，若有給名稱，則會依照名稱而非順序

# # 函式參數變化：不定長度的參數
# def add(*ns):
#     sum=0
#     for n in ns:
#         sum=sum+n
#     print(sum)
# add(3,5,7,8,9)
# add(2,9,3)
# add(66,9,7,8,5,3)

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) # * 代表任意字元 / sep 代表區隔 / end 後的的 "\n" 等於換行
# print("Hello", "World", "HaHa", sep=',', end='') # 用 "," 區隔 / 不換行
# print("bbbb")

# 模組 module 與封包 package 
# 模組可以把程式放在另外一個檔案（組織程式的工具）
# import 模組名稱
# import core # 載入模組 core.py 
# core.add(3,4,5,6) # 呼叫 core 裡面的 add 函式
# core.test() # 呼叫 core 裡面的 test()
# import 模組名稱 as 別名
# import core as c 
# c.add(3,4,5,6)
# c.test()

# 建立封包的流程
# 1. 建立資料夾
# 2. 在資料夾中加入 __init__.py 檔案
# 3. 將模組的程式放進去

# import lib.core # import 封包名稱.模組名稱（用"."隔開）
# lib.core.add(3,4,5,6)
# import lib.core as c
# c.add(3,4,5,6)

# 作業
# 1. 程式包裝
# 1.1 把 99 乘法表包裝成函式，可做 n1*n2 乘法
# def list(n1,n2):
#     return
# 1.2 把四則運算機包裝成函式
# 1.3 將以上函式包裝在你自己的模組和封包中，並且在主程式成功使用

# 2. 使用系統內建的模組 random 產生 1~100 間的亂數 （練習到官網找文件 - The Python Standard Library 9.6）