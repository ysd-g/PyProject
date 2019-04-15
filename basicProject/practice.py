from statistics import mean, median, variance, stdev

name = "Endo"
age = 21
weight = 68.93

print("name:{0:<10s} age:{1:<10d} weight:{2:<10.3f}".format(name, age, weight))
                                                #name:Endo       age:21         weight:68.930    

print("name:{0:>10s} age:{1:10d} weight:{2:10.1f}".format(name, age, weight))
                                                #name:      Endo age:        21 weight:      68.9



for i in range(0, 10):
    if i % 2 == 0:
        continue
    print(i)
print("finish")



class User:
    count = 0

    def __init__(self, name, age):
        User.count += 1
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, {0}".format(self.name))

usr1 = User("Yoshida Kensuke", 24)
usr2 = User("Tanaka", 18)

usr2.greet()

#--------------------------------------------------------------

def diff(scores, ave):
    diff = []
    for score in scores:
        diff.append(score - ave)
    return diff

def squared_diff(diff):
    squared_diff = []
    for num in diff:
        squared_diff.append(num*num)
    return squared_diff

def Variance(squared_diff):
    sq_sum = sum(squared_diff)
    vari = sq_sum / len(squared_diff)
    return vari

scores = [10, 30, 50, 20, 20, 60, 50, 45, 30]
scores.append(20)


ave = mean(scores)

diff = diff(scores, ave)

squared_diff = squared_diff(diff)

vari = Variance(squared_diff)

std = vari**0.5
print(std)


#--------------------------------------------------------------
old = 49

if old % 3 == 0 and old % 2 == 0:
    print("6の倍数")
elif old//25 >= 1 and old//25 < 2:
    print("25以上の数字で50より小さい")

