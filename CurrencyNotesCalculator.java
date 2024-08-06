import java.util.Scanner;

public class CurrencyNotesCalculator {
    public static void main(String[] args) {
        // Create a Scanner object to read input from the user
        Scanner scanner = new Scanner(System.in);

        // Array of currency denominations
        int[] notesOf = {2000, 500, 100};

        // Prompt the user to enter the amount
        System.out.print("Enter amount: ");
        int amount = scanner.nextInt();

        // Iterate through each denomination and calculate the number of notes required
        for (int i = 0; i < notesOf.length; i++) {
            int notes = amount / notesOf[i];  // Integer division to get the number of notes
            System.out.println(notes + " notes of " + notesOf[i]);
            amount = amount % notesOf[i];  // Update the amount to the remainder
        }

        // Close the scanner
        scanner.close();
    }
}
