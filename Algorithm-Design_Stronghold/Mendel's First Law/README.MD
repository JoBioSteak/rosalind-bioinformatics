Problem:

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

Reflection:

A lot of math was required for this one, something I should've suspected when the Problem section was 90% background information and explaining probability, https://rosalind.info/problems/iprb/. I wrestled for a long time trying to make an algorithm by myself but upon realizing that I was lacking an intimate understanding of probability to attempt this, I decided to do some research and fill in the gaps. This article from Khan Academy was especially helpful in bridging those gaps, https://www.khanacademy.org/science/ap-biology/heredity/mendelian-genetics-ap/a/probabilities-in-genetics.

At first, I had the idea to use "brute-force" and try to calculate the probability of all pairings having offspring with dominant alleles for every single possible pairing type. However, I quickly realized that using that solution might've worked but was inefficient. The goal of these problems is to improve not only my programming abilities but also my critical-thinking and algorithmic design skills.

So, I moved away from thinking about these as individuals and pairings and focused more on considering only the recessive probabilities. Regardless of whether that was the most efficient way or not, I still ended up relying mostly on theoretical proabability knowledge. At that point, the programming wasn't even a concern, with the biggest bottleneck how inexperienced I was with probability calculations.

Finally, after much research and trial and error, I finally got the formula right. Almost embarrassing how long it took for a single calculation but it was a surprisingly fun learning experience regardless. The lesson in question being that I need to get better at Mathematics.