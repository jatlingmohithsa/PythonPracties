x=int(input())
y=int(input())

y*=12
profit=y-x
if profit<0:
  print("LOSS: %.2f"%profit)
else:
  print("PROFIT: %.2f"%profit)
  