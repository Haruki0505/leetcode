const sortedSquares = (nums: number[]): number[] => nums.map(num => num ** 2).sort((a, b) => a - b);
