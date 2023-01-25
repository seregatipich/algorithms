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
