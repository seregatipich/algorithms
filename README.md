# Basic algorithms

Solving algorithm problems in Python language

---

<details>
<summary>
<b>Nearest zero (<a href="nearest_zero.py">nearest_zero.py</a>)</b>
</summary>

#### Problem
  Timothy is looking for a place to build himself a house. The street he wants to live on has length n, that is, it consists of n identical consecutive plots. Each plot is either empty, or a house has already been built on it.

Social Timofey doesn't want to live far away from other people on that street. That's why for each plot he needs to know the distance to the nearest empty plot. If the plot is empty, this value will be zero - the distance to himself.

Help Timothy calculate the distances he is looking for. You have a street map to do this. The houses in Timothy's town are numbered in the order in which they were built, so their numbers are not ordered on the map in any way. Empty areas are marked with zeros.

#### Input format
The first line contains street length n (1 ≤ n ≤ 10^6). 
The next line contains n non-negative integers - house numbers and designations of empty areas on the map (zeros). 
It is guaranteed that there is at least one zero in the sequence. 
The house numbers (positive numbers) are unique and do not exceed 10^9.

#### Output format
Output the distance to the nearest zero for each plot. 
Output the numbers on one line, separated by spaces.

#### Example
<table><tbody>
  <tr>
    <td><b>Input</b></td>
    <td><b>Output</b></td>
  </tr>
  <tr>
    <td valign='top'>
5<br>
0 1 4 9 0<br>

</td>
  <td valign='top'>
0 1 2 1 0<br>
</td>
  </tr>
</tbody></table>
</details>

------  

<details>
<summary>
<b>Manual Dexterity (<a href="manualDexterity.py">manualDexterity.py</a>)</b>
</summary>
  
#### Problem
  The "Speed Print Simulator" game is a 4x4 field of keys. In it a configuration of numbers and dots appears on each round. Either a dot or a number from 1 to 9 is written on the key.

At time t the player must simultaneously press all the keys on which the digit t is written. Gosha and Timofey can press k keys each at a moment of time. If at time t all necessary keys are pressed, the players get 1 point.

Find the number of points that Gosha and Timofey can earn, if they press the keys together.
  
#### Input format
The first line contains an integer k (1 ≤ k ≤ 5).

The next four lines give the form of the simulator - 4 characters in each line. Each character is either a dot or a digit from 1 to 9. Characters on one line are consecutive and not separated by spaces.
  
#### Output format
Output a single number - the maximum number of points that Gosha and Timothy can score.

#### Пример
<table><tbody>
  <tr>
    <td><b>Input</b></td>
    <td><b>Output</b></td>
  </tr>
  <tr>
    <td valign='top'>
3<br>
1231<br>
2..2<br>
2..2<br>
2..2<br>

</td>
  <td valign='top'>
2<br>
</td>
  </tr>
</tbody></table>
</details>

---

<details>
<summary>
<b>Deque (<a href="deque.py">deque.py</a>)</b>
</summary>

#### Problem
  Gosha has implemented a data structure Dec, whose maximum size is defined by a given number. Methods push_back(x), push_front(x), pop_back(), pop_front() worked correctly. But if there were a lot of items in the deck, the program took very long. The thing is, not all operations were performed in O(1). Help Gosha! Write an efficient implementation.

Note: When implementing, use a ring buffer.
#### Input format
  The first line contains the number of commands n - an integer not exceeding 100000. The second line contains a number m - the maximum size of the deck. It does not exceed 50,000. The next n lines contain one of the commands:

push_back(value) - add an element to the end of the deck. If the deck already contains the maximum number of items, print "error".
push_front(value) - add an item to the beginning of the deck. If maximal number of items is already in the deck, print "error".
pop_front() - print first element of the deck and remove it. If the deck was empty print "error".
pop_back() - output the last element of the deck and remove it. If the deck has been emptied, output "error".
Value - integer modulo not greater than 1000.
#### Output format
  Output the result of each command on a separate line. For successful push_back(x) and push_front(x) queries nothing needs to be output.
#### Example
<table><tbody>
  <tr>
    <td><b>Input</b></td>
    <td><b>Output</b></td>
  </tr>
  <tr>
    <td valign="top">
4<br>
4<br>
push_front 861<br>
push_front -819<br>
pop_back<br>
pop_back<br>

</td>
    <td valign="top">
861<br>
-819<br>

</td>
  </tr>
</tbody></table>

</details>

<details>
<summary>
<b>Calculator (<a href="calculator.py">calculator.py</a>)</b>
</summary>

#### Problem
  The task is related to reverse polish notation. It is used for parsing arithmetic expressions. It is also sometimes called postfix notation.

In postfix notation, the operands are in front of the operation signs.

Example 1:
3 4 +
means 3 + 4 and equals 7

Example 2:
12 5 /
Since division is integer, the result is 2.

Example 3:
10 2 4 * -
means 10 - 2 * 4 and equals 2

Let us go into the last example in detail:

The * sign stands right after 2 and 4, so the operation it stands for must be applied to them, i.e. the two numbers are multiplied. The result is 8.

The expression then takes the form

10 8 -

Minus' should be applied to the preceding two numbers, 10 and 8. The result is 2.

Let's take a closer look at the algorithm. We will use the stack to implement it.

To calculate the value of an expression written in the reverse polish notation, read the expression from left to right and follow the following steps:

Handling the input symbol:
If an operand is given as input, it is placed at the top of the stack.
If an operand is input, this operation is performed on the required number of values taken from the stack in order of addition. The result of the operation performed is placed at the top of the stack.
If the input character set is not completely processed, skip to step 1.
When the input character set is completely processed, the result of expression calculation is placed at the top of the stack. If there are several numbers left in the stack, only the top element should be printed.
Note about negative numbers and division: in this problem, division means mathematical integer division. This means it is always rounded down. Namely, if a / b = c, then b ⋅ c is the largest number that does not exceed a and is simultaneously divisible by b without a remainder.

For example, -1 / 3 = -1. Be careful: in C++, Java and Go, for example, number division works differently.

In the current problem, it is guaranteed that there is no division by a negative number.
#### Input format
  The only line contains an expression written in inverse Polish notation. Numbers and arithmetic operations are written with a space.

The following operations can be input: +, -, *, / and numbers not exceeding 10000 modulo.

It is guaranteed that the value of intermediate expressions in the test data modulo does not exceed 50000.
#### Output format
  Output the singular - the value of the expression.
#### Example
<table><tbody>
  <tr>
    <td><b>Input</b></td>
    <td><b>Output</b></td>
  </tr>
  <tr>
    <td valign="top">
2 1 + 3 *

</td>
    <td valign="top">
9

</td>
  </tr>
</tbody></table>

</details>

---
