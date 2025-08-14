
n=int(input())
#       *   i+j>=n+1
#     * *
#   * * *
# * * * *
print("===========")
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i+j>=n+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")

# * * * *   i+j<=n+1
# * * *
# * *
# *
print("===========")
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i+j<=n+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")

# *         i>=j
# * *
# * * *
# * * * *
print("===========")
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i>=j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")

# * * * *       i<=j
#   * * *
#     * *
#       *
print("===========")
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i<=j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")