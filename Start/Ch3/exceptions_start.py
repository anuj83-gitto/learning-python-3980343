# LinkedIn Learning Python course by Joe Marini
# Example file for working with Exceptions
#

# Errors can happen in programs, and we need a clean way to handle them
# This code will cause an error because you can't divide by zero:
#print(5 / 0)
# Exceptions provide a way of catching errors and then handling them in 
# a separate section of the code to group them together

def _divide_numbers(_idividend=24,_idivisor=8):
  print("This function will divide two numbers.")
  _dividend = _idividend if _idividend is not None else int(input("Enter the dividend: "))
  _divisor = _idivisor if _idivisor is not None else int(input("Enter the divisor: "))
  try:
      result = _dividend / _divisor
      print(f"The result is: {result}")
  except ZeroDivisionError as e:
      print("You can't divide by zero!")
  except ValueError as e:
      print("You didn't give me a valid number!")
      print(e)
  finally:
      print("Lets try again next time!")
# You can also catch specific exceptions

#_divide_numbers(145,None)
_divide_numbers(None,14)
#_divide_numbers(145,0)