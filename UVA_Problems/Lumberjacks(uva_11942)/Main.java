import java.util.*;

public class Main{

     public static void main(String []args){
    	 System.out.println("Lumberjacks:");
    	// System.out.println("Give input number");
       Scanner in = new Scanner(System.in);
       int n= in.nextInt();
       boolean larger=false;
       boolean smaller=false;
       for(int i=1; i<=n;i++){
           
            int first_value= in.nextInt();
            //System.out.println("fisrst value"+first_value);
            int second_value= in.nextInt();
            //System.out.println("second value"+second_value);
            if (first_value> second_value){
                larger= true;
            
            }
            else{
                smaller= true;
            }
            for(int j=3;j<=10;j++){
                first_value= second_value;
                second_value= in.nextInt();
                if (first_value> second_value && larger==true){
                    larger= true;
                    smaller=false;
                }
                else if (first_value< second_value && smaller==true) {
                    smaller= true;
                    larger=false;
                
                }
                else{
                    //System.out.println("Unordered");
                    larger=false;
                    smaller=false;
                    //break;
                }
            
           }
           if((larger==true&& smaller==false) || (larger==false && smaller==true)){
               System.out.println("Ordered");
           }
           else
        	   System.out.println("Unordered");
       }
     }
}

