m=int(input())
am=float(input())
days=int(input())
if m<=12:
    if m in {4,5,6,7,11,12}:
        am=am*1.2*days
        print("%.2f"%am)
    else :
        print("%.2f"(am*days))
else:
    print("invalid Mounth")