count = 0
n = "tamrin_01f.txt"
f1 = open(n,"r")
x = f1.readlines()
for i in x:
    for j in i:
        if(ord(j) == 32 or ord(j) == 10):
            continue
        else:
            count += 1
f1.close()
print(f"count : {count}")