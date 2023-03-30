class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewels_set = set(jewels)
        count = 0
        for stone in stones:
            if stone in jewels_set:
                count += 1
        return count
