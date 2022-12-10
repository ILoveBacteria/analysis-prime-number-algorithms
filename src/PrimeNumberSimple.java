public class PrimeNumberSimple implements PrimeNumber {
    @Override
    public boolean isPrimeNumber1(int n) {
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
    
    @Override
    public boolean isPrimeNumber2(int n) {
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
    public int countPrimeNumbers4(int end) {
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
