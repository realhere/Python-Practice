#1.讓使用者輸入5個數字 #input出來為字串
x0=int(input("請輸入第一個數字："))#int強制轉換字串成整數
x1=int(input("請輸入第二個數字："))
x2=int(input("請輸入第三個數字："))
x3=int(input("請輸入第四個數字："))
x4=int(input("請輸入第五個數字："))
#2.算總和
sum=0  #宣告變數sum=0
sum=x0+x1+x2+x3+x4  #整數相加
print("5個數字總和是 : %d"%(sum))   #%s代表字串  %d代表整數  %f代表浮點數
#3.找出哪個數字最大?
x=[x0,x1,x2,x3,x4]  #list串列格式 
x.sort()  #sort()涵式將串列由小到大排序
print("最大的數為 : %d"%(x[4]))  #x[0]為串列第一個數就是x1的值  所以x[4]為第五個數值
