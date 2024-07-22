package org.ProgramPractice;

public class SumOfAllNumbers {

	public static void main(String[] args) {
		// Print the sum of all the items of the array
		
		int arr1[] = {1,100,1, 20000, 300,300, 4, 5};
		int sum = 0;
		
		for(int i = 0; i < arr1.length; i++){		
			
			sum += arr1[i];
			
		}
		
		System.out.println(sum);
		
		

	}

}
