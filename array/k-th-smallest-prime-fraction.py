class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:

        if len(arr) == 2:
            return [arr[0], arr[1]]

        store = []

        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                store.append((arr[i]/arr[j], [arr[i],arr[j]]))

        store.sort()        
        return store[k-1][1]