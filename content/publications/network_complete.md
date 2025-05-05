---
title: "Graph Completion Through Local Pattern Generalization"
year: 2024
authors: 'Zhang Zhang, Ruyi Tao, Yongzai Tao, Mingze Qi, Jiang Zhang'
journal: " Complex Networks & Their Applications XII"
link: 'https://link.springer.com/chapter/10.1007/978-3-031-53468-3_22'
draft: false
---

Network completion is more challenging than link prediction, as it aims to infer both missing links and nodes. Although various methods exist for this problem, few utilize structural information-specifically, the similarity of local connection patterns. In this study, we introduce a model called C-GIN, which captures local structural patterns in the observed portions of a network using a Graph Auto-Encoder equipped with a Graph Isomorphism Network. This model generalizes these patterns to complete the entire graph. Experimental results on both synthetic and real-world networks across diverse domains indicate that C-GIN not only requires less information but also outperforms baseline prediction models in most cases. Additionally, we propose a metric known as “Reachable Clustering Coefficient (RCC)” based on network structure. Experiments reveal that C-GIN performs better on networks with higher Reachable CC values. 