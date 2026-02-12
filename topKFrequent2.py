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

