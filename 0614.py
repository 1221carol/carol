# #猜數字1
# import random
# a = random.randint(1,10)                         # 產生 1～99 的隨機整數
# b = int(input('輸入 1～10 的數字：'))            # 讓使用者輸入數字，使用 int 轉換成數字
# while a!=b:                                      # 使用 while 迴圈，如果 a 不等於 b，就不斷繼續
#     if b < a:
#         b = int(input('數字太小：'))             # 如果 b<a，提示數字太小
#     elif b > a:
#         b = int(input('數字太大：'))             # 如果 b>a，提示數字太大
# print('答對囉！')                                # 如果 b=a 會停止 while 迴圈，顯示正確答案


#猜數字2
# import random

# answer = random.randint(1, 10)
# print(f'測試用: {answer}')

# count = 0 # 紀錄總共猜了幾次

# while True:
#     user = int(input('請猜一個數字: '))
#     count += 1  # 加一次

#     if user == answer:
#         print(f'猜對了，總共猜了{count}次')
#         break
#     else:
#         print(f'猜錯了，已經猜了{count}次')
        

# a = 1, 2, 3, # 打包

# print(a, type(a))

# c, d, e = a  # 解包

# e, *f = a

# print('e:', e)
# print('f:', f)

# a = 1, 2, 3, 4, 5

# b, *c, d = a

# print(b)
# print(d)
# print(c)


# a = ['aaron', 'andy', 'alan', 'apple']
# b = [66, 77, 88, 99]

# c = zip(a, b)

# print(list(c))


# 算參加人數
# a = ['aaron', 'andy', 'andy', 'apple', 'abner','aaron' ]

# print (set(a))        #名子不重覆
# print (len(set(a)))   #顯示人數


# a = (n for n in range(10))

# # generaotr                 #只能執行一次
# print(type(a))

# for i in a:
#     print('1st:', i)

# for i in a:
#     print('2nd:', i)


# 交集 聯集 差集 對稱差集

# employee1 = {'英文', '日語', '粵語', '台語'}
# employee2 = {'法文', '德語', '中文', '日語', '台語'}

# print(f'兩個人都會的語言: {employee1 & employee2}')

# print(f'兩個人總共會的語言: {employee1 | employee2}')

# print(f'只有員工1會的語言: {employee1 - employee2}')
# print(f'只有員工2會的語言: {employee2 - employee1}')

# print(f'只有一個人會的語言: {employee1 ^ employee2}')







