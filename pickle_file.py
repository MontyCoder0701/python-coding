import pickle

data = {
    "목표1": "매일 팔굽혀펴기",
    "목표2": "매일 코딩공부하기"
}

# file = open("data.pickle", "wb")
# pickle.dump(data, file)
# file.close()

file = open("data.pickle", "rb")
data = pickle.load(file)
print(data)
file.close()

with open("data.txt", "r", encoding="utf8") as file:
    data = file.read()
    print(data)
