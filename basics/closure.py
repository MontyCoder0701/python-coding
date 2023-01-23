# def outer(name):
#     def inner():
#         print(name, "님 안녕하세요")
#     return inner


# func = outer("startcoding")
# func()


def greeting(name, age, gender):
    def inner():
        print(name, "님 안녕하세요")
        print("나이:", age)
        print("성별:", gender)
    return inner


closure = greeting("나미", 18, "female")
# closure()
# print(closure.__closure__[0].cell_contents)

for i in closure.__closure__:
    print(i.cell_contents)
