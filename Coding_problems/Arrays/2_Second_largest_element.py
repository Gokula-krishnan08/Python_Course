arr = [10 , 20 , 4 , 45 , 99]

first = second = -1

for num in arr:
    if first < num:
        second = first 
        first = num
    elif second < num and num != first:
        second = num 

print(second)