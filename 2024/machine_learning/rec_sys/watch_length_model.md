# directly modeling regression doesnt have good effect


model output z, exp(z) / 1 + exp(z)
model label t, t / 1 + t

use cross entrophy as cost function since both values are between 0 and 1. Using this makes it easier for neural net to converge.
