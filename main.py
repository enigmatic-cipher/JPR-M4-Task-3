"""
Given a string as input, if the length of the string is even print the first half and the latter half of the string. If the length of the string is odd, print the first half, middle char and the latter half of the string. You have to use substring to solve this problem and cannot use for loop and charAt.
Input-> "Trisect"
Output-> First Half:Tri Middle char:s Second Half:ect
"""

st = "Trisect"
ln = len(st)
if (ln%2==0):
  print(st[0:ln//2])
  print(st[ln//2:ln])
elif (ln%2!=0):
  print(st[0:(ln//2)])
  print(st[(ln//2)-((ln//2)-1)])
  print(st[(ln//2)+1:ln])
