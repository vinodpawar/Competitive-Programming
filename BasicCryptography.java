public class BasicCryptography {
    public static void main(String[] args) {
        // Define the alphabet
        char[] alphabet = "abcdefghijklmnopqrstuvwxyz".toCharArray();
        
        // Input string to be encrypted
        String inputName = "abdcz";
        
        // Convert inputName to a char array for processing
        char[] inputChars = inputName.toCharArray();
        
        // StringBuilder to build the encrypted result
        StringBuilder encryptedName = new StringBuilder();
        
        for (char ch : inputChars) {
            // Find the index of the character in the alphabet
            int index = new String(alphabet).indexOf(ch);
            
            // Calculate new index by shifting 4 positions ahead
            int newIndex = (index + 4) % alphabet.length;
            
            // Append the corresponding letter to the encrypted result
            encryptedName.append(alphabet[newIndex]);
        }
        
        // Print the encrypted result
        System.out.println(encryptedName.toString());
    }
}
