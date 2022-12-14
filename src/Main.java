import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Formatter;
import java.util.Scanner;

public class Main {
    public static void run(PrimeNumber primeNumber) throws IOException {
        String PARENT_PATH = "outputs/" + primeNumber.getClass().getSimpleName();
        new File(PARENT_PATH).mkdirs();
        
        try (Scanner scanner = new Scanner(new File("inputs.txt"));
             Formatter formatter1 = new Formatter(new File(PARENT_PATH, "algorithm1.txt"));
             Formatter formatter2 = new Formatter(new File(PARENT_PATH, "algorithm2.txt"));
             Formatter formatter3 = new Formatter(new File(PARENT_PATH, "algorithm3.txt"));
             Formatter formatter4 = new Formatter(new File(PARENT_PATH, "algorithm4.txt"))) {
            while (scanner.hasNext()) {
                int n = scanner.nextInt();
                System.out.println("Running for n = " + n);
    
                System.out.println("Starting algorithm 1");
                long unixTimeStart = System.currentTimeMillis();
                primeNumber.countPrimeNumbers1(n);
                long unixTimeEnd = System.currentTimeMillis();
                formatter1.format("%d\n", unixTimeEnd - unixTimeStart);
                System.out.println("Finished algorithm 1 in " + (unixTimeEnd - unixTimeStart) + " ms");
    
                System.out.println("Starting algorithm 2");
                unixTimeStart = System.currentTimeMillis();
                primeNumber.countPrimeNumbers2(n);
                unixTimeEnd = System.currentTimeMillis();
                formatter2.format("%d\n", unixTimeEnd - unixTimeStart);
                System.out.println("Finished algorithm 2 in " + (unixTimeEnd - unixTimeStart) + " ms");
                
                System.out.println("Starting algorithm 3");
                unixTimeStart = System.currentTimeMillis();
                primeNumber.countPrimeNumbers3(n);
                unixTimeEnd = System.currentTimeMillis();
                formatter3.format("%d\n", unixTimeEnd - unixTimeStart);
                System.out.println("Finished algorithm 3 in " + (unixTimeEnd - unixTimeStart) + " ms");
                
                System.out.println("Starting algorithm 4");
                unixTimeStart = System.currentTimeMillis();
                primeNumber.countPrimeNumbers4(n);
                unixTimeEnd = System.currentTimeMillis();
                formatter4.format("%d\n", unixTimeEnd - unixTimeStart);
                System.out.println("Finished algorithm 4 in " + (unixTimeEnd - unixTimeStart) + " ms");

                formatter1.flush();
                formatter2.flush();
                formatter3.flush();
                formatter4.flush();
            }
        }
    }
    
    public static void main(String[] args) {
        try {
            if (Files.notExists(Paths.get("inputs.txt"))) {
                TestCaseGenerator.generate();
            }
           run(new PrimeNumberSimple());
//            run(new PrimeNumberParallel());
        //    run(new PrimeNumberNotOptimized());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
