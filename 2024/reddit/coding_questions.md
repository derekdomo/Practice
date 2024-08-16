Backtracking
---
Input:

list of menu items: think of something like List<Map<String,Integer>>, where the key is the name of the menu item and the value is the cost. Example: Popcorn:10, CocaCola:4, Water:2, Coffe:3
amount of coin
Output:
return all the possible items you can buy (without repetition) with the given coins.


Dijstra with walls
---


Hit Counter
---
Return the pageViewCount across all clients in the last 7 days.
Last 7 days starts counting from the most recent day in the page_view_data
广告
PauseUnmute
Loaded: 1.82%
Fullscreen
Input data are not sorted in any order, input data are given in python dictionary
page_view_data =
{
“2022-06-11”: {
  “ios”: {
   “pageViewCount”: 20000
   “unique”: 12999
  },
  “reddit web”: {
   “pageViewCount”: 20000
   “unique”: 12999
  },
   …. different client counts
}
“2022-01-12”: { …
}
}




Tennis match
---
设计一个网球比赛，每一局是一个class，每一次赛事是另一个class。比赛的规则会给出，只需要implement 即可，难点应该是赛事是class of class。

player 1 & player 2 打一场球赛，让你设计一个积分器，可以take player ID和给他加的分数 （怎么加分加多少分都是user input）。同时需要实现比赛是否终结的功能，和如果终结给出优胜者的功能。
第二小问要求实现一个赛事，五局三胜，每一局比赛使用第一小问的class，然后要求可以判定赛事是否终结，如果终结给出优胜者




Memcached coding
---


Merge intervals(segment tree?)
---
表面上是给了一个json文件，里面有 id, time, message.需要找到某个时间段的所有message




Classification model
---
train_test_split with stratify
lr code snippet
lightgbm code snippet



DFS - printing string
---
给一个数组，每个数组元素是一串人名，第一个人名（idx 0）是老板，之后的人名是手下direct report人名。第一小问要求打印org structure，第二小问给定mgr名字，打印skip level report名单。

a,b,c
b,d
d,e

tricky part, there might be multiple connected components

follow up:
print所有可以skip一级的meeting


Threaded message board
---



Rate limiter API
---



Print path of the alpha
---
coding 打印每个字母的路径
输入：[A, B, [C, D], [E, [F, [G, H]]]]
输出：A, B, B->C, B->D, B->E, B->E->F, B->E->F->G, B->E->F->H
