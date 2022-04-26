# [Tic-Tac-Toe Checker](https://www.codewars.com/kata/525caa5c1bf619d28c000335)
by [eugene-bulkin](https://www.codewars.com/users/eugene-bulkin)
## Description
If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for us!

Assume that the board comes in the form of a 3x3 array, where the value is `0` if a spot is empty, `1` if it is an "X", or `2` if it is an "O", like so:

```
[[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]
```

We want our function to return:

* `-1` if the board is not yet finished AND no one has won yet (there are empty spots),
* `1` if "X" won,
* `2` if "O" won,
* `0` if it's a cat's game (i.e. a draw).

You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.
## Solution:
```python
def is_solved(board):
    return redacted
```
###
Tags: `Algorithms` `Arrays` `Data Types`
<br>
# [The Hashtag Generator](https://www.codewars.com/kata/52449b062fb80683ec000024)
by [AKJ.IO](https://www.codewars.com/users/AKJ.IO)
## Description
The marketing team is spending way too much time typing in hashtags.   
Let's help them with our own Hashtag Generator!

Here's the deal:

- It must start with a hashtag (`#`).
- All words must have their first letter capitalized.
- If the final result is longer than 140 chars it must return `false`.
- If the input or the result is an empty string it must return `false`.


## Examples

```
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
```
## Solution:
```python
def generate_hashtag(s):
    return redacted
    
```
###
Tags: `Algorithms` `Strings` `Data Types`
<br>
