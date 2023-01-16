
from typing import List


class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        
        founded = False
        str_count = words.count(target)
        if str_count:         
            n=len(words)
            i=0
            while not founded :
                
                if words[(startIndex+i)%n] == target or words[(startIndex-i)%n] == target:
                    founded = True
                    return i
                i+=1
        else :
            return -1

if __name__ == "__main__" :
    s= Solution()
    words = ["a","b","c" ]
    i=s.closetTarget(words=words,target="a",startIndex=2)
    print(i)
