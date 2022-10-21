"""
User will enter a floating point number let say 238.915. Your task
is to find out the interger portion before the point in this case
238 and then check if that integer portion is an even number or not?
"""

x = float(input("Enter a real number: "))
y = round(x) 
if x > 0: 
    if y > x:
        intPortion = y - 1
    else:
        intPortin = y 
else:
    if y < x:
        intPortion = y + 1
    else:
        intPortion = y 
if intPortion % 2 == 0:
    print("Even")
else:
    print("Odd")              
      
      
        
          
