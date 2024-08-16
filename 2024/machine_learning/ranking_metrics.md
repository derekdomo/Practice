MRR
---
mean reciprocal rank

measure the quality of the model by considering the ranking of the first relavant item in each output list

1/m * sum(1/rank_i)

Con: only consider the first relevant item


Recall@k
---

number of relevant items among top k / total relevant items

Cons: doesnt consider ranking quality of the list


Precision@k
---

number relavant items among top k in the list / k

Cons: doesnt consider the ranking quality of the list


mAP
---
sum(Precision@i)/total relevant items

More designed for binary relevances


nDCG
---
DCG = sum(rel/log(i+1))

IDCG: DCG of the ideal ranking
