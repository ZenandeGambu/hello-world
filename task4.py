def task4(a,b,c):
   def rect(x,y,z): 
     s = (x + y + z) / 2
     area = (s * (s - x) * (s - y) * (s - z)) ** 0.5
     return int(area)
   return rect(a, b, c)
print(task4(3, 4, 5))  # Example usage