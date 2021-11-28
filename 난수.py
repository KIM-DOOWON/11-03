import random

l = set()


while len(l) < 10:

  l.add(random.randint(1,100))

# 2. 단, 파이썬의 max(), min()함수를 사용하지 말고 작성하시오.
max = 0
min = 101

for i in l:

  if max < i:
    max = i
  if min > i:
    min = i

  
print('max',max)
print('min',min)
