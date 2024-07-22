package org.ProgramPractice;

public class DuplicateElement {

	public static void main(String[] args) {
		// Print the duplicate elements of an array
		
		int arr1[] = {1,100,1, 20000, 300,300, 4, 5};
		
		
		for(int i = 0; i < arr1.length - 2 ; i++){
		
			
			for(int j = i+1; j < arr1.length; j++) {
			
				if(arr1[i] == arr1[j]) {
					
					System.out.println(arr1[i]);
					
				}
				
			}
			
		}
		
		
		

	}

}
