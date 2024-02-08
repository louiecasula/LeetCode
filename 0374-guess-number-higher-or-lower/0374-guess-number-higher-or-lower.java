/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        // Cast between long and int to handle large test cases
        // Commence bin search
        long l = 1L;
        long r = (long) n;
        while (true) {
            long g = (l + r) / 2L;
            System.out.println((int) g);
            if (guess((int) g) == -1) {
                r = g - 1L;
            }
            else if (guess((int) g) == 1) {
                l = g + 1L;
            } else { return (int) g; }
        }
    }
}