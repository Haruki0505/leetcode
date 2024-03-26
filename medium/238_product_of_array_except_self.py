nums = [1,2,3,4]

def product_except_self(nums):
  nums_length = len(nums)
  prefix_products = [1] * nums_length
  suffix_products = [1] * nums_length
  answers = []

  for i in range(nums_length-1):
    prefix_products[i+1] = prefix_products[i] * nums[i]

  for i in range(nums_length-1, 0, -1):
    suffix_products[i-1] = suffix_products[i] * nums[i]

  for i in range(nums_length):
    answers.append(prefix_products[i] * suffix_products[i])

  return answers

def main():
  print(product_except_self(nums))

if __name__ == '__main__':
  main()