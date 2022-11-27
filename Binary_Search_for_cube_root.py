a = float(input("Enter a number: "))

lower, upper = 0, a #先設定好lower.upper

if 0< a < 1: upper = 1 
if 0> a > -1: lower = -1
    
if a < -1:
  lower, upper = a, 0
  while round(upper,10) != round(lower,10):
    avg = (upper + lower) / 2.0
    if avg**3 >= a:
      upper = avg 
    else:
      lower = avg
          
else:
  while round(upper,10) != round(lower,10):
    avg = (upper + lower) / 2.0
    if avg**3 >= a:
      upper = avg 
    else:
      lower = avg

sol = round(upper, 5)

print('cubeRoot(', a, ') = ', sol)