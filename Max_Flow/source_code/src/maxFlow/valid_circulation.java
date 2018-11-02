package maxFlow;

import java.io.File;
import java.util.LinkedList;
import java.util.Scanner;

public class valid_circulation {
	static int[] demand;
	static boolean valid_circulation = false;

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

	void edmondsKarp(int Graph[][], int s, int t, int V) {
		int u, v;
		int rGraph[][] = new int[V][V];// temporary graph
		for (u = 0; u < V; u++) {
			for (v = 0; v < V; v++) {
				rGraph[u][v] = Graph[u][v];
				//Coping from the main graph
			}
		}

		int[] parent = new int[V]; // parents array

		while (BreadFirstSearch(rGraph, s, t, parent, V)) { // checking if there any path exits
			int path_flow = Integer.MAX_VALUE; // infinite value

			LinkedList<Integer> q = new LinkedList<Integer>();// queue
			LinkedList<Integer> p = new LinkedList<Integer>();// queue
			
			q.add(t); // add sink to queue
			while (q.size() != 0) {
				v = q.poll();
				if (parent[v] != -1) { // if source comes stop adding to the queue
					u = parent[v];
					q.add(u);
					path_flow = Math.min(path_flow, rGraph[u][v]);
					// Evaluating the minimum value through the path from source to sink
				}
			}

			p.add(t);
			while (p.size() != 0) {
				v = p.poll();
				if (parent[v] != -1) {
					u = parent[v];
					p.add(u);
					rGraph[u][v] -= path_flow; // subtracting path flow to the edges

					rGraph[v][u] += path_flow;// adding path flow
				}
			}

		}

		for (int i = 1; i < V - 1; i++) {
			for (int j = 1; j < V - 1; j++) {
				//Printing the flows along the edges
				// if [i][j] actually has edge in the real graph then printing the flows
				//Of the residual graph
				if (Graph[i][j] != 0)
					System.out.printf("%d %d %d\n", i, j, rGraph[j][i]);
			}
		}

		

	}

	public static void main(String[] args) {
		valid_circulation ek = new valid_circulation();
		Scanner scan = null;
		Scanner x = null;

		try {
			scan = new Scanner(new File("C:\\Users\\Sen\\eclipse-workspace\\maxFlow\\src\\Problem_2.txt")); // text
																										// file
																										// location
		} catch (Exception e) {
			System.out.println("Could not find file");
		}

		try {
			x = new Scanner(new File("C:\\Users\\Sen\\eclipse-workspace\\maxFlow\\src\\Problem_2.txt")); // text
																									// file
																									// location
		} catch (Exception e) {
			System.out.println("Could not find file");
		}
		int v = 0;
		int u, v1, c;
		int a, b;

		String s = scan.nextLine();
		s = s.trim();
		if (s.length() == 1) {
			v = x.nextInt();

		}
		int[][] Given_Graph = new int[v + 2][v + 2]; 
		// Given graph with two extra vertex.
		// One is super source s=0 and another is super sink t=v-1
		demand = new int[v + 2];
		// demand for every vertex with super source and super sink
		while (scan.hasNextLine()) { 
			// check if the file has any line left
			s = scan.nextLine();
			//scaning the line with whitespaces
			s = s.trim();
			// triming the whitespaces at the end of line

			if (s.length() >= 5) {
				//if the input contains 3 number and two whitespace this condition work
				// like as if the input contains 1 2 2 ; it has 3 number and 2 spaces. Total length 5
				u = x.nextInt();
				v1 = x.nextInt();
				c = x.nextInt();

				Given_Graph[u][v1] = c;

			}

			if (s.length() >= 3 && s.length() < 5) {
				//if the input contains 2 number and 1 whitespace this condition work
				// like as if the input contains 2 2 ; it has 2 number and 1 spaces. Total length 3
				// if value contains negative the length will be 4. such as 2 -2
				a = x.nextInt();
				b = x.nextInt();
				demand[a] = b;
			}

		}
		for (int i = 0; i < v + 2; i++) {
			if (demand[i] < 0) {
				// A super source s=0 is taken
				// vertex v which has demand(dv)<0 they will be connected with the super source(s)
				// And the edge capacity will be -dv

				Given_Graph[0][i] = -demand[i];

			}
		}

		for (int i = 0; i < v + 2; i++) {
			if (demand[i] > 0) {
				// A super source t=v-1 is taken
				// vertex v which has demand(dv)>0 they will be connected with the super sink(t)
				// And the edge capacity will be dv

				Given_Graph[i][v + 1] = demand[i];

			}
		}

		int dem = 0;
		for (int i = 0; i < v + 2; i++) {
			dem += demand[i];
		}

		if (dem == 0) {
			//if the total demand is equals zero; which means sum(-dv)= sum(+dv)
			// the circulation is valid
			valid_circulation = true;
		}

		if (valid_circulation) {
			//If the circulation is valid then prints the flows
			System.out.println("valid circulation ");
			//Invoking Edmonds-Karp algorithm to compute the max flow through the new created graph
			// with an extra source and sink
			ek.edmondsKarp(Given_Graph, 0, v + 1, v + 2);

		} else
			//Else print NO
			System.out.println("NO");

	}

}
