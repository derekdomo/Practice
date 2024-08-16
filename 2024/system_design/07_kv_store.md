TLDR:
- Big data:             consistent hash to distribute kv pairs
- High available read:  data replication across multiple dc
- High available write: versionsing and conflict resolution with vector clocks
- Dataset partition:    consistent hashing
- Incremental scale:    consistent hashing
- Hetergoeneity:        consistent hashing
- Tunable consistency:  quorum consensus
- Temporary failure:    sloppy quorum and hinted handoff
- Permanent failure:    merkle tree
- data center outage:   cross dc replication



# Problem statement
- Non relational database
    - unique identifiers stored as key
    - key must be unique and can be plain text or hashes
    - performance wise, short keys are preferred

- main functionalities
    - put(key, value)
    - get(key)

- main characteristics
    - kv pair is small
    - need to store a lot of data
    - High availability
    - High scalability
    - Automatic scale
    - Tunable consistency
    - Low latency



# Start - single server kv store

In memory hash will be sufficient

Bottleneck
- memory limitation
    - data compression
    - LRU, to store only frequent data in memory


# Distributed kv store

The key idea is a distributed hash table which distributes keys across many nodes

CAP therom
- consistency
- availability
- partition tolerance

We definitely want to support consistency and availability but since network failures are inevitable. This will make it impossible to support both.


## Data partition

### Solve memory limitation

Consistent hashing is the way to solve the challenge that
- distribute data evenly
- minimize data movement when cluster scale up or down

## Data replication

### Increase availability and reliability
 The key idea is to allocate a key to multiple nodes


## Consistency

The key idea is quorum consensus
- N - number of replicas
- W - write quorum, write operations must be acknowledged by at least W nodes
- R - read quorum, read opreations must be acknowledged by at least R nodes

W and R can be tuned to trade off between latency and consistency


### Consistency modes
- Strong consistency
- Weak consistency
- Eventual consistency

to achieve eventual consistency, we need inconsistency resolution. This is mainly done by versioning. 

The key idea of detecting a conflict is to check the all version stamps are less or euqal to the other one.



## Failure handling
- Approach one: all to all multi casting
- Approach two: gosip protocol
    -  a member is marked as offline if the last heartbeat is not recived with in x mins

### Temporary failures
Having a server standby to replace it when this happens and regularly check if it comes back online

### Permanent failures
Merkle tree to reduce the amount of data to compare and move when inconsistency happens

### Data center outages
Data need to be replicated across multiple data centers


# System architecture

Client - read/write -> coordinator -> Node[0:7]

## Node
- client API
- Failure detection
- Conflict resolution
- Failure repairment
- Replication
- Storage engine


## Write path within node

Client -> write -> 
    - Disk: commit log
    - Memory: memory cache
        - Offload to disk

## Read path within node

Client -> read ->
    - memory cache
    - retrieve from disk if cache miss

