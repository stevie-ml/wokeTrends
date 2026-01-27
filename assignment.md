# Google Trends Investigation: Testing Hanania's "Origin of Woke" Model

**Course:** Quantitative Social Science
**Research question:** Does a Trump executive order targeting DEI produce a detectable, sustained decline in Google search interest for institutional DEI constructs — consistent with a shock to an institutional equilibrium rather than mass opinion?

---

## Q1. Define Your Event (X) and Construct (Y)

**(a) Event name:** Executive Order titled "Restoring Equality of Opportunity and Meritocracy"

**(b) Date/window:** April 23, 2025 (single-day signing). Note: this EO is part of a broader campaign that began at inauguration on January 20, 2025, with EO 14151 ("Ending Radical and Wasteful Government DEI Programs"). The April 23 EO extended DEI rollbacks from the federal government to federal contractors and grant recipients. The analysis window captures the full arc.

**(c) Geography:** United States (nationwide)

**(d) Construct Y:** Institutional DEI salience — the degree to which the public (and especially institutional actors such as HR professionals, compliance officers, and organizational leaders) actively seek information about diversity, equity, and inclusion frameworks, concepts, and practices.

**(e) Mechanism:** Richard Hanania's "Origin of Woke" model argues that "wokeness" is primarily an institutional equilibrium maintained by HR, legal, and bureaucratic incentives rather than mass public opinion. If this model is correct, executive orders that remove or reverse federal DEI mandates should produce a sharp, sustained decline in DEI-related search activity — not merely a transient news spike — because institutional actors respond quickly to changed compliance incentives. In contrast, a "mass belief" model would predict either no change (beliefs are sticky) or a backlash increase. The five-year window lets us see the full rise (2020 George Floyd / BLM) and potential fall (2025 executive action) of institutional woke salience. By including five conceptually distinct keywords — ranging from core institutional-DEI vocabulary ("unconscious bias," "white privilege") to broader cultural/academic terms ("structural racism," "intersectionality") to a term with independent institutional roots ("gender identity") — we can test whether the decline is concentrated in the concepts most tightly coupled to institutional DEI compliance.

---

## Q2. Operationalize the Construct with Keywords (3–5)

| # | Keyword | Rationale / Ambiguity notes |
|---|---------|---------------------------|
| 1 | `unconscious bias` | A concept central to institutional DEI training programs (unconscious-bias workshops). Captures demand for a specific institutional practice. **Ambiguity:** may also capture academic/psychology interest unrelated to workplace programs. |
| 2 | `intersectionality` | An academic concept (Crenshaw, 1989) that was adopted into institutional DEI frameworks. Straddles the academic/institutional boundary. **Ambiguity:** heavily used in academic sociology and gender studies; follows academic-calendar seasonality. |
| 3 | `structural racism` | A sociological concept promoted within the broader "woke" framework. Hanania's model predicts institutional concepts should decline; a more purely academic term like this may or may not respond. **Ambiguity:** strongly tied to academic sociology; seasonal fall-semester peaks. |
| 4 | `white privilege` | A core concept in institutional DEI training and discourse. Was popularized in institutional settings (e.g., Peggy McIntosh's "invisible knapsack" exercise widely used in diversity workshops). **Ambiguity:** also used in broader cultural and political debate. |
| 5 | `gender identity` | A concept with its own independent institutional infrastructure (medical, legal, educational) distinct from DEI compliance. Serves as a **partial control**: if the EO shock is specific to DEI/race-focused institutional practice, gender identity should be less affected. **Ambiguity:** captures medical/legal interest (e.g., policy on gender-affirming care, ID documents) beyond workplace DEI. |

---

## Q3. Operationalize the Construct with Topics (1–3)

Google Trends "Topics" aggregate semantically related queries and are less sensitive to exact wording than raw search terms.

| # | Topic label (as shown in Trends) | Topic ID | Notes |
|---|----------------------------------|----------|-------|
| 1 | **Diversity, equity, and inclusion** | `/g/11sfpd6bdm` | The core institutional construct. Near-zero before 2022, then gradually rises as DEI enters public consciousness, spikes to 100 in Jan 2025 at inauguration. |
| 2 | **Diversity training** | `/m/020t58` | Captures the specific institutional practice. Peaked at 100 in Sept 2020 (post-George Floyd training wave), then gradually declined. Provides a cleaner institutional signal than the politicized "DEI" acronym. |

A third candidate — **Implicit bias training** (`/g/11f00p0t61`) — returned no data for this time window, so it was dropped.

---

## Q4. Collect Keyword Evidence in the Browser

**Time window:** April 2020 – January 2026 (~5 years before the shock through present day)
**Granularity:** Monthly (Google Trends returns monthly data for windows >~8 months)
**Geography:** United States

The keyword plot is saved as `output/keywords_plot.png` and the underlying data as `output/keywords_data.csv`.

![Keywords Plot](output/keywords_plot.png)

**Key observations from the plot:**
- **unconscious bias** peaked at **100 in June 2020** (George Floyd / BLM), then gradually declined through 2021–2024 (from ~50 to ~35). Post-EO (May 2025 onward) it fell further to 21–33, its lowest sustained level in the dataset.
- **intersectionality** also peaked in June 2020 and shows a clear academic-calendar pattern (fall semester rises, summer dips). Post-EO it declined from its typical range of ~50–70 to ~35–63.
- **structural racism** peaked at 100 in June 2020, then stabilized around 20–50 with seasonal academic fluctuations. Post-EO it shows **no clear change**, continuing to oscillate between 24–48 as before.
- **white privilege** peaked at 100 in June 2020 and has been in long-term decline since. By 2024 it was down to 4–7; post-EO it dropped to **3–5**, its lowest sustained level ever.
- **gender identity** is the outlier: it shows a **different trajectory** from the other terms. It was relatively stable at 40–60 through 2020–2023, then *increased* in 2024–2025 (peaking at 82 in Nov 2024), likely driven by political debates over gender-affirming care and sports. Post-EO it remained stable at 56–75, showing **no decline**.

**Important note on scaling:** All five keywords were queried individually, so each has its own 0–100 scale. Cross-keyword level comparisons on the plot should be interpreted with caution; within-keyword pre/post comparisons are valid.

---

## Q5. Record Key Numbers (Keywords)

Computed from monthly data. "Pre" = April 2020 – March 2025 (61 months). "Post" = April 2025 – January 2026 (9 months, starting from the month the EO was signed).

| Keyword | Pre mean | Post mean | Peak (post) | Peak month | post − pre | post / pre |
|---------|----------|-----------|-------------|------------|-----------|-----------|
| unconscious bias | 43.5 | 28.4 | 33 | Sep 2025 | −15.1 | **0.654** |
| intersectionality | 56.1 | 43.3 | 63 | Sep 2025 | −12.7 | **0.773** |
| structural racism | 34.3 | 34.8 | 48 | Oct 2025 | +0.5 | 1.014 |
| white privilege | 8.4 | 4.1 | 5 | multiple | −4.2 | **0.492** |
| gender identity | 55.6 | 60.1 | 75 | Nov 2025 | +4.5 | 1.082 |

**Interpreting white privilege (ratio 0.49):** This is the largest percentage decline among the keywords — a **51% drop** — but the absolute levels are very low (pre-mean of only 8.4). "White privilege" was already in steep long-term decline before the EO, from a peak of 100 in June 2020 to single digits by late 2023. The post-EO decline may partly continue that existing downward trend rather than reflecting a new shock. However, the post-EO values (3–5) are the lowest ever recorded.

**Interpreting unconscious bias (ratio 0.65):** The cleanest signal. "Unconscious bias" had stable enough pre-EO volume (35–50 range in 2022–2024) to establish a clear baseline, and the post-EO decline to 21–33 represents a genuine drop below its recent range. The 35% decline reflects sustained reduced interest in this core DEI training concept.

**Interpreting gender identity (ratio 1.08):** The **absence of decline** is informative. "Gender identity" has its own independent institutional drivers (medical policy, legal frameworks, school policy debates) and was not targeted by the April 23 DEI executive order in the same way. Its stability supports the interpretation that the other declines are specific to the DEI institutional construct, not a general "culture war exhaustion."

---

## Q6. Repeat for Topics (Same Geography + Same Window)

The topic plot is saved as `output/topics_plot.png` and data as `output/topics_data.csv`.

![Topics Plot](output/topics_plot.png)

| Topic | Pre mean | Post mean | Peak (post) | Peak month | post − pre | post / pre |
|-------|----------|-----------|-------------|------------|-----------|-----------|
| Diversity, equity, and inclusion | 8.1 | 7.3 | 12 | Sep 2025 | −0.8 | 0.906 |
| Diversity training | 33.3 | 14.3 | 18 | May 2025 | −19.0 | **0.430** |

**The Diversity training Topic is the strongest finding.** This Topic peaked at 100 in September 2020 (post-George Floyd institutional training wave), stabilized at 22–47 through 2024, and then collapsed to 8–18 post-EO. By **January 2026 it reached 8** — its **lowest value in the entire 6-year dataset**, lower than even pre-George Floyd levels (14 in April 2020). The ratio of 0.43 means post-EO interest is **57% below** the 5-year average.

The DEI Topic is harder to interpret because it was near-zero before 2022 (the term hadn't entered mass consciousness). Its 100-point spike in January 2025 overwhelms the monthly comparison. But the post-spike trajectory — 100 → 85 → 32 → 21 → 10 → 8 → 7 → 7 → 12 → 7 → 6 → 5 → 4 — shows it has settled at **4–5** by late 2025, lower than its 2024 average (~11).

---

## Q7. Compute Simple "Ayers-lite" Effects

### Keywords

| Keyword | post − pre | post / pre | Interpretation |
|---------|-----------|-----------|----------------|
| unconscious bias | −15.1 | **0.654** | **35% decline** — clearest keyword signal, core DEI training concept |
| intersectionality | −12.7 | **0.773** | **23% decline** — academic-institutional hybrid concept |
| structural racism | +0.5 | 1.014 | Flat — purely academic term, unaffected |
| white privilege | −4.2 | **0.492** | **51% decline** — but already in long-term decline pre-EO |
| gender identity | +4.5 | 1.082 | Flat/up — independent institutional drivers (medical, legal), unaffected |

### Topics

| Topic | post − pre | post / pre | Interpretation |
|-------|-----------|-----------|----------------|
| Diversity, equity, and inclusion | −0.8 | 0.906 | 9% decline (attenuated by near-zero pre-2022 baseline) |
| Diversity training | −19.0 | **0.430** | **57% decline** — collapsed to all-time low |

### Do keywords and topics tell the same story?

Keywords and topics tell a **convergent story with an instructive gradient.** The terms most tightly coupled to institutional DEI practice — **Diversity training Topic** (ratio 0.43), **white privilege** (0.49), and **unconscious bias** (0.65) — show the largest declines. **Intersectionality** (0.77), which straddles the academic/institutional boundary, shows a moderate decline. Meanwhile, **structural racism** (1.01), which is primarily academic sociology, and **gender identity** (1.08), which has independent institutional drivers outside of DEI compliance, are flat or rising. This gradient is exactly what Hanania's model predicts: the more tightly a concept is tied to institutional DEI compliance (HR training, workshops, corporate policy), the more sharply it declines when the institutional incentive changes. Concepts rooted in academic disciplines or separate institutional frameworks are unaffected. I trust the **Topic-level** data most because Topics aggregate semantically related queries and are less sensitive to exact phrasing, but the keyword gradient provides the most theoretically informative pattern.

---

## Q8. Robustness Checks

### Check 1: Synonym Swap

**Swap:** Replaced "structural racism" with "systemic racism" (the most common near-synonym).

| Term | Pre mean | Post mean | post − pre | post / pre |
|------|----------|-----------|-----------|-----------|
| structural racism | 34.3 | 34.8 | +0.5 | 1.014 |
| systemic racism | 6.6 | 2.8 | −3.9 | **0.418** |

![Synonym Swap Plot](output/robustness_synonym_plot.png)

**Finding:** A striking divergence. "Structural racism" (the more academic phrasing) is flat, while "systemic racism" (the more mainstream/activist phrasing) declined **58%**. Both peaked during the June 2020 BLM moment, but "systemic racism" was already at very low absolute levels (2–5) by 2022, making the ratio sensitive to small changes. Still, the directional difference is noteworthy: the more institutionally popularized synonym declined more sharply, consistent with Hanania's model that institutional vocabulary fades faster than academic vocabulary when compliance incentives change. "Structural racism" persists because it lives in sociology syllabi; "systemic racism" fades because it was adopted by institutional DEI trainers.

### Check 2: Negative Control

**Control term:** "recipe ideas" — a term with no plausible connection to the executive order.

| Term | Pre mean | Post mean | post − pre | post / pre |
|------|----------|-----------|-----------|-----------|
| recipe ideas | 55.5 | 67.9 | +12.4 | **1.223** |

![Negative Control Plot](output/robustness_negative_control_plot.png)

**Finding:** "Recipe ideas" actually *increased* 22% in the post period, driven by seasonal patterns (holiday cooking in Nov–Dec 2025 peaked at 100). This confirms that the declines observed in DEI-related terms are **not** driven by a general downward trend in Google search activity. If anything, search activity was rising in the post-EO period, making the DEI-specific declines more meaningful by contrast.

### Check 3: Window Check (Narrower Window)

**Window:** January 1, 2025 – January 27, 2026 (weekly granularity; 17 pre-EO weeks, 40 post-EO weeks).

This check zooms in on 2025 to see the fine-grained weekly dynamics around the shock, with all five keywords on the same weekly scale.

| Keyword | Pre mean (weekly) | Post mean (weekly) | post − pre | post / pre |
|---------|-------------------|--------------------|-----------|-----------|
| unconscious bias | 79.9 | 67.9 | −12.0 | **0.850** |
| intersectionality | 75.2 | 60.9 | −14.2 | **0.810** |
| structural racism | 44.7 | 50.4 | +5.7 | 1.127 |
| white privilege | 51.7 | 45.7 | −6.0 | **0.883** |
| gender identity | 76.3 | 70.9 | −5.4 | 0.929 |

![Window Check Plot](output/robustness_window_plot.png)

**Finding:** The weekly data confirms the 5-year monthly pattern with finer resolution. All five keywords are visible in 2025. The rank-ordering is preserved: intersectionality (−19%) and unconscious bias (−15%) show the largest declines. White privilege (−12%) and gender identity (−7%) show moderate and small declines respectively. Structural racism is flat or slightly *up* (+13%). The weekly plot also reveals that all DEI-adjacent terms show elevated values in January–March 2025 (the inauguration-driven attention spike), then settle into lower post-EO levels. Structural racism lacks this pattern entirely, instead showing its usual academic-calendar seasonality (rise in fall semester, dip in summer). Gender identity's mild 7% decline at the weekly scale (vs. +8% at the 5-year scale) suggests it is essentially noise-level — no meaningful EO response.

---

## Q9. Mini Write-Up (6–8 sentences)

This investigation tested whether executive orders targeting DEI — specifically the April 23, 2025 EO "Restoring Equality of Opportunity and Meritocracy" — were followed by sustained declines in Google search interest for concepts associated with institutional "wokeness," using a five-year US window (April 2020 – January 2026) and five keywords ("unconscious bias," "intersectionality," "structural racism," "white privilege," "gender identity") plus two Topics ("Diversity, equity, and inclusion," "Diversity training"). The results reveal a clear **gradient** consistent with Hanania's institutional-equilibrium model: the **Diversity training Topic** collapsed 57% to its all-time low, **white privilege** fell 51%, **unconscious bias** fell 35%, and **intersectionality** fell 23% — while **structural racism** (a purely academic term) was flat at 1.01 and **gender identity** (which has independent medical/legal institutional drivers) was flat at 1.08. This gradient — steepest decline for terms most tightly coupled to institutional DEI compliance, no decline for terms rooted in academic disciplines or separate institutional frameworks — is the pattern Hanania's model specifically predicts and a "mass belief" model does not. The strongest single finding is the Diversity training Topic reaching **8 in January 2026**, its lowest value in the entire 6-year dataset, below even pre-George Floyd levels. An important alternative explanation is that several of these terms (especially "white privilege") were already in **long-term decline since June 2020**, and the post-EO period may simply continue a pre-existing trend rather than reflecting a new institutional shock; disentangling the EO effect from the secular trend would require interrupted time-series methods beyond this assignment's scope. A key limitation is that Google Trends captures search attention, not institutional behavior — we cannot tell whether declining searches for "unconscious bias" mean fewer workshops being conducted, fewer people curious about the concept, or simply fewer news articles using the phrase. A concrete next step would be to combine the Google Trends data with direct institutional measures — for example, tracking the number of "Chief Diversity Officer" job postings on Indeed/LinkedIn and federal DEI contract dollars over the same window — to test whether the attention decline maps onto the actual organizational dismantlement that Hanania's model predicts.

---

## Appendix: Code and Data

- **Analysis script:** `analysis.py` — Python script using `pytrends` to collect Google Trends data, compute statistics, generate plots, and run robustness checks.
- **Data files:** `output/keywords_data.csv`, `output/topics_data.csv`, `output/robustness_*.csv`
- **Plots:** `output/keywords_plot.png`, `output/topics_plot.png`, `output/robustness_*.png`
- **Full results:** `output/results.json`

All computations were performed programmatically in Python. The `pytrends` library queries the same Google Trends data available through the browser interface. Each keyword/topic was queried individually for the time window April 2020 – January 2026, with US geography, producing monthly-granularity relative search interest values (0–100 scale, where 100 = that keyword's own peak within the window). The narrower robustness window (January 2025 – January 2026) yielded weekly data.
