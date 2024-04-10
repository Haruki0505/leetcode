s = 'III'

def roman_to_integer(s):
  roman_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
  }

  result = 0
  for i in range(0, len(s) - 1):
    if roman_dict[s[i]] < roman_dict[s[i+1]]:
        result -= roman_dict[s[i]]
    else:
        result += roman_dict[s[i]]

  return result

def main():
  print(roman_to_integer(s))

if __name__ == '__main__':
  main()