# matrix completion model

embedding(user_id) * embedding(item_id)


# two tower model

## user tower
user_embedding = neural_net(embedding(user_id), embedding(user_categorical), user_numerical)

## item tower
item_embedding = neural_net(embedding(item_id), embedding(item_categorical), item_numerical)

cos(user_embedding, item_embedding) = dot(u_e, i_e) / (u_e ** 2 * i_e ** 2)


## notes
the importance or the key idea of two tower model is that there are no feature crossing between user tower and item tower. the neural net has to be within the tower itself and cannot be shared.

the feature crossing model is no longer a recall model but a ranking model


