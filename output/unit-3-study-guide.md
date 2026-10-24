# AP Statistics Unit 3
**Short study guide | Lessons 3.1-3.6 | QuickNotes first**

The six QuickNotes boxes are the main study list. Bold GOLDEN sentences are answer frames: replace the brackets with the actual context and numbers.

## 1. The note boxes: what to know

### 3.1 - Probability and the Law of Large Numbers
- Probability is a long-run relative frequency, between 0 and 1. Short-run results vary; streaks can happen by chance.
- As the number of trials increases, the proportion of successes tends to approach the true probability. It does not have to get closer on every trial.
**GOLDEN: Over many, many [trials], the proportion of [event] will approach [probability].**
**GOLDEN: If trials are independent, previous results do not change the probability of [event] on the next trial.** An outcome is never "due." Expected count = n x p; this is not guaranteed.

### 3.2 - Simulation and evidence for a claim
- Model the claimed probability with a coin, die, cards, or random numbers. Match the real process and sample size.
- Assuming the claim is true, estimate the probability of the observed result OR MORE EXTREME in the direction being tested.
- Your note box uses less than 5% as the cutoff for statistical significance and convincing evidence against a claim. Use the cutoff given on the test.
**GOLDEN: Assuming [claim] is true, the estimated probability of [observed result or more extreme] purely by chance is [value]. Because this is [below/above] 0.05, there [is/is not] convincing evidence that [alternative claim].**

### 3.3 - Sample space, notation, and complements
- Sample space = all possible outcomes. A valid probability model has probabilities from 0 to 1 that sum to 1.
- P(A) = favorable outcomes / total outcomes ONLY when outcomes are equally likely.
- Complement: P(not A) = 1 - P(A). A^c means "not A."
- A AND B = intersection (both). A OR B = union (either or both).
**GOLDEN: These outcomes are not equally likely, so I cannot divide the number of favorable categories by the total number of categories.**

### 3.4 - Addition rule, two-way tables, and Venn diagrams
- P(A or B) = P(A) + P(B) - P(A and B).
- Mutually exclusive = cannot occur together, so P(A and B) = 0.
- Venn regions: both = overlap; A only = P(A) - overlap; neither = 1 - P(A or B).
**GOLDEN: I subtract P(A and B) because the overlap was counted twice.**

### 3.5 - Conditional probability and independence
- P(A | B) = P(A and B) / P(B). The event AFTER the bar is the condition and determines the denominator.
- Independent means knowing whether one event occurs does not change the probability of the other. Test P(A | B) = P(A), or P(A and B) = P(A)P(B).
**GOLDEN: Since P(A | B) = [value] differs from P(A) = [value], the events are not independent. Knowing [B] changes the probability of [A].** If equal, write "are independent" and "does not change."

### 3.6 - Multiplication rule and tree diagrams
- Always: P(A and B) = P(A) x P(B | A). If independent: P(A and B) = P(A) x P(B).
- Multiply along a path; add different paths that satisfy the event. Branches from the SAME split sum to 1.
- P(at least one) = 1 - P(none). For n independent trials with constant success probability p: 1 - (1 - p)^n.
**GOLDEN: The second-stage probability is conditional on the first-stage outcome, so I use the probability on that branch.**

---PAGE---

# FRQ: how to earn the points
**Write the event, show the calculation, then explain in context.** A decimal alone may not show your method.

## 2. Describe a simulation completely
**Do these four things:** assign outcomes -> define one full trial -> repeat -> count successes / trials.

**Class example: 3.2 HW #6.** A website claims 50% of students skip breakfast. In a survey of 42 students, only 12 skip breakfast. Is the true proportion lower?

1. Let heads = skips breakfast and tails = eats breakfast. Use a fair coin to model the claimed 50%.
2. Flip the coin independently 42 times. One trial represents one survey of 42 students. Record the number of heads.
3. Repeat the entire 42-flip trial many times, such as 1,000 trials.
4. Estimate the probability by dividing the number of trials with **12 or fewer heads** by 1,000.

**GOLDEN: One trial consists of [42 flips], representing [42 students]; I record [the number who skip breakfast].**

**Reading a dotplot:** One dot is ONE simulated sample, not one student. Count the observed value AND the more extreme values in the relevant direction. Divide by the total number of simulated samples, not the sample size.

**Class example: 3.2 notes.** With a fair wheel, 4 of 100 simulated samples of 50 spins had 10 or more Bankrupts. Estimated probability = 4/100 = 0.04.

**GOLDEN: Assuming the wheel is fair, there is an estimated 4% probability of getting 10 or more Bankrupts in 50 spins purely by chance. Since 0.04 < 0.05, there is convincing evidence that Bankrupt occurs more often than 1/9 of the time.**

A large probability means insufficient evidence against the claim; it does not prove the claim true. "Some evidence" = a result in the suspected direction; "convincing evidence" requires a result unlikely under the claim.

## 3. Two-way table: OR, AND, GIVEN
**Class example: 3.4 notes.** Choose one of these 116 students at random. Let A = takes an AP class and Y = procrastinates often.

| Student | AP | No AP | Total |
| --- | --- | --- | --- |
| Procrastinates often | 58 | 24 | 82 |
| Does not procrastinate often | 12 | 22 | 34 |
| Total | 70 | 46 | 116 |

- **AND:** P(A and Y) = 58/116 = 0.500. Use the overlap and the grand total.
- **OR:** P(A or Y) = (70 + 82 - 58)/116 = 94/116 = 0.810.
- **GIVEN:** P(Y | A) = 58/70 = 0.829. Restrict to the 70 AP students.
- **NEITHER:** P(not A and not Y) = 22/116 = 0.190.

**GOLDEN: Among students taking an AP class, about 82.9% procrastinate often.**

## 4. Justify independence with numbers
Using the same table: P(Y | A) = 58/70 = 0.829, while P(Y) = 82/116 = 0.707.

**GOLDEN: Because 58/70 is not equal to 82/116, taking an AP class and procrastinating often are not independent in this sample. Knowing a student takes an AP class changes the probability that the student procrastinates often.**

Do not write only "they are related." Show two comparable probabilities. Compare exact fractions when possible; rounding can hide a difference.

---PAGE---

# FRQ: tree diagrams and final review

## 5. Tree question: multiply, add, then condition
**Class example: 3.6 notes.** Let F = has flu and + = positive test. P(F) = 0.22. Of patients with flu, 3.7% test negative. Of patients without flu, 2.6% test positive.

**Set up:** First split: flu 0.22 / no flu 0.78. After flu: positive 0.963 / negative 0.037. After no flu: positive 0.026 / negative 0.974.

| Complete path | Multiply along the path | Probability |
| --- | --- | --- |
| Flu AND positive | 0.22 x 0.963 | 0.21186 |
| Flu AND negative | 0.22 x 0.037 | 0.00814 |
| No flu AND positive | 0.78 x 0.026 | 0.02028 |
| No flu AND negative | 0.78 x 0.974 | 0.75972 |

**(a) Probability of a positive test:** Add BOTH positive paths.
P(+) = (0.22)(0.963) + (0.78)(0.026) = **0.23214**.

**(b) Probability of at least one positive among four patients:** Assuming independent patient outcomes, use the complement.
P(at least one +) = 1 - (1 - 0.23214)^4 = **0.6524**.

**(c) Probability of actually having flu GIVEN a positive result:** The denominator includes ALL positive patients; the numerator includes patients with BOTH flu and a positive result.
P(F | +) = P(F and +) / P(+) = 0.21186/0.23214 = **0.9126**.

**GOLDEN: Among patients who test positive, about 91.3% actually have the flu.**

**The big trap:** P(+ | F) = 0.963 is NOT P(F | +) = 0.9126. Reversing the condition changes the denominator. Keep full precision until the final answer; the class key rounds intermediate values.

## 6. With or without replacement
**Class example: 3.6 HW #1.** There are 9 A tiles among 100 Scrabble tiles.

- **With replacement:** P(two A tiles) = (9/100)(9/100) = **0.0081**.
- **Without replacement:** P(two A tiles) = (9/100)(8/99) = **0.00727**.

**GOLDEN: Without replacement, the events are not independent because drawing an A first changes the probability of an A on the second draw from 9/100 to 8/99.**

With random draws and replacement/mixing, the probabilities stay the same and the draws are independent. For these without-replacement problems, update both the remaining count and the total.

## 7. Last-minute mistakes to avoid
- **Independent is not mutually exclusive.** Independent = no probability change. Mutually exclusive = cannot happen together. Two mutually exclusive events with positive probabilities are NOT independent.
- **OR includes both.** Subtract the overlap once. Add disjoint tree paths; multiply consecutive branches.
- **GIVEN changes the denominator.** Use the condition group, not everyone.
- **At least one = 1 - none.** Using a power requires independent trials with the same probability. Otherwise, find "none" using the appropriate conditional probabilities.
- **Probability does not guarantee a count.** A 70% shooter need not make exactly 70 of 100 shots. Streaks do not make an independent outcome "due."
- **Simulation conclusion is conditional on the claim.** A 4% simulated tail probability is NOT a 4% probability that the claim is true.

**Before moving on:** Did I define the event, show the formula and substituted values, use the correct denominator, and answer in context?

Sources: QuickNotes and examples from Lesson 3.1-3.6 notes keys; Lesson 3.2 HW #6 and Lesson 3.6 HW #1. Added in commit 7a21f84, October 23, 2026. This is a condensed review, not a full homework answer key.
