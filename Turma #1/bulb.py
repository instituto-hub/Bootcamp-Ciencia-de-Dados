"""
There are N bulbs, numbered from 1 to N, arranged in a row. The first bulb is plugged into the power socket and each successive bulb is connected to the previous one (the second bulb to the first, the third bulb to the second, etc.). (Wow, whoever wrote this doesn't know crap about wiring up lighting!)

Initially, all the bulbs are turned off. At moment K (for K from 0 to N−1), we turn on the A[K]-th bulb. A bulb shines if it is on and all the previous bulbs are turned on too. Write a function solution that, given an array A of N different integers from 1 to N, returns the number of moments for which every turned on bulb shines. Examples:

Given [2, 1, 3, 5, 4], the function should return 3.
At the 0th moment only the 2nd bulb is turned on, but it does not shine because the previous one is not on.
At the 1st moment two bulbs are turned on (1st and 2nd) and both of them shine.
At the 2nd moment three bulbs are turned on (1st, 2nd and 3rd) and all of them shine.
At the 3rd moment four bulbs are turned on (1st, 2nd, 3rd and 5th), but the 5th bulb does not shine because the previous one is not turned on.
At the 4th moment five bulbs are turned on (1st, 2nd, 3rd, 4th and 5th) and all five of them shine. There are three moments (1st, 2nd and 4th) when every turned on bulb shines.
More sample cases:

A=[2, 3, 4, 1, 5], the function should return 2 (at the 3rd and 4th moment every turned on bulb shines).

A=[1, 3, 4, 2, 5], the function should return 3 (at the 0th, 3rd and 4th moment every turned on bulb shines). Assume that:

Furtive validation criteria: N is an integer within the range [1..100]; the elements of A are all distinct; each element of array A is an integer within the range [1..N].
"""
