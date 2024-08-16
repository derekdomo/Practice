

# Notes
- control the rate of traffic from clients to a given server
- control the maximum number of requests allowed in a given time period

- behavior of not exceeding
    - drop
    - stash in a queue



# Step 1 - requirements
- client side or server side
- rate limit based on what information
- scale of the company
- service or library
- do we need to inform the throttled users


Summary 
- accurately limit excess requests
- low latency & little memory consumed
- distributed rate limiting
- exception handling
- high fault tolerance: consider vairous failure modes



# Step 2 - high level design

Option 1
-
client -> API servers [rate limiter]

Option 2
-
client -> rate limiter -> API servers

The second option is mostly letting the rate limiter living in the API gateway


The considerations on which to choose
- current tech stack: client side or server side
- api gateway available or not
- off the shelf 3rd party solutions: lyft's rate limiter



# Algorithms

## Token bucket algorithm

There is a bucket keeping getting refilled and each request will take a token from it

parameter:
- bucket size
- refill rate


## Leaking bucket algorithm

There is a bucket which is essentially a queue. The server is processing the requests at its own capacity

parameter
- bucket size
- outflow rate


## Fixed window counter algorithm

Bucket the requests by minute or customized time window


## Sliding window log algorithm

accurate but memory costly




# Step 3 - Deep Dive

Check lists
- high level architectures
- different rate limit algorithms and pros&cons

Not covered
- rate limit rules
- how to handle rate limited request


## Rule example
```
domain: messaging
descriptors:
    - key: message_type
      value: marketing
      rate_limit:
         unit: day
         requests_per_unit: 5
```

## Exceed the rate limit

- 429 error
- enqueue for future processing

## Detailed design

client -> rate limiter middleware

- step 1: fetch rules from cache, and utilize redis to check if rate limited
- step 2.1: if not rate limited, route to api server
- step 2.2: if rate limited, drop with 429 or enqueue


## Distributed environment
challenges:
1. race conditions
2. synchronization

Ways to resolve
1. locks
2. sticky sessions
3. lua? or sorted sets?


## Monitoring
- if the algorithm is effective
- if the rules are effective

# Step 4 - Wrap up

Recap
- algorithms


Additional talking points
- hard vs. soft rate limiting
- rate limiting at low layers(network) compared to application layer
- Client side measures to avoid being rate limited
- Canaray test on effectiveness



