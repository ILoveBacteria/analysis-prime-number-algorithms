import java.util.stream.IntStream;

public class PrimeNumberParallel extends PrimeNumberAbstract {
    @Override
    public int countPrimeNumbers1(int end) {
        long result = IntStream.rangeClosed(1, end).parallel().filter(this::isPrimeNumber1).count();
        return (int) result;
    }
    
    @Override
    public int countPrimeNumbers2(int end) {
        long result = IntStream.rangeClosed(1, end).parallel().filter(this::isPrimeNumber2).count();
        return (int) result;
    }
    
    @Override
    public int countPrimeNumbers3(int end) {
        boolean[] notPrime = new boolean[end + 1];
        notPrime[1] = true;
        IntStream.rangeClosed(2, end)
                .parallel()
                .forEach(x -> IntStream.rangeClosed(2, end / x)
                        .forEach(y -> notPrime[x * y] = true));
        
        int result = 0;
        for (int i = 1; i <= end; i++) {
            if (!notPrime[i]) {
                result++;
            }
        }
        return result;
    }
}
