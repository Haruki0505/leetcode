# prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]

def calc_max_profix(prices):
  min_price = prices[0]
  max_profit = 0

  for price in prices[1:]:
    if price < min_price:
      min_price = price

    if price - min_price > max_profit:
      max_profit = price - min_price

  return max_profit

  # max_price = 0
  # for i in range(len(prices)):
  #   for j in range(i+1, len(prices)):
  #     if prices[j] - prices[i] > max_price:
  #       max_price = prices[j] - prices[i]

  # return max_price

def main():
  print(calc_max_profix(prices))

if __name__ == '__main__':
  main()