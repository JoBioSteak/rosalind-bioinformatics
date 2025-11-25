Problem (Summarized):

We start with 1 pair of rabbits. Each pair matures after 1 month. After maturing, each pair can reproduce and reproduce to give one pair after a month. Rabbits can't die and won't stop reproducing. 

This is an application of the Fibonacci sequence, Fₙ = Fₙ₋₁ + Fₙ₋₂

Given: Positive integers n ≤ 40 and k ≤ 5.

Return: The total number of rabbit pairs that will be present after n
months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair)


Reflection:

This one was very challenging because recursion is one of my weaker areas. My initial approach was copying the Fibonacci sequence and making random modifications to get the solution. I had to break down the actual mechanics of the problem (ignoring any coding applications) to adapt it for the differeing k offspring. Overall, I cam out with this feeling more confident about recursion.