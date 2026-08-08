#Remove Duplicates from list

numbers=[10,30,30,46,67,66,66,78,65,66]
unique=[]
for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)