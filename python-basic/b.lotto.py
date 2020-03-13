# %%
def test():
    print("test message.")

def add(a, b):
    return a + b

test()
print(add(3,4))

# %%
from random import randint

print(randint(1, 45))

# %%
def select_basic_numbers():
    """
    로또 기본 규칙에 따라 6개 숫자 생성
    """
    numbers = [0, 0, 0, 0, 0, 0]
    idx = 0
    while idx < 6:
        numbers[idx] = randint(1, 45)

        for idx2 in range(idx):
            if numbers[idx] == numbers[idx2]:
                idx -= 1
                break

        idx += 1

    numbers.sort()
    return numbers

# %%
def check_mean(numbers):
    """
    평균이 20~26 일 때 True 반환, 아니면 False
    """
    sum = 0
    for number in numbers:
        sum += number

    mean = sum / len(numbers)
    print(mean)

    return mean >= 20 and mean <= 26

# %%
while True:
    numbers = select_basic_numbers()
    valid = check_mean(numbers)

    if valid:
        break

print(numbers)