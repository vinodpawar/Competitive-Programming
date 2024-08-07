import java.util.HashMap;
import java.util.Map;

public class CricketScoreCalculator {
    public static void main(String[] args) {
        // Input score given
        Object[] inputScore = {1, ".", 2, "w", "W", 6, ".", 2, "b", 3, 4};

        // Initial player score
        Map<Integer, Integer> playerScore = new HashMap<>();
        for (int i = 1; i <= 11; i++) {
            playerScore.put(i, 0);
        }

        // Values set for Players, Players on strike, Players on non-strike, Ball count, Score, extras and overs
        int[] players = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11};
        int playerOnStrike = players[0];
        int playerOnNonStrike = players[1];
        int ballCount = 0;
        int score = 0;
        int extras = 0;
        int overs = 0;

        // Loop to operate on given input score
        for (Object obj : inputScore) {
            ballCount++;

            if (ballCount == 6) {
                overs++;
                int temp = playerOnStrike;
                playerOnStrike = playerOnNonStrike;
                playerOnNonStrike = temp;
                ballCount = 0;
            }

            // Extras-bye
            if (obj.equals("b")) {
                extras++;
                // Tip: do not consider ball here
                ballCount--;
            }

            // Wicket
            else if (obj.equals("W")) {
                if (playerOnNonStrike > playerOnStrike) {
                    playerOnStrike = playerOnNonStrike + 1;
                    if (playerOnStrike == 11) break;
                } else {
                    playerOnStrike = playerOnStrike + 1;
                    if (playerOnStrike == 11) break;
                }
            }

            // Extras-wide
            else if (obj.equals("w")) {
                extras++;
                // Tip: do not consider ball here
                ballCount--;
            }

            // Add score to player
            else if (obj instanceof Integer) {
                int runs = (Integer) obj;
                playerScore.put(playerOnStrike, playerScore.get(playerOnStrike) + runs);
                score += runs;

                // Strike change on odd runs
                if (runs % 2 == 1) {
                    int temp = playerOnStrike;
                    playerOnStrike = playerOnNonStrike;
                    playerOnNonStrike = temp;
                }
            }
        }

        score += extras;

        // Print final output scores
        int lastPlayer = 0;
        if (playerOnStrike > playerOnNonStrike) {
            lastPlayer = playerOnStrike + 1;
        } else {
            lastPlayer = playerOnNonStrike + 1;
        }

        // Printing score of all players who have been on the ground
        for (int i = 1; i < lastPlayer; i++) {
            System.out.println("P" + i + ": " + playerScore.get(i));
        }

        System.out.println("Extras: " + extras);
    }
}
