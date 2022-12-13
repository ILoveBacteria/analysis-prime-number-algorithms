import java.io.FileWriter;
import java.io.IOException;

public class TestCaseGenerator {
    private static final String FILE_PATH = "inputs.txt";
    private static final int MAX_INPUT = 1_000_000;
    public static void generate() throws IOException {
        try (FileWriter writer = new FileWriter(FILE_PATH)) {
            for (int i = 1; i < 1000; i++) {
                writer.write(String.format("%d\n", i));
            }
            int i = 1000, j = 10_000;
            while (j <= MAX_INPUT) {
                for (int k = i; k < j; k += i / 2) {
                    int n = ((int) (Math.random() * i / 2)) + k;
                    writer.write(String.format("%d\n", n));
                }
                i *= 10;
                j *= 10;
            }
        }
    }
}
