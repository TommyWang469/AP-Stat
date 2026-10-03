# AP Statistics Unit 2 Study Guide

**Lessons 2.1-2.9 | Sampling, experiments, and scope of inference**

Prepared from your October 3, 2026 uploads: **37 PDFs (91 pages) and 20 screenshots**. This guide follows your teacher's lesson numbering. It includes explanations, worked examples, all 20 screenshot review questions, new practice, and worked answers.

**How to use this guide:** Read the lesson explanations, cover the worked answers and try the examples, then complete the practice set without notes. Use the answer explanations to identify the specific distinction you missed. Source references such as “2.4 HW Q3” point to the original files in **Unit 2 Resources / Lesson 2.4**. The resource folder's README links to every original file.

**Source limits:** No completed Lesson 2.8 notes key was uploaded. Its section uses the blank lesson and homework/key. The John/Jenn classroom ratings and classroom simulation results are blank, so no class-specific means or simulation percentage are invented. New practice problems are labeled separately from your class material.

## Your study map

| Lesson | Main skill | What you must be able to write |
| --- | --- | --- |
| 2.1 | Simple random samples | Identify population/sample; describe an SRS completely. |
| 2.2 | Stratified random samples | Choose useful strata; explain lower variability. |
| 2.3 | Cluster and systematic samples | Distinguish some from all versus all from some; use a random start. |
| 2.4 | Sampling problems | Name the bias, explain its mechanism, and justify its likely direction. |
| 2.5 | Observational studies and experiments | Identify variables, treatments, units, and confounding. |
| 2.6 | Designing experiments | Explain comparison, random assignment, replication, control, and blinding. |
| 2.7 | Choosing an experimental design | Design completely randomized, blocked, and matched-pairs experiments. |
| 2.8 | Inference and experiments | Read a simulation and decide whether a result is statistically significant. |
| 2.9 | Scope of inference | Decide whether results support causation and to whom they generalize. |

### The two questions behind almost every problem

**How were individuals selected?** This determines whether the sample can represent a larger population. Random sampling helps support generalization.

**How were treatments assigned?** This determines whether treatment groups can be compared fairly. Random assignment in a well-designed experiment helps support a cause-and-effect conclusion when the evidence is convincing.

A large sample, an impressive difference, or the word “random” somewhere in the question does not answer both questions. Locate exactly what was random.

### Core vocabulary

- **Population:** the entire group about which the study wants information.
- **Sample:** the individuals selected from that population for study. Distinguish the selected sample from the subset who actually respond when nonresponse occurs.
- **Parameter:** a numerical description of a population, such as its true mean or proportion.
- **Statistic:** a numerical description computed from a sample, such as its sample mean or sample proportion.
- **Sampling frame:** the list or collection from which the sample is actually chosen. A poor frame may omit part of the target population.
- **Bias:** a method systematically favors some results over others. It is a property of the process, not simply one estimate missing the truth.
- **Sampling variability:** different random samples naturally produce different statistics.

## 2.1 - Simple Random Sample

**Main idea:** Use a genuine chance process to select individuals. Choosing people who seem typical or grabbing whichever observations catch your eye is not random sampling.

### Population, sample, and census

In **2.1 HW Q1**, the college has 11,000 students, including 3,000 incoming freshmen. The athletic director wants the proportion of **incoming freshmen** who want football tickets and selects 400 freshmen.

- Population: the **3,000 incoming freshmen**, not all 11,000 students.
- Sample: the **400 selected freshmen**.
- Parameter: the true proportion of incoming freshmen who want tickets.
- Statistic: the proportion in the sample who want tickets.

A **census** attempts to collect information from every member of the population. It can be expensive, slow, and difficult when individuals are hard to find or move around. A census can still suffer from nonresponse or inaccurate answers; it does not automatically eliminate all error.

### What makes a sample an SRS?

A **simple random sample of size n** gives **every possible set of n individuals the same chance of selection**. Equal chances for individual people alone are not sufficient. For example, randomly selecting one entire classroom can give every student an equal chance if classrooms are equal in size, but it excludes most possible combinations of students, so it is not an SRS of students.

### A complete SRS procedure

For the 91 Apple customers in **2.1 HW Q5**, to select 10:

1. Obtain the list of all 91 customers and assign unique labels 1 through 91.
2. Use a random number generator to select 10 distinct integers from 1 through 91. Ignore repeated labels and continue until 10 different labels are obtained.
3. Survey the customers whose labels were selected.

**Names-in-a-hat alternative:** Write each name on an identical slip, mix thoroughly, and draw 10 slips without replacement. Every eligible customer must appear exactly once. “Choose 10 randomly” is not a complete description of how the selection happens.

**Without replacement** means the same individual cannot occupy two places in the sample. When sampling people for a survey, this is normally what you want.

### Two poor methods

| Method | How it happens | Class example and likely consequence |
| --- | --- | --- |
| Convenience sample | Researcher chooses easy-to-reach individuals. | Interviewing coffee-shop customers about remote work likely overestimates the city's remote-worker proportion. |
| Voluntary response sample | An open invitation lets people select themselves. | A social-media poll about destroying wetlands may attract especially strong opponents, overstating opposition. |

For the business offering a gift card for a five-star review, people choose whether to participate, and the reward also encourages inflated responses. The 92% five-star result likely overstates genuine community approval.

### The Beyonce activity: the statistical lesson

The lesson compares handpicked samples of five words with samples chosen using numbered word positions. Longer or more noticeable words may be overselected by hand. The notes show the random method centered near the stated population mean of **3.53 letters**, whereas the handpicked method tends high.

The material file contains the song and numbered words for sampling. Label **word occurrences**, not only distinct words: repeated words occupy separate positions. The activity illustrates selection bias; similar average word lengths alone do not prove who wrote a song or constitute a formal significance test.

**Check yourself:** In HW Q6, the sample is all **1,200 selected members**, not just the 1,100 familiar with the new standards. The outcome does not redefine the sample.

**Sources:** 2.1 lesson/notes pp. 1-2; material pp. 1-2; HW Q1-Q7 and key.

## 2.2 - Stratified Random Samples

**Main idea:** Split the population into meaningful groups, then take a separate SRS from **every** group. Remember: **some from all groups**.

### How to choose strata

**Strata** are nonoverlapping groups that together contain the population. Useful strata are relatively homogeneous with respect to a characteristic related to the response. Individuals should be similar **within** strata, while the strata may differ from one another.

For the concert activity, the stage is at the front of a 5-row by 10-column seating area. Enjoyment changes with distance from the stage. Therefore, **rows are better strata than columns**: people within a row have similar viewing distances, and sampling two from each row guarantees representation at every distance.

For opinions on perfect-attendance requirements for athletes, **athlete versus non-athlete** is likely a better stratifying variable than grade because the rule directly affects athletes. Explain why the grouping variable is related to the response; merely saying “the groups are different” is incomplete.

### Proportional allocation: worked example

In **2.2 HW Q3**, a restaurant has 120 hourly workers and 30 salaried managers, and wants 20 employees:

**Hourly:** (120 / 150) × 20 = **16**.

**Management:** (30 / 150) × 20 = **4**.

Take an SRS of 16 from the hourly-worker list and an SRS of 4 from the management list, without replacement within each list. Combine them.

An SRS of 10 from each group is still a stratified random sample. However, an unweighted combined average would overrepresent management. Disproportionate sampling can be valid when estimates are appropriately weighted. Equal sample counts are not always proportional counts.

### Bias versus variability

Imagine repeatedly taking samples and plotting one estimate per sample.

| Pattern | Meaning |
| --- | --- |
| Center near the true parameter | Low bias. |
| Center consistently away from the true parameter | High bias. |
| Estimates tightly grouped | Low variability; good precision. |
| Estimates widely spread | High variability; poor precision. |

**Best combination:** low bias and low variability. Estimates can be very consistent and still consistently wrong.

The main advantage of well-chosen stratification over an SRS is usually **less sampling variability**, because the composition of the sample across important groups is controlled. Both properly implemented methods can have low bias. A larger random sample generally reduces variability but does not fix a biased selection method.

**Model explanation:** “Athletes may oppose the attendance rule more strongly than non-athletes. Randomly sampling within both groups guarantees that both viewpoints are represented and can reduce the sample-to-sample variability of the estimated proportion in favor.”

### Class applications

- **Amazon deliveries:** An SRS could miss Michigan customers by chance. Stratify by Illinois, Michigan, and Ohio to ensure all three states are represented.
- **Digital hall passes:** Stratify by grade because opinions may differ by grade. The notes use 25 per grade; this is proportional only if the four grades have equal enrollment.
- **Baseball runs:** The key estimates a population mean near **8.3 runs** from the center of the repeated-sample dotplot. An effective stratified method should have about the same center and less spread.
- **Social-media use by age:** Stratification aims to decrease variability in the estimated mean time spent, not estimate the proportion of people in each age group.

**Sources:** 2.2 lesson/notes pp. 1-3; HW Q1-Q7, especially Q3-Q7; HW key p. 1.

## 2.3 - Cluster and Systematic Samples

### Cluster sampling

Split the population into groups, randomly select **some groups**, and collect data from **every individual in each selected group**. Remember: **all from some groups**.

Good clusters often resemble small versions of the population: heterogeneous internally, with similar mixes across clusters. This is a desirable design feature, not a requirement for calling a method cluster sampling. Choosing homogeneous clusters can still be cluster sampling, but may produce much more variable estimates.

In the concert activity, selecting two entire **columns** includes people from each distance from the stage. Selecting one entire **row** may yield a high estimate from a front row or a low estimate from a back row. The notes show both centered around the truth over repetitions, but row clusters have greater variability. A poor individual estimate does not by itself prove systematic bias.

**Main practical advantage:** lower travel, time, or collection cost. Surveying everyone in three selected classrooms is easier than locating scattered students across a school.

### Systematic sampling

Select a random starting point, then select individuals at a fixed interval on an ordered list. If N / n is an integer, a common procedure uses interval **k = N / n** and a random start from **1 through k**.

For **780 players and a sample of 78**, k = 780 / 78 = **10**. Randomly select an integer r from 1 to 10, then select labels r, r + 10, r + 20, and so on through 78 players. If r = 6, the labels are 6, 16, 26, ..., 776.

Do not always start at 1. Also inspect the ordering: a repeating pattern aligned with the interval may make systematic sampling unrepresentative. Being easy to describe does not make it an SRS.

**Class-activity detail:** The concert worksheet uses an every-eighth-seat rule with wraparound. Follow that stated activity procedure. For a standard linear-list exam description, specify the start in 1 through k so the desired sample size is obtained without running off the list.

### One situation, four designs: MLB homework

There are 30 teams with 26 players per team, totaling 780.

| Design | Complete idea from 2.3 HW Q3 |
| --- | --- |
| SRS of 100 | Label all players 1-780; generate 100 distinct labels; select those players. |
| Stratified sample of 90 | Use teams as strata; take an SRS of 3 players from each of all 30 teams. |
| Cluster sample of 78 | Randomly select 3 teams; include all 26 players on each selected team. |
| Systematic sample of 78 | Random start 1-10; select every 10th player on the full list. |

### Hotel example

The hotel has 10 floors, 50 rooms per floor, half ocean-view and half street-view overall. To select 50 rooms:

- **Stratified:** Separate rooms by view; take an SRS of 25 from each view group. This ensures both views are represented.
- **Cluster:** Randomly select one of the 10 floors; survey all 50 rooms on that floor. This makes collection convenient; floors work better as clusters if their room mixes are similar.
- **Systematic:** Order and label all 500 rooms, randomly start at 1-10, and select every 10th room until 50 are chosen. With floor-by-floor ordering, the selections spread across floors.

### Frequent traps

- “Grouped” does not automatically mean stratified: find out whether all groups or only selected groups contribute.
- “Random” does not automatically mean SRS: cluster and stratified samples also use chance.
- In the driver's-license homework, mixed-grade PE classes make better clusters than grade-specific English classes because license status is strongly related to age/grade.
- For the housing example, neighborhoods make useful strata if values differ between neighborhoods; visiting a few whole neighborhoods is easier but may be less precise. If neighborhood sizes differ, equal numbers per neighborhood require appropriate weighting for a citywide estimate.

**Sources:** 2.3 lesson/notes pp. 1-3; HW Q1-Q7 and key pp. 1-2.

## 2.4 - Potential Problems with Sampling

**Main idea:** Identify the point at which the study goes wrong: who can be selected, who answers, or what answer is recorded.

| Problem | Diagnostic question | Example | Improvement |
| --- | --- | --- | --- |
| Undercoverage | Who is missing from the sampling frame? | Homeowner list excludes renters and children. | Use a frame that covers the target population. |
| Nonresponse | Who was selected but did not provide data? | 100 teachers selected; only 56 respond. | Follow up at different times and through multiple contact methods. |
| Response bias | Are recorded answers systematically inaccurate? | Students exaggerate practice time to please a teacher. | Protect anonymity, use neutral procedures, or measure directly. |
| Question-wording bias | Does the wording push an answer? | A long warning about social-media harms precedes a usage question. | Ask a neutral, clearly worded question. |
| Voluntary response | Was there an open invitation with self-selection? | Followers choose to answer an influencer's public poll. | Select a probability sample instead. |
| Convenience sampling | Were participants chosen for easy access? | Survey the first 50 students to submit a form. | Randomly select from a complete student list. |

Question-wording bias is a source of response bias. More than one problem can occur in one study.

### Nonresponse versus voluntary response

A random sample of 100 teachers receives an invitation, and 56 answer: **nonresponse**, because 44 selected teachers did not provide responses. It is not a voluntary-response sampling method just because participation is optional.

A survey posted for any teacher who wishes to answer: **voluntary response**, because participants select themselves into the sample from an open invitation.

### How to write a full bias explanation

Use this chain: **name the problem → identify the affected people or answers → explain the link to the response → state the likely direction**.

**Whole Fruits, HW Q2:** “There is undercoverage because millennials who do not shop at Whole Fruits cannot be selected. Its customers may be more willing than other millennials to pay for high-quality food, so 70% likely overestimates the population proportion willing to pay more.”

**Teacher planning time, HW Q3:** “There is possible nonresponse bias because 44 selected teachers did not answer. Teachers with less planning time may be too busy to respond, leaving teachers with more time overrepresented. Thus, 85 minutes may overestimate the true mean.”

**Firefighter survey:** The uniform may pressure people to conceal support for cuts. That is response bias, likely causing an **underestimate of support for budget cuts**.

**Practice logs:** Students may overreport minutes to earn credit or impress the teacher, producing an upward bias. Recorded practice sessions may improve measurement, though monitoring can also change behavior.

### What larger samples can and cannot fix

Increasing sample size can reduce random sampling variability. It does not repair a systematically incomplete frame, misleading wording, or systematic nonresponse. A huge biased sample can be precisely wrong.

An SRS from a bad frame still has a coverage problem. Randomly selecting homeowners does not make them representative of all residents.

**Direction is a contextual argument:** Nonresponse alone does not prove that the estimate is too high. State why respondents might differ from nonrespondents. In the screenshot teacher-rating question, “higher” is the expected answer under the plausible assumption that happier or more engaged students are more likely to respond; the exact direction is not mathematically guaranteed.

**Sources:** 2.4 lesson/notes pp. 1-2; HW Q1-Q7 and key p. 1; first screenshot review Q3, Q6, Q7.

## 2.5 - Observational Studies and Experiments

### The defining distinction

An **observational study** records characteristics or choices without imposing treatments. An **experiment** deliberately imposes treatments and observes responses. Random assignment makes an experiment stronger, but treatment imposition is what makes it an experiment.

Randomly selecting people for a survey does not make the study an experiment. Likewise, volunteering to participate does not prevent a study from being an experiment if treatments are then assigned.

| Term | Meaning | SAT-prep example |
| --- | --- | --- |
| Explanatory variable | Variable used to explain or predict the response. | Whether the student takes the prep course. |
| Response variable | Outcome measured. | SAT score. |
| Experimental unit | Smallest unit independently assigned a treatment. | Student, if students are assigned individually. |
| Subject | A human experimental unit. | Each participating student. |
| Factor | An explanatory variable manipulated in an experiment. | Prep format. |
| Level | A particular value or category of a factor. | Online or classroom instruction. |
| Treatment | A specific experimental condition; possibly a combination of factor levels. | Online prep versus classroom prep. |

**Factor combinations:** In 2.9 HW Q5, caffeine (yes/no) and light condition (yes/no) give **2 × 2 = 4 treatments**: caffeine only, light only, both, neither.

### Confounding: explain both connections

A confounding variable is related to the explanatory variable and also affects the response, so their effects cannot be separated cleanly.

In the class SAT example, students chose whether to take prep. Their means were 1220 and 1050, a difference of **170 points**. This establishes an observed association, not a causal effect of 170 points.

**Model explanation:** “More motivated students may be more likely to enroll in prep and may also study independently and earn higher SAT scores. Therefore, motivation could help explain the score difference, and the effects of prep and motivation are confounded.”

Naming “motivation” alone is incomplete. Explain both its link to course choice and its possible effect on scores.

Other plausible examples include family resources, prior achievement, and time available for studying. A variable that merely affects the response is extraneous; to explain confounding, describe its relationship with treatment/explanatory-variable groups too.

### Worked classifications from the homework

- **Chocolate and pregnancy:** Observational; researchers asked about consumption. Amount consumed is quantitative if measured as servings; development of the outcome is categorical (yes/no). The association does not establish causation.
- **Reading and mortality:** Prospective observational study because people were followed for 12 years after their reading habits were recorded. Education could be related to reading and to health/longevity.
- **Diet/stress intervention:** Experiment because treatments were assigned. Random assignment supports causal analysis, but losing about half the participants before the follow-up can bias the comparison if missingness differs across groups or outcomes.
- **“Help” versus “helper”:** 51 children are units; the three wording conditions are treatments; number of toys picked up is the quantitative response.
- **Speech services:** An experiment because service frequency is imposed; the response is the number of speech errors. Do not call it observational merely because random assignment is not explicitly stated.

**Retrospective:** Looks back using past records or past experiences. **Prospective:** Follows individuals forward. Neither word by itself tells you whether there was random assignment.

### A subtle class example: roofs and cell service

Employees are randomly assigned to Ben's or Jerry's house, so this is an experiment comparing the two house conditions. However, each roof type occurs on just one house. Roof type is inseparable from other differences between those houses. The design does not isolate the effect of roof material across homes simply by assigning many employees.

**Sources:** 2.5 lesson/notes pp. 1-2; HW Q1-Q6 and key pp. 1-2; 2.9 HW Q5.

## 2.6 - Designing Experiments

### Four principles and why they matter

| Principle | What to do | Why it matters |
| --- | --- | --- |
| Comparison | Compare at least two treatment conditions. | Reveals what would happen under an alternative condition. |
| Random assignment | Use chance to allocate units to treatments. | Tends to balance uncontrolled variables and supports causal comparisons. |
| Replication | Use enough independent units in each treatment. | Reduces the impact of individual variation and improves precision. |
| Control | Keep other relevant conditions consistent. | Prevents systematic differences besides the treatments from explaining the result. |

**Control is not the same as a control group.** Control means holding conditions consistent. A control group is a baseline treatment group, such as no treatment, a placebo, or standard treatment. Comparing two active treatments can be valid without a no-treatment group.

**Random assignment does not guarantee identical groups.** It makes systematic group differences less likely and provides a way to evaluate chance differences. Its main purpose is not to make subjects represent a population.

**Replication does not mean repeatedly measuring the same unit and pretending those measurements are independent people.** Repeating the entire experiment is valuable, but within an experiment, use enough independent units per treatment.

### Complete design: 180 students and review sheets

For **2.6 HW Q2**:

1. Label the 180 students 1-180.
2. Generate 90 distinct random labels; assign those students the teacher's review sheet.
3. Assign the remaining 90 students to prepare on their own.
4. Give all students the same preparation interval and the same test under comparable conditions.
5. Compare the mean test scores of the two groups.

**Purpose statement:** “Random assignment tends to balance prior achievement and motivation between the two groups, helping isolate the effect of the review-sheet treatment on test scores.”

A coin flip for every student is random assignment but does not guarantee exactly 90 per group. If equal group sizes are required, randomly choose 90 without replacement or randomly shuffle the full list and split it in half.

### Three-treatment design: painted cows

The lesson uses 1,200 cattle. Label 1-1200 and randomly assign **400 to eyes, 400 to crosses, and 400 to no marks** using a shuffled list split into three groups. Keep the follow-up period and other relevant conditions comparable, and compare death proportions.

The no-mark group supplies the baseline. The cross-mark group helps distinguish an effect specific to eyes from an effect of simply adding paint/marks. With equal group sizes, counts and proportions give the same ordering; with unequal sizes, compare proportions rather than raw counts.

### Placebo and blinding

- **Placebo:** A treatment resembling the active treatment but without its active ingredient.
- **Placebo effect:** A response associated with receiving a treatment and its context/expectations even when the active ingredient is absent.
- **Single-blind:** One relevant party, such as participants or outcome assessors, does not know the treatment assignments. Say exactly who is unaware.
- **Double-blind:** Both participants and the people interacting with/evaluating them do not know their assignments.

Blinding means being unaware of **which treatment each subject receives**, not being unaware that a study exists. Identical-looking pills, coded containers, and independent assessors can help.

For the medication-versus-placebo injection homework, both groups experience an injection and similar attention. This helps isolate the active ingredient's effect. The blinded evaluator is less likely to interpret symptoms differently because of expectations.

### Fixing flawed experiments

- **Beard oil:** Growth after using oil is not enough; beards naturally grow. Use a suitable comparison, multiple participants, and random assignment. A single person's different months may also differ in season or other conditions.
- **Self-selected workouts:** More motivated or fitter athletes may choose harder training. Randomly assign workouts instead.
- **Labeled “smart” and “sugar” pills:** Labels reveal treatment and may change expectations. Use indistinguishable, coded pills and blind the evaluator if possible.
- **All six classes get a new method:** Add a comparison by randomly assigning three classes to each teaching method. If whole classes receive assignment, the experimental units are the **six classes**, not every student independently.

**Sources:** 2.6 lesson/notes pp. 1-2; HW Q1-Q7 and key pp. 1-2.

## 2.7 - Selecting an Experimental Design

### Completely randomized design

Assign all experimental units to treatment groups using one randomization process. Use this when no particular blocking variable needs to be controlled or when units are fairly similar.

**Class SAT example:** Randomly assign 25 of the 50 volunteers to online prep and the other 25 to classroom prep; use comparable preparation and testing conditions; compare mean SAT scores.

### Randomized block design

First form blocks of units similar on a **pre-treatment characteristic likely to affect the response**. Then randomly assign treatments **within every block**. Compare treatments within blocks, then combine the treatment evidence appropriately.

**Class SAT example:** There are 30 juniors and 20 seniors. Form grade-level blocks. Randomly assign 15 juniors to each format, and 10 seniors to each format. Compare formats within each grade.

**Why it helps:** Grade may affect SAT performance. Comparing students within grade reduces variation due to grade and makes the treatment difference easier to detect. Blocking helps control a known source of variation; random assignment within blocks helps balance other variables.

**Wrong design:** All juniors online and all seniors in person. Grade and treatment would be confounded.

### Matched-pairs design

A special randomized block design for comparing **two treatments**, with closely matched comparisons:

1. **Two similar individuals per pair:** Match students by prior GPA, then randomly assign one in each pair to each prep method. Analyze the treatment differences within pairs.
2. **One individual receives both treatments:** Each person serves as their own comparison. Randomize the order, or randomize which side receives which treatment.

For the shin-guard homework, each player wears the new guard on one shin and the standard guard on the other. Flip a coin for each player to decide which shin gets the new guard. Compare each player's two comfort ratings, reducing variability due to differences in how people rate comfort.

For pilots trying both breakfast drinks, randomly assign the first drink, allow the stated washout period, then give the other drink. Randomizing order helps avoid confounding treatment with practice, fatigue, or period effects. The washout helps limit carryover.

### Choosing a useful block: worked examples

- **Physical therapy:** Age is more plausibly related to pain/mobility than morning-versus-afternoon appointment time.
- **Teacher bonuses:** Block by elementary, middle, and high school. Within each 100-teacher block, randomly select 50 for bonuses; the remaining 50 get no bonus. Compare retention within each school level.
- **Irrigation:** HW Q5's **Option 1** groups plots by distance from the stream. Randomly give three of the six plots within each block irrigation A and three irrigation B. Nearby water can affect growth, so it should not line up with only one treatment.
- **Advertisements:** Block users by a characteristic plausibly related to response, such as age, then randomly assign all three advertisements within every block. Do not assume equal-sized age blocks unless the numbers are provided.
- **Butterfly screenshot:** Opposite sides of the same road section form pairs. Randomly mow one side and leave the other unmowed; compare the two sides within each section.

### Blocks versus strata

Both group similar individuals to improve precision. **Strata belong to sampling:** select people from each group. **Blocks belong to experiments:** assign treatments within each group. Neither grouping step itself is the random step.

**Sources:** 2.7 lesson/notes pp. 1-2; HW Q1-Q7 and key pp. 1-3; second screenshot review Q7, Q9, Q10.

## 2.8 - Inference and Experiments

**Main idea:** Even equally effective treatments can produce different sample results by chance. Statistical inference asks whether the observed result is unusual under a specific no-effect model.

### The logic of a simulation

1. **State the chance model:** Assume the treatments have no effect, or state the claimed population value.
2. **Choose a statistic:** For example, mean rating for John minus mean rating for Jenn, or click proportion for A minus click proportion for B.
3. **Simulate chance alone:** Reassign labels consistent with the original design while keeping the observed outcomes and group sizes fixed, or simulate new outcomes from the stated guessing model.
4. **Repeat many times:** Record one statistic per repetition. Each dot represents one complete simulated study's statistic, not one individual.
5. **Count equally or more extreme results:** Use the direction stated in the question.
6. **Interpret the fraction in context** and decide whether there is convincing evidence against the no-effect model.

**Estimated tail probability = number of simulated statistics at least as extreme as observed / total simulations.**

For a question about A being **greater**, count the right tail. For A being **less**, count the left tail. For a difference in **either direction**, count extremes on both sides appropriately. Include equality: “at least 6” means 6 and above.

### Statistical significance: precise wording

A result is **statistically significant** when it would be sufficiently unlikely under the no-effect/null model, according to the chosen significance level. Your class commonly uses **5%**. Follow a stated level or cutoff convention; do not decide solely from the size of a raw difference.

**Model sentence:** “If the treatments were equally effective, a difference at least this large in the observed direction would occur in only about 2% of repeated random assignments. Since 2% is below 5%, there is convincing evidence that the treatments differ in the stated direction.”

This is **not** a 2% probability that the null model is true. It does not mean chance was impossible, that every subject benefits, or that the effect is large enough to matter practically.

**Not statistically significant** means the study has insufficient evidence against the no-effect model. It does not prove that the treatments are equally effective.

### John/Jenn: what can be computed

The worksheet's reported original-study means are **3.78 for John** and **2.93 for Jenn**:

**Observed difference = 3.78 - 2.93 = 0.85 rating points.**

To simulate no name effect, pool the observed ratings, shuffle, deal them into the two groups using the original group sizes, and calculate John minus Jenn again. Repeat. If testing for higher John ratings, count simulated differences at least 0.85.

The classroom ratings and classroom dotplot are blank in the provided file. You cannot calculate the class's observed difference, tail percentage, or compare its evidence numerically without those data. A bigger raw difference alone is not always stronger evidence; sample size and variability also matter.

### Yelp A/B testing

Format A: 21 / 50 = **0.42**. Format B: 19 / 50 = **0.38**.

**A - B = 0.04, or 4 percentage points.** This is not a 4% relative increase; relative to 38%, it is about 10.5%.

Under no format effect, pool the **40 clicks and 60 non-clicks**, randomly divide into two groups of 50, and recompute the difference. The worksheet's simulation has many differences comparable to or beyond 4 percentage points, so this is not convincing evidence of a format effect. Do not conclude “A wins” merely because 42% exceeds 38%.

**Sources:** 2.8 blank lesson pp. 1-3; 2.8 HW and key. The next page works through the homework simulation evidence.

## 2.8 - Worked simulation evidence

### Ring test: 56 correct out of 100

The homework simulates guessing with a 50% chance of a correct answer. The key reports **24 of 200** simulated samples with at least 56% correct:

**24 / 200 = 0.12 = 12%.**

**Interpretation:** If each guess had a 50% chance of being correct, about 12% of simulated samples of 100 would have at least 56 correct. Because 12% is greater than 5%, the result does not provide convincing evidence that the test performs better than guessing.

A dot at **61%** means that in one simulated sample of 100, 61 guesses were correct. It does not mean one woman was 61% correct.

The supplied key identifies **59% or more** as sufficiently unusual in this particular 200-trial plot. That cutoff belongs to this simulation and sample size; it is not a universal rule. With 500 observations, the same 56% would be more convincing under the same valid model because sample proportions vary less at larger sample sizes. A new simulation with n = 500 would be needed for the corresponding estimated tail probability.

### University of Michigan webinar selection

From 1,207 interested students, 93 are from Michigan and 1,114 are not. Six Michigan students appear in a randomly selected group of 40.

Use 93 blue and 1,114 red chips, select 40 **without replacement**, and count blue chips. Replace all chips and remix before the next trial. In the supplied 1,000-trial histogram, counts for 6, 7, 8, and 9 blue chips are **41, 24, 7, and 2**.

**Tail count = 41 + 24 + 7 + 2 = 74.**

**74 / 1000 = 0.074 = 7.4%.**

At the 5% level, this is **not convincing evidence** that getting at least six Michigan students is too unusual under random selection. HW Q6 answer: **C**. Count the whole tail, not only the bar at six.

### Peanut-exposure experiment

The homework reports allergy rates of **17.3% in the avoidance group** and **3.2% in the regular-exposure group**.

**Avoidance - exposure = 17.3% - 3.2% = 14.1 percentage points.**

The stated chance probability is **less than 0.01%**, equivalent to less than **0.0001** as a proportion. This is much smaller than 5%. Given the randomized experiment described, the result supplies strong evidence of a causal reduction in the measured allergy outcome for the studied setting. The percentage-point difference is not the same as a 14.1% relative reduction. This is an interpretation of the supplied statistics problem.

### Significant does not repair a bad design

The four-day-workweek study compares employees with their own workplace a year earlier. Changes in workload, technology, or staffing may also change productivity. Randomly assign comparable units to four-day versus five-day schedules during the same period to improve the comparison. A significance claim does not remove confounding from a historical comparison.

The exercise homework's nonsignificant resistance-only comparison means its observed difference is compatible with chance variation under the null model. It does not prove resistance exercise has zero effect.

**Sources:** 2.8 HW Q1-Q6, pp. 1-5; key pp. 1-2. Simulation counts and numerical results are taken from the supplied plots/keys, not invented trial outcomes.

## 2.9 - Scope of Inference

**Main idea:** Separate **causation** from **generalization**. They require different features of the design.

| Random sample? | Random assignment? | Supported scope, assuming valid conduct and appropriate evidence |
| --- | --- | --- |
| Yes | Yes | A causal conclusion can generalize to the population sampled. |
| Yes | No | An association can generalize to the population sampled; causation is not established. |
| No | Yes | A causal conclusion for the experimental units; broader application requires justification. |
| No | No | Describe the observed association for those studied; neither broad generalization nor causation is established by the design. |

The table concerns what the **design permits**. The observed data must still provide convincing evidence before you assert that a treatment really has an effect. “Group A's mean was higher” alone is not a significance test.

### Exact population boundaries

Random sampling supports inference to the **population actually sampled**, not automatically to all similar people everywhere.

- Randomly sampled U.S. teachers → U.S. teachers.
- Randomly sampled Michigan high-school teachers → Michigan high-school teachers.
- Randomly sampled high-school teachers at one conference → high-school teachers attending that conference.
- Randomly sampled wrestlers at Jefferson High → wrestlers at Jefferson High, not all athletes or all students.
- Randomly sampled new iPhones at one store → the new iPhones in that store's sampling population, not all phones worldwide.

The Wisconsin volunteering study uses a random sample but no assigned volunteering. It supports a population-level **association** between volunteering and mortality, not proof that volunteering causes longer life.

### SAT-prep card sort: all six cases

The activity explicitly assumes a statistically significant score difference. The matching letters refer to the supplied **2.9 material** file.

| Case | Selection and assignment | Correct conclusion and card |
| --- | --- | --- |
| 1 | One senior class; students chose prep. | Association for students in that class. **C** |
| 2 | Random sample of school seniors; students chose prep. | Association for all seniors at the school. **E** |
| 3 | Random sample of the school's SAT-takers; students chose prep. | Association for all SAT-takers at the school. **A** |
| 4 | One senior class; randomly assign prep. | Causal effect for the students in that class. **D** |
| 5 | Random sample of seniors; randomly assign prep. | Causal effect for all seniors at the school. **F** |
| 6 | Random sample of SAT-takers; randomly assign prep. | Causal effect for all SAT-takers at the school. **B** |

### Volunteers and “similar people”

Your second screenshot review Q4 gives **D: university students similar to the volunteers** as the best of the available options. This is a cautious practical extension, not a probability-sampling guarantee. The safest free-response answer is to state that no random sample was taken, so broad population generalization is not established by the design; any extension to similar people needs justification.

### Model conclusion: restaurant dessert experiment

Tables during one shift receive a suggestion or no suggestion by coin flip, and the difference is statistically significant.

**Answer:** “For the tables in this study, suggesting a specific dessert caused an increase in average total bill. The coin flips randomly assigned the treatments. Because the tables were not randomly sampled from a wider population, the study does not by itself justify generalizing to all customers or all restaurants.”

### Keep the class key's shorthand precise

The iPhone lesson and astronaut homework keys use causal wording after reporting only a higher mean. Their designs permit causal analysis, but an actual causal-effect claim needs evidence that the difference is not plausibly chance alone. If a question asks only what the design allows, state the scope. If it asks whether the result proves effectiveness, do not invent statistical significance.

**Sources:** 2.9 lesson/notes pp. 1-2; material p. 1; HW Q1-Q7 and key pp. 1-2; second screenshot review Q4 and Q12.

## Essential comparisons and answer templates

### Six distinctions to memorize

| Pair | Difference |
| --- | --- |
| Random sampling vs random assignment | Select people from a population vs allocate units to treatments. |
| Stratified vs cluster | Some individuals from every group vs everyone in selected groups. |
| Stratification vs blocking | Organize sampling vs organize treatment assignment. |
| Nonresponse vs response bias | Missing answers from selected people vs systematically inaccurate recorded answers. |
| Nonresponse vs voluntary response | Selected people fail to answer vs people self-select from an open invitation. |
| Statistical significance vs practical importance | Unusual under a null model vs large/useful enough to matter in context. |

### Reusable free-response structures

**Describe an SRS:** “Label all [N individuals] 1 through N. Use a random number generator to select [n] distinct labels, ignoring repeats. Select the corresponding [individuals].”

**Describe random assignment:** “Label the [N experimental units]. Randomly select [n] distinct labels for treatment A; assign the remaining units to B. Apply the treatments under comparable conditions and compare [specific response].”

**Explain confounding:** “[Variable Z] may be related to [explanatory variable X] because ____. It may also affect [response Y] because ____. Therefore, the observed difference cannot be attributed to X alone.”

**Explain bias:** “[Type] occurs because [specific group/answer issue]. These people may [differ in the response], so the estimate likely [over/underestimates] [exact population parameter].”

**Justify blocking:** “[Blocking variable] is likely related to [response]. Group similar units by it and randomly assign all treatments within each block. This reduces variation due to [blocking variable] in treatment comparisons.”

**Interpret significance:** “Assuming [no effect/null claim], a result at least as extreme as [observed result] would occur about [tail percentage] of the time. Since this is [below/above] [level], there [is/is not] convincing evidence for [contextual alternative].”

### Before submitting an experimental design

- Name the units, treatments, and response precisely.
- Specify an actual randomization mechanism and required group sizes.
- If blocking, assign every treatment within every block.
- Say what is held consistent and how outcomes will be compared.
- Distinguish independent units from repeated measurements.
- Describe who is blinded when blinding is possible.
- Match the conclusion to both the design and the strength of the evidence.

## Screenshot review - Lessons 2.1-2.4

These are explanations of your provided review questions, preserving their original question numbers. Source screenshots are dated October 3 and named by capture time in **Unit 2 Resources / Screenshots**.

### Q1 - Dentist sampling by age | 12.30.44 PM

**Answer C.** Randomly sample 30 patients under 20 and 30 patients age 20 or older. There is a sample from each age stratum. Selecting every fifth name is systematic as described; restricting selection to recent or long-absent patients omits other groups.

### Q2 - Parking lot versus sports field | 12.30.48 PM

**Method 1: SRS.** Label all 3,600 students, select 360 distinct random labels, and survey those students.

**Method 2: Stratified.** Take an SRS of 85 from 850 athletes and 275 from 2,750 non-athletes. Each group contributes 10%, so the allocation is proportional. Athlete status is relevant because the proposal would replace a practice field.

**Method 3: Cluster.** Randomly select 12 classrooms and survey everyone in them. This is efficient but needs the classroom groups to be defined without double-counting students. The screenshot crops some dropdown text; these explanations are based on the fully visible methods, not a reconstruction of hidden wording.

### Q3 - Political survey nonresponse | 12.30.52 PM

**Answer C.** Selected households have nobody home when visited. Leading background information is wording bias; untruthful political answers are response bias; excluding apartments is undercoverage.

### Q4 - Gym booth at county fair | 12.30.54 PM

**Answer D: convenience sampling.** The manager approaches easy-to-reach passersby. There is no random selection of people or groups and no fixed-interval random-start procedure.

### Q5 - SRS of faculty | 12.30.57 PM

**Answer D.** Number the full employee roster and use a random generator to choose 20 distinct faculty members. First arrivals are convenience sampling; every fifth arrival is systematic; choosing 10 teachers and 10 staff is stratified.

### Q6 - Influencer's 94% approval | 12.31.00 PM

**Voluntary response; likely biased; possible response bias; likely higher.** Followers self-select, devoted fans may be more likely to respond, and respondents may give flattering answers directly to the influencer. Having 2,482 responses does not cure the selection problem.

### Q7 - 22 of 50 students rate a class | 12.31.03 PM

**Nonresponse bias; expected direction: higher.** Twenty-eight selected students did not answer. A plausible explanation is that more satisfied or engaged students responded more often. The average of 8.2 describes the respondents; it does not automatically represent everyone. The direction depends on how respondents differ.

### Q8 - University return plans | 12.31.03 and 12.31.06 PM

**Answer D.** Population: all 12,000 university students. Sample: the 250 selected students, consisting of 150 undergraduates and 100 graduate students. The 223 intending to return are an outcome-defined subset, not the full sample.

## Screenshot review - Lessons 2.5-2.9

### Q1 - Digital versus print reading | 12.32.24 PM

**Units:** the 60 middle-school students. **Treatments:** reading the passage on printed paper or a digital device. **Response:** reading-comprehension test score. Thirty students receive each condition.

### Q2 - Drainage and mosquitoes | 12.32.24 and 12.32.27 PM

**Answer C: observational; mosquito population is the response.** Researchers selected locations with existing drainage conditions; they did not randomly assign standing water. The use of random sampling does not create an experiment.

### Q3 - Workout time and BMI | 12.32.29 PM

**Explanatory:** time of day of exercise. **Response:** BMI score. Tracking activity over two years does not impose a treatment, so this remains observational.

### Q4 - Advertising with 200 university volunteers | 12.32.29 and 12.32.32 PM

**Best listed answer D: students at that university similar to the volunteers.** Random assignment supports causal comparison, but volunteering does not produce a random population sample. Do not extend the findings automatically to every student. See the scope-of-inference qualification in Lesson 2.9.

### Q5 - Confounding in the workout study | 12.32.35 PM

**Nutrition is a plausible confounder.** People who exercise in the morning may have different eating habits, and eating habits can affect BMI. Both links must be explained; the study does not establish that nutrition actually differed.

### Q6 - Powerline markers and cranes | 12.32.35 and 12.32.37 PM

**Answer B: association, not necessarily causation.** Markers were installed on newer lines rather than randomly assigned. New and old lines may differ in location or construction, which could affect collisions. Statistical significance does not eliminate this confounding.

### Q7 - Why spelling instruction cannot be double-blind | 12.32.40 PM

**Answer B.** Children know whether they are copying words in colors or taking retrieval quizzes. Knowing one's age is irrelevant to treatment blinding. The scorer can still be blinded to treatment using coded work; double-blinding fails because the children cannot be blinded to the obvious activity.

### Q8 - Why the reading study is an experiment | 12.32.44 PM

**A treatment was imposed.** Researchers assigned reading format. Merely measuring test scores or using a sample of students would not be enough.

### Q9 - Grade may affect comprehension | 12.32.44 and 12.32.46 PM

**Use a randomized block design with grades 6, 7, and 8 as blocks.** Randomly assign print and digital reading within each grade and compare responses within grades. Do not assign one grade entirely to one format.

### Q10 - Mowing and butterflies | 12.32.46 and 12.32.49 PM

**Answer A: matched-pairs experiment.** Each half-mile road section provides two comparable sides. Randomly assign one side to mowing and the other to no mowing. The road section is the block/pair; the side receiving treatment is the experimental unit. There are 20 pairs, not an SRS of butterflies.

### Q11 - Meaning of significant dessert effect | 12.32.53 and 12.32.55 PM

If dessert suggestions had no effect on bills, a difference in average bills at least as large in the observed direction would be unlikely under random assignment. “Significant” does not mean every table spent more or that the increase was necessarily large in dollars.

### Q12 - Conclusion of the dessert study | 12.32.53 and 12.32.55 PM

For the tables studied, suggesting a specific dessert caused a higher average total bill. Random assignment and statistical significance support this conclusion. The one-shift sample does not establish generalization to all restaurants or all future customers.

## Practice - Sampling and bias

**New practice, created for this guide.** These are not additional uploaded class questions. Try them without the explanations. Show procedures and reasoning, not just vocabulary.

### P1 - Population versus outcomes

A district wants to estimate the proportion of its 2,400 seniors applying to college. It selects 120 seniors; all respond, and 96 say yes. Identify the population, sample, parameter, and statistic. Is 96 the sample size?

### P2 - Proportional stratification

A school has 600 ninth-graders, 500 tenth-graders, 400 eleventh-graders, and 300 twelfth-graders. Select a proportional stratified sample of 180 students. Give the sample size from each grade and a complete selection procedure. Explain why the resulting sample is not an SRS of 180 from the whole school.

### P3 - Four sampling methods

A dorm has 12 floors with 20 residents per floor. Describe an SRS of 24 residents, a stratified sample of 24 using floors, a cluster sample of 40 using floors, and a systematic sample of 24 using a floor-by-floor list. Give an advantage of cluster sampling.

### P4 - Three ways a survey can fail

A city wants to know support for a park. It randomly selects 200 adults from a landline list, receives 80 replies, and asks, “Do you support this much-needed park that will make our community safer?” Identify three possible sources of bias. Can you confidently predict the direction of all three? Would contacting 2,000 people with the same procedure eliminate the problems?

### P5 - Repeated-sample distributions

The true approval rate is 45%. Method A produces estimates centered at 45%, usually between 43% and 47%. Method B produces estimates centered at 60%, usually between 59% and 61%. Method C produces estimates centered at 45%, usually between 30% and 60%. Compare their bias and variability. Which method is preferable?

### P6 - Responding voluntarily

Explain why these are different: (a) a public website poll that anyone can answer; (b) an SRS of 300 households receives a survey and 180 respond. In (b), identify the selected sample, respondents, and nonrespondents.

## Practice - Experiments and inference

### P7 - Confounding

A study finds that students who choose to use flashcards earn higher exam scores. Identify the explanatory and response variables. Explain one plausible confounder using both required connections. Design a randomized comparison for 80 willing students.

### P8 - Blocking and paired designs

There are 40 students, 24 juniors and 16 seniors, comparing two SAT-prep formats. Describe a randomized block design by grade. Then describe a different matched-pairs design using prior test scores. State where randomization occurs in each design.

### P9 - Experimental units and blinding

Six greenhouses are randomly assigned, three per group, to receive one of two temperature settings. Researchers measure 100 plants in each greenhouse. What are the experimental units? Are there 300 independently assigned units per treatment? How could outcome measurement be blinded?

### P10 - Simulation tail

An experiment compares click rates for A and B. A gets 18 clicks out of 40 and B gets 10 out of 40. Under no treatment effect, a 1,000-trial randomization simulation produces differences at least as large as the observed A-minus-B difference in 18 trials. Calculate the observed difference, the estimated tail probability, and a conclusion at the 5% level. Explain what one simulation trial represents.

### P11 - Nonsignificance

In a second randomized experiment, the corresponding estimated tail probability is 0.28. A student writes, “There is a 28% probability that the two treatments are equal, so we proved they have the same effect.” Explain both errors.

### P12 - Four scopes of inference

For each design, state whether a causal conclusion is possible with convincing results and name the population, if any, to which a sampling-based generalization is justified:

1. Randomly sample city residents, then record their existing exercise habits and blood pressure.
2. Recruit 100 volunteers, randomly assign exercise programs, then compare outcomes.
3. Randomly sample city residents and randomly assign exercise programs.
4. Survey people leaving one gym about their existing habits and blood pressure.

### P13 - Combined free response

A school randomly samples 120 students: 60 athletes and 60 non-athletes. Within each group, it randomly assigns 30 students to use a study app and 30 to use printed exercises for four weeks. Everyone completes the same assessment. The app group has a higher mean, but no significance analysis is provided.

(a) Name the sampling method and the experimental design. (b) Explain the separate purpose of each random step. (c) Is the sampling allocation necessarily proportional? (d) Does the design permit causal analysis? (e) Can you already conclude the app causes higher scores? (f) How should assessment and comparison be carried out?

## Worked answers - P1-P6

### P1

Population: all 2,400 district seniors. Sample: the 120 selected seniors. Parameter: the true proportion of all seniors applying to college. Statistic: **96 / 120 = 0.80 = 80%**. The 96 are the “yes” subgroup, not the sample size.

### P2

Total enrollment = 1,800, and 180 / 1,800 = 10%. Select **60, 50, 40, and 30** students from grades 9, 10, 11, and 12, respectively.

Within grade 9, label students 1-600 and generate 60 distinct random labels. Select those students. Repeat using labels 1-500 and 50 selections, 1-400 and 40 selections, and 1-300 and 30 selections in the other grades. Combine the four samples.

It is not an SRS of 180 from the whole school because grade counts are fixed. Many possible 180-student sets, such as 180 ninth-graders, have zero chance of selection, while valid sets have positive chances.

### P3

- **SRS:** Label all 240 residents 1-240; generate 24 distinct random labels and select them.
- **Stratified:** On each floor label its 20 residents 1-20; randomly select 2 distinct labels. Repeat on all 12 floors for 24 residents.
- **Cluster:** Label floors 1-12; randomly choose 2 distinct floor labels. Survey all 20 residents on each selected floor for 40 residents.
- **Systematic:** k = 240 / 24 = 10. Randomly choose r from 1-10, then select r, r + 10, ..., r + 230 on the ordered resident list.

Cluster sampling reduces collection effort because only two floors need to be visited. Its precision depends on how similar the floor populations are.

### P4

**Undercoverage:** Adults without landlines cannot be selected. **Nonresponse:** 120 selected adults do not reply. **Question-wording/response bias:** “Much-needed” and “safer” push respondents toward support.

The wording plausibly pushes the estimate upward. The direction from undercoverage and nonresponse cannot be determined without explaining how excluded adults and nonrespondents differ in park support. A larger sample using the same flawed method does not remove these biases. Improve the frame, follow up with selected nonrespondents, and use neutral wording.

### P5

A has low bias and low variability. B has high upward bias and very low variability. C has low bias and high variability. **A is preferable**, because its estimates are concentrated near the true parameter. B's narrow spread does not make it accurate.

### P6

(a) is voluntary-response sampling because respondents self-select from an open invitation. (b) has nonresponse after an SRS was selected. The selected sample is **300 households**, with **180 respondents** and **120 nonrespondents**. Nonresponse causes bias if the response is related to characteristics relevant to the survey outcome.

## Worked answers - P7-P13

### P7

Explanatory: flashcard use. Response: exam score. Motivation may increase both the likelihood of choosing flashcards and the amount of other studying, raising scores. This creates a plausible alternative explanation for the association.

For a randomized comparison, label the 80 volunteers 1-80; randomly select 40 distinct labels for flashcards and assign the remaining 40 to a specified comparison method. Keep content and study time comparable, administer the same exam, and compare mean scores. The volunteered sample limits broad generalization, but random assignment supports causal analysis.

### P8

**Blocked:** Separate juniors and seniors. Randomly choose 12 of 24 juniors for online prep and give the other 12 classroom prep. Randomly choose 8 of 16 seniors for online prep and give the other 8 classroom prep. Compare formats within grade.

**Matched pairs:** Rank all 40 by prior score and form 20 adjacent-score pairs. Flip a coin within each pair to assign one student online prep and the other classroom prep. Compare scores within pairs. Randomizing who receives each treatment is necessary in both designs.

### P9

The **six greenhouses** are experimental units because temperature is assigned to entire greenhouses. There are only **three independently assigned units per treatment**, not 300. Plants within a greenhouse share its treatment and environment; more measured plants do not substitute for more independently assigned greenhouses. A person measuring plant growth can use coded samples/photos without knowing temperature assignments.

### P10

A = 18 / 40 = 0.45; B = 10 / 40 = 0.25. Difference = **0.20 = 20 percentage points**. Estimated tail probability = **18 / 1000 = 0.018 = 1.8%**.

If the two formats were equally effective, differences of at least 20 percentage points in A's favor occurred in only 1.8% of simulated random assignments. This is below 5%, giving convincing evidence that A produces a higher click rate in the studied setting.

One trial pools the 28 clicks and 52 non-clicks, randomly divides the 80 outcomes into two groups of 40, and records the A-minus-B click-rate difference. It represents one complete reassignment under the no-effect model.

### P11

The 0.28 is a probability of equally or more extreme **data assuming no effect**, not the probability that the treatments are equal. Because 0.28 is not small, there is insufficient evidence against no effect. Failure to find evidence of a difference does not prove equality.

### P12

1. Random sample, no random assignment: association can generalize to city residents; no causal claim from this design.
2. Volunteers, random assignment: causal conclusion for the experimental units if evidence is convincing; no automatic population generalization.
3. Both random steps: causal conclusion can generalize to the city's sampled population, assuming valid follow-up and conduct.
4. Convenience selection, no assignment: association among surveyed gym patrons; no established broad generalization or causal effect.

### P13

(a) **Stratified random sampling** by athlete status and a **randomized block experiment** using the same characteristic.

(b) Sampling randomly within each stratum supports representing the corresponding school groups. Assigning treatments randomly within each block tends to balance uncontrolled variables for the app-versus-print comparison.

(c) No. Equal athlete/non-athlete sample sizes are proportional only if half of the school's students are athletes. Otherwise a schoolwide estimate needs appropriate population weighting.

(d) Yes. Random assignment permits causal analysis when the experiment is properly conducted.

(e) No convincing causal-effect conclusion is established by “higher mean” alone. The difference could be chance variation; evaluate its statistical evidence before asserting effectiveness.

(f) Use the same assessment and testing conditions, preferably with scorers blinded to treatment. Compare app and print within athlete-status blocks, then combine evidence appropriately. Random sampling supports generalization to the school population with appropriate weighting and no serious coverage/nonresponse problems.

## Source clarifications and final checklist

### Clarifications to keep beside your class notes

- **Low variability:** Estimates are close to each other; they need not be close to the truth. The latter requires low bias too. The 2.2 key's wording blends these ideas.
- **Stratification:** Equal counts per group remain stratified sampling, but may require weights for a population estimate. It is not automatically proportional.
- **Clusters:** Heterogeneous clusters are often desirable; this is not the definition of cluster sampling.
- **Random-start procedures:** State the start range and stopping rule. The 2.3 hotel notes omit a start range; 1-10 gives exactly 50 rooms on a linear 500-room list.
- **Confounding:** Random assignment of people to two existing houses does not separate roof type from house identity. See 2.5's cell-service example.
- **Attrition:** Random assignment does not excuse large or differential dropout. See 2.5 HW Q3.
- **Replication:** More independent experimental units are needed; repeated observations of one person or many plants in one greenhouse are not equivalent.
- **Blinding:** Name who is unaware of the treatment assignments; participant-only and evaluator-only blinding are both possible.
- **Percentage points:** Differences such as 42% - 38% and 17.3% - 3.2% are 4 and 14.1 percentage points, respectively.
- **Significance:** A no-effect model, sampling variability, and sample size matter. Similar means in the song activity do not by themselves establish nonsignificance.
- **Scope:** The design determines what claims are possible; the data determine whether an effect is convincingly supported. Some 2.9 key answers compress these two steps.

### Source coverage

Every lesson's blank worksheet and homework was checked against its available answer keys. The 2.1 material supplies numbered word positions; the 2.9 material supplies the six inference cards. All 20 screenshots were reviewed, including overlapping captures, and their 20 distinct review questions are explained above. Original filenames, locations, sizes, and hashes appear in **Unit 2 Resources/inventory.json**; clickable file links appear in its **README.md**.

This is a synthesis of all supplied materials, not a line-by-line replacement of every homework answer. Use the original homework for further practice. Named scenarios and numerical results are classroom examples as supplied, not updates or independent checks of the underlying real-world studies.

### Ready-for-the-test checklist

- I can identify the exact population, selected sample, respondents, parameter, and statistic.
- I can describe SRS, stratified, cluster, and systematic sampling with actual random steps.
- I can explain why a method is biased and justify its likely direction in context.
- I can distinguish low bias from low variability.
- I can identify an experiment by treatment imposition and separate selection from assignment.
- I can explain both connections that make a variable a plausible confounder.
- I can design a fair comparison with random assignment, replication, control, and appropriate blinding.
- I can choose useful blocks, randomize within them, and recognize both forms of matched pairs.
- I can interpret a simulation dot, count the correct tail, and interpret significance under a no-effect model.
- I can make a conclusion that states both causation limits and the exact population scope.
