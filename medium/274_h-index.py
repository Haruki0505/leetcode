citations = [3,0,6,1,5]

def h_index(citations):
  citations.sort(reverse=True)
  h = 0

  for i in range(len(citations)):
    if citations[i] >= i + 1:
      h += 1

  return h

def main():
  print(h_index(citations))

if __name__ == '__main__':
  main()