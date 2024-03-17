nums = [3,2,1,0,4]

def can_jump(nums):
  reachable = 0
  for i in range(len(nums)):
    if reachable >= len(nums) - 1:
      return True
    if i > reachable:
      return False
    reachable = max(reachable, i + nums[i])

def main():
  print(can_jump(nums))

if __name__ == '__main__':
  main()