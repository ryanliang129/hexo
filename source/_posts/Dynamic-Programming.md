title: Dynamic Programming
---


# Overview
Dynamic Programming is a powerful technique that allows one to solve many different types of problems in time _O_(_n_<sup>2</sup>) or _O_(_n_<sup>3</sup>) for which a naive approach would take exponential time. In this lecture, we discuss this technique, and present a few key examples. Topics in this lecture include:  

  • The basic idea of Dynamic Programming.  
  • Example: Longest Common Subsequence.  
  • Example: Knapsack.     
  • Example: Matrix-chain multiplication.  
  
  ## The Basic IdeaDynamic Programming is a powerful technique that can be used to solve many problems in time _O_(_n_<sup>2</sup>) or _O_(_n_<sup>3</sup>) for which a naive approach would take exponential time. (Usually to get running time below that—if it is possible—one would need to add other ideas as well.) Dynamic Programming is a general approach to solving problems, much like “divide-and-conquer” is a general method, except that unlike divide-and-conquer, the subproblems will typically overlap. This lecture we will present two ways of thinking about Dynamic Programming as well as a few examples.  
There are several ways of thinking about the basic idea.  
**Basic Idea (version 1):** What we want to do is take our problem and somehow break it down into a reasonable number of subproblems (where “reasonable” might be something like _n_<sup>2</sup>) in such a way that we can use optimal solutions to the smaller subproblems to give us optimal solutions to the larger ones. Unlike divide-and-conquer (as in mergesort or quicksort) it is OK if our subproblems overlap, so long as there are not too many of them.  

## Example \#1: Longest Common Subsequence**Definition 1** _The **Longest Common Subsequence (LCS)** problem is as follows. We are given two strings: string S of length n, and string T of length m. Our goal is to produce their longest common subsequence: the longest sequence of characters that appear left-to-right (but not necessarily in a contiguous block) in both strings._  
For example, consider:  <center><em>S</em> = ABAZDC</center> <center><em>T</em> = BACBAD</center>  
In this case, the LCS has length 4 and is the string **ABAD**. Another way to look at it is we are finding a 1-1 matching between some of the letters in _S_ and some of the letters in _T_ such that none of the edges in the matching cross each other.  
For instance, this type of problem comes up all the time in genomics: given two DNA fragments, the LCS gives information about what they have in common and the best way to line them up.  
Let’s now solve the LCS problem using Dynamic Programming. As subproblems we will look at the LCS of a prefix of _S_ and a prefix of _T_, running over all pairs of prefixes. For simplicity, let’s worry first about finding the _length_ of the LCS and then we can modify the algorithm to produce the actual sequence itself.  
So, here is the question: say LCS[i,j] is the length of the LCS of _S_[1..i] with _T_[1..j]. How can we solve for LCS[i,j] in terms of the LCS’s of the smaller problems?**Case 1:** what if _S_[i] <> _T_[j]? Then, the desired subsequence has to ignore one of _S_[i] or _T_[j] so we have:  <center>LCS[i,j] = max(LCS[i − 1,j], LCS[i,j − 1]).</center>    
**Case 2:** what if _S_[i] = _T_[j]? Then the LCS of _S_[1..i] and _T_[1..j] might as well match them up. For instance, if I gave you a common subsequence that matched _S_[i] to an earlier location in _T_, for instance, you could always match it to _T_[j] instead. So, in this case we have:  <center>LCS[i,j] = 1 + LCS[i−1,j−1].</center>   
So, we can just do two loops (over values of _i_ and _j_) , filling in the LCS using these rules. Here’s what it looks like pictorially for the example above, with S along the leftmost column and T along the top row.  

<center><table>
<tbody>
<tr><td><em></em></td><td><em>B</em></td><td><em>A</em></td><td><em>C</em></td><td><em>B</em></td><td><em>A</em></td><td><em>D</em></td></tr>
<tr><td>A</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr>
<tr><td>B</td><td>1</td><td>1</td><td>1</td><td>2</td><td>2</td><td>2</td></tr>
<tr><td>A</td><td>1</td><td>2</td><td>2</td><td>2</td><td>3</td><td>3</td></tr>
<tr><td>Z</td><td>1</td><td>2</td><td>2</td><td>2</td><td>3</td><td>3</td></tr>
<tr><td>D</td><td>1</td><td>2</td><td>2</td><td>2</td><td>3</td><td>4</td></tr>
<tr><td>C</td><td>1</td><td>2</td><td>3</td><td>3</td><td>3</td><td>4</td></tr>
</tbody>
</table>
</center>   

We just fill out this matrix row by row, doing constant amount of work per entry, so this takes _O_(_mn_) time overall. The final answer (the length of the LCS of _S_ and _T_) is in the lower-right corner.  

**How can we now find the sequence?** To find the sequence, we just walk backwards through matrix starting the lower-right corner. If either the cell directly above or directly to the right contains a value equal to the value in the current cell, then move to that cell (if both to, then chose either one). If both such cells have values strictly less than the value in the current cell, then move diagonally up-left (this corresponts to applying Case 2), and output the associated character. This will output the characters in the LCS in reverse order. For instance, running on the matrix above, this outputs **DABA**.

## More on The Basic Idea, and Example \#1 Revisited
We have been looking at what is called “bottom-up Dynamic Programming”. Here is another way of thinking about Dynamic Programming, that also leads to basically the same algorithm, but viewed from the other direction. Sometimes this is called “top-down Dynamic Programming”.  
**Basic Idea (version 2):** Suppose you have a recursive algorithm for some problem that gives you a really bad recurrence like _T_(_n_) = 2*T*(_n_ − 1) + _n_. However, suppose that many of the subproblems you reach as you go down the recursion tree are the same. Then you can hope to get a big savings if you store your computations so that you only compute each _different_ subproblem once. You can store these solutions in an array or hash table. This view of Dynamic Programming is often called _memoizing_.  
For example, for the LCS problem, using our analysis we had at the beginning we might have produced the following exponential-time recursive program (arrays start at 1):  

	LCS(S,n,T,m)    	{    		if (n==0 || m==0)   
			return 0;    
		if (S[n] == T[m]) 
			result = 1 + LCS(S,n-1,T,m-1); // no harm in matching up
		else 
			result = max{LCS(S,n-1,T,m), LCS(S,n,T,m-1)};  
		return result;	}  
This algorithm runs in exponential time. In fact, if _S_ and _T_ use completely disjoint sets of characters (so that we never have _S_[n] == _T_[m]) then the number of times that LCS(S,1,T,1) is recursively called equals [n+m−2,m-1]. In the memoized version, we store results in a matrix so that any given set of arguments to LCS only produces new work (new recursive calls) once. The memoized version begins by initializing arr[i][j] to unknown for all _i_, _j_, and then proceeds as follows:  
	LCS(S,n,T,m)	{		if (n==0 || m==0) 
			return 0;		if (arr[n][m] != unknown) return arr[n][m]; // <- added this line (*) if (S[n] == T[m]) 
			result = 1 + LCS(S,n-1,T,m-1);		else 
			result = max{LCS(S,n-1,T,m), LCS(S,n,T,m-1)};		arr[n][m] = result; // <- and this line (**)  
		return result;	}  
All we have done is saved our work in line (\*\*) and made sure that we only embark on new recursive calls if we haven’t already computed the answer in line (\*).  
In this memoized version, our running time is now just _O_(_mn_). One easy way to see this is as follows. First, notice that we reach line (\*\*) at most _mn_ times (at most once for any given value of the parameters). This means we make at most 2*mn* recursive calls total (at most two calls for each time we reach that line). Any given call of LCS involves only _O_(1) work (performing some equality checks and taking a max or adding 1), so overall the total running time is _O_(_mn_).  
Comparing bottom-up and top-down dynamic programming, both do almost the same work. The top-down (memoized) version pays a penalty in recursion overhead, but can potentially be faster than the bottom-up version in situations where some of the subproblems never get examined at all. These differences, however, are minor: you should use whichever version is easiest and most intuitive for you for the given problem at hand.  
**More about LCS: Discussion and Extensions.** An equivalent problem to LCS is the “mini- mum edit distance” problem, where the legal operations are insert and delete. (E.g., the unix “diff” command, where _S_ and _T_ are files, and the elements of _S_ and _T_ are lines of text). The minimum edit distance to transform _S_ into _T_ is achieved by doing |_S_|−LCS(S,T) deletes and |_T_|−LCS(S,T) inserts.  
In computational biology applications, often one has a more general notion of sequence alignment. Many of these different problems all allow for basically the same kind of Dynamic Programming solution.
## Example \#2: The Knapsack Problem
Imagine you have a homework assignment with different parts labeled A through G. Each part has a “value” (in points) and a “size” (time in hours to complete). For example, say the values and times for our assignment are:  
<center><table>
<tbody>
<tr><td><em></em></td><td><em><center>A</em></td><td><em><center>B</em></td><td><em><center>C</em></td><td><em><center>D</em></td><td><em><center>E</em></td><td><em><center>F</em></td><td><em><center>G</em></td></tr>
<tr><td><em><center>value</em></td><td><center>7</td><td><center>9</td><td><center>5</td><td><center>12</td><td><center>14</td><td><center>6</td><td><center>12</td></tr>
<tr><td><em><center>time</em></td><td><center>3</td><td><center>4</td><td><center>2</td><td><center>6</td><td><center>7</td><td><center>3</td><td><center>5</td></tr>
</tbody>
</table>
</center>  

Say you have a total of 15 hours: which parts should you do? If there was partial credit that was proportional to the amount of work done (e.g., one hour spent on problem C earns you 2.5 points) then the best approach is to work on problems in order of points/hour (a greedy strategy). But, what if there is no partial credit? In that case, which parts should you do, and what is the best total value possible?  
The above is an instance of the _knapsack problem_, formally defined as follows:  
**Definition 2** _In the **knapsack problem** we are given a set of n items, where each item i is specified by a size si and a value vi. We are also given a size bound S (the size of our knapsack). The goal is to find the subset of items of maximum total value such that sum of their sizes is at most S (they all fit into the knapsack)._  
We can solve the knapsack problem in exponential time by trying all possible subsets. With Dynamic Programming, we can reduce this to time _O_(_nS_).  
Let’s do this top down by starting with a simple recursive solution and then trying to memoize it. Let’s start by just computing the best possible total value, and we afterwards can see how to actually extract the items needed.
	// Recursive algorithm: either we use the last element or we don’t.
   	Value(n,S) // S = space left, n = # items still to choose from 
	{
		if (n == 0) 
			return 0; 
		if (s_n > S) 
			result = Value(n-1,S); // can’t use nth item
		else 
			result = max{v_n + Value(n-1, S-s_n), Value(n-1, S)};
		return result;	}
Right now, this takes exponential time. But, notice that there are only _O_(_nS_) _different_ pairs of values the arguments can possibly take on, so this is perfect for memoizing. As with the LCS problem, let us initialize a 2-d array arr[i][j] to “unknown” for all _i_, _j_.  
	Value(n,S) 
	{		if (n == 0) 			return 0;		if (arr[n][S] != unknown) 
			return arr[n][S]; // <- added this 
		if (s_n > S) 
			result = Value(n-1,S);		else 
			result = max{v_n + Value(n-1, S-s_n), Value(n-1, S)}; 
		arr[n][S] = result; // <- and this 
		return result;	}
Since any given pair of arguments to Value can pass through the array check only once, and in doing so produces at most two recursive calls, we have at most 2*n*(_S_ + 1) recursive calls total, and the total time is _O_(_nS_).  
So far we have only discussed computing the _value_ of the optimal solution. How can we get the items? As usual for Dynamic Programming, we can do this by just working backwards: if arr[n][S] = arr[n-1][S] then we _didn’t_ use the nth item so we just recursively work backwards from arr[n-1][S]. Otherwise, we _did_ use that item, so we just output the *n*th item and recursively work backwards from arr[n-1][S-s_n]. One can also do bottom-up Dynamic Programming.
## Example \#3: Matrix product parenthesizationOur final example for Dynamic Programming is the matrix product parenthesization problem.
Say we want to multiply three matrices _X_, _Y_, and _Z_. We could do it like (_XY_)_Z_ or like _X_(_YZ_). Which way we do the multiplication doesn’t affect the final outcome but it can affect the running time to compute it. For example, say _X_ is 100x20, _Y_ is 20x100, and _Z_ is 100x20. So, the end result will be a 100x20 matrix. If we multiply using the usual algorithm, then to multiply an _lxm_ matrix by an _mxn_ matrix takes time _O_(_lmn_). So in this case, which is better, doing (_XY_)_Z_ or _X_(_YZ_)?  
Answer: _X_(_YZ_) is better because computing _YZ_ takes 20x100x20 steps, producing a 20x20 matrix, and then multiplying this by _X_ takes another 20x100x20 steps, for a total of 2x20x100x20. But, doing it the other way takes 100x20x100 steps to compute _XY_ , and then multplying this with _Z_ takes another 100x20x100 steps, so overall this way takes 5 times longer. More generally, what if we want to multiply a series of _n_ matrices?  
**Definition 3** _The **Matrix Product Parenthesization** problem is as follows. Suppose we need to multiply a series of matrices: A<sub>1</sub> × A<sub>2</sub> × A<sub>3</sub> × . . . × A<sub>n</sub>. Given the dimensions of these matrices, what is the best way to parenthesize them, assuming for simplicity that standard matrix multiplication is to be used (e.g., not Strassen)?_  
There are an exponential number of different possible parenthesizations, in fact [2(n−1),n-1]/_n_, so we don’t want to search through all of them. Dynamic Programming gives us a better way.  
As before, let’s first think: how might we do this recursively? One way is that for each possible split for the final multiplication, recursively solve for the optimal parenthesization of the left and right sides, and calculate the total cost (the sum of the costs returned by the two recursive calls plus the _lmn_ cost of the final multiplication, where “_m_” depends on the location of that split). Then take the overall best top-level split.  
For Dynamic Programming, the key question is now: in the above procedure, as you go through the recursion, what do the subproblems look like and how many are there? Answer: each subproblem looks like “what is the best way to multiply some sub-interval of the matrices _A<sub>i</sub> × . . . × A<sub>j</sub>_?” So, there are only _O_(_n_<sup>2</sup>) _different_ subproblems.  
The second question is now: how long does it take to solve a given subproblem assuming you’ve already solved all the smaller subproblems (i.e., how much time is spent inside any _given_ recursive call)? Answer: to figure out how to best multiply _A<sub>i</sub> × . . . × A<sub>j</sub>_, we just consider all possible middle points _k_ and select the one that minimizes:
<center>optimal cost to multiply _A<sub>i</sub> . . . A<sub>k</sub>_ ← already computed</center><center>+ optimal cost to multiply _A<sub>k+1</sub> . . . A<sub>j</sub>_ ← already computed</center> <center>+ cost to multiply the results. ← get this from the dimensions</center>  
  
 This just takes _O_(1) work for any given _k_, and there are at most _n_ different values _k_ to consider, so overall we just spend _O_(_n_) time per subproblem. So, if we use Dynamic Programming to save our results in a lookup table, then since there are only _O_(_n_<sup>2</sup>) subproblems we will spend only _O_(_n_<sup>3</sup>) time overall.  
If you want to do this using bottom-up Dynamic Programming, you would first solve for all sub- problems with _j_ − _i_ = 1, then solve for all with _j_ − _i_ = 2, and so on, storing your results in an _n_ by _n_ matrix. The main difference between this problem and the two previous ones we have seen is that any given subproblem takes time _O_(_n_) to solve rather than _O_(1), which is why we get _O_(_n_<sup>3</sup>) total running time. It turns out that by being very clever you can actually reduce this to _O-(1) amortized time per subproblem, producing an _O_(_n_<sup>2</sup>)-time algorithm, but we won’t get into that here.
## High-level Discussion of Dynamic Programming
What kinds of problems can be solved using Dynamic Programming? One property these problems have is that if the optimal solution involves solving a subproblem, then it uses the optimal solution to that subproblem. For instance, say we want to find the shortest path from _A_ to _B_ in a graph, and say this shortest path goes through _C_. Then it must be using the shortest path from _C_ to _B_. Or, in the knapsack example, if the optimal solution does not use item _n_, then it is the optimal solution for the problem in which item _n_ does not exist. The other key property is that there should be only a polynomial number of different subproblems. These two properties together allow us to build the optimal solution to the final problem from optimal solutions to subproblems.  
In the top-down view of dynamic programming, the first property above corresponds to being able to write down a recursive procedure for the problem we want to solve. The second property corresponds to making sure that this recursive procedure makes only a polynomial number of _different_ recursive calls. In particular, one can often notice this second property by examining the arguments to the recursive procedure: e.g., if there are only two integer arguments that range between 1 and _n_, then there can be at most _n_<sup>2</sup> different recursive calls.  
Sometimes you need to do a little work on the problem to get the optimal-subproblem-solution property. For instance, suppose we are trying to find paths between locations in a city, and some intersections have no-left-turn rules (this is particulatly bad in San Francisco). Then, just because the fastest way from _A_ to _B_ goes through intersection _C_, it doesn’t necessarily use the fastest way to _C_ because you might need to be coming into _C_ in the correct direction. In fact, the right way to model that problem as a graph is not to have one node per intersection, but rather to have one node per ⟨_intersection_, _direction_⟩ pair. That way you recover the property you need.