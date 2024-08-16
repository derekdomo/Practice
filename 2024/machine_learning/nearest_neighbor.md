Exact nearest neighbor
---
search against the whole index

Time complexity is O(N * D)



Approximate nearest neighbor
---

- Tree baesd ANN
    - The nodes in the tree are crieterias
    - This requires upfront knowledge about the query image
- Locality sensitivity hashing baed ANN
    - pariticular hash function to reduce the dimensions of the points and group them into buckets
- Clustering based ANN
    - Group the points into clusters based simmilarities

Two widely used libraries
- FAISS
- ScaNN


