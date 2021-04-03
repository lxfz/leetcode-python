
def reverse(arr, i, j):
  while(i < j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    i += 1
    j -= 1

def calCost(arr):
  ans = 0
  for i in range(len(arr) - 1):
    min_pos = i
    for j in range(i, len(arr)):
      if arr[j] < arr[min_pos]:
        min_pos = j
    reverse(arr, i, min_pos)
    ans = ans + min_pos - i + 1
  return ans



if __name__ == "__main__":
  t = int(input())
  for i in range(1, t+1):
    n = int(input())
    arr = [int(s) for s in input().split(" ")]
    ans = calCost(arr)
    print(f"Case #{i}: {ans}")