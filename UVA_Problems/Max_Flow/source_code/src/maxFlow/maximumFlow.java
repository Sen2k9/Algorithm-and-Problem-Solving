package maxFlow;

import java.io.File;
import java.util.LinkedList;
import java.util.Scanner;

public class maximumFlow {
	

 
	private boolean BreadFirstSearch(int rGraph[][], int s, int t, int parent[], int V) {
		
		boolean visited[] = new boolean[V];
		//A visited array
		for (int i = 0; i < V; i++) {
			//Assign false to the visited array
			visited[i] = false;
		}
		LinkedList<Integer> queue = new LinkedList<Integer>();
		//A queue data structure created
		queue.add(s);
		//Add source to the queue
		// Make it visited as true
		visited[s] = true;
		parent[s] = -1;
		//parent of source is -1
		while (queue.size() != 0) {
			//Until queue is not empty
			int u = queue.poll();
			// Take the first value of the queue

			for (int v = 0; v < V; v++) {
				// From source checking which vertex is reachable in the passed graph

				if (visited[v] == false && rGraph[u][v] > 0) {
					queue.add(v);
					//which vertex is reachable adding to the queue

					visited[v] = true;
					parent[v] = u;
					// storing parent vertex
				}
			}
		}

		return (visited[t] == true);
		// return true if sink t is reachable

	}
private int edmondsKarp(int Graph[][], int s, int t, int V) {
	 int u,v;
	 int temp_graph[][] = new int[V][V];// temporary graph
	 
	 
	 for( u=0;u<V;u++) {
		 for( v=0;v<V;v++) {
			 temp_graph[u][v]=Graph[u][v];
		 }
	 }
	 int[] parent= new int[V]; // parents array
	 int max_flow=0; // initialize max flow as zero
	 
	 while(BreadFirstSearch(temp_graph,s,t,parent, V)) { // checking if there any path exits
		 int path_flow= Integer.MAX_VALUE; // infinite value
		
		 LinkedList<Integer> q = new LinkedList<Integer>();//queue
		 LinkedList<Integer> p = new LinkedList<Integer>();// queue
		 q.add(t); // add sink to queue
		 while(q.size()!=0) {
		 v= q.poll();
		 if(parent[v]!=-1) { //if source comes stop 
			 u=parent[v];
			 q.add(u);
			 path_flow= Math.min(path_flow, temp_graph[u][v]);
			// Evaluating the minimum value through the path from source to sink
		 }
		 }
	
	 p.add(t);
		 while(p.size()!=0) {
		 v= p.poll();
		if(parent[v]!=-1) {
			 u=parent[v];
			 p.add(u);
			 temp_graph[u][v]-=path_flow; // adding path flow to the edges
			 temp_graph[v][u]+=path_flow;// adding path flow
		 }
		 }

		 max_flow+=path_flow;
		// System.out.println("max flow "+max_flow);
		 boolean recheable[]= new boolean[V];
		 
	DepthFirstSearch(temp_graph,s,recheable,V);
	
	for(int i=0;i<V;i++) {
		for(int j=0;j<V;j++) {
			if(recheable[i]==true && recheable[j]==false && Graph[i][j]!=0) {
				// Which vertex is reachable and which are not reachable makes s-t cut
				System.out.printf("(%d %d)\n",i+1,j+1);
				
			}
		}
	}
	 }
	
	 
	 return max_flow;
 }
	private void DepthFirstSearch(int[][] residual_Graph, int s, boolean[] visited, int V) {
		// Assigning true of the vertex which are reachable
	visited[s]=true;
	for(int i=0;i<V;i++) {
		if(residual_Graph[s][i]>0 && visited[i]!=true) {
			DepthFirstSearch(residual_Graph, i, visited, V);
		}
	}
	
}
	public static void main(String[] args) {
		maximumFlow max= new maximumFlow();
		//Creating object of maximumFlow class
		Scanner x=null;
		// An scanner object
		try {
			x = new Scanner(new File("C:\\Users\\Sen\\eclipse-workspace\\maxFlow\\src\\Problem_1.txt")); // text
																														// file
																														// location
		} catch (Exception e) {
			System.out.println("Could not find file");
		}
		int v= x.nextInt();
		//Taking vertex number
		int s=x.nextInt();
		//taking source number
		int t=x.nextInt();
		//taking sink number
		int Given_Graph[][]= new int[v][v];
		// Adjacency matrix of graph
		
		while(x.hasNextInt()) {
			// Taking edges with capacity
			int u=x.nextInt();
			int c=x.nextInt();
			int value=x.nextInt();
		
			Given_Graph[u-1][c-1]=value;
			//Graph in an adjacency matrix
		}
	
		int flow=max.edmondsKarp(Given_Graph, s-1, t-1, v);
		System.out.println(flow);
	}
		
}
