nums = [3,2,2,3]
val = 3

def remove_elements(nums, val):
  k = 0
  for reader in range(len(nums)):
    if nums[reader] != val:
      nums[k] = nums[reader]
      k += 1

  return k

def main():
  k = remove_elements(nums, val)

  print(k)

if __name__ == '__main__':
  main()