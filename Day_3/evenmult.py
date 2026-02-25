class Solution(object):
    def smallestEvenMultiple(self, n):
       value = n
       if value % 2 == 0:
         return value
       else:
         return 2*value