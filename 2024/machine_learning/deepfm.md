link: https://arxiv.org/pdf/1703.04247


## Factorization Machine
- y(x) = w_0 + sum(w_i * x_i) + sum(<v_i, v_j> * x_i * x_j)
- v is a size k vector, and k is restricting expressivity of the factorization machine
- svm vs. fm
    - svm's linear kernel is equivalent to fm order 1
    - svm's polynomial kernel is different since the parameters on x_i * x_j are independent while fm's is sharing the same vectors

##  FM + DNN

y(x) = sigmoid(y_fm + y_dnn)

### Model Strurcture


Features -> Embedding Layer
                -> FM component    ->|
                -> DNN             ->| -> sgimoid


FM Component
y = <w, x> + sum(<v_i, v_j> * x_i * x_j)

DNN Component
a_0 = [e_0, ... e_m]
a(l+1) = sigmoid(W * a(l) + b(l))

