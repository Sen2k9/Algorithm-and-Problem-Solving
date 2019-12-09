
import java.util.Scanner;
import java.util.*;
public class Main {

	public static void main(String[] args)  {

		Scanner in = new Scanner(System.in);
		for(int testCase=1;in.hasNext();testCase++) {
			int m= in.nextInt();
			int n= in.nextInt();
			int total=in.nextInt();
			int[] weight = new int[2];
			weight[0]=m;
			weight[1]=n;
			int n2=2;
			int[] total_burger= new int[10000+10];
;
			int time=0;

			total_burger[m]=1;
			total_burger[n]=1;
			for(int w=1;w<=total;w++) {
				

				if(total_burger[w]>0) {
					
					
					if(w+m<=total) {
						total_burger[w+m]= Math.max(total_burger[w+m], total_burger[w]+1);
						//System.out.printf("inside w= %d, number=%d \n",w+m,total_burger[w+m]);
					}
					if(w+n<=total) {
						total_burger[w+n]= Math.max(total_burger[w+n], total_burger[w]+1);
						//System.out.printf("inside w= %d, number=%d \n",w+n,total_burger[w+n]);
					}
				}
					
					
			}
			if(total_burger[total]>0) {
				System.out.println(total_burger[total]);
			}
			else {
				boolean printed =false;
				for(int i=total-1;i>=0;i--) {
					if(total_burger[i]>0) {
						time= total-i;
						printed=true;
						System.out.println(total_burger[i]+" "+time);
						break;
					}
				}
				if(!printed)
				{System.out.println(total_burger[total]+" "+total);}
			}

			
		}

	}

	

}
