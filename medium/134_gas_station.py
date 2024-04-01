gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

def can_complete_circuit(gas, cost):
  if sum(gas) < sum(cost):
    return -1

  tank = 0
  start = 0
  for i in range(len(gas)):
    tank += (gas[i] - cost[i])
    if tank < 0:
      tank = 0
      start = i + 1

  return start

def main():
  print('aaa')
  print(can_complete_circuit(gas, cost))

if __name__ == '__man__':
  main()