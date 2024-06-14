# aaa = open('hello.txt', 'w')  

# print('Hello Python', 'test', 'test', file = aaa)

# aaa.close()

name = 'coco'
age = 77
money = 6666
score = 78.78
                                # 010.2f 中的010是指前十位數字空白用0表示，.2f是指到小數第二位
# print(f'姓名: {name}, 年齡: {age}, 財產: {money}元, 平均分數: {score:010.2f}') 
# print('姓名: %s, 年齡: %d, 財產: %010d, 平均分數: %010.2f' % (name, age, money, score))
# print('姓名: {}, 年齡: {}, 財產: {}元, 平均分數: {:010.2f}'.format(name, age, money, score))

# with open('code.txt', 'r', encoding='utf-8') as file_code, open('data.txt', 'r', encoding='utf-8') as file_data:
#     code = file_code.readline()
#     data = file_data.readline()

#     print(code.replace('$data', data))

#     eval(code.replace('$data', data))

# year = int(input('請輸入年份'))    # 使用變數 year 紀錄使用者輸入的年份
# if year%4 == 0:                    # 如果除以 4 能整除
#     if year%100 == 0:              # 如果除以 100 能整除
#         if year%400 == 0:          # 如果除以 400 能整除，就是閏年
#             print(f'{year} 是閏年')
#         else:
#             print(f'{year} 是平年')
#     else:
#       print(f'{year} 是閏年')
# else:
#     print(f'{year} 是平年')
    
# year = int(input('請輸入年份'))
# text = '平年'                # 新增變數 text 預設平年
# if year%4 == 0:
#     text = '閏年'            # 如果除以 4 能整除，將 text 改為閏年
# if year%100 == 0:
#     text = '平年'            # 如果除以 100 能整除，將 text 改為平年
# if year%400 == 0:
#     text = '閏年'            # 如果除以 400 能整除，將 text 改為閏年
# print(f'{year} 是{text}')

# year = int(input('請輸入民國年: '))
# print(f'民國{year}年 = 西元{year+1911}年')

# zodiac = year % 12

# if zodiac == 1:
#     print(f'{year}為鼠年')
# elif zodiac == 2:
#     print(f'{year}為牛年')
# elif zodiac == 3:
#     print(f'{year}為虎年')
# elif zodiac == 4:
#     print(f'{year}為兔年')
# elif zodiac == 5:
#     print(f'{year}為龍年')
# elif zodiac == 6:
#     print(f'{year}為蛇年')
# elif zodiac == 7:
#     print(f'{year}為馬年')
# elif zodiac == 8:
#     print(f'{year}為羊年')
# elif zodiac == 9:
#     print(f'{year}為猴年')
# elif zodiac == 10:
#     print(f'{year}為雞年')
# elif zodiac == 11:
#     print(f'{year}為狗年')
# else:
#     print(f'{year}為豬年')

# match zodiac:
#     case 1:
#         print(f'{year}為鼠年')
#     case 2:
#         print(f'{year}為牛年')
#     case 3:
#         print(f'{year}為虎年')
#     case 4:
#         print(f'{year}為兔年')
#     case 5:
#         print(f'{year}為龍年')
#     case 6:
#         print(f'{year}為蛇年')
#     case 7:
#         print(f'{year}為馬年')
#     case 8:
#         print(f'{year}為羊年')
#     case 9:
#         print(f'{year}為猴年')
#     case 10:
#         print(f'{year}為雞年')
#     case 11:
#         print(f'{year}為狗年')
#     case 0:
#         print(f'{year}為豬年')
#     case _:
#         print('發生錯誤')

         # := 指派回傳
# if (user := int(input('請輸入數字: '))) % 2 == 0:
#     print(f'{user}為偶數')
# else:
#     print(f'{user}為奇數')

a =[1, 2, 3, 4, 5, 6, 7]
print (a [2])
print (a [1:4])
print (a [ :3])
print (a [3: ])
print (a [ : ])
print (a [ :-1])
print (a [-3:-1])
print (a [1:4:2])
print (a [ : :2])
print (a [ : :-1])
print (a [-3:-1:-1])   #空資料
print (a [5: :-2])
print (a [-2: :-2])
print(a[::len(a)-1])
print(a[:2] + a[len(a)-2::])
