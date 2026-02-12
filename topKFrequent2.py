#347. Top K Frequent Elements
import heapq
from collections import Counter
from typing import List

class Solution(object):
      def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
            counter = Counter(nums)
            heap = []
            for key, val in counter.items():
                  if len(heap) < k:
                      heapq.heappush(heap, (val, key))
                  else:
                      heapq.heappushpop(heap, (val, key))

            return [h[1] for h in heap]

# Time: O(n log k), Space: O(k)

if __name__ == "__main__":
    sol = Solution()
