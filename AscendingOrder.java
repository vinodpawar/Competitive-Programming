package org.ProgramPractice;

public class AscendingOrder {

	public static void main(String[] args) {
		// Sort the elements of an array in ascending order

		int arr1[] = { 101, 100, 1, 20000, 300, 300, 4, 5 };
		int temp;
		
//		System.out.println(arr1[arr1.length-2]);

		for (int i = 0; i < arr1.length-1; i++) {

			for (int j = 1; j < arr1.length; j++) {

				if (arr1[i] > arr1[j]) {

					temp = arr1[j];
					arr1[j] = arr1[i];
					arr1[i] = temp;
				}
			}
		}

		for (int i = 0; i < arr1.length; i++) {

			System.out.print(arr1[i] + ", ");
		}

	}

}
