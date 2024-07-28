public class PrintAlternateAlphabates {

	// Program that takes two strings and merges their characters alternately

	public String mixMatch(String a, String b) {

		String altrString = "";

		if (b.length() > a.length()) {

			for (int i = 0; i < a.length(); i++) {

				altrString = altrString + String.valueOf(a.charAt(i) + String.valueOf(b.charAt(i)));

			}

			for (int i = a.length(); i < b.length(); i++) {

				altrString = altrString + String.valueOf(b.charAt(i));
			}

		}

		else {

			for (int i = 0; i < b.length(); i++) {

				altrString = altrString + String.valueOf(a.charAt(i) + String.valueOf(b.charAt(i)));

			}

			for (int i = b.length(); i < a.length(); i++) {

				altrString = altrString + String.valueOf(a.charAt(i));
			}

		}

		return altrString;

	}

	public static void main(String args[]) {

		PrintAlternateAlphabates obj = new PrintAlternateAlphabates();

		String finalAltrString = obj.mixMatch("abcdfadfsadf", "pqr");

		System.out.println(finalAltrString);

	}

}
