# LinkedIn Learning Python course by Joe Marini
# Example file for using built-in functions
#

mystring = "The quick, brown fox jumped over the lazy dog!"
mynumbers = [1,3,5,6,9,12,14,17,20,30]

# the len() function calculates the length of a sequence


# the max() and min() functions will find the largest and smallest value in a sequence


# the str() function will return a string version of an object
prefix = "result: "
result = 5


# range(start, stop, step) will create a range of numbers 
# You can use ranges along with loops 


# the print function itself is pretty flexible - you can embed variables directly in it
greeting = "Hello!"
count = 10
# LinkedIn Learning Python course by Joe Marini
# Example file for working with classes
#
def _findLongestString(_testStrings):
  longestString="";
  for _string in _testStrings:
    if len(_string) > len(longestString):
      longestString = _string
  return longestString
  
longestString = _findLongestString(["Hello World!",
    "And how can this be? For he is the Kwisatz Haderach!",
    "Four score and seven years ago",
    "Life moves pretty fast. If  you could miss it."])

print (f"The longest string is: {longestString}")