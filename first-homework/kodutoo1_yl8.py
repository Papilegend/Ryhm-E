class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        juveelid= Counter(jewels)
        kivid = Counter(stones)
        
        kokku=0
        for i in range(len(stones)):
            if stones[i] in jewels:
                kokku = kokku + 1
            
        return kokku
        
