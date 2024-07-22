package org.ProgramPractice;

public class LargestNumber {

	public static void main(String[] args) {
		// Print the largest element in an array
		
		int arr1[] = {100, 20000, 300, 4, 5};
		int max = arr1[0];
		
		for(int i = 0; i < arr1.length - 1 ; i++){
		
			if(arr1[i+1] > max) {
				
				max = arr1[i+1];
				
			}
		}
		
		System.out.println("Largest number is: " + max);
		

	}

}
