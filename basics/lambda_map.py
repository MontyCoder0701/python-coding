# 람다 연습
print((lambda a: a-1)(10))
print((lambda a: True if a > 0 else False)(10))

# map 연습
print(list(map(int, ["3", "4", "5", "6"])))

items = [" 로지텍 ", " 키보드 "]

# for i in range(len(items)):
#     items[i] = items[i].strip()

# def strip_all(x):
#     return x.strip()
# items = list(map(strip_all, items))

items = list(map(lambda x: x.strip(), items))
print(items)

# filter 연습

# def func(x):
#     return x < 0

# print(list(filter(func, [-3, -2, 0, 5, 7])))

animals = ["cat", "tiger", "dog", "bird", "monkey"]


# def word_check(x):
#     return len(x) <= 3


# result = list(filter(word_check, animals))

result = list(filter(lambda x: len(x) <= 3, animals))
print(result)
