
def solve(k):
  cheater = -1
  correct_rate = 0.0
  for i in range(100):
    s = input()
    arr = [int(x) for x in s]
    tmp_rate = sum(arr) / len(arr)
    if(tmp_rate > correct_rate):
      cheater = i
      correct_rate = tmp_rate
  print(f"Case #{k}: {cheater}")

if __name__ == "__main__":
  t = int(input())
  p = int(input())
  for i in range(1, t+1):
    solve(i)