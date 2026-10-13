# Subtopic-wise Explanations

One file per subtopic that has at least one past-paper question. **84 files.**

Same subtopics, same block IDs, same `refs` as `../topicwise_answers_exam_style/`.
The two folders are generated from one source, `../../scripts/merge_map.csv`, by the
same `../../scripts/gen_topicwise.py` run twice, and gate **V4** compares their block
headings, their order and their provenance lines byte for byte. If one says
`[2017 Q.5(c)]` and the other says `[2017 Q.5(c), 2020 Q.3(b)]`, the build stops.

The headings carry the unit ids and nothing else, deliberately. A title after the
colon would have to be identical in both folders for V4 to pass, and the two
layers legitimately phrase the same question differently, so the question text
sits in the body where it belongs.

## What this layer adds

Reason. Not new numbers. The exam-style file shows the working. This file names
the method, states the formula, explains the substitution and warns about the
trap.

Every boxed number here is character identical to the exam-style file it came
from, and to the year-wise file above that. Three-way agreement, checked by gate
V8, which also confirms that no long numeral in this folder was born here.

## Block shape

```
### [2024 Q.3(b)]: Census Population, Estimate 1995

**Appeared in:** 2017 Q.5(c), 2020 Q.3(b), 2024 Q.3(b)

**What is asked.** The population of a town at a year outside the given range,
so this is extrapolation, not interpolation.

**Method.** Newton's divided difference extrapolation from the nearest tabulated
point. With five equally spaced decades the step is h = 10 years.

**Work.** ...
$$\boxed{P(1995) = 20.1888 \text{ thousand}}$$

> [!warning] Watch this
> Two of the three appearances change the target year and leave the tabulated
> data alone. Use the decade step, not the gap to the target year, when you
> build the difference table.
```

## Where the numbers come from

```
year-wise exam-style  ->  year-wise explanation  ->  subtopic-wise folders
      (origin)                (same characters)          (copied, never retyped)
```

No new number is ever born in a topic-wise file.

No em dashes. Plain words.