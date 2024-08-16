class SparseVector:
    def __init__(self, nums: List[int]):
        self.k = []
        self.v = {}
        for i,n in enumerate(nums):
            if n != 0:
                self.k.append(i)
                self.v[i] = n
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        cur_sum = 0
        for i in self.k:
            if i in vec.v:
                cur_sum += self.v[i] * vec.v[i]

        return cur_sum
