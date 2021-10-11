#coding=gbk
#题目：输入某年某月某日，判断这一天是这一年的第几天？


months = [31,28,31,30,31,30,31,31,30,31,30,31]

year = raw_input("Enter the year(such as: 1955)")
month = raw_input("Enter the moth(such as: 5 for may)")
day = raw_input("Enter the day(such as: 3 for day)")


leapYear = 0
if int(year)%4==0 and int(year)%100!=0:
    leapYear+=1
else:
    if int(year)%400==0:
        leapYear+=1

monthDay = months[:(int(month)-1)]

days = sum(monthDay)+leapYear + int(day)
print "the day is no.",days,"days in this year"