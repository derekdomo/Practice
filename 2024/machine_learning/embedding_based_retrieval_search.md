Typical search components
---
- Retrieval Layer
- Ranking layer

For retrieval layer, use a two tower model for query tower and document tower


Metrics
---
- ranking metric: recall
- offline evaluatio metric
    - triplet loss: max(0, D(q, d+) - D(q, d-) + m)
    - m is a margin parameter, recommend to use 5%-10% knn recall variance
    - random sample negative is better to approximate the recall optimizationt task
    - D(q, d) = 1 - cos(q, d)

Unified Embedding
---
- One hot encoding feature
    - embedding look up layer
- Multi hot encoding feature
    - weighted combination 



Training Data
---



Feature Engineer
---
- Text features
    - character n-gram
    - word n-gram
- Pros
    - fuzzy word matches
    - optionalization


