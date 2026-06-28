---
date: '2024-12-04T15:53:14+08:00'
draft: false
title: 'Economics Meets Physics: An Introduction to Granular Models of Company Growth'
math: true
---
[Original Link](https://mp.weixin.qq.com/s/BvD-oBcfVwCTCs3L8zFijQ)

Economic systems are more complex than physical systems. Can the methods and ideas of physics, which were developed for nature, be used to study human society? Econophysics tries to answer this question. It aims to find universal regularities in economic systems from data.

Firms are a useful example. As basic units of economic activity, they raise several natural questions. How can we discover laws of firm growth from complex firm-level data? Why do small firms often grow faster than large firms? Do larger firms face stronger fluctuations when markets are hit by shocks? Why do some firms rise and fall so sharply?

Granular models of firm growth try to answer these questions from the internal product structure and product diversity of firms. This article uses granular models as an example to introduce the research style of econophysics.

<!--more-->

The idea of a granularity effect first came from physics and materials science, where it describes the behavior of systems made of many discrete particles. Economics and finance later used the idea to describe small components of economic and financial systems, such as agents or assets. In firm modeling, granular models have helped explain several macroscopic facts about firm growth, including extreme fluctuations in growth rates.

Recently, José Moran, Angelo Secchi, and Jean-Philippe Bouchaud published *Revisiting Granular Models of Firm Growth*. This article uses that work as an entry point to review the development of quantitative models of firm growth and to introduce the econophysics approach through granular models.

## 1. What Is Econophysics?

Econophysics emerged in the 1990s, led by physicists such as Eugene Stanley. It brought methods from physics into economics. Traditional economics often studies aggregate economic growth at the macro level and supply, demand, input, and output at the micro level. Econophysics focuses more on empirical regularities in data. What is the size distribution of firms or financial assets? What is the distribution of growth rates? The many power laws found in economic systems during the 1990s attracted physicists and led to many physics-inspired models of economic systems.

There are also clear difficulties. Economic systems are more complex than physical systems. At first glance, these models may look too approximate and too far from reality. They also differ strongly from mainstream economics in both methods and questions. This can make econophysics look like an isolated project by physicists entering economics. Huang Jiping made a similar comment in his book *Econophysics*: studying human society, such as economic markets, can look like a new place for physicists to satisfy their curiosity.

But the link between economics and physics is old. Physics has influenced many sciences, including economics. The option pricing formula was inspired by Brownian motion. The discovery of power-law behavior in economic systems also pushed economists to correct some model assumptions. The Santa Fe Institute, a birthplace of complexity science, began with meetings that brought economists and physicists together. From this view, econophysics connects the closed mathematical kingdom of economics to the real world. It is not perfect, but it brings empirical reality back into the discussion. I therefore believe that the two fields can still talk to each other.

This article cannot give a full introduction to econophysics. Readers interested in the topic can read Wang Yougui's article on physics in economics and Huang Jiping's book *Econophysics*.

> Wang, Y., & Guo, L. (2010). Physics in the study on economics, 39(2), 85-94.  
> Huang, J. (2013). *Econophysics: Using Physical Methods or Ideas to Study Economic and Financial Problems*. Higher Education Press.

## 2. Econophysics Models and Firm Growth

Firm growth is directly related to economic growth and is an important part of it. In basic macroeconomic models, firms are important production units. They are also the smallest units of economic activity and an essential part of the economic system. Modeling firm growth helps us understand micro-level firm behavior and, at a more universal level, the growth of larger systems such as industries and countries.

At the micro level, firm growth depends on many factors. Economics and management have developed many theories about what drives firm growth. Modern science, however, requires more than theory. It requires systematic empirical tests. Case studies often have small samples and are hard to generalize. Large-sample methods, such as econometric analysis of time series, are also limited because many factors in firm growth interact in complex ways.

The econophysics approach follows the style of physics. It starts from real data and looks for patterns in complex firm-level data. Because firms are highly heterogeneous at the micro level, these patterns are usually found at the macro level. Examples include power-law distributions and self-similarity in stock-price fluctuations. The collection of large economic datasets since the 1990s made this approach possible. After finding macroscopic patterns, researchers build microscopic models to identify mechanisms, develop economic theory, and return to real-world explanation. Granular models of firms are a typical example of this loop.

## 3. Quantitative Models of Firm Growth: Does Growth Depend on Size?

Quantitative models of firm growth appeared in economics as early as 1937. Gibrat's law assumes proportionate growth and gives a simple baseline model. It assumes that the growth rate of a firm is an independent and identically distributed random variable $\epsilon$, independent of firm size:

$$
S_{t+1}-S_t=S_t\epsilon
$$

This dynamics implies that larger firms may face larger absolute fluctuations. It is also called the law of proportionate effect. The model is simple, but it remains important as a benchmark. Due to the theory-first style of economics and the limits of data at the time, its assumptions and conclusions were not fully tested with real data.

Later tests took two main directions. The first tested the key assumption: is firm growth rate related to firm size? Many econometric studies discussed this question. Technically it is a regression problem, but firm data are highly heterogeneous. Results differ by country, region, and industry. For example, Chinese firms appear closer to the proportional growth model than U.S. firms. A relatively common conclusion is that small firms grow faster than large firms, so growth rate and size are negatively related.

The second direction tested the macroscopic distribution implied by the model. The random growth process gives a lognormal size distribution. Stanley and coauthors showed that firm growth rates have a tent-shaped distribution: the center is close to a Laplace distribution, while the tails follow power laws. This is much more fat-tailed than a lognormal pattern. Today, Gibrat's law is generally viewed as incorrect as a full description, but useful as a benchmark. The work by Stanley's group led to more careful estimates of growth-rate distributions. It corrected the long-standing random-growth assumption in economics and made researchers take fat tails in firm growth seriously.

> Figure 1: Left, the distribution of firm growth rates. Right, the power-law decrease of growth-rate volatility with firm size.

A fat-tailed growth-rate distribution means that extreme growth fluctuations are larger than expected. Some firms rise and fall sharply. At the same time, data show that the width of the growth-rate distribution, that is, the variance of growth rates, decreases with firm size as a power law. The exponent is about 0.15. Thus, even though extreme growth events are larger than expected, large firms have relatively smaller growth-rate fluctuations.

These empirical facts lead to the next question: why do they appear? What market mechanism produces extreme growth fluctuations?

## 4. Granular Models of Firm Growth

Granular models try to explain these macroscopic facts. The term has two meanings. First, these models divide a firm into many basic particles. These particles follow simple growth rules. Firm growth is then the result of changes in the sizes and number of these particles. This idea has been widely used to model macroscopic distributions in complex systems. Fu and coauthors systematically applied it to firms, and Gabaix later gave it stronger economic meaning.

In the firm context, particles can be interpreted as products. Firm growth can be viewed as a combination of producing existing products, which changes particle size, and producing new types of products, which changes particle number. In *Revisiting Granular Models of Firm Growth*, the authors review models by Fu, Gabaix, Schwarzkopf, and others, and summarize them in a unified framework.

> Moran, J., Secchi, A., & Bouchaud, J.-P. (2024). Revisiting Granular Models of Firm Growth. *SSRN Electronic Journal*, 1-46. https://doi.org/10.2139/ssrn.4804771

### 4.1 Basic Setup

The basic setup is as follows. There are $N$ firms in the market. Each sufficiently large firm is made of a number of subunits, interpreted as products. Each subunit operates in an independent submarket. The size of firm $i$ at time $t$, denoted $S_{it}$, is the sum of its subunits:

$$
S_{it}=\sum_{j=1}^{K_i}s_{ijt}
$$

Here $K_i$ is the number of subunits in firm $i$, and $s_{ijt}$ is the size of subunit $j$ at time $t$.

A key assumption is that product size follows size-independent proportional growth:

$$
s_{ij,t+1}=(1+\sigma_0\eta_{ij,t})s_{ij,t}
$$

This has the same form as Gibrat's law, but the proportional growth mechanism is placed at the product level. Economically, it means that the number of products a firm can successfully commercialize is proportional to the number of products it has already commercialized.

The implied firm growth rate is also approximately proportionate, but its variance decreases with size as a power law, with an exponent near 0.5. This matches part of the data: the model reproduces the decline of growth volatility with size. But it also fails in important ways. Growth rates remain normally distributed, so the model does not reproduce the fat tails of growth rates. The predicted exponent is also much larger than the empirical value, so the model underestimates real growth fluctuations.

### 4.2 Introducing Heterogeneity

The setup above is shared by several granular models. The main differences come from different forms of heterogeneity. There are two major types.

The first is heterogeneity in product sizes across the whole market. The model assumes that product sizes $s_{ij}$ follow a power-law distribution. In other words, a small number of products take most market share, while many products take only small shares.

The second is heterogeneity in the number of product types within firms. The number of products $K_i$ differs across firms and may also follow a power law.

After adding these two forms of heterogeneity, the model can represent more realistic cases. Firms can be divided by product diversity:

- Some firms operate many products, and each product contributes to sales.
- Other firms have low diversity. This can happen in two ways:
  - A firm may have many product categories, but its size depends mainly on a few core products. Such a firm can still be large.
  - A firm may have only a few product categories, which usually also means it is small.

With this view, the authors show mathematically that the observed growth-rate distribution is closer to the coexistence of these different firm types. In particular, large firms that depend on only a few products are more likely to show extreme growth fluctuations. This fits intuition: firms with homogeneous product lines are more fragile under environmental shocks. At the aggregate level, such firms strongly affect the distribution of growth rates.

This reveals the second meaning of granular models: small local components can, under certain conditions, have strong effects on macroscopic system behavior.

The authors therefore propose that firm diversity is a key factor in the statistics of firm growth. Growth fluctuations are not driven only by firm size. They also depend on internal product structure and product richness. Inspired by this idea, the authors find a new empirical fact: after adjusting growth-rate volatility by average size, the distribution of growth volatility becomes size-independent. This is another important empirical contribution of the paper. In my view, the paper would be even stronger if it connected this theoretical insight more directly with existing economic theories.

> Figure 2: Left, growth-rate volatility calculated for different firm-size bins. Right, the result after rescaling by average size. See the original paper for the exact mathematical operation.

The authors also note that current granular models are limited. They still cannot fully explain the empirical distribution of growth rates and growth-rate volatility, especially in the tails. Current models overpredict the probability of highly volatile growth rates. One possible reason is that product-level shocks may no longer be independent as firm size increases, due to competition or supply-chain effects. This can be tested by studying how growth-rate autocorrelation depends on firm size. The paper does not develop this point further, making it a useful direction for future work.

## 5. Conclusion

This article introduced the use of granular models in the study of firm growth without going deeply into mathematical details. *Revisiting Granular Models of Firm Growth* brings together several core models and places them in a unified framework. I used that framework to review quantitative models of firm growth.

Granular models describe firm growth as the random dynamics of subunits. Economically, they describe how random market shocks affect firm growth. The same micro mechanism can also be used beyond firm growth. Gabaix used it to explain the micro origins of GDP fluctuations, and other studies used related ideas to model firm income dynamics.

This article also used granular models to introduce the research style of econophysics and its value for understanding economic systems. Economic complexity is widely recognized. Many econophysics models try to reproduce interesting macroscopic phenomena from microscopic mechanisms. Compared with traditional economic models, they start more directly from real data, travel through a mathematical model, and then return to the real world. Beyond granular models, many other physical models and perspectives may help discover economic laws, develop economic theory, and explain real phenomena. Those topics are left for another time.

## References

> [1] Moran, J., Secchi, A., & Bouchaud, J.-P. (2024). Revisiting Granular Models of Firm Growth. *SSRN Electronic Journal*, 1-46.  
> [2] Stanley. (1996). Scaling behavior of firm growth. *Nature*, 3.  
> [3] Fu, D., Pammolli, F., Buldyrev, S. V., Riccaboni, M., Matia, K., Yamasaki, K., & Stanley, H. E. (2005). The growth of business firms: Theoretical framework and empirical evidence. *PNAS*, 102(52), 18801-18806.  
> [4] Gabaix, X. (2011). The Granular Origins of Aggregate Fluctuations. *Econometrica*, 79(3), 733-772.  
> [5] Schwarzkopf, Y., Axtell, R. L., & Farmer, J. D. (2010). The cause of universality in growth fluctuations.  
> [6] Mizuno, T., Takayasu, M., & Takayasu, H. (2004). The mean-field approximation model of company's income growth. *Physica A*, 332(1-4), 403-411.
