layered user bucketing
---
layer 0: randomly split n users into k groups, i.e.: group_0_0, group_0_1, ... group_0_k
layer 1: still k groups but ensure group_1_i and group_0_j intersection is only n / k**2

each function group can select groups from each layer


long term holdout
---

