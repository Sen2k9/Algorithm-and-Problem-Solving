//import java.io.File;
//import java.io.FileNotFoundException;
import java.util.*;
public class Main {

	public static void main(String[] args)  {
		//File file = new File("C:\\Users\\Sen\\eclipse-workspace\\UVA594\\src\\in.txt"); 
	    //Scanner in = new Scanner(file);
		Scanner in = new Scanner(System.in);
		while (in.hasNext()) {
			int n = in.nextInt();
			int reverse=0;
			int j=0;
			for(int i=31;i>=0;i--) {
				
				int b= i%8;
				
				if((n & (1<<i))!=0) {
					reverse |=(1<<(b+j));
				}
				else {
				    reverse &= ~(1<<(b+j));
				}
				if(b==0) {j=j+8;}
			}
			
			
			//00000111 01011011  11001101  00010101
			//00010101 11001101 01011011  00000111
			//10100010110011110110101110000
			
			System.out.println(n+" converts to "+reverse);
			
		}
		
		

	}

}
