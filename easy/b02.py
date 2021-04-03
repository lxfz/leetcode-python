class Solution:
  def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
    s1 = sentence1.split(" ")
    s2 = sentence2.split(" ")
    if (len(s2) > len(s1)):
      tmp = s1
      s1 = s2
      s2 = tmp
    res = True
    # head
    i = 0
    for word in s2:
      if(word != s1[i]):
        res = False
        break
      i+=1
    if res:
      return True
    
    # tail
    i = len(s1)-1
    j = len(s2)-1
    res = True
    while(j>=0):
      if(s1[i] != s2[j]):
        res = False
        break
      i-=1
      j-=1
    if res:
      return True
    
    #both
    i = 0
    j = len(s2)-1
    while(i<len(s2)):
      if(s1[i] == s2[i]):
        i+=1
      else:
        break
    while(j>=0):
      if(s1[len(s1)-len(s2)+j] == s2[j]):
        j-=1
      else:
        break
    if(j+1 != i):
      return False
    else:
      return True

sl = Solution()
sentence1 = "My name is Haley"
sentence2 = "My Haley"
print(sl.areSentencesSimilar(sentence1, sentence2))