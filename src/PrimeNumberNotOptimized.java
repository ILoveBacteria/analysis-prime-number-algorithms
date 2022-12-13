public class PrimeNumberNotOptimized implements PrimeNumber {
    @Override
    public int countPrimeNumbers3(int end) {
        long[] notPrime = new long[end + 1];
        notPrime[1] = 1;
        for (long i = 2; i <= end; i++) {
            for (long j = 2; i * j <= end; j++) {
                long index = i * j;
                notPrime[(int) index] = 1;
            }
        }
        
        long result = 0;
        for (long i = 1; i <= end; i++) {
            if (notPrime[(int) i] == 0) {
                result++;
            }
        }
        return (int) result;
    }
    
    @Override
    public int countPrimeNumbers1(int end) {
        long result = 0;
        for (long i = 1; i <= end; i++) {
            if (isPrimeNumber1((int) i)) {
                result++;
            }
        }
        return (int) result;
    }
    
    @Override
    public int countPrimeNumbers2(int end) {
        long result = 0;
        for (long i = 1; i <= end; i++) {
            if (isPrimeNumber2((int) i)) {
                result++;
            }
        }
        return (int) result;
    }
    
    @Override
    public boolean isPrimeNumber1(int n) {
        if (n == 1) {
            return false;
        }
        if (n == 2) {
            return true;
        }
        
        for (long i = 2; i < n; i++) {
            long mod = n % i;
            if (mod == 0) {
                return false;
            }
        }
        return true;
    }
    
    @Override
    public boolean isPrimeNumber2(int n) {
        if (n == 1) {
            return false;
        }
        if (n == 2) {
            return true;
        }
        
        for (long i = 2; i <= Math.sqrt(n); i++) {
            long mod = n % i;
            if (mod == 0) {
                return false;
            }
        }
        return true;
    }
    
    @Override
    public int countPrimeNumbers4(int end) {
        long[] notPrime = new long[end + 1];
        notPrime[1] = 1;
        for (long i = 2; i <= end; i++) {
            if (notPrime[(int) i] == 0) {
                for (long j = 2; i * j <= end; j++) {
                    notPrime[(int) (i * j)] = 1;
                }
            }
        }
        
        long result = 0;
        for (long i = 1; i <= end; i++) {
            if (notPrime[(int) i] == 0) {
                result++;
            }
        }
        return (int) result;
    }
}