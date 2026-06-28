---
date: '2024-03-04T12:30:05+08:00'
draft: false
title: 'When Renormalization Group Meets Machine Learning'
type: post
math: true
---

Because structures that are too small are invisible to us, and structures that are too large cannot be fully observed, we need renormalization. It highlights the important features of a system and removes the irrelevant details. In the end, we may find that the world is made of a finite number of islands, and every system belongs to one of them.

This article starts from the renormalization of the Ising model, introduces the basic picture of the renormalization group, reviews work connecting renormalization and machine learning, and then discusses multiscale modeling of non-equilibrium dynamical systems, including causal emergence, eigen microstates, and world models in reinforcement learning.

<!--more-->

Renormalization plays a central role in physics, especially in particle physics and statistical physics. You Yizhuang once summarized its use in a simple way: structures that are too small cannot be seen clearly, and structures that are too large cannot be seen completely. We therefore need renormalization to truncate a system or describe it in a coarse-grained way.

This article explains renormalization through my own learning path. At this stage, I understand it as a picture of dynamics in parameter space. We will return to You's summary at the end. Let us begin with dynamics.

## 1. What Is Renormalization?

First, write a system in a formal way. For a dynamical system, we can use

$$
\frac{dx}{dt}=f(x,\theta)
$$

where $x$ is the system variable, and $\theta$ and the form of $f$ are fixed for a given problem. For example, the equation of a spring oscillator is

$$
m\ddot{x}=-kx
$$

I use a dynamical form because dynamical systems are common in complex systems research. If the system is an equilibrium system, we can instead describe it by a probability distribution $p(x,\theta)$. For convenience, I focus on dynamical systems below, but the idea is broader.

Now introduce scale. What does scale mean? It is like observing the same system with eyes of different resolution. If the resolution becomes lower, the system looks blurrier and many details disappear, but we can still see it move. At this new scale, we can describe the system with a new equation:

$$
\frac{dy}{dt}=f^\prime(y,\theta^\prime)
$$

For an equilibrium system, we could write $p^\prime(y,\theta^\prime)$. In this new description, the variables, parameters, and even the form of the equation may change. Traditional methods in many fields often handle different scales in this way. We have many mature tools for differential equations, nonlinear dynamics, flows, chaos, attractors, and fractals.

Renormalization asks a different question. When we keep coarse-graining a system, what changes? In other words, what is the relation between the system at different scales?

In the language above, renormalization models the dynamics of system parameters across scales:

$$
\frac{d\theta}{dl}=g(\theta,\gamma)
$$

The independent variable is now scale $l$, not time $t$. The dependent variable is $\theta$, the parameter of the original system. This equation says how system parameters change with scale. To write it, we assume that the dynamics at different scales, $f$ and $f^\prime$, can be written in essentially the same form. This looks strong, but it is reasonable in many physical systems.

Consider the equilibrium Ising model. Block coarse-graining is approximately equivalent to changing the coupling coefficient, or temperature, because the coupling coefficient and temperature are directly related. This gives the classic picture of real-space renormalization for the Ising model. The reason this works is that the Ising model at a new scale is still an Ising model, not a different model such as the Potts model. Under this condition, the renormalization equation defines a new dynamical system: the multiscale view of the original system. We can then use dynamical-systems tools to study quantitative laws across scales.

> Figure 1: Real-space renormalization of the two-dimensional Ising model with zero external field. Each column represents a different reduced temperature. Each row shows the original system, the system after one renormalization step, and the system after two steps.

What laws can we get from this picture? Since the renormalization equation is a dynamical system, it can be represented by a phase diagram. In the one-dimensional Ising model there is no nontrivial fixed point. In the two-dimensional Ising model there is one. A fixed point in parameter space means that the parameters do not change under a change of scale. This is surprising. It means that coarse-graining does not change the basic rules of interaction inside the system. This can happen in two cases: either the internal correlation is zero, so there is no interaction, or the system has infinite long-range correlations, so coarse-graining removes only irrelevant local information.

Therefore, a nontrivial fixed point of the renormalization equation corresponds to a phase transition point in a critical system. The parameter $K$ in the Ising model is the coupling coefficient, similar to temperature, and controls interaction strength. This method can also be used to calculate critical exponents.

> Further reading:  
> - *Complexity and Criticality*  
> - JiZhi Encyclopedia: Renormalization of the Ising model  
> - *Miracles at the Edge: Phase Transitions and Critical Phenomena*

> Figure 2: Renormalization and phase diagrams for one-dimensional and two-dimensional Ising models.

There is another important detail. We said that renormalization assumes that the dynamics at different scales, $f$ and $f^\prime$, have essentially the same form. In the Ising model, the microscopic system has first-order nearest-neighbor interactions. After one renormalization step, higher-order interactions appear. The change in coupling coefficient $K$ is not just a change in numerical value. More accurately, the dimension of parameter space expands. The phase diagram is therefore a low-dimensional projection of a higher-dimensional dynamical system.

The coupling coefficient $K$ should be understood as an infinite-dimensional vector:

$$
\mathbf{K}=(K_1,K_2,K_3,\ldots)
$$

Here $K_1$ is the nearest-neighbor interaction, $K_2$ is the next-nearest-neighbor interaction, and $K_3$ represents higher-order interactions. The energy function can be written schematically as

$$
H=K_1\sum_{nn}s_is_j+K_2\sum_{nnn}s_is_j+K_3\sum s_is_js_ks_l+\cdots
$$

In the usual Ising model, all coefficients except $K_1$ are zero. A more precise description of renormalization is therefore a trajectory in a higher-dimensional parameter space.

> Figure 3: A three-dimensional sketch of parameter space. In the usual Ising model, $K_2$ and $K_3$ are zero. The one-dimensional phase diagram is a projection along the $K_1$ direction. The gray surface is the critical surface where all coupling constants are $\infty$.

After using renormalization to remove details, we also find something remarkable. Natural systems differ greatly, but they show only a finite number of renormalization behaviors. For example, ferromagnetic phase transitions and liquid-gas phase transitions behave in the same way near criticality. This leads to the concept of universality classes. Systems are classified by their behavior under renormalization. This idea changed our understanding of critical phenomena.

This returns to the opening statement. Because structures that are too small cannot be seen clearly, and structures that are too large cannot be seen completely, we use renormalization to highlight important features and remove irrelevant ones. In the end, the world may consist of a finite number of islands, and each system belongs to one island.

There are still barriers when we use renormalization on concrete systems. We need to design a suitable renormalization strategy, but sometimes we do not know the right principle. This depends heavily on experience and intuition. Can we automate the process and let machines find universality classes? This question led to a set of data-driven methods that connect machine learning with renormalization.

## 2. Renormalization Group and Machine Learning

### 2.1 Renormalization Group for Machine Learning

The connection between machine learning and renormalization is active and not entirely new. Discussions go back at least to PCA. Deep learning also has structural similarities with renormalization. Renormalization extracts key features by repeated coarse-graining. Each layer of a deep network also extracts features. Different layers can have a scale meaning: shallow layers encode small-scale features, while deeper layers encode larger-scale features.

Mehta and Schwab first made this connection explicit. They built a neural-network architecture based on the restricted Boltzmann machine, or RBM, and established an exact analytic mapping between Kadanoff block coarse-graining in the Ising model and neural networks. This suggested that deep learning may extract features from data in a way similar to a renormalization flow.

> [1] Bradde, S., & Bialek, W. (2017). PCA meets RG. *Journal of Statistical Physics*, 167, 462-475.  
> [2] Mehta, P., & Schwab, D. J. (2014). An exact mapping between the variational renormalization group and deep learning. arXiv:1410.3831.

A later paper pushed this idea further. It also used RBMs to reproduce the renormalization flow of the Ising model and even obtained critical exponents numerically. This made the link between renormalization and machine learning more concrete.

> [3] Koch, E. D. M., Koch, R. D. M., & Cheng, L. (2020). Is deep learning a renormalization group flow? *IEEE Access*, 8, 106487-106505.

Another line of work studies trained RBMs directly and finds an RG flow in them. Some papers argue that the stable fixed point of an RBM is a nontrivial critical point. This picture is the opposite of the Ising case, where the critical point is an unstable fixed point. The reason behind this difference is still worth studying.

> [4] Iso, S., Shiba, S., & Yokoo, S. (2018). Scale-invariant feature extraction of neural network and renormalization group flow. *Physical Review E*, 97(5). https://doi.org/10.1103/PhysRevE.97.053304  
> [5] Funai, S. S., & Giataganas, D. (2020). Thermodynamics and feature extraction by machine learning. *Physical Review Research*, 2(3). https://doi.org/10.1103/PhysRevResearch.2.033415

These studies are interesting because they ask how statistical physics can help us understand neural representations. But they are often limited to a specific neural architecture, usually the RBM, because RBMs are almost designed to match statistical physics. This limits their scientific impact on real applications and on statistical physics itself. The RBM sometimes becomes a toy repeatedly studied by physicists. Although there are attempts to compute critical exponents, the method has not yet moved far into more complex systems.

Beyond RBMs, CNNs, tensor networks, and generative models may also connect with RG. The more important question is what this connection can actually do. Can it solve real problems? Can it improve neural networks? This leads to another direction: using RG theory as prior knowledge for designing neural networks and for solving real physical problems.

### 2.2 Machine Learning for Renormalization Group

A classic paper in this direction appeared in *Nature Physics* in 2018. Its goal was to use data-driven methods to automatically construct coarse-graining rules. The method maximizes the mutual information between the coarse-grained variable and the environment variables of the original system, without adding other prior knowledge. The environment variables are variables outside the current local real-space block. The learned coarse variable becomes the relevant variable. This matches the RG picture and can recover critical exponents.

> [6] Koch-Janusz, M., & Ringel, Z. (2018). Mutual information, neural networks and the renormalization group. *Nature Physics*, 14(6), 578-582. https://doi.org/10.1038/s41567-018-0081-4

A later paper in *Physical Review X* derived the analytic form of this information-theoretic coarse-graining rule. It provided a valuable principle for building renormalization transformations and reduced the need to design coarse-graining rules by intuition alone.

> [7] Lenggenhager, P. M., Gökmen, D. E., Ringel, Z., Huber, S. D., & Koch-Janusz, M. (2020). Optimal renormalization group transformation from information theory. *Physical Review X*, 10(1). https://doi.org/10.1103/PhysRevX.10.011037

Wang Lei and You Yizhuang then proposed the principle of minimizing holographic mutual information. In each step, the information discarded should have minimal mutual information, so the relevant information of the system is preserved. This extends the idea of maximizing environmental mutual information. They also introduced invertible neural networks, which turn renormalization into a true group operation rather than the semigroup operation of traditional RG. The learned network becomes a generative model. It can extract key variables like ordinary renormalization and also perform inverse renormalization to resample configurations at the original scale. In this framework, each layer has a physical meaning. Later work focused more on interpretability in applications, while the theoretical side remains open.

> [8] Hu, H. Y., Li, S. H., Wang, L., & You, Y. Z. (2020). Machine learning holographic mapping by neural network renormalization group. *Physical Review Research*, 2(2), 023369. https://doi.org/10.1103/PhysRevResearch.2.023369  
> [9] Sheshmani, A., You, Y. Z., Fu, W., & Azizi, A. (2023). Categorical representation learning and RG flow operators for algorithmic classifiers. *Machine Learning: Science and Technology*, 4, 20.

You's group also proposed a self-training framework that can discover universality classes from symmetry alone, without simulated data. The idea is to build a fine-grained model and a coarse-grained model. The coarse model is trained to generate configurations similar to the fine model, mimicking renormalization. A third model then learns the dynamics between the parameters of the two systems. Together, the three models can learn the renormalization equation and the critical exponents for systems with a given symmetry.

> [10] Hou, W., & You, Y. Z. (2023). Machine Learning Renormalization Group for Statistical Physics. arXiv:2306.11054.

## 3. Multiscale Modeling of Non-Equilibrium Systems

So far, most of the discussion has concerned equilibrium models. Renormalization theory is most powerful in equilibrium systems. Non-equilibrium systems are much harder. We still lack a unified theory comparable to equilibrium statistical physics. Complex systems research often studies dynamical systems, and these systems are usually non-equilibrium. Non-equilibrium physics also lacks a canonical toy model as mature as the Ising model. As a result, RG work on non-equilibrium systems is less developed, and data-driven RG work is even rarer.

At the same time, multiscale dynamical modeling has developed rapidly in other areas. For prediction and control, information at different scales plays different roles. Small-scale high-frequency information helps short-term prediction, while large-scale low-frequency information is crucial for long-term modeling. Reduced-order models, equation-free models, and causal emergence theory all try to reduce or simplify dynamical systems using their own principles.

Data-driven reduction of dynamical systems has also become very active. Chen Xiaosong's group developed the eigen microstate method, which starts from data, uses singular value decomposition to decompose modes, and finds clear physical meanings in those modes. This method can solve critical phase transitions in classical equilibrium systems and has also been applied to swarms, turbulence, climate, finance, quantum systems, and other complex systems.

Other work combines data-driven methods with the Koopman operator to perform dynamic mode decomposition or learn latent spaces. The Koopman operator linearizes nonlinear dynamical systems, but it is hard to compute. Some work inspired by equation-free modeling uses machine learning methods such as VAEs to reduce system variables and then learn dynamics directly in latent space. This is often called effective dynamics and can improve prediction.

In reinforcement learning, world models follow a related idea. They represent the environment interacting with an agent by a low-dimensional model, improving prediction and control. This has become an important frontier in that field.

> Figure 4: Prediction does not require all information in the system. It needs a simplified representation.

> [11] Hu, G. K., Liu, T., Liu, M. X., Chen, W., & Chen, X. S. (2019). Condensation of eigen microstate in statistical ensemble and phase transition. *Science China Physics, Mechanics & Astronomy*, 62(9). https://doi.org/10.1007/s11433-018-9353-x  
> [12] Khazaei, H. (2016). A data-driven approximation of the Koopman operator: Extending dynamic mode decomposition. *AIMS*, X(0), 1-33.  
> [13] Lusch, B., Kutz, J. N., & Brunton, S. L. (2018). Deep learning for universal linear embeddings of nonlinear dynamics. *Nature Communications*, 9(1). https://doi.org/10.1038/s41467-018-07210-0  
> [14] Vlachas, P. R., Arampatzis, G., Uhler, C., & Koumoutsakos, P. (2022). Multiscale simulations of complex systems by learning their effective dynamics. *Nature Machine Intelligence*, 4(4), 359-366. https://doi.org/10.1038/s42256-022-00464-w  
> [15] Ha, D. (2018). World Models.

As data become richer and systems become more complex, multiscale thinking becomes increasingly important for dynamical modeling. It improves computational efficiency and helps identify the low-dimensional variables that matter for a task. These ideas are becoming common in the study of complex systems. Their origins may look unrelated to renormalization, but they arrive at similar problems from another direction. Because they are less constrained by formal theory, they can sometimes look crude, yet they work across many fields and become useful tools.

## 4. Conclusion

This article introduced renormalization from a dynamical-systems perspective and used visual intuition where possible. It then reviewed recent work connecting machine learning and renormalization. These studies are imaginative and provide useful routes for applying RG more broadly and more intelligently.

The third part gave a rough review of multiscale modeling for dynamical systems. This field is diverse and active. At its core, it searches for multiscale solutions to non-equilibrium dynamical systems and offers important ideas for real problems.

One important area not discussed in detail is renormalization of complex networks. This line of work asks how a large complex network can be represented by a smaller network, so that difficult computations on large networks become easier. It is also highly promising.

For now, neither multiscale dynamical modeling nor network renormalization has produced a unified theory comparable to equilibrium RG. But we can still believe that, in the future, we may find where the islands of complex systems are located.
