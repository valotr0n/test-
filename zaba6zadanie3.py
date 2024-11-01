array = [-1,2,-3,4,-4,-5,-9,10,-6,5,4]
count = 0
for num in array:
    if num < 0:
        count += 1
if count < len(array)/2:
    array[-1] = -array[-1]
print(f'Количество отрицательных чисел: {count}')
print(f'Новый массив: {array}')