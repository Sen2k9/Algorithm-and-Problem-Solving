
import java.util.*;

public class Main {

	public static void main(String[] args){

		Scanner in = new Scanner(System.in);
		
		Queue<Integer> q = new LinkedList<>();
		Stack<Integer> test = new Stack<Integer>();
		while (in.hasNextInt()) {
			int n = in.nextInt();
			
			if (n == 0) {
				break;
			}
			boolean non_zero = true;
			while (non_zero) {

				int coach = in.nextInt();
				if (coach != 0) {
					q.add(coach);
					for (int i = 1; i < n; i++) {

						

						q.add(in.nextInt());
						

					}
					for (int j = 1; j <= n; j++) {
						test.push(j);
						while (!test.isEmpty()) {
							if ((int)test.peek() == (int)q.peek()) {
								test.pop();
								q.remove();
							} else {
								break;
							}
						}
					}
					if (q.isEmpty()) {
						System.out.println("Yes");
					} else {
						System.out.println("No");
					}

					
					q.clear();
					test.clear();
					

				} else {
					
					non_zero = false;
					break;

				}

			}
			System.out.println();

		}

	}

}
