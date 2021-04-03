chosen = []
n = 2
def calc(x):
  if (x == n+1):
    if len(chosen) != 0:
      print(chosen)
    return
  # 不选
  calc(x + 1)
  # 选
  chosen.append(x)
  calc(x + 1)
  # 还原现场
  chosen.pop()
  
calc(1)