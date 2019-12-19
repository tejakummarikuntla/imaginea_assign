in_date = str(input())
dd,mm,yy = in_date.split('/')
dd = int(dd)
mm = int(mm)
yy = int(yy)
lst_31 = [1,3,5,7,8,10,12]
lst_30 = [4, 6, 9, 11]
if mm in lst_31:
    max_days = 31
elif mm in lst_30:
    max_days = 30
elif(yy%4==0 and yy%100!=0):
    #or yy%400==0
    max_days = 29
else:
    max_days = 28
if(mm<1 or mm>12):
    print("Date is invalid.")
elif(dd<1 or dd>max_days):
    print("Date is invalid.")
else:
    print("Date is Valid")
