#動動腦
#1.若需要除以2運算後得到數字500的話怎麼辦？
num="1000"  #str字串型態
num=int(num)/2              
print("1000/2: ",num)
#2.若需要將重複的元素去除的話怎麼辦？
nums1=[1,1,1,2,2,3,4,5] #list串列型態
nums1=set(nums1)
print(nums1)
#3.tuple並不提供排序的方法，若要排序(由小到大)該怎辦？
nums2=(10,5,7,1,6,2) #tuple序對型態
nums2=list(nums2)
print("排列前：",nums2)
nums2.sort() 
print("排列後：",nums2) 
#提示：適時的轉換型態可以解決非常多的問題


#專題練習 Q1:使用

#Q1.使用set型別完成下列問題：本班期末考試
    #數學及格的有：Tom,John,Mary,Jimmy,Sunny,Amy
    #英文及格的有：John,Mary,Tony,Bob,Pony,Tom,Alice
    #分別印出數學及格但英文不及格的名單，數學不及格但英文及格的名單，兩科都及格的名單
    #最後印出全班總共有幾個同學
mathPass={"Tom","John","Mary","Jimmy","Sunny","Amy"}
engPass={"John","Mary","Tony","Bob","Pony","Tom","Alice"}
MathPAEngNO=mathPass-engPass 
print("數學及格但英文不及格: ",MathPAEngNO)
MathNOEngPA=engPass-mathPass
print("數學不及格但英文及格: ",MathNOEngPA)
ALLPASS=mathPass&engPass
print("兩科都及格: ",ALLPASS)
#Q2.使用dict，list型別完成下列問題：
    #Tom作業成績為80,100,90,95,John作業成績為100,93,75,80
    #請以dict型別存放兩個同學的資料
    #key:名字，value:分數列表(list)
    #請分別算出兩位同學的平均分數並且印出

score ={"Tom":[80,100,90,95],"John":[100,93,75,80]}
print("Tom的成績：",score["Tom"])
print("John的成績：",score["John"])
Tomsum=0
Johnsum=0
for x in score["Tom"]:
    Tomsum+=x

print("Tom的平均：",Tomsum/4)

for x in score["John"]:
    Johnsum+=x
print("Johnsum的平均：",Johnsum/4)

