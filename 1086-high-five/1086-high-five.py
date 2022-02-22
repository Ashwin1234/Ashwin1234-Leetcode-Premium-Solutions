class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        dict1 = {}
        res = []
        for ele in items:
            if ele[0] in dict1:
                dict1[ele[0]].append(ele[1])
            else:
                dict1[ele[0]] = [ele[1]]
       
        for key,item in dict1.items():
            item = sorted(item,reverse = True)
            
            avg = int(sum(item[:5])/5)
            res.append([key,avg])
        return sorted(res)
        
        
        