n=int(input())
for i in range(n):
    if i==3:
        
        print(f"Execition is terminated at {i}")
        break
    print(i,end=" ")

print("continue")
for i in range(n):
    if i==3:
        print(f"Execition is pashed at {i}")
        continue
    print(i,end=" ")
