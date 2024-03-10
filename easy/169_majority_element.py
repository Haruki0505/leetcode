nums = [3,2,3]

def majority_element(nums):
  dict = {}
  for n in nums:
    if n in dict:
      dict[n] = 0
    dict[n] += 1
    if dict[n] > len(nums) // 2:
        return n

def main():
  majority_element(nums)

if __name__ == '__main__':
  main()