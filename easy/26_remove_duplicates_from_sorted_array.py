nums = [0,0,1,1,1,2,2,3,3,4]

def remove_duplicates_from_sorted_array(nums):
  k = 0
  for i in range(len(nums)):
    if nums[i] != nums[k]:
      k += 1
      nums[k] = nums[i]

  return k + 1

def main():
  print(remove_duplicates_from_sorted_array(nums))

if __name__ == '__main__':
  main()