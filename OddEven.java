package org.ProgramPractice;

public class OddEven {

	public static void main(String[] args) {
		// Print odd and even numbers from an array

		int arr1[] = { 101, 103, 1, 20000, 300, 300, 4, 5 };

		System.out.println("Even : ");

		for (int i = 0; i < arr1.length - 1; i++) {

			if (arr1[i] % 2 == 0) {

				System.out.println(arr1[i]);
			}

		}

		System.out.println("Odd : ");

		for (int i = 0; i < arr1.length - 1; i++) {

			if (arr1[i] % 2 != 0) {

				System.out.println(arr1[i]);
			}

		}

	}

}
