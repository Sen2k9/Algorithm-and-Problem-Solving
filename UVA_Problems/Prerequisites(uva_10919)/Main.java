//import java.io.File;
//import java.io.FileNotFoundException;

import java.util.*;

public class Main {

	public static void main(String[] args)  {
		//File file = new File("C:\\Users\\Sen\\eclipse-workspace\\uva 10919\\src\\in.txt");
		//Scanner in = new Scanner(file);
		Scanner in = new Scanner(System.in);
		// Stack<Integer> stack = new Stack<Integer>();
		
		Stack<Integer> total_course = new Stack<Integer>();
		while (in.hasNext()) {
			int chosen_course = in.nextInt();
			//System.out.println(chosen_course);
			if (chosen_course != 0) {
				int category = in.nextInt();
				boolean pass = true;
				for (int course = 0; course < chosen_course; course++) {
					total_course.push(in.nextInt());
				}
				//System.out.println(total_course);
				for (int c = 0; c < category; c++) {
					int available_course = in.nextInt();
					int minimum = in.nextInt();
					Stack<Integer> cat_course = new Stack<Integer>();
					for (int i = 0; i < available_course; i++) {
						cat_course.push(in.nextInt());
					}
					//System.out.println(cat_course);
					int match = 0;
					Stack<Integer> copy_total_course = new Stack<Integer>();
					copy_total_course = cat_course;
					while (!copy_total_course.isEmpty()) {
						int a = copy_total_course.pop();
						//System.out.println(a);
						if (total_course.contains(a)) {
							match++;
						}

					}
					//System.out.println(cat_course);
					//System.out.println(total_course);
					//System.out.println("match "+match);
					if (match < minimum) {
						pass = false;
					}

				}
				if (pass == true) {
					System.out.println("yes");
				} else {
					System.out.println("no");
				}
				total_course.clear();

			} else {
				break;
			}

		}
	}

}
