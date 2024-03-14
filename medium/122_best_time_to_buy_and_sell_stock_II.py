nums = [1,2,3,4,5]

def max_profit(prices):
  min_price = prices[0]
  max_profit = 0

  for i in range(len(prices)):
    if prices[i] > min_price:
      max_profit += prices[i] - min_price
    min_price = prices[i]

  return max_profit

def main():
  print(max_profit(nums))

if __name__ == '__main__':
  main()