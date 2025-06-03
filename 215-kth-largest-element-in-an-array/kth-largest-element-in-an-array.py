class Solution:
    def findKthLargest(self, A, k):

        q = []

        for a in A:

            heapq.heappush(q, a)

            if len(q) > k:
                heapq.heappop(q)


        return heapq.heappop(q)
        