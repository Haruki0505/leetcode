// const twoSum = (nums: number[], target: number): number[] => {
//   const result = []
//   for (let i = 0; i < nums.length; i++) {
//     for (let j = i + 1; j < nums.length; j++) {
//       const sum = nums[i] + nums[j]
//       if (sum === target) {
//         result.push(i);
//         result.push(j);
//         return result;
//       }
//     }
//   }
//   return [-1, -1];
// }

const twoSum = (nums: number[], target: number): number[] => {
  const map = new Map<number, number>()

  for (let i = 0; i < nums.length; i++) {
    const sub = target - nums[i];
    if (map.has(sub)) {
      return [i, map.get(sub)];
    }
    map.set(nums[i], i);
  }

  return [-1, -1];
}

// [2,7,11,15]
// 9
// [3,2,4]
// 6
// [3,3]
// 6