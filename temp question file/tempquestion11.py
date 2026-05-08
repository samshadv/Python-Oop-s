f = open("info.txt", "w")
f.write("Name : Samshad\nRoll No: 10")
f.close()

f = open("info.txt", "r")
print(f.read())
f.close
