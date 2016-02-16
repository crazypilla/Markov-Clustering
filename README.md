Python with numpy package installed .Run on any IDE. We used Pycharm.
Markov_clustering was used to generate the .clu files.
Markov_With _Modularity was used to calculate modularity .
We used Pajek tool to visualize the results.

# Markov-Clustering
 MCL  Algorithm
 
 Step 1. Input is an un-directed graph, power parameter e, and inflation parameter r. 
 
 Step 2. Create the associated matrix 
 
 Step 3. Add self loops to each node (optional) 
 
 Step 4. Normalize the matrix 
 
 Step 5. Expand by taking the eth power of the matrix  [EXPANSION]
 
 Step 6. Inflate by taking inflation of the resulting matrix with parameter r  [INFLATION]
 
 Step 7. Repeat steps 5 and 6 until a steady state is reached (convergence). [Iterate till
converging point is reached] 

 Step 8. Interprete the resulting matrix to discover clusters. 

The algorithm has  a complexity of O(N
3
), where N is the number of vertices. –>( N
3
 =cost of one matrix
multiplication on two matrices of dimension N) +( Inflation = O(N
2
) ) +( number of steps to converge is not
proven, but experimentally shown to be ~10 to 100 steps)+several other sparse matrices. 

*************************************
We implemented the MCL algorithm in Python with the help of numpy  and math packages . Python has
several inbuilt packages and is fast. The code will be small yet very powerfully efficient.  
Here are the methods we used to implement in each step of the algorithm 
Step 1. Input is an un-directed graph, power parameter e, and inflation parameter r. 
 Get USER INPUT for filename, inflation and power parameters 
Step 2. Create the associated matrix 
 Getdata( filename ) method creates the adjacency matrix needed to represent the graph. 

Step 3. Add self loops to each node (optional)  
 Included it in the getdata(filename) method 
 
Step 4. Normalize the matrix 
 Normalize(matrix) method written to fulfill this step. 

Step 5. Expand by taking the eth power of the matrix: [EXPANSION STEP] 
 expansion(matrix,expansion_value) method which takes in the matrix generated and the user
input of expansion value as inputs and  returns
numpy.linalg.matrix_power(matrix,expansion_value) matrix as the output.  
Step 6. Inflate by taking inflation of the resulting matrix with parameter r  [INFLATION STEP]
 inflation(matrix, inflation_value) takes in the matrix generated and the user input of inflation 
value as inputs and  returns a normalized version of the numpy.power(matrix,inflation_value)
matrix as the output. 

Step 7.  Repeat steps 5 and 6 until a steady state is reached (convergence). [Iterate till converging point is
reached] 
 In the main, we iterated till the difference of the resultant matrix from previous iteration and
the matrix from the present iteration was zero, so as to achieve convergence. 
Step 8. Interprete the resulting matrix to discover clusters.
 Getclusters(matrix) method returns a list of clusters. 
 

 


 





