num = 1994

def int_to_roman(num):
  num_dict = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M"
  }

  if num in num_dict:
    return num_dict[num]

  result = ''

  for i in reversed(list(num_dict)):
    if num // i > 0:
      result += num_dict[i] * (num // i)
      num = num % i

  return result

def main():
  print(int_to_roman(num))

if __name__ == '__main__':
  main()