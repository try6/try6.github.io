---
date: '2026-09-02T10:39:34+08:00'
draft: false
title: 'Two Explanations for Power Laws: Simon vs. Mandelbrot'
type: post
math: true
---

<!-- Original placeholder: [Image] -->
<!-- REVIEW: There is no corresponding image asset in this post bundle. A featured image can be added later. -->

Power-law distributions are ubiquitous statistical patterns in nature and society, but their origins have long been a subject of scientific debate. This article traces and compares two fundamentally opposed explanatory paradigms proposed by two intellectual giants: Herbert Simon and Benoit Mandelbrot. Simon's preferential-attachment model represents a generative perspective based on stochastic processes, path dependence, and micro-level causality. Mandelbrot's information-optimization model represents a design-oriented perspective based on global constraints, equilibrium, and teleology. Through precise mathematical formulations, this article explains the core of both models, explores their essential philosophical differences, and ultimately argues that these seemingly contradictory theories coexist and complement one another in modern complexity science.

<!--more-->

## Power Laws Everywhere

At the center of this debate is Zipf's law, a special kind of power-law distribution. The linguist George Kingsley Zipf popularized the law in the 1940s. He found that, in any sufficiently long corpus, if words are ranked by their frequency, a word's frequency is inversely proportional to its rank. For example, the most common word appears about twice as often as the second most common word and three times as often as the third, and so on. Mathematically,

$$
f(r)\sim \frac{1}{r^{\alpha}}
$$

where $f(r)$ is the frequency of the word with rank $r$, and the exponent $\alpha$ is approximately one.

This rank-frequency power law has since been repeatedly observed in many socioeconomic phenomena, including city populations, firm sizes, website traffic, and personal wealth. It raises an intriguing question: why do such different systems produce such similar statistical regularities? Does this simple mathematical form conceal a deep underlying principle? In the middle of the twentieth century, Herbert Simon and Benoit Mandelbrot proposed two very different explanations for the origins of power laws. Their long-running intellectual confrontation continues to shape our understanding of the complex world.

## The Simon Model: History, Chance, and “The Rich Get Richer”

Herbert Simon was a quintessential polymath: an economist, computer scientist, psychologist, and sociologist. He received the Turing Award in 1975 and the Nobel Memorial Prize in Economic Sciences in 1978. Before the AI pioneer Geoffrey Hinton, Simon was the only person in history to have received both a Nobel Prize and a Turing Award. He was also a pioneer of bounded rationality and artificial intelligence.

<!-- Original placeholder: [Image] -->
<!-- REVIEW: There is no Herbert Simon image in this post bundle. The following line may be used as its caption if one is added. -->

> Herbert Alexander Simon, American economist, political scientist, cognitive psychologist, and computer scientist. See the [JiZhi Encyclopedia entry](https://wiki.swarma.org/index.php/%E8%B5%AB%E4%BC%AF%E7%89%B9%C2%B7%E4%BA%9A%E5%8E%86%E5%B1%B1%E5%A4%A7%C2%B7%E8%A5%BF%E8%92%99_Herbert_Alexander_Simon) for details.

In 1955, Simon published his famous paper *On a Class of Skew Distribution Functions*. It presented an elegant mechanism for explaining Zipf's law, which later became known as the Simon model or preferential attachment.

Simon's explanation is a story about **process**. He argued that a power-law distribution is the inevitable product of a particular stochastic process evolving through time. His model is dynamic, generative, and path dependent. We can describe the process precisely through the example of urban population growth. Suppose that we have a growing system of cities:

1. **A new member arrives.** At every time step $t$, one “new resident” enters the system.
2. **The resident chooses where to settle.**
   - With a small, fixed probability $p$, the resident founds a new city—that is, a new category of size one.
   - With probability $1-p$, the resident moves to an existing city.
3. **Preferential attachment applies.** If the resident chooses an existing city, the probability of selecting a particular city is proportional to that city's current population.

The next part gives a somewhat more rigorous mathematical description, but it can be skipped without affecting a qualitative understanding of the article.

Let $N_k(t)$ be the number of cities with population $k$ at time $t$. At the next time step, $t+1$, the total population increases from $t$ to $t+1$. Consider a city of size $k$. Its population can change in the following way:

- **Population growth ($k→k+1$).** A new resident moves in. The probability of this event is proportional to both the population $k$ of each city and the number $N_k(t)$ of such cities in the system. The total probability is $\frac{(1−p)kN_k(t)}{t}$.
- The original Simon model does not include population decline.

We can construct a master equation for the change in the number of cities of different sizes:

$$
N_k(t+1)-N_k(t) = p\delta_{k1} + \frac{1-p}{t} \left[ (k-1)N_{k-1}(t)-kN_k(t) \right].
$$

Here $\delta_{k1}$ is the Kronecker delta, which distinguishes the birth of a new city when $K=1$ from the population change of an existing city when $K>1$.

Simon showed that, when $t→∞$, the fraction of cities with population $k$, $f(k)=N_k/∑_iN_i$, satisfies $f(k)∝k^{−α}$, where $α=1+\frac{p}{1−p}$. In particular, when the probability of a new city appearing is very small ($p→0$), $α→1$. This provides a perfect explanation of Zipf's law.

<!-- REVIEW: This passage may conflate the size-distribution exponent with the rank-frequency exponent. Standard presentations of the Simon model commonly use different exponents for these related distributions. The original statement and formula have been retained for review. -->

The essence of the Simon model can be summarized in three points:

- **Path dependence.** A city's accidental early success reinforces itself, allowing the city to attract more resources later. The system's final state depends strongly on its evolutionary path.
- **Micro-causality.** The model provides a clear, step-by-step causal chain. Individuals make decisions using local information—the size of a city—and the macroscopic power-law distribution emerges from the accumulation of these microscopic actions.
- **Structure within randomness.** Randomness is not completely uniform. It is structured by preferential attachment, and this structure produces inequality.

## The Mandelbrot Model: Efficiency, Constraints, and “Optimal Design”

Benoit Mandelbrot was also a wide-ranging polymath. He was a mathematician and an IBM researcher, and his most representative contribution was the concept of fractals. He is known as the father of fractal geometry. Scale invariance and optimization were central themes throughout his research career. Unlike Simon, Mandelbrot therefore tended to search for universal mathematical structures from a global, static, and even teleological perspective.

<!-- Original placeholder: [Image] -->
<!-- REVIEW: There is no Benoit Mandelbrot image in this post bundle. The following line may be used as its caption if one is added. -->

> Benoit Mandelbrot, founder of fractal geometry.

In his doctoral dissertation and the subsequent paper *An Informational Theory of the Statistical Structure of Language*, Mandelbrot first proposed an optimization-based explanation of Zipf's law. He treated language as a communication system and assumed that its evolution followed a principle of “maximizing efficiency.”

More specifically, he assumed that, when people communicate, they unconsciously balance the maximization of transmitted information against the minimization of encoding and decoding costs. He constructed a model in which the “cost” of a word was related to its length or difficulty of pronunciation. Using Lagrange multipliers for constrained optimization, he found that, under a fixed average-cost constraint, maximizing information entropy—that is, the amount of information—requires word frequencies to follow a power-law distribution. This elegant explanation attributes Zipf's law to the maximization of communication efficiency.

Unlike Simon's process-based theory, Mandelbrot's explanation is therefore a story about **state**. He argued that a power-law distribution indicates an optimal equilibrium state reached by a system under particular constraints. His classic model treats language as an optimized communication code.

Here is a more rigorous mathematical formulation.

Suppose a vocabulary contains $M$ words. The frequency of the $i$th word is $p_i$, and its “cost”—such as its length or pronunciation difficulty—is $C_i$. Mandelbrot's objective was to maximize the entropy of language while keeping the total average cost fixed.

1. **Information entropy ($H$):** a measure of information or uncertainty.

   $$
   H=−\sum_{i=1}^M p_i log p_i
   $$

2. **Cost constraint ($C$):** the total average cost is a constant $C_0$.

   $$
   C=\sum_{i=1}^M p_iC_i=C_0
   $$

3. **Probability normalization:**

   $$
   \sum_{i=1}^M p_i=1
   $$

This is a classic constrained-optimization problem that can be solved with Lagrange multipliers. We construct the Lagrangian $L$:

$$
L(p_1,...,p_M,\lambda,\beta)=H−\lambda(\sum p_iC_i−C_0)−\beta(\sum p_i−1)
$$

Taking the partial derivative with respect to any $p_i$ and setting it to zero, $\frac{∂L}{∂p_i}=0$, gives

$$
−log⁡p_i−1−λC_i−β=0
$$

$$
p_i=e^{−1−β}e^{−λC_i}
$$

This result shows that the optimal frequency $p_i$ decays exponentially with the cost $C_i$. It is not yet a power law. Mandelbrot then made a crucial assumption about the relationship between cost and rank. An efficient coding system assigns the lowest costs to the most frequently used words. He assumed that a word's cost $C_i$ was proportional to the logarithm of its frequency rank $r_i$, so that $C_i∝log⁡r_i$. This assumption also follows from coding ideas in information theory. Substituting $C_r=Alog⁡r+B$, where $r$ is the rank, gives

$$
p(r)∝e^{−λ(Alog⁡r+B)}=(e^{−λB})(e^{log⁡r})^{−λA}=Const⋅r^{−λA}
$$

Letting $α=λA$, we obtain a standard power-law distribution:

$$
p(r)∝\frac{1}{r^α}
$$

The essence of the Mandelbrot model can likewise be summarized in three points:

- **Teleology.** The model assumes that the system has a “goal”: maximizing efficiency. The distribution realizes this goal rather than emerging from an unconscious evolutionary process.
- **Global optimization.** It describes an optimal static solution selected by the whole system from among all possibilities, without considering the particular dynamics through which that solution is reached.
- **A principle of universality.** The power law is attributed to a universal economic or physical principle—maximizing some utility function under constraints—rather than to the historical contingencies of a particular system.

## The Debate Between Simon and Mandelbrot

Although Mandelbrot was several years younger than Simon, and Simon was already a well-known economist when their power-law models appeared, the young Mandelbrot was perhaps dismissive of Simon's model and took the initiative in attacking it. This led to a remarkable exchange in the journal *Information and Control*.

<!-- Original placeholder: [Image] -->
<!-- REVIEW: There is no image corresponding to this exchange in the post bundle. -->

The paper titles alone convey the flavor of the exchange:

- Benoit Mandelbrot (1959): "a Note "on a class of skew distribution functions:analysis and critique of a paper by H.A. simon"
- Herbert  A. Simon (1960): "Some Further Notes on a Class of Skew Distribution Functions"
- Benoit Mandelbrot (1961): "Final Note on a Class of Skew Distribution Functions: Analysis and Critique of a Model Due to H. A. Simon"
- Herbert  A. Simon (1961): Reply to "Final Note" by Benoit Mandelbrot
- Benoit Mandelbrot (1961): "Post Scriptum to "Final Note""
- Herbert  A. Simon (1961): "Reply to Dr. Mandeibrot's Post Scripture"

<!-- REVIEW: The titles above contain apparent capitalization, quotation-mark, and spelling issues, including “Mandeibrot” and “Post Scripture.” They have been retained from the source text for review; the journal records give the official titles. -->

The public debate ended when the editors of *Information and Control* appeared unwilling to muddy the waters any further, but the two scholars did not reach a substantive agreement. The language of their papers became increasingly blunt. In the final exchange, each abstract consisted of only one sentence, conveying how firmly opposed they had become.

> **Benoit Mandelbrot:** My criticism has not changed since I first had the privilege of commenting upon a draft of Simon (1955).

> **Herbert A. Simon:** Dr. Mandelbrot has proposed a new set of objections to my 1955 models of the Yule distribution. Like his earlier objections, these are invalid.

My personal impression is that Mandelbrot was indeed somewhat inclined to find fault. From my broad reading of these papers, Simon initially responded seriously to Mandelbrot's objections and even extended his model in response. Mandelbrot remained unconvinced and raised entirely new objections in later notes. Simon also mentioned this interesting debate in his autobiography, whereas Mandelbrot did not mention it at all.

Returning to their fundamental disagreement, Mandelbrot regarded Simon's explanation as “special-case” and “trivial.” He mocked it in the following terms: “You can ‘explain’ a power-law result by assuming a power-law process, but this does not really explain anything.” In his view, Simon had simply encoded the power law directly into the model's assumptions, because making selection probability proportional to the number of previous occurrences is itself a power-law tendency.

<!-- REVIEW: The sentence above is presented as a direct quotation, but the draft does not provide its exact source or page number. It has been retained unchanged in meaning for review. -->

Simon replied that his model was based on a very simple and intuitive mechanism, widely known in sociology as the Matthew effect. It was a causal mechanism that explained how the distribution evolved step by step. Mandelbrot's optimization model, although mathematically elegant, resembled a “black box”: it assumed that the system reached an optimal equilibrium but did not explain how the system arrived there. It was closer to a teleological explanation—one based on achieving a goal—than to a causal explanation.

From today's perspective, history did not declare a single winner. Instead, it revealed the value and range of application of both intellectual paradigms. For a long time, Mandelbrot's reputation in mathematics and his later success in fractal geometry seemed to make his perspective more attractive to physicists and mathematicians. Simon's model, by contrast, developed deep roots in the social sciences, computer science, and especially the later field of network science.

In 1999, the physicists Barabási and Albert “rediscovered” preferential attachment and used it to explain the scale-free properties of complex networks such as the World Wide Web and social networks. It was a “rediscovery” because they did not cite Simon's paper, and others later pointed out that the BA model is essentially a graph-theoretic variant of the Simon model. This development brought a major revival of Simon's process-based thinking in twenty-first-century complexity science. Preferential attachment is now a standard model for explaining many kinds of growth phenomena.

Mandelbrot's ideas of optimization and scale invariance, meanwhile, became foundations of fractal theory, chaos theory, and financial-market analysis, including multifractal models. His work emphasized the self-similar structures that systems exhibit at different scales, a perspective that is essential in physics and many other natural sciences.

The debate between Simon and Mandelbrot therefore did not end in victory for either side. Instead, it left later researchers with two powerful intellectual tools. When confronting a power-law phenomenon, we can ask, “How did it become this way, step by step?”—Simon's question. We can also ask, “Does its existence in this form satisfy some principle of optimality?”—Mandelbrot's question. The significance of their debate lies not in telling us who was right or wrong, but in clearly displaying two paths of scientific explanation: process-driven and historical explanation versus state-driven and universal explanation. Together, these paths give us a fuller picture of a complex world interwoven with randomness and order.

---

## References

1. Herbert A. Simon. On a Class of Skew Distribution Functions. Biometrika, 1955, 42(3/4): 425-440
2. Mandelbrot, B. An Information Theory of the Statistical Structure of Language. Communication Theory, 1953, 84: 486-502
3. https://mp.weixin.qq.com/s/iRUVTGFV3Y_gQoLpoku2Eg
4. https://mp.weixin.qq.com/s/zzUuP8mLoO-TElmbdbjmYg
5. https://mp.weixin.qq.com/s/zBBB7KiEf2p8CpOkxZs8FQ
6. https://mp.weixin.qq.com/s/MeQ6r4BbUWErdCfsYN3YcA
7. https://mp.weixin.qq.com/s/h5gvnaU-0LsYDiICtSU49g

<!-- REVIEW: Reference 2 uses “An Information Theory...” while the body uses “An Informational Theory...”; “84” before the page range may also not be a volume number. The source text has been retained for review. -->
