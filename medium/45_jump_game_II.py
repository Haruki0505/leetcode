nums = [2,3,1,1,4]

def jump(nums):
  reachable = 0
  end = 0
  count = 0

  for i in range(len(nums)):
    reachable = max(reachable, i + nums[i])

    if reachable >= len(nums) - 1:
      count += 1
      break

    if i == end:
      count += 1
      end = reachable

  return count

def main():
  print(jump(nums))

if __name__ == '__main__':
  main()