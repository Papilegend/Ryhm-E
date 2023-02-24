class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        arvud = [str(digit) for digit in digits]
        arvud2 = "".join(arvud)
        arvkokku = int(arvud2) + 1
        return [int(i) for i in str(arvkokku)]
""" see norm aga github/leetcode ei indentinud su koodi niiet ma lisasin ;) """
