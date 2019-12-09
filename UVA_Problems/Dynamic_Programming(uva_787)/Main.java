
import java.io.File;
import java.io.FileNotFoundException;
import java.math.BigInteger;
import java.util.ArrayList;

import java.util.Scanner;
import java.util.*;

public class Main {
	public static void main(String[] args) throws FileNotFoundException{
		//File file = new File("C:\\Users\\Sen\\eclipse-workspace\\uva 787\\in.txt");
		//Scanner in = new Scanner(file);
		Scanner in = new Scanner(System.in);
		

		for (int testCase = 1; in.hasNext(); testCase++) {
			ArrayList<Integer> arr = new ArrayList<>();
			int n = in.nextInt();
			while (n != -999999) {

				arr.add(n);
				n = in.nextInt();
			}
			

			ArrayList<BigInteger> dist = new ArrayList<>();
			BigInteger max = BigInteger.valueOf(-999999);

			for (int u = 0; u < arr.size(); u++) {

				BigInteger mul = BigInteger.valueOf(1);
				

				for (int v = u; v < arr.size(); v++) {
					
						BigInteger number = BigInteger.valueOf( arr.get(v));
						mul = mul.multiply(number);
						
						if(mul.compareTo(max)==1) {
							max=mul;

						}


					
				}
				
			}
			System.out.println(max.toString());


			arr.clear();

		}

	}
}