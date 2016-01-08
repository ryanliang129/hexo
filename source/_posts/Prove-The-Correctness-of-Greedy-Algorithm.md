title: The Correctness of Greedy Algorithm
---
# Overview

Greedy algorithms can be some of the simplest algorithms to implement, but they're often among the hardest algorithms to design and analyze. You can often stumble on the right algorithm but not recognize that you've found it, or might find an algorithm you're sure is correct and hit a brick wall trying to formally prove its correctness.  


• Maximize the number of events you can attend, but do not attend any overlapping events.  
• Minimize the number of jumps required to cross the pond, but do not fall into the water.  
• Minimize the cost of all edges chosen, but do not disconnect the graph.  

  
Here is how we might formalize this:  






**• Define Your Measure.** Your goal is to find a series of measurements you can make of your solution and the optimal solution. Define some series of measures _m<sub>1</sub>_(_X_), _m<sub>2</sub>_(_X_), ..., _m<sub>n</sub>_(_X_) such that _m<sub>1</sub>_(_X\*_), _m<sub>2</sub>_(_X\*_), ..., _m<sub>k</sub>_(_X\*_) is also defined for some choices of *m* and *n*. Note that there might be a different number of measures for _X_ and _X\*_, since you can't assume at this point that _X_ is optimal.  






















