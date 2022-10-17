class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        dict1 = {}
        char = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        for ele in char:
            dict1[ele] = 0
        for ele in sentence:
            if ele in dict1:
                dict1[ele] = dict1[ele] + 1
            else:
                dict1[ele] = 1
        for key,value in dict1.items():
            if value == 0:
                return False
        return True
        