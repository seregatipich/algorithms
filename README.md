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
    <td><b>Ввод</b></td>
    <td><b>Вывод</b></td>
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
</details>
------
