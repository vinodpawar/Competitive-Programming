public class ReverseString {

	public static void main(String[] args) {
	
		// Reverse a string

		String str = "Hello this is test String";

		for(int i = str.length()-1; i >= 0; i--) {
			
			System.out.print(str.charAt(i));
			
			
		}

	}

}