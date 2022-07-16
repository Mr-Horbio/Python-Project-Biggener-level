# Python-Project-Biggener-level
project :Write a function named collatz() that has one parameter named number.
If number is even, then collatz() should print number // 2 and return this value. 
If number is odd, then collatz() should print and return 3 * number + 1.


  project code:
  
  
  def collatz(number):
 if number%2==0:
    c=number//2

    print("The number is even,")
    return c
 else:    
    print('no is odd')
    b=3*number+1
    return b 
 

print (collatz(12))



output:
The number is even 
2

  
