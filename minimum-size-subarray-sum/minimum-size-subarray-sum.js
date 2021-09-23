/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
  var n = nums.length
  var solution = n + 1
  for(var i = 0; i < n; i++) {
    var sum = 0
    for(var j = i; j < n; j++) {
      sum += nums[j]
      if (sum >= target) {
        solution = Math.min(solution, j - i + 1)
        break;
      }
    }
  }
  return solution == n + 1 ? 0 : solution
}