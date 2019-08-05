
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


// 思路：那一个哈希set记录访问过的字符，若有重复则删除，长度l加2。遍历完string后，判断哈希set size是否为0，为0说明全部消完，return l。 
// 若不为0则长度l加1 (也就是把set里面任何拿一个来做middle）。


// 优化思路：并不需要记录长度l,最后拿string.length()减去set.size()就行了
// 时间复杂度：O(n)
// 空间复杂度：O(key)

def 
