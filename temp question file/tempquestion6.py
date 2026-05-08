ext = input("Enter string: ")
freq = {}

for char in ext:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(freq)