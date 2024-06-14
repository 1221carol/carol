#  99乘分表   
# for a in range(1, 10):    
#      for b in range(1, 10):
#          c = a * b
#          print('%d x %d = %d' %(a, b, c))
#      print('\n')

    
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for b in a[1::2]:
#     print(b)

# total = 0
# for b in a:
#     total += b
# print(f'總合為: {total}')


# a_v2 = list(range(1, 10))
# print(a_v2)

# a_v2 = list(range(20, 3, -3))
# print(a_v2)

# a_v2 = list(range(-1, -6, -2))
# print(a_v2)

# a_v2 = list(range(3, 10, -1))
# print(a_v2)

# a_v2 = list(range(10, 60, 10))
# print(a_v2)

# # 一般寫法
# new_list = []
# for b in a:
#     new_list.append(b + 10)
# print(new_list)

# # for comprehension寫法
# new_list = [b + 10 for b in a]
# print(new_list)


# a = [32, 54, 67, 88]

# new_list = []
# for b in a:
#     new_list += [b // 10]
# print(new_list)

# print([b // 10 for b in a])


# user_input = []

# for e in range(10000):
#     score = input('請輸入成績(quit=離開): ')

#     if score == 'quit':
#         break
#     else:
#         user_input.append(int(score))

# print(user_input)

# # 處理成績
# new_list = []

# for s in user_input:
#     if s < 60:
#         new_list.append(s + 10)
#     else:
#         new_list.append(s)

# print(new_list)

# # 使用單行if
# # new_list = []
# # for s in user_input:
# #     new_list.append(s + 10 if s < 60 else s)

# new_list = [s + 10 if s < 60 else s for s in user_input]

# print(new_list)


# a = [9, 58, 63, 100]

# b = []                         基礎寫法
# for c in a:
#     if c >= 60:
#         b.append(c)
# print(b)

# b = [c for c in a if c >= 60]   一行的寫法

# print(b)


# attendee = ['aaron', 'andy', 'apple', 'aaron', 'abner']

# name = input('請輸入要查找的人名: ')
# # 通用寫法
# isAttend = False  # 有沒有參加

# for n in attendee:
#     if n == name:
#         isAttend = True
#         break

# if isAttend:
#     print('有參加')
# else:
#     print('無參加')

# # 通用寫法二
# new_list = []
# for n in attendee:
#     if n == name:
#         new_list.append(n)

# # if len(new_list) > 0:
# if new_list:
#     print('有參加')
# else:
#     print('無參加')

# # 張大哥寫法
# if [n for n in attendee if n == name]:
#     print('有參加')
# else:
#     print('無參加')

# # for-else寫法
# for n in attendee:
#     if n == name:
#         print('有參加')
#         break
# else:
#     print('無參加')

# # in寫法
# if name in attendee:
#     print('有參加')
# else:
#     print('無參加')

# if name in 'My name is aaron':
#     print('有出現')
# else:
#     print('無出現')
    
# 聖誕樹   
# def christmas_tree(rows):
#     for i in range(rows):
#         print(' ' * (rows - i - 1) + '*' * (2 * i + 1))
#     print(' ' * (rows - 1) + '|')

# christmas_tree(5)


# user = int(input('請輸入數字: '))

# for j in range(user):
#     for i in range(j+1):
#         print('*', end='')
#     print()
    
# # 另一種寫法:

# user = int(input('請輸入數字: '))

# data = []
# for i in range(user):
#     data += ['*']
#     print(''.join(data))


