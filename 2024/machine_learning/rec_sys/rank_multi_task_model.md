# multi task prediction model
- p1: ctr
- p2: like rate
- p3: collect rate
- p4: repost rate
cross_entrophy(y1, p1) = -(y1 * ln(p1)+(1 - y1) * ln(1 - p1))

cost_func = sum_i(alph_i * cross_entrophy(y_i, p_i))

difficulties:
1. class unbalance
    - ctr is always low
    - solved by down sampling, but need adjustment since it will have higher prediction rate than facts
    -

