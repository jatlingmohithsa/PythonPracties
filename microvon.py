items=int(input())
heat_time=float(input())
if items<=2:
    print("%.2f"%(items+(heat_time*1.5)))
elif items==3:
    print("%.2f"%(heat_time*2))
else:
    print("Number of items is more")

"""A microwave oven manufacturer recommends that when heating two items, 
add 50% to the heating time, and when heating three items double the heating
 time. Heating more than three items at once is not recommended.
 Write a python program to find out the recommended heating time. 
 Input format: The first input containing an integer which denotes
 the number of items The second input containing the floating point number
   which denotes the single item heating time. Output format: Print the
     recommended heating time in floating point with 2 decimal places. If
       the number of items is more than three, print "Number of items is 
more" Refer the sample output for formatting


Input (stdin)

2
5.0

Output (stdout)

7.50

Input (stdin)

3
6.5

Output (stdout)

13.00"""