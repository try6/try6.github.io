---
date: '2026-06-04T15:53:14+08:00'
draft: false
title: 'The Trade-off Between Efficiency and Risk: Understanding the Economic World at the Edge of Criticality'
math: true
---

[Original Link](https://mp.weixin.qq.com/s/x-Y0WjNSYYjVj6vS6uv9Yg)

This article reviews self-organized criticality in economic and financial systems. It takes econophysics as the entry point and follows Jean-Philippe Bouchaud's 2025 review, *The Self-Organized Criticality Paradigm in Economics & Finance*, to summarize how the idea of self-organized criticality has developed in these fields.

<!--more-->

> [1] Bouchaud, J.-P. (2026). *Mandelbrot, Financial Markets and the Origins of "Econophysics."* http://arxiv.org/abs/2602.02078  
> [2] Bouchaud, J.-P. (2025). *The Self-Organized Criticality Paradigm in Economics & Finance.* http://arxiv.org/abs/2407.10284

## Introduction

Modern economic and financial systems are deeply embedded in global supply chains, cross-border capital flows, and layered financial derivatives. Although deglobalization is often discussed, real economies have become more tightly and more complexly connected. A single chip may require production steps across several countries. Global payment systems move capital across borders in milliseconds. Large asset managers hold core assets in many major markets at the same time, so risks can travel through portfolios across markets. Changes in dollar liquidity can quickly affect exchange rates and debt costs in emerging markets. These global coupling structures make economies rise and fall together. Estimating the impact of external crises, and limiting the damage, is therefore central to economic stability.

What is most disturbing is not the existence of crises, but the feeling that crises often lack a proportional cause. Markets sometimes crash without obvious major bad news. On Black Monday in 1987, global stock markets fell sharply in one day, yet no fundamental shock seemed large enough to explain the fall. Cutler, Poterba, and Summers studied the relation between news and stock market movements in 1989 and found that many crashes have no clear external event signal. Fluctuations that cannot be explained by fundamentals are often called excess volatility.

> [3] Cutler, D. M., Poterba, J. M., & Summers, L. H. (1989). What Moves Stock Prices? *Journal of Portfolio Management*, 15(3), 4-12.

These problems are not new. They have long stayed near the edge of mainstream economic theory. Equilibrium models, rational expectations, representative agents, and efficient markets may help explain long-run trends and average behavior. They are much weaker when they face violent fluctuations, extreme events, and systemic instability. In this setting, a research path from statistical physics gradually took shape. It emphasizes empirical facts, the structure of fluctuations, and collective dynamics. It is now known as econophysics.

## 1. From Statistical Physics to Financial Systems

Physics also moved from reductionism toward a more systemic view during the twentieth century. Spin glasses, critical phenomena, turbulence, and non-equilibrium systems are typical examples. In these systems, physicists are used to several facts: macroscopic behavior cannot be obtained by simply adding microscopic parts; small perturbations can trigger highly nonlinear responses; fluctuations are not just noise, but part of the structure of the system.

From this perspective, economic systems, especially financial markets, look familiar to physicists. Price time series show fat tails, volatility clustering, and long memory. These patterns are strikingly similar to the statistical features of turbulence, critical systems, and disordered media.

Benoit Mandelbrot, the father of fractals, argued in his 1963 paper on speculative prices that price changes in financial markets are not Gaussian. They have fat tails. This means large price movements are not rare anomalies. They are part of the distribution itself. Around the same time, Herbert Simon also noticed fat-tailed distributions in economic systems.

> [4] Mandelbrot, B. (1963). The Variation of Certain Speculative Prices. *The Journal of Business*, 36, 394.

Mandelbrot and Simon approached the issue from different backgrounds. One started from optimality. The other used preferential attachment in stochastic processes. Both offered elegant mathematical mechanisms for fat-tailed distributions. Around 1960, they also published a sequence of papers in *Information and Control* debating what mechanism should explain such distributions. That debate is worth a separate discussion.

At the time, however, these ideas were treated as marginal by mainstream economics. Standard models did not produce these phenomena, and simple extensions did not explain them well. Because economic theory had developed a highly polished mathematical structure, these statistical regularities were often seen as secondary deviations or measurement errors, not as facts that theory had to explain directly. As a result, Mandelbrot's and Simon's emphasis on fat tails did not receive sustained mainstream attention.

This changed in the early 1990s, when the American physicist Eugene Stanley helped launch econophysics as a visible research program. During that period, many empirical and theoretical works used methods from physics to describe and model power laws in economic systems and the mechanisms behind them. *Physica A*, originally a journal close to traditional statistical physics, became an important venue for complex systems and econophysics. Thanks to this line of work, fat tails, volatility clustering, and related properties in economic systems are now recognized as robust statistical regularities that appear across markets and time periods.

## 2. From Empirical Facts to Mechanisms: Why Are These Systems So Sensitive?

Respect for empirical facts is the starting point of econophysics. The deeper question is mechanism: why do economic and financial systems so easily turn small perturbations into large events? It is not enough to say that fat tails and volatility clustering exist. Any serious explanation has to address the mechanism.

Bouchaud's 2025 review offers one framework for this question and moves the methodology of econophysics to a more theoretical level. Below, I use that work as a guide to review representative examples of self-organized criticality in economic and financial systems. Before doing so, I briefly introduce self-organized criticality.

> Note: Jean-Philippe Bouchaud is one of the central figures in modern econophysics. Unlike many econophysicists who try to hide physics terminology when speaking to economists, Bouchaud still presents the econophysics perspective clearly. He was trained in the French tradition of statistical physics. In the early 1990s he worked mainly on statistical physics, and later turned to financial markets, applying physical methods to market fluctuations and risk modeling. He also founded the quantitative investment firm CFM, linking academic research with financial practice. CFM is now a leading global quantitative firm, known for strong risk control and stable returns.

### 2.1 A Brief Introduction to Self-Organized Criticality

Self-organized criticality, or SOC, was first proposed by Per Bak in 1987. It describes open, dissipative many-body systems that can evolve toward a critical state under continuous external driving, without fine tuning. SOC was first used to describe systems such as the sandpile model, which has slow driving and fast relaxation. Energy accumulates gradually and is then released intermittently through sudden events.

A critical branching process gives a quantitative description of this idea. Consider a sandpile. When grains are randomly placed on a finite grid, the local slope increases. Once the slope at a location exceeds a threshold, that location topples. Sand is transferred to neighboring locations and increases their slopes.

A general form is the following. Suppose one rolling grain can knock down $n$ other grains, and these grains can in turn knock down more grains. Let $n$ be an independent and identically distributed random variable with distribution $p(n;R_0)$, finite second moment, and mean

$$
E[n]=R_0
$$

Here $R_0$ is the basic reproduction number. When $R_0<1$, one unstable grain knocks down only a finite number of other grains on average. The mean avalanche size is

$$
(1-R_0)^{-1}
$$

and the probability of large avalanches decays exponentially. When $R_0 \to 1$, however, a single grain can trigger large damage. When $R_0=1$, the avalanche size $S$ follows a scale-free power-law distribution,

$$
P(S) \sim S^{-3/2}
$$

and its mean diverges. In a self-organized critical system, feedback drives the system toward the critical state near $R_0=1$.

Once a system reaches criticality, its observable signatures include not only a power-law distribution of avalanche sizes, but also power laws in avalanche durations, correlation lengths and time scales that extend to the system scale, and in some cases an approximate $1/f$ noise spectrum. SOC is therefore a canonical mechanism for scale-free fluctuations and sudden cascades in natural systems.

> Further reading: [Sandpile model](https://swarma.org/?p=24464)  
> Bak, P. (2013). *How Nature Works: The Science of Self-Organized Criticality*. Springer Science & Business Media.

Many phenomena in economic and financial systems are close to this SOC picture. Inspired by SOC, Per Bak and coauthors modeled an economy using a sandpile-like production network. In their classic model, the input-output network of firms is placed on a lattice. Each site is a firm, and neighboring sites are upstream or downstream supply-chain partners. After assigning capacity and orders to firms, the system responds to exogenous demand shocks as a self-organized critical production network. Demand shocks propagate upstream like grains on a sandpile, producing avalanches with a power-law size distribution. In this view, the economy evolves toward a critical state and becomes volatile and fragile.

> [5] Bak, P., Chen, K., Scheinkman, J., & Woodford, M. (1993). Aggregate fluctuations from independent sectoral shocks: Self-organized criticality in a model of production and inventory dynamics. *Ricerche Economiche*, 47(1), 3-30.

This paper contains many useful ideas, but the model that Bak built to explain spontaneous large output fluctuations is somewhat artificial. It feels designed to create self-organized criticality. For economic systems, it remains mainly a qualitative theory with limited direct guidance for real-world analysis.

### 2.2 Self-Organized Criticality in Economic Systems

#### a. Timeliness Criticality

A more realistic way to interpret Bak's framework is to study how production delays propagate along supply chains. The core logic is simple: if intermediate inputs do not arrive on time, production must stop unless firms hold enough buffers.

Moran and coauthors proposed the idea of timeliness criticality. They showed that the buffer time has a critical value $B_c$. When the actual buffer $B$ is larger than $B_c$, reducing the buffer has little effect on the whole system and causes only small occasional disruptions. Firms therefore find it reasonable to keep reducing $B$, until a major systemic failure occurs. After such failures, regulators often intervene and require firms to keep safety margins. This process is close to a sandpile whose slope slowly crosses a critical value.

> [6] Moran, J., Romeijnders, M., Doussal, P. L., Pijpers, F. P., Weitzel, U., Panja, D., & Bouchaud, J. P. (2024). Timeliness criticality in complex systems. *Nature Physics*, 20(8), 1352-1358. https://doi.org/10.1038/s41567-024-02525-w

The same logic applies to supply shocks in production networks. To reduce costs, firms keep inventories of production inputs as low as possible. In a just-in-time supply chain, any delay can travel through the network and produce large disruptions. Local cost cutting by individual firms may unintentionally push the whole system toward criticality. The argument also extends naturally to other settings, such as bank liquidity regulation, where the same tension appears between the local cost of holding liquidity and systemic risk.

> Further reading: [JiZhi article](https://mp.weixin.qq.com/s/sRnq6mfa9sKdHCIg7mfg2g)  
> [7] Moran, J., Pijpers, F. P., Weitzel, U., Bouchaud, J., & Panja, D. (2025). Critical fragility in sociotechnical systems. *Proceedings of the National Academy of Sciences*, 122(9), e2415139122. https://doi.org/10.1073/pnas.2415139122

#### b. Production Networks: From Static Equilibrium to Dynamic Non-Equilibrium

Another view of shock propagation in production networks focuses on network effects. Under economic equilibrium assumptions, heterogeneous productivity shocks can be amplified through supply and demand links between firms and affect aggregate output. Further analysis shows that this abnormal volatility is related to Gabaix's granular hypothesis. When network topology makes firm size, measured by total sales, follow a power-law distribution, aggregation effects become important. Idiosyncratic shocks to large firms can become a dominant source of GDP fluctuations. But equilibrium models have important limits, and later work introduced linear approximations to study non-equilibrium shock propagation.

> Further reading: [JiZhi article](https://mp.weixin.qq.com/s/BvD-oBcfVwCTCs3L8zFijQ)  
> [8] Moran, J., Secchi, A., & Bouchaud, J.-P. (2024). Revisiting Granular Models of Firm Growth. *SSRN Electronic Journal*, 1-46. https://doi.org/10.2139/ssrn.4804771  
> [9] Dessertaine, T., Moran, J., Benzaquen, M., & Bouchaud, J.-P. (2022). Out-of-equilibrium dynamics and excess volatility in firm networks. *Journal of Economic Dynamics and Control*, 138, 104362.

Beyond shock propagation, another force in economic evolution is the increasing complexity of production. Technological progress changes the supply-chain network: production uses more intermediate inputs, the average network degree rises, and productivity also rises. At the same time, production costs increase. We can infer that average productivity $\bar{z}$ tends to fluctuate around the minimum threshold needed to keep the system running. Sometimes it falls behind that threshold, which can trigger occasional endogenous crises.

#### c. Repricing Avalanches

A 2024 paper raised a highly suggestive question. Nirei and Scheinkman argued that firms' repricing decisions, meaning price increases in response to inflation, are clustered in time. In other words, inflation can occur in waves or avalanches.

They built a carefully designed equilibrium model for the repricing strategy of profit-maximizing firms. The core mechanism is that one firm's price increase raises the average inflation faced by its customers, which then encourages other firms to raise prices. This is the basic mechanism of a repricing avalanche. The model has several interesting implications. First, empirical calibration suggests that real systems are very close to criticality. The model is critical at $J=1$, while estimates for several countries give $J \approx 0.88-0.95$. Second, the model predicts that inflation volatility rises with the level of inflation, which is also consistent with data.

> [10] Nirei, M., & Scheinkman, J. A. (2024). Repricing avalanches. *Journal of Political Economy*, 132(4), 1327-1388.

A closely related model appears in work on endogenous bankruptcy waves. That paper focuses on the case $J>1$. In this regime, the system has no steady state and instead shows oscillating business-cycle dynamics. The feedback mechanism synchronizes firm bankruptcies and produces sharp increases in unemployment. In the Nirei-Scheinkman model, one may expect similar inflation cycles when $J>1$, although monetary policy could change the result substantially.

> [11] Gualdi, S., Bouchaud, J.-P., Cencetti, G., Tarzia, M., & Zamponi, F. (2015). Endogenous crisis waves: Stochastic model with synchronized collective behavior. *Physical Review Letters*, 114(8), 088701.

Repricing avalanches remain a phenomenological model. An open question is why empirical values of $J$ are so close to 1. In other words, why is the system close to criticality? This still needs further study.

### 2.3 Self-Organized Criticality in Financial Markets

Asset price series in financial markets also show puzzling statistical features that resemble critical systems. For example, the distribution of daily returns $r$ has fat tails on both the positive and negative sides and follows a power-law decay. For almost all traded assets, the tail has the form

$$
|r|^{-1-\alpha}
$$

where $\alpha$ is usually between 3 and 5. A second important feature is long memory. Volatility, market activity, and the direction of market orders all have autocorrelation functions that can be fitted by slowly decaying power laws.

There are also non-critical explanations for power laws and long memory. The strongest sign of market criticality is different: most large price jumps seem unrelated to specific real-world events. As noted above, at least in mainstream news sources, one often cannot find a clear trigger. This is excess volatility, and it is the focus here.

#### a. Near-Critical Self-Feedback

Researchers have often argued that endogenous feedback loops may cause excess volatility in financial markets. The classic ARCH framework is the simplest model of how past realized volatility feeds back into future volatility. It assumes that daily returns can be written as

$$
r_t=\sigma_t \xi_t
$$

where $\xi_t$ is independent standard Gaussian noise and $\sigma_t$ is time-varying volatility. The model can be generalized into the feedback equation

$$
\sigma_t^2 = \sigma_0^2 + \sum_{s<t} \Phi(t-s)r_s^2
$$

where $\Phi$ is a kernel. Taking the time average and assuming stationarity gives the average squared volatility $\sigma_\infty^2=E_t[\sigma_t^2]$:

$$
\sigma_\infty^2=\frac{\sigma_0^2}{1-g}, \qquad g:=\sum_{\tau=1}^{\infty}\Phi(\tau)<1
$$

This result shows that the feedback strength, measured by $g$, is a source of excess volatility. When $g \to 1$, self-feedback becomes very strong and volatility can explode. Again, $g=1$ is the critical value. Empirical calibrations of ARCH-type models find high feedback values, usually $g \gtrsim 0.8$, and the kernel $\Phi(\tau)$ decays as a power law.

This remains a phenomenological model. It does not explain the micro-level origin of excess volatility.

#### b. Critical Liquidity

One plausible explanation of financial-market criticality starts from a basic tension at the core of every market: buyers want to buy at low prices, and sellers want to sell at high prices. Market makers reduce this tension. They buy from sellers and sell to buyers, or the reverse, and provide immediacy and liquidity. Their profit comes from the bid-ask spread.

But market makers always face adverse selection. They must post binding bid and ask quotes, and informed traders may exploit these quotes. This can expose market makers to large losses. As a result, their profit distribution is strongly negatively skewed.

Because extreme losses are always possible, market makers quickly widen spreads and reduce the amount of liquidity they are willing to provide when market volatility rises. This simple logic shows why liquidity is fragile. First, high volatility can trigger a liquidity crisis. In such a state, no bid-ask spread allows market makers to break even. Second, liquidity can disappear almost instantly.

Financial markets therefore contain a general endogenous destabilizing feedback loop. It comes from the basic mechanism of markets and does not depend on a specific microstructure:

> higher volatility -> wider spreads and lower liquidity -> worse market liquidity -> higher volatility

This mechanism has been studied and empirically tested. Higher efficiency, meaning narrower spreads for liquidity demanders, necessarily comes with greater system instability. Market stability depends on a delicate balance between liquidity demanders, who provide the driving force, and liquidity suppliers, who provide the stabilizing force.

> [12] Bouchaud, J.-P., Bonart, J., Donier, J., & Gould, M. (2018). *Trades, Quotes and Prices: Financial Markets under the Microscope*. Cambridge University Press.

#### c. The Ecosystem of Trading Strategies

Another way to understand market criticality is to view financial markets as an ecological equilibrium among different investment strategies. Investors can be divided into value investors, trend followers, and noise traders. If investors can switch between value investing and trend following according to their relative performance, these simple assumptions are already enough to generate fat-tailed returns and long memory in volatility. The reason is that investors may keep using one strategy for long periods. Empirical studies also support the coexistence of trend followers and value investors in financial markets.

> [13] Chiarella, C. (1992). The dynamics of speculative behaviour. *Annals of Operations Research*, 37(1), 101-123.

This line of work has many extensions. The minority game is an agent-based model of market ecology that can be solved analytically. It shows a phase transition between a market with exploitable regularities and a market with no arbitrage. As the number of investors $M$ increases, profit opportunities gradually decrease and vanish at a critical value $M_c$. When the number of investors exceeds $M_c$, transaction costs make average returns negative. The attraction of criticality is clear here. As markets become more complex and less predictable, they also become more fragile.

> [14] Challet, D., Marsili, M., & Zhang, Y.-C. (2004). *Minority Games: Interacting Agents in Financial Markets*. Oxford University Press.

Doyne Farmer developed a theoretical model of financial-market ecology based on generalized Lotka-Volterra equations. Trading by market participants affects asset prices, and price changes then benefit or hurt other participants. This gives another explanation of market criticality: different strategies interact, depend on one another, and form mutualistic or predator-prey relations. Together they evolve toward a marginally stable equilibrium.

> [15] Farmer, J. D. (2002). Market force, ecology and evolution. *Industrial and Corporate Change*, 11(5), 895-953.

#### d. Contagion and Stability

Contagion also plays an important role in financial markets. It is similar to leverage contagion in banking. In trading markets, one investor's trades affect the marked-to-market value of every other participant's portfolio.

Suppose Alice and Bob hold overlapping portfolios. If Alice deleverages, the prices of the assets she sells may fall, reducing the value of Bob's portfolio. If Bob's losses become large enough, he may also deleverage. That further reduces the value of Alice's portfolio and may affect more investors. This contagion mechanism creates a deleveraging spiral: an avalanche of trades in the same direction that imposes collective losses on investors with similar positions. This mechanism is widely viewed as one source of the 2007 quant meltdown.

The same branching-process framework can describe this phenomenon. Here the contagion parameter $R_0$ measures the similarity of portfolios and the sensitivity of funds to losses. When leverage constraints bind, $R_0$ becomes larger. Yet this framework still does not explain why $R_0$ should be so close to the critical value $R_0=1$.

A plausible interpretation is that as market participants become more complacent, portfolios take on more risk and become more exposed to downside shocks. The process again resembles a sandpile that grows slowly and then suddenly collapses.

## 3. Conclusion: The Trade-off Between Local Efficiency and Systemic Risk

Modern economies and financial markets are not machines in stable equilibrium. They are complex systems driven by network coupling, feedback loops, and individual strategies. Global supply chains, capital flows, and derivatives connect local disturbances into system-wide loops, allowing risk to spread across markets and industries.

Understanding the deep mechanisms that cause instability, failure, and systemic crises in socioeconomic and financial systems is essential for designing responses, safeguards, and reasonable regulation. As this article and the related literature suggest, the pursuit of efficiency and optimality can conflict with the need for global stability.

Self-organized criticality adds a sharper point: in many complex systems, optimization can push the system toward a marginally stable and highly fragile critical state. The examples above show several forces that can move economic and financial systems into a state where destructive avalanches of many sizes become possible. More generally, systems driven by opposing forces, such as incentives and constraints, often operate near criticality.

The mechanisms reviewed here are enough to make financial markets and the macroeconomy frequently approach, or even cross, critical points and lose stability. But for now, the SOC explanation of excess volatility and large business cycles triggered by small shocks remains more theoretical than empirically settled. More data-driven research is needed. Economics needs to take fragility seriously as an explanation of excess volatility, rather than relying only on large exogenous shocks that are often hard to identify and verify. In some cases, we still lack a clear mechanism explaining why the system is attracted to criticality.

The main policy implication is direct. System operators, policymakers, and regulators should include a resilience term in any welfare function they try to optimize. That term should measure robustness to small perturbations, sensitivity to parameter uncertainty, and tolerance of extreme events. Adding such a resilience penalty will raise costs and reduce economic performance in a narrow sense. But it can keep the system away from the edge of the cliff and within a safer region. Good policy should aim to build antifragile systems: systems that can improve themselves under major shocks.
