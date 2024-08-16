# Step 1 - Understand the problem and establish the design scope

- What kind of ID do we expect?
    - numeric? unique? uuid?
- different options
    - increment by 1
    - increment by time
- length requirements
- system scale
    - how fast do we want to generate the IDs



# Step 2 - High level design

Options to consider

## Multi master replication

Database's auto increment features, it will auto increment number of servers



## UUID
UUID crashes very unlikely

Cons:
1. ID size is large
2. Doesnt increase with time
3. Non numerical


## Ticker server
A dedicated server to generate incremental ID

Cons:
1. single point of failure
2. additional latency



## Twitter snowflake approach
breakdown the number at bit level into different chunks
- timestamp: 41 bits
- datacenter ID: 5 bits
- machine ID: 5 bits
- sequence number: 12 bits



# Step 3 - Design deep dive

Go with twitter snowflake appraoch

# Step 4 - Wrap up

Additional talking points
- clock synchronization
- section length tuning
- high availability



