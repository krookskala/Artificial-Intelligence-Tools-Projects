import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DataSet {
    public static int vectorLength;
    public static Map<String, Integer> determinationValues = new HashMap<>();

    public static List<Perceptron.InputVector> readFile(String path) {
        List<Perceptron.InputVector> vectors = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(path))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] arr = line.split(",");
                vectorLength = arr.length - 1;
                double[] values = new double[vectorLength];
                for (int i = 0; i < vectorLength; i++) {
                    values[i] = Double.parseDouble(arr[i].trim());
                }
                determinationValues.putIfAbsent(arr[vectorLength], determinationValues.size());
                vectors.add(new Perceptron.InputVector(arr[vectorLength], values));
            }
        } catch (IOException e) {
            System.out.println("Error: The Specified File Was Not Found Or Could Not Be Read: " + path);
            return new ArrayList<>();
        }
        return vectors;
    }
}