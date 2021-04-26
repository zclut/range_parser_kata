# Range Parser

Implement a function that parses a string which is composed from tokens of the form 'n1-n2,n3,n4-n5:n6' where 'nX' is a positive integer. Each token represent a different range:

- 'n1-n2' represents the range n1 to n2 (inclusive in both ends)
- 'n3' represents the single integer n3
- 'n4-n5:n6' represents the range n4 to n5 (inclusive in both ends) but only includes every other n6 integer.

Notes:
- The input string doesn't not have to include all the token types.
- All integers are assumed to be positive.
- Tokens may be separated by `','` or `', '`

Some examples:

`"2"` -> `[2]`

`"5-10"` -> `[5, 6, 7, 8, 9, 10]`

`"1-10,14, 20-25:2"` -> `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 20, 22, 24]`


The output should be a list of integers.

---

_**Source**: https://www.codewars.com/kata/57d307fb9d84633c5100007a_
