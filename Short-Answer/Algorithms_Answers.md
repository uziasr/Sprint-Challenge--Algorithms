#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This snippet of code is running a while loop for as long as a is less than the cube of n. a is incrementing by square of n for every iteration inside the while loop.

By testing a few numbers we can see that the while loop will run n times, every time. This is linear.


b) This is a nested while loop inside of a for loop. Individually these pieces are linear, however with the way that this algorithm is put together, the bigger n is the longer it may take to run.

This function will have to exhaust its for loop every time, however j increments at the rate of 2 squared inside the while loop.

This is not linear and it is not as bad as O(n^2) it may closely resemble     O(n log n)  


c) I notice that function is calling itself until it reaches the base case of bunnies == 0. That fact that it calls itself only once and decrements the amount bunnies by 1 leads me to believe that this is a classic 0(n). It is linear.

## Exercise II

The first approach I would rule is a linear one. This would require looking through an entire set of floors before determining the value of f and thus costing too many eggs. I would take the approach of  dropping the egg from the middle of the building and seeing if it breaks. If it does, then I would no longer need to check upper half of the building. I would keep halving the floors and determine what direction to check based on whether the egg cracked or not!

It uses the best feature of a merge sort WITHOUT having to iterate through every floor. In this case, we are working with O(log(n))


