a=10
b=9
c=9
print(a+b)
print(type(a))
print(id(a))
print(("""he;+lo"""))
# print statement
import time
for i in range(5):
    print(i,end="-",flush=True)
    time.sleep(0.00009)
#pattern printing
print("hello\n world")
print("hello\t world")
print("hello \\world")
print("hello @world")
print("hello \\@ world")
print("hello /?world")

print("hello"[0])
print("hello"[-3])

print("%2s"%"hello")
print("%.2s"%"hello")
print("%5.2s"%"hello")
print("%-1.2s"%"helloworld")

#decimal integers
print("%d" %20)
print("%i" %2)
print("%5d" %2)
print("%.5d" %122222)
print("%05d" %122222)

print("%f" %10)
print("%.2f" %10)

