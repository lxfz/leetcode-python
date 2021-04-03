min_cost = float("inf")
X = 0
Y = 0

def search(s, i, cost):
  global min_cost
  global X
  global Y
  if(len(s) == 1):
    min_cost = 0
    return
  if(len(s)-1 == i):
    if(s[i] != "?"):
      if(s[i-1:] == "CJ"):
        cost += X
      elif(s[i-1:] == "JC"):
        cost += Y
    if(min_cost > cost):
      min_cost = cost
  else:
    if(s[i] != "?"):
      if(s[i-1:i+1] == "CJ"):
        cost += X
      elif(s[i-1:i+1] == "JC"):
        cost += Y
      if(cost < min_cost):
        search(s, i+1, cost)
    else:
      temp_cost = cost
      sc1 = list(s)
      sc1[i] = "C"
      sc1 = "".join(sc1)
      if(i > 0):
        if(sc1[i-1:i+1] == "CJ"):
          cost += X
        elif(sc1[i-1:i+1] == "JC"):
          cost += Y
      if(cost < min_cost):
        search(sc1, i+1, cost)
      
      cost = temp_cost
      sc1 = list(s)
      sc1[i] = "J"
      sc1 = "".join(sc1)
      if(i>0):
        if(sc1[i-1:i+1] == "CJ"):
          cost += X
        elif(sc1[i-1:i+1] == "JC"):
          cost += Y
      if(cost < min_cost):
        search(sc1, i+1, cost)

if __name__ == "__main__":
  t = int(input())
  for i in range(1, t+1):
    arr = input().split(" ")
    X = int(arr[0])
    Y = int(arr[1])
    S = arr[2]
    search(S, 0, 0)
    print(f"Case #{i}: {min_cost}")
    min_cost = float("inf")
    