#%%
print('Hello, Python with VS Code !!!!!')

a = 456 *123
print('456 * 123 = %d' % a)

# %%
print('test')
if True:
    print('test2')

# %%
print('test3')

#%%
print([1, 2, 3] * 3)
print("*" * 10)

# %%
person = { 'no': 1, 
           'name': 'John Doe', 
           'email': 'johndoe@example.com', 
           'phone': '01098445135' }

# %%
for key in person.keys():
    print(key)

for value in person.values():
    print(value)

for key in person.keys():
    print("{0} : {1}".format(key, person[key]))

for key, value in person.items(): # dict.items() -> (key, value) 목록 반환
    print("{0} # {1}".format(key, value))
# %%
from random import randint

numbers = []
for _ in range(30):
    numbers.append(randint(100, 999))

print(numbers)

# %%
numbers2 = []
for number in numbers:
    if number % 3 == 0:
        numbers2.append(number)
print(numbers2)

# %%
numbers2 = [ (number * 100) for number in numbers if number % 3 == 0]
print(numbers2)

# %%
if True:
    pass

print("passed")

# %%
def sum_and_mul(a, b):
    sumx = a + b
    mulx = a * b
    return sumx, mulx

# %%
result = sum_and_mul(10, 20)
print(result)
sumr, mulr = sum_and_mul(100, 200)
print(sumr, mulr)

# %%
class Person:
    """
    이 문자열은 자바의 문서주석과 같은 효과를 만듭니다.
    """
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_string(self):
        return "[{0}][{1}][{2}]".format(self.name, self.phone, self.email)

# %%
person = Person('John', '010-1234-1234', 'john@mail.com')
print(person.to_string())

# %%
from com.example import my_module

print(my_module.sum(20, 30))