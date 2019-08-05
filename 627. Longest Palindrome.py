
https://www.jiuzhang.com/solution/longest-palindrome/

Question: 
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built 
with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Example
Example 1:

Input : s = "abccccdd"
Output : 7
Explanation :
One longest palindrome that can be built is "dccaccd", whose length is `7`.

https://leetcode.com/problems/two-sum/

// 思路：暴力解法，对每个数都遍历数组后面的所有数
// 出现的问题：时间复杂度太高，为O(n^2)


// 优化思路：One-pass HashMap
//         HashMap中key为nums数组每个数【被target减去后的剩下的数】，value为这个数在nums数组的位置。
//         遍历nums数组，先判断HashMap中是否存在nums[i]，如果有，那么说明和nums[i]相加为target的数在前面已经出现过，
//         因此返回它们的index组成的数组。否则，将target - nums[i]和对应的i放进HashMap。
// 时间复杂度：O(n)
// 空间复杂度：O(n)

