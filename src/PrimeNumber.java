public interface PrimeNumber {
    /**
     * This method checks if a number is prime or not and contains all statuses
     * @param n Number to be checked
     * @return Prime or not
     */
    boolean isPrimeNumber1(int n);
    
    /**
     * This method checks if a number is prime or not until the square root of n
     * @param n Number to be checked
     * @return Prime or not
     */
    boolean isPrimeNumber2(int n);
    
    /**
     * This method finds number of prime numbers in [{@code start}, {@code end}] range
     * @param end The last number in range
     * @return Count of prime numbers
     */
    int countPrimeNumbers1(int end);
    
    /**
     * This method finds number of prime numbers in [{@code start}, {@code end}] range and checks it until root of n
     * @param end The last number in range
     * @return Count of prime numbers
     */
    int countPrimeNumbers2(int end);
    
    /**
     * This method finds number of prime numbers in [1, {@code end}] range by saving numbers in an array
     * @param end The last number in range
     * @return Count of prime numbers
     */
    int countPrimeNumbers3(int end);
    
    /**
     * This method finds number of prime numbers in [1, {@code end}] range by saving numbers in an array
     * and more efficient algorithm
     * @param end The last number in range
     * @return Count of prime numbers
     */
    int countPrimeNumbers4(int end);
}
