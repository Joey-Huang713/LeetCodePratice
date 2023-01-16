class Solution:
    
    def isValid(self, s: str) -> bool:
        begin=['(','{','[']
        end = [')','}',']' ]
        for i,ch in enumerate(begin):
            b_count=s.count(ch)
            e_count=s.count(end[i])
            if b_count!=e_count:
                return False
            if b_count == 0:
                continue
            elif b_count==1 :
                b_inx=s.find(ch)
                e_inx=s.find(end[i])
                
                if (e_inx-b_inx)%3==2 :
                    return False
            elif b_count>1:
                b_index = -1
                e_index =-1
                b_indexs=[]
                e_indexs=[]
                for _ in range(b_count):
                    b_index=s.find(ch,b_index+1)
                    e_index=s.find(end[i],e_index+1)
                    b_indexs.append(b_index)
                    e_indexs.append(e_index)
                b_indexs_np=np.asanyarray(b_indexs)
                e_indexs_np=np.asanyarray(e_indexs)
                for i in range(b_count):
                    dis = e_indexs_np[i]-b_indexs_np[b_indexs_np<e_indexs_np[i]][-1]
                    if dis%3==2:
                        return False            
        return True

import numpy as np  
# a=[1,2,3]
# a_np=np.asanyarray(a)
# print(a_np[a_np<3])
S=Solution()
s="[({])}"
# print(S.isValid(s))

# print(s.find('{',2))
t ={'1':'t1','3':'t2'}
a=[]
print(len(a))