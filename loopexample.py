print("Example of a for loop:")
for i in range(1, 6):
    print("Counting:", i)
print("-" * 30)

print("Example of a while loop:")
count = 1
while count <= 5:
    print("Counting:", count)
    count += 1
print("-" * 30)

print("Example of a nested loop (multiplication table):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("--- End of row", i)
print("-" * 30)

