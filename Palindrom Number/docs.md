## The Problem At Hand. 

### Given an integer x, return true if x is a palindrome, and false otherwise.

<hr>

###  Examples

Example 1:
```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
```
Example 2:
```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```
Example 3:
```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```
## My thought process while first encountering the problem. 

Approach #1

when i think of palindromes i think of strings. 
what i mean by this is that one string as usual, other string reversed and we
compare and check them to see if they're palindromes.
I was thinking i take the number, convert it into a string. Later, reverse the string and have 2 pointers to compare the strings. 


If they match, return true else false. Easy right? 

RIGHT? 

well, the question has a follow-up part where it asks us how we could do this without reversing a string? 

That's where i was stuck for a while... 

Coming up with the follow up part was atleast a medium at least for me. 

Approach #2 

On further thinking and some googling, we get it without converting the number into a string. we just do some MATH. 

getting the right value is easy. 
just use the module '%' with 10 and get the right value 

we can similarly get the left value (divide it by 100 keeping in mind we're using 121 as the number )... 

get rid of the left value by % 100 

now we just compare 

how do i get the left value? 
