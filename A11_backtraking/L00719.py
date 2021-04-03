from typing import List

class Solution:
  def __init__(self):
    super().__init__()
    self.resList = []
    
  def dfs(self, i, graph, res):
    res.append(i)
    if i == len(graph)-1:
      self.resList.append(res.copy())
      res.pop()
      return
    for node in graph[i]:
      self.dfs(node, graph, res)
    res.pop()  
    
  def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    self.dfs(0, graph, [])
    return self.resList    
  
s = Solution()
graph = [[4,3,1],[3,2,4],[3],[4],[]]
print(s.allPathsSourceTarget(graph))