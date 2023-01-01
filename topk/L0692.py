import heapq
from typing import List
import collections

class Item:
    def __init__(self, word, freq) -> None:
        self.word = word
        self.freq = freq
        
    def __lt__(self, next):
        if self.freq == next.freq:
            return self.word > next.word
        
        return self.freq < next.freq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        w2f = collections.Counter(words)
        pq = []
        
        for word, freq in w2f.items():
            item = Item(word, freq)
            heapq.heappush(pq, item)
            if(len(pq) > k):
                heapq.heappop(pq)
        return [heapq.heappop(pq).word for i in range(len(pq))][::-1]        


if __name__ == "__main__":
    s = Solution()
    words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
    k = 4
    print(s.topKFrequent(words, k))