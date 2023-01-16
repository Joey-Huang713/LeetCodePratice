from typing import List
import numpy as np
import time
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_result=0
        tmp_value=prices[0]
        for index in range( len(prices)):
            if tmp_value<prices[index]:
                tmp_value=prices[index]
            elif prices[index]- tmp_value > max_result:
                max_result = prices[index]- tmp_value
        return max_result