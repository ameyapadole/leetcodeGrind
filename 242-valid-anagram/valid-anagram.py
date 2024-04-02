class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count = defaultdict(int)
        
        for x in s:
            count[x] += 1
        for x in t:
            count[x] -= 1

        for val in count.values():
            if val!= 0:
                return False
        return True
     
        # time = O(n)
        # space = O(1) The Size of the table stays constant
        

        """
        Idea is to use a counter, i
        f the same char is encountered the value of count will be zero. 
        so at the end the val in count has to be zero. if not return False"""