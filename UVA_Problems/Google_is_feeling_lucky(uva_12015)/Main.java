import java.util.*;
import java.util.Map.Entry;
import java.io.*;

public class Main {

	public static void main(String[] args) throws FileNotFoundException {
		// Create a File instance
	    //File file = new File("G:\\java\\Practice\\in.txt"); //file address
	    // Create a Scanner for the file
	    //Scanner input = new Scanner(file); //scanner for file
		Scanner input = new Scanner(System.in);
	    int loop= input.nextInt();
	    //Set<String,Integer> set = new LinkedHashSet<>();
	    Map<String, Integer> hashMap = new LinkedHashMap<>();
	    // Read data from a file
	    for(int i=1;i<=loop;i++){
	    	for(int j=1;j<=10;j++){
	    		String name = input.next();
	    		int score = input.nextInt();
	    		hashMap.put(name,score);
	    		
	    		
	    	}
//	    	System.out.println(hashMap+" ");
//		    hashMap.forEach(
//		    	      (name, age) -> System.out.print(name + ": " + age + "\n "));
		    System.out.printf("Case #%d:\n",i);
		    getAddresswithMaxValue(hashMap);
		    hashMap.clear();
	    }

	    

	      // Close the file
	    input.close();
	}
public static void getAddresswithMaxValue(Map<String, Integer> hashMap){
    int maxValue =(Collections.max(hashMap.values())); 
    for (Entry<String, Integer> entry : hashMap.entrySet()) {  // Itrate through hashmap
        if (entry.getValue()==maxValue) {
            System.out.println(entry.getKey());     // Print the key with max value
        }
    }
	//return null;
}

}
