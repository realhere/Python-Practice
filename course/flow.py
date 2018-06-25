# 流程控制
# if 判斷式
# if 布林值：
#    如果布林值是 True 執行這個程式區塊
# "TAB"鍵縮排

# money=int(input("多少錢？"))
# if money<=0:
#     print("請輸入大於 0 的數字")
# elif money<=30000:
#     print("OK")
# else:
#     #如果布林值是 False, 執行這個區塊
#     print("Too Much")

# 作業一
# n1=int(input("Enter a Number："))
# n2=int(input("Enter a Number："))
# op=input("運算： +, -, *, /")

# if 
#     print("n1+n2")
# else:
#     print("不合法")

# 迴圈
# break, continue
# n=1
# while n<=5:
#     # 如果布林值是 True, 執行這個區塊的程式碼
#     n+=1
#     if n%2==0: # 如果 n 是偶數
#         continue # 立刻進入下一個圈圈
#     print(n)
# #        break # 立刻終止迴圈
# print("Final", n)  

#1+2+3+......+50
# sum=0 # 紀錄最後加總的結果
# n=1 # 在迴圈中追蹤 1, 2, 3, ..., 5
# while n<=5:
#     print(n, sum)
#     sum=sum+n # 將 n 的數字累加進 sum 裡面
#     n+=1
# print(sum)

# 作業二
# n=int(input("輸入一個正整數"))
# 算整數平方根 9=>3, 25=>5, 8=>沒有

# for 變數名稱 in 列表:
#     迴圈區塊

# for n in [2,5,6,7]:
#     print(n)
# print("=======")
# for x in range(1,6): # range(1,6) 產生 [1,2,3,4,5] 的列表
#     print(x)

# 作業三
# 印出 99 乘法表
# 用 for 迴圈寫兩層