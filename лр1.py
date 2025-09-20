# 1 задача
from operator import index

a = int(1)
b = float(10.18)
sum = a + b
razn = a - b
proizv = a * b
delen = a/b
print (sum,razn,proizv,delen, type(delen))

import math
p = math.pi
r = 5
s = r**2 * p
print("Площадь круга: ", round(s,2))

# 2 задача

text = " Hello, Python! "
st = text.strip()
print(st)

print(text.replace("!", "?"))

print(text.upper())

print(st.lower())

 #3 задание

import copy
n = [7,2,5]
n.append(4)
n.insert(2, 10)
n.extend([1,1,1])
n.remove(7)
last = n.pop()
n.sort()
n.reverse()
print(n.count(2))
print(n)
print(n.index(1))
print(n.copy())
copy.deepcopy(n)
print(n)
print(n.clear())


#4 задача

t = (1, 2, 3)
try:
    t[1] = 100
except:
    print("false")
t1 = (4,5)
t2 = t + t1
print(t2)
print(t2.count(3),t2.index(4))
print(t)


# 5 задание

values = [3, 1, 3, 2, 1, 5, 2]
a = unique_values = set(values)
b = len(unique_values)
print(a,b)
other = {2, 4, 5}
print(unique_values & other)
print(unique_values | other)
print(unique_values - other )
print(other - unique_values)

# 6 задание

scores = {"Alice": 85, "Bob": 90}
scores["Charlie"] = 78
print(scores)
scores["Bob"] = 95
print(scores)
c = scores.get("Bob")
print("Балл существующего студента: " , c)
d = scores.get("Dave")
print(d) # для несуществующего студента выдает None
scores.pop("Alice")
print(scores)


# 7 задание

text = """
    Python is a powerful programming language. 
    It is used in data science, web development, automation, and many other fields!
    PYTHON is easy to learn, yet very versatile.
"""
a = text.strip()
b = a.lower()
print(b)
print(b.replace('!', '.'))
parts = text.split('.')
print(parts)
print(parts[0].strip())
print(parts[1].strip())
print(parts[2].strip())

print(parts[0].split())
print(parts[0].count("python"))
print(parts[0].startswith("python"), parts[0].endswith("language"))
print(len(parts[0]))
print(parts[0].count("a"))
print(parts[0].find("data"))
words = parts[0].split()
print('-'.join(words))
slovar = {}
for i in words:
    slovar[i] = words.count(i)
print(slovar)
word = parts[0]
import re
n = word.strip()
n = text.lower()
cleaned_text= re.sub(r'[^a-zа-яё\s]', '', n)
print(cleaned_text)
