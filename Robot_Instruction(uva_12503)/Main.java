
//import java.io.File;
//import java.io.FileNotFoundException;
import java.util.*;

public class Main{

	public static void main(String[] args)  {
		// Create a File instance
		//File file = new File("G:\\java\\competitive programming\\in.txt"); // file
																			// address
		// Create a Scanner for the file
		//Scanner in = new Scanner(file); // scanner for file

		Scanner in = new Scanner(System.in);
	
		int n = Integer.parseInt(in.nextLine());
		

		if (n > 100) {
			return;
		}
		// iterate through test cases
		String s = null;
		//HashMap<Integer, String> maping = new HashMap<>();// to save operation
															// for each
															// instruction
		
		for (int i = 0; i < n; i++) {
			int position = 0;// initial position
			
			int instruction = Integer.parseInt(in.nextLine());//number of instruction
			

			if (instruction > 100 || instruction < 1) {
				break;
			}
			

			String[] store = new String[instruction];
			

			for (int j = 1; j <= instruction; j++) {
				s= in.nextLine();

				

				if (s.equals("LEFT")) {
					position = position - 1;
					
					//maping.put(j - 1, "LEFT"); // saving operation for each
												// instruction
					store[j-1]= "LEFT";

				}
				if (s.equals("RIGHT")) {
					position = position + 1;
					
					//maping.put(j - 1, "RIGHT");
					store[j-1]= "RIGHT";

				}
				if (s.contains("SAME")) {
					s = s.trim();
					
					s = s.replaceAll("\\s","");
					
					int index = s.lastIndexOf("S");
					
					
					String sub = s.substring(6);
					
					int value = Integer.parseInt(sub);

					if (value > j) {
						break;
					}

					
					//maping.put(j - 1, s21); // action for present instruction
					String s21 = store[value-1];
					store[j-1]= s21;

					if (s21.equals("RIGHT")) {
						position = position + 1;
						

					}
					if (s21.equals("LEFT")) {
						position = position - 1;
						

					}

				}
				s = null;
				

			}
			
			//maping.clear();
			
			System.out.println(position);

		}

	}

}
