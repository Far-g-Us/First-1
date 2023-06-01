#-------------Hw-3-#10----------------------------#
#Запросить дату (день, месяц, год) и вывести следующую
#за ней дату. Учтите возможность перехода на следующий
#месяц, год, а также високосный год.



# 1-Вариант (Неработает)
# year=int(input('Enter a year: '))
# month=int(input('Enter a month: '))
# day = int(input('Enter a day: '))
# while(((month==4 or month==6 or month==9 or month==11) and day>30) or 
#     (day>28 and month==2 and (year%400!=0 or 
#         (year%4!=0 and year%100==0)))or (day>29 and month==2 and day==28 and month==2 and (year%400==0 or (year%4==0 and year%100!=0)))):

#     if(day==28 and month==2 and (year%400!=0 or (year%4!=0 and year%100==0))):
#         day=1
#         month=3
    
#     elif(day==28 and month==2 and (year%400==0 or (year%4==0 and year%100!=0))):
#         day=29
    
#     elif(day==30):
#         if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
#             day=31
        
#         else:
#             day=1
#             month+= 1
#             if(month>12):
#                 month-= 1
#                 year+= 1
            
#     elif (day==31):
#         day=1
#         month= month + 1
#         if(month>12):
#             month=1
#             year+= 1
        
#     else:
#         day+= 1
    
# print(f'Next data: {day}/{month}/{year}')


# 2-Вариант
CNT_DAYS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

day = int(input("Введите день:\n"))
month = int(input("Введите месяц:\n"))
year = int(input("Введите год:\n"))


v_year = year % 4 == 0 and year % 100 != 0 or year % 400 == 0

max_day = CNT_DAYS[month - 1]
if month == 2 and v_year:
    max_day += 1

day += 1
if day > max_day:
    day = 1
    month += 1

if month > 12:
    month = 1
    year += 1

if day > 9:
    day_res = f'{day}'
else:
    day_res = f'0{day}'
if month > 9:
    month_res = f'{month}'
else:
    month_res = f'0{month}'

print(f'{day_res}.{month_res}.{year}')