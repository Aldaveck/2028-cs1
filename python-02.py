#!/usr/bin/python3

## Aleck David Fajardo: Pisay CLC CS1 / 20230424

# Aleck David Fajardo  Q4      04/24/2023
# 7 - Sapphire        FA1      Ms. Jona Tibay

total = 0
count = 1

while count <= 10:
    num = float(input(f"Enter n{count}: "))
    total += num
    count += 1

average = total / 10

print(f"\nTotal: {total}")
print(f"Average: {average}")
