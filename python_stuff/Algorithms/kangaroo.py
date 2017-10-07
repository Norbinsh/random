"""

Print YES if they can land on the same location at the same time; otherwise, print NO.
Note: The two kangaroos must land at the same location after making the same number of jumps.



"""
x1,v1,x2,v2 = 0,3,4,2
print("YES" if (v2 < v1) and (x2 - x1) % (v2 - v1) == 0 else "NO")
"----------------------------- x1----x2---------------------------------"
"------------------------------3mph--2mph-------------------------------" """FINISH LINE"""
"------------------------------v1----v2---------------------------------"
# Check that the speed of v2 which we want to catch up with is not greater than v1's.
# Also check that the distance % rate difference between the two is the same, otherwise they will never catch up
# If the rate is not a factor of the distance...
