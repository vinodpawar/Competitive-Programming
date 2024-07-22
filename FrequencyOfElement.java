package org.ProgramPractice;

public class FrequencyOfElement {

	public static void main(String[] args) {
		// Find the frequency of each element in the array

		int arr1[] = { 101, 103, 1, 20000, 300, 300, 4, 101 };

		for (int i = 0; i < arr1.length - 2; i++) {

			int count = 1;

			for (int j = 1; j < arr1.length - 1; j++) {

				if (arr1[i] == arr1[j]) {

					count = count + 1;

				}

			}

			System.out.println(arr1[i] + " is " + count + " times");

		}

	}

}
