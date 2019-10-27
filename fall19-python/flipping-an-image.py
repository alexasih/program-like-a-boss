class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        for row in A:
            if len(row)%2==1:
                for i in range(len(row)//2 + 1):
                    row[i], row[len(row)-1-i]= row[len(row)-1-i] ^ 1, row[i] ^ 1
            elif len(row)%2==0:
                for i in range(len(row)//2):
                    row[i], row[len(row)-1-i]= row[len(row)-1-i] ^ 1, row[i] ^ 1
        return A
                
        
