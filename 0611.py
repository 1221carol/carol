# help ('keywords')

#print (5 + 3)
#print (5 - 3)
#print (5 * 3)
#print (5 / 3)
#print (5 % 3)
#print (5 // 3)
#print (5 ** 3)

#print ('abc + def')
#print ('abc' * 3)

# score = int(input('請輸入你的分數: '))

# # 基本
# if score >= 60:
#    print('及格')
# else:
#    print('不及格')

# # 進階
# score = int(input('請輸入你的分數: '))
# print('及格') if score >=60 else print('不及格')

# 專業
#print('及格' if int(input('請輸入你的分數: ')) >=60 else '不及格')

# 引用隨機數模組
# import random

# # 產生1~5之間的隨機整數
# answer = random.randint(1, 5)
# print(f'答案: {answer}')

# # 讓使用者輸入數字(資料必須轉型成int)
# user = int(input('請猜一個1~5之間的數字: '))

# if answer == user:
#     print('猜對了')
# else:
#     print('猜錯了')

# print(0.6 / 2)
# print(0.1 * 3)  # IEEE-754

# from decimal import Decimal

# a = Decimal('0.1')
# print(a * 3)

with open('test.txt', encoding='utf-8') as file:
    data = file.readline()

    print(data)

# 用cp950編碼寫入檔案
with open('test.txt', 'w') as file:
    file.write('你好')