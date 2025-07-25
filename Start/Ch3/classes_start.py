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