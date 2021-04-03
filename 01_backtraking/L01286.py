class CombinationIterator:

  def __init__(self, characters: str, combinationLength: int):
    self.characters = characters
    self.combinationLength = combinationLength
    self.resList = []
    self.idx = 0
    for i in range(len(characters)):
      self.backtrack(characters, i, [])
    
  def backtrack(self, characters, i, res):
    res.append(characters[i])
    if(len(res) == self.combinationLength):
      self.resList.append("".join(res))
      res.pop()
      return
    for k in range(i+1, len(characters)):
      self.backtrack(characters, k, res)
    res.pop()
    
  def next(self) -> str:
    self.idx += 1
    return self.resList[self.idx - 1]

  def hasNext(self) -> bool:
    if(self.idx < len(self.resList)):
      return True
    else:
      return False

s = CombinationIterator("abc", 2)
print(s.next())
