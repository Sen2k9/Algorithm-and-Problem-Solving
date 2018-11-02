
import java.util.*;

public class Main {

	public static void main(String[] args){

		Scanner in = new Scanner(System.in);
		while (in.hasNext()) {
			int n = Integer.parseInt(in.next());
			String[] words = new String[n];
			for (int i = 0; i < n; i++) {
				words[i] = in.next();
			}
			int num_rule = Integer.parseInt(in.next());

			String[] rules = new String[num_rule];
			for (int i = 0; i < num_rule; i++) {
				rules[i] = in.next();
			}
			char[][] rule_board = new char[num_rule][];
			for (int i = 0; i < num_rule; i++) {
				rule_board[i] = rules[i].toCharArray();
			}
			ArrayList<String> password = new ArrayList<String>();
			
			for (int i = 0; i < num_rule; i++) {

				find(rule_board[i], words, password);

			}
			System.out.println("--");
			for(String s: password) {
				System.out.println(s);
			}

		}

	}

	private static void find(char[] rule, String[] words, ArrayList<String> password) {
		String rules= new String(rule);
		
		for (String s : words) {
			
			
				
				
				if(rules.contains("#") && rules.contains("0")) {
					
					typeI(rule,s,password);
					
					
				}

			
		}

		
		if(rules.contains("#") && !rules.contains("0")) {
			typeII(words,rule.length,words.length, password);
		}
		
		if(rules.contains("0") && !rules.contains("#")) {
			String[] number= new String[10];
			for(int i=0;i<10;i++) {
				number[i]= Integer.toString(i);
			}
			typeII(number,rule.length,number.length, password);
		}
		
	}



	private static void typeII(String[] words, int length, int word_length, ArrayList<String> password) {
		recursion(words, length, "", word_length, password); 
		
	}

private static void recursion(String[] words, int length, String s, int word_length, ArrayList<String> password) {
	
	if(length==0) {
		password.add(s);
		return;
	}
	
    for (int j = 0; j < word_length; j++) { 

        String whole_word = s + words[j];  
      
        recursion(words, length - 1, whole_word, word_length, password); 
    } 
  
    return;
	}



	private static void typeI(char[] rule, String s, ArrayList<String> password) {
		
		for (int j = 0; j < 10; j++) {
			String pass ="";
			for (int i = 0; i < rule.length; i++) {
				
				
				if (rule[i] == '#') {
					pass += s;

				} else {

					pass += j;
				}
			}
			password.add(pass);
		}
		
	}

}
