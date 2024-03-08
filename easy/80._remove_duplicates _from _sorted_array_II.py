nums = [1,1,1,2,2,3]

def remove_duplicates_from_sorted_array(nums):
    j = 1
    for i in range(1, len(nums)):
        if j == 1 or nums[i] != nums[j - 2]:
            nums[j] = nums[i]
            j += 1
    return j

def main():
  print(remove_duplicates_from_sorted_array(nums))

if __name__ == '__main__':
  main()