import java.util.Arrays;

public class PrimeNumber {
    /**
     * This method checks if a number is prime or not and contains all statuses
     * @param n Number to be checked
     * @return Prime or not
     */
    private static boolean isPrimeNumber1(int n) {
        if (n == 1) {
            return false;
        }
        if (n == 2) {
            return true;
        }
        
        for (int i = 2; i < n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
    
    /**
     * This method checks if a number is prime or not until the square root of n
     * @param n Number to be checked
     * @return Prime or not
     */
    private static boolean isPrimeNumber2(int n) {
        if (n == 1) {
            return false;
        }
        if (n == 2) {
            return true;
        }
        
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
    
    /**
     * This method finds number of prime numbers in [1, {@code end}] range by saving numbers in an array
     * @param end The last number in range
     * @return Count of prime numbers
     */
    public static int countPrimeNumbers3(int end) {
        boolean[] notPrime = new boolean[end + 1];
        notPrime[1] = true;
        for (int i = 2; i <= end; i++) {
            for (int j = 2; i * j <= end; j++) {
                notPrime[i * j] = true;
            }
        }
        
        int result = 0;
        for (int i = 1; i <= end; i++) {
            if (!notPrime[i]) {
                result++;
            }
        }
        return result;
    }
    
    /**
     * This method finds number of prime numbers in [1, {@code end}] range by saving numbers in an array
     * and more efficient algorithm
     * @param end The last number in range
     * @return Count of prime numbers
     */
    public static int countPrimeNumbers4(int end) {
        boolean[] notPrime = new boolean[end + 1];
        notPrime[1] = true;
        for (int i = 2; i <= end; i++) {
            if (!notPrime[i]) {
                for (int j = 2; i * j <= end; j++) {
                    notPrime[i * j] = true;
                }
            }
        }
        
        int result = 0;
        for (int i = 1; i <= end; i++) {
            if (!notPrime[i]) {
                result++;
            }
        }
        return result;
    }
    
    /**
     * This method finds number of prime numbers in [{@code start}, {@code end}] range
     * @param end The last number in range
     * @return Count of prime numbers
     */
    public static int countPrimeNumbers1(int end) {
        int result = 0;
        for (int i = 1; i <= end; i++) {
            if (isPrimeNumber1(i)) {
                result++;
            }
        }
        return result;
    }
    
    /**
     * This method finds number of prime numbers in [{@code start}, {@code end}] range and checks it until root of n
     * @param end The last number in range
     * @return Count of prime numbers
     */
    public static int countPrimeNumbers2(int end) {
        int result = 0;
        for (int i = 1; i <= end; i++) {
            if (isPrimeNumber2(i)) {
                result++;
            }
        }
        return result;
    }
}
