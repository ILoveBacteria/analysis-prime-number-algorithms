import java.io.FileWriter;
import java.io.IOException;

public class TestCaseGenerator {
    private static final String FILE_PATH = "inputs.txt";
    private static final int MAX_INPUT = 1_000_000;
    public static void generate() throws IOException {
        try (FileWriter writer = new FileWriter(FILE_PATH)) {
            int i = 1, j = 10;
            while (j <= MAX_INPUT) {
                for (int k = i; k < j; k += i) {
                    int n = ((int) (Math.random() * j)) % i + k;
                    writer.write(String.format("%d\n", n));
                }
                i *= 10;
                j *= 10;
            }
        }
    }
}
