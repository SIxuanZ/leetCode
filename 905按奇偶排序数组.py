class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        o_list = []
        ji_list = []
        return_list = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                o_list.append(A[i])
            else :
                ji_list.append(A[i])
        return_list = o_list + ji_list
        return return_list
