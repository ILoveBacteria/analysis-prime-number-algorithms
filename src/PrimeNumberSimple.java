public class PrimeNumberSimple extends PrimeNumberAbstract {
    @Override
    public int countPrimeNumbers3(int end) {
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
    
    @Override
    public int countPrimeNumbers1(int end) {
        int result = 0;
        for (int i = 1; i <= end; i++) {
            if (isPrimeNumber1(i)) {
                result++;
            }
        }
        return result;
    }
    
    @Override
    public int countPrimeNumbers2(int end) {
        int result = 0;
        for (int i = 1; i <= end; i++) {
            if (isPrimeNumber2(i)) {
                result++;
            }
        }
        return result;
    }
}
