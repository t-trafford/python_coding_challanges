# dict = {0: 10, 1: 11, 2: 12}
#
# for key,value in dict.items():
#     # print(key, value)

s="abc"

for i, let in enumerate(s):
    # print(i, let)
    print("===========")
    print(s[0:0])


a = set()

for i in range(len(s)):
    a.add(s[i])
print(a)

a.remove('a')
print(a)


animal = ['cat', 'dog', 'rabbit']

# an element is added
animal.append(min(1,2))

print(animal)