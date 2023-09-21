# Repeating Heads

### Category: Math Concepts

You’re considering a $100 bet with your friend. If <span class="CodeEditor-promptParameter">n</span> consecutive
fair coin flips result in all heads, then you win - else your friend wins. Your friend agrees to let you attempt
the bet as many times as you’d like. Assuming you attempt the bet <span class="CodeEditor-promptParameter">x</span>
times, what's the probability that you’ll win the bet at least once? As well, what should your winning payout ($100, $200, etc)
be to ensure that you at least break even given unlimited attempts of the bet?

Write a function which takes in the number of consecutive coin flips (n) and the
number of bet attempts (x) and returns a list containing:

* Firstly, the probability that you win the bet at least once</li>
* Secondly, your required winning payout

Note that:
* You can assume a fair coin.
* You shouldn't use any libraries.
* Your output values will automatically be rounded to the fourth decimal.

**Sample input**
``` 
n = 3
x = 10
```
**Sample output**
```
[73.6…, 135.6…]
```
