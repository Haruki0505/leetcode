nums = [1,2,3,4,5,6,7]
k = 3

def routate_array(nums, k):

  k = k % len(nums)

  nums[:] = reversed(nums)
  nums[:k] = reversed(nums[:k])
  nums[k:] = reversed(nums[k:])

  # nums[:] = nums[-k:] + nums[:-k]

  # return nums

  # length = len(nums)
  # result = [0] * length
  # for i in range(length):
  #   shifted_index = i + k
  #   if shifted_index < length:
  #     result[shifted_index] = nums[i]
  #   else:
  #     result[shifted_index-length] = nums[i]
  # return result

def main():
  print(routate_array(nums, k))

if __name__ == '__main__':
  main()