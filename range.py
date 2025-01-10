
x=int(input('enter a value of x'))
y=int(input('enter a value of y'))
z=int(input('enter a value of z'))
largest = 0
def max_of_three(x,y,z):
   if x>=y and x>=z:
      largest=x
   elif y>=x and y>=z:
      lagest=y
   else:
      largest=z
   print(largest)
   return largest
max_of_three(x,y,z)
print(max_of_three(x,y,z))
print("largest number among three numbers is ", largest)


'''def square(x):
    print( x*x)
    return x*x
    print( x*x)
print("hello",square(4))
'''
