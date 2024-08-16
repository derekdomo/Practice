# interest score on a new item

## item cf
sum_j(like(user, item_j) * sim(item, item_j))

## user cf
sum_j(like(user, item_j) * sim(user, uesr_j))


# how to calculate similarity between items

## binary label
W1: users like item1
W2: users like item2
V = W1 intersect W2

sim(item1, item2) = |V| / sqrt(|W1| * |W2|)

## countious score
sim(item1, item2) = sqrt(sum(like_v(v_i, item1)**2) + sum(like(v_i, item2)**2)) / (sqrt(sum(like_w1(v_i, item1)**2)) + sqrt(sum(like_w2(v_i, item2)**2)))


# how to calculate similarity between users

## binary label

J1: items user1 likes
J2: items user2 likes
I = J1 intersect J2

sim(user1, user2) = |I| / sqrt(|J1| * |J2|)

## reduce weight on popular items 
similar concept as idf


