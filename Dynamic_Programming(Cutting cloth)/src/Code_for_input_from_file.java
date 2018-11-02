import java.io.File;
import java.util.Scanner;

public class Code_for_input_from_file {

	public static void main(String[] args) {
		Scanner x = null;
		
		try {
			x= new Scanner(new File("C:\\Users\\Sen\\eclipse-workspace\\PA1\\pa2.txt")); //text file location
		}
		catch(Exception e) {
			System.out.println("Could not find file");
		}
		//Reading values from file by using x
		int X= x.nextInt(); // X(height) dimension of cloth
		int Y=x.nextInt(); //Y(width) dimension of cloth
		
		int[][] cloth= new int[X+1][Y+1];  // 2D matrix for cloth cutting
		int n=x.nextInt(); // Number of template
		int[] template_a= new int[n+1]; // x(height) value of template
		int[] template_b= new int[n+1]; // y(width) value of template
		int[] template_c= new int[n+1]; // selling price of template
		for(int i=1;i<=n;i++) {
			template_a[i]=x.nextInt();
			template_b[i]=x.nextInt();
			template_c[i]=x.nextInt();
		}
		x.close(); // closing access from file
		for(int i=1;i<=X;i++) {  // row of the cloth matrix
			for(int j=1;j<=Y;j++) { //column of the cloth matrix
				int template_cutting =0;
				int template_cutting2=0;
				for(int k=1;k<=n;k++) {
					if(template_a[k]==i && template_b[k]==j) // for every index of template x and y 
						template_cutting = template_c[k];    // if x and y matches with the value of X and Y print out the selling price c
					if(template_b[k]==i&& template_a[k]==j)  // Same value of X and Y is also checking for y and x value of template
						template_cutting2=template_c[k];
						
						
				}
				int template_max= Math.max(template_cutting , template_cutting2); // taking the max of both
				int Cutting_X_max=0; // initialize as zero value
				for(int k=1;k<i;k++) { // for every possible cutting in the horizontal(height) side from 1 to X value
					                     //taking the max value for fixed Y(width)
					if(cloth[k][j]+cloth[i-k][j]>Cutting_X_max)
						Cutting_X_max = cloth[k][j] + cloth[i-k][j];
					
				}
				int Cutting_Y_max=0;
				for(int k=1;k<j;k++) {// for every possible cutting in the vertical(width) side from 1 to Y value
                     //taking the max value for fixed X(height)
					if(cloth[i][k]+cloth[i][j-k]>Cutting_Y_max)
						Cutting_Y_max=cloth[i][k]+cloth[i][j-k];
				}
				int max_cutting= Math.max(Cutting_X_max, Cutting_Y_max);
				
				cloth[i][j]= Math.max(template_max, max_cutting);
				
			}
		}
		System.out.println("Best return price: "+cloth[X][Y]);



	}

}
