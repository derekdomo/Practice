# Step 1 - Understand the problem and establish design scope
- example of URL shortening
- traffic volume
- length of the shortened url
- allowed characters
- mutable

## Caluclation
- request per second
- read-to-write ratio: reads per second
- # of records needed to support if we run x years
- storage estimation




# Step 2 - High level design

API
- api/shorten
- api/shortURL

## Read
Client -> tinyURL server -> return long URL


## Write

a hash functiont to conver the long URL to the short version


# Step 3 - Design deep dive

## Data model
URL table
- id
- shortURL
- longURL

## Hash function
flow
- input: long url
- hash function
- short URL
- check DB collision
- if collision, regenerate with salt
- save to DB

Bloom filters to help speed up check if collision

Two approaches
- Hash + collision resolution
- Base 62 conversion


# Step 3 - URL redirection deep dive

client -> load balancer(shortURL) -> cache -> Long URL -> load balancer(longURL) -> server




