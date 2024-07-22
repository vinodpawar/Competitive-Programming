package org.ProgramPractice;

public class SmallestNumber {

	public static void main(String[] args) {
		// Print the smallest element in an array
		
		int arr1[] = {1,100, 20000, 300, 4, 5};
		int min = arr1[0];
		
		for(int i = 0; i < arr1.length - 1 ; i++){
		
			if(arr1[i+1] < min) {
				
				min = arr1[i+1];
				
			}
		}
		
		System.out.println("Smallest number is: " + min);
		

	}

}
