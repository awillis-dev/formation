// Group 0s and 1s

// Given an array of 0s and 1s, what is the minimum number of moves needed to group all 0s on one side and 1s on the other side. A "move" is a swap between any adjacent positions.

// Examples

// [0, 1] => 0, no swaps are needed since they are already grouped.
// [0, 1, 0] => 1, swap 1 with either 0 to group them.
// [1, 0, 1, 1, 0] => 2, swap 0 with 1 then swap it again with the next 1.
// [1, 1, 1, 0, 0]
// Function Signature

// function minSwaps(input: Array): number

// [1, 0, 1, 1, 0]  = 4 / 2
//.    l
//           r
function minSwaps(input) {
  return Math.min(helper(input, 0), helper(input, 1))
}

function helper(input, lookingFor) {
  let currIdx = 0 // incremented every time
  let searchIdx = 0 // incremented only when we find number we are lookingFor
  let swapCount = 0

  while (currIdx < input.length) {
    const curr = input[currIdx]

    if (curr === lookingFor) {
      swapCount += currIdx - searchIdx
      searchIdx += 1
    }

    currIdx++

  }

  return swapCount;

}


let arr1 = [1, 0, 1, 1, 0]
let arr2 = [0,1]
let arr3 = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0]
let arr4 = [1,0,1,1,1,1,1,1,1,1,0,0]
let arr5 = [1,0,1,0,1,0]
console.log(minSwaps(arr1)) // 2
console.log(minSwaps(arr2)) // 0
console.log(minSwaps(arr3)) // 10
console.log(minSwaps(arr4)) // 8
console.log(minSwaps(arr5)) // 3
