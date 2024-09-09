import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Knapsack {
    private static class Item {
        int weight;
        int value;

        Item(int weight, int value) {
            this.weight = weight;
            this.value = value;
        }
    }

    private static int bestValue = 0;
    private static int bestWeight = 0;
    private static String bestVector = "";

    public static void main(String[] args) {
        try {
            List<Item> items = new ArrayList<>();
            Scanner scanner = new Scanner(new File("C:\\Users\\krook\\IdeaProjects\\NAI-Knapsack\\knapsack_data\\5"));

            if (!scanner.hasNextInt()) {
                System.out.println("Error: First line must contain the backpack capacity.");
                return;
            }

            int capacity = scanner.nextInt();

            while (scanner.hasNextInt()) {
                int weight = scanner.nextInt();
                if (!scanner.hasNextInt()) {
                    System.out.println("Error: Each item line must contain both weight and value.");
                    return;
                }
                int value = scanner.nextInt();
                items.add(new Item(weight, value));
            }
            scanner.close();

            long startTime = System.nanoTime();

            int numItems = items.size();
            int[] vector = new int[numItems];
            generateCombinations(items, vector, 0, numItems, capacity);

            long endTime = System.nanoTime();
            double duration = (endTime - startTime) / 1e9;


            System.out.println("Best characteristic vector: " + bestVector);
            System.out.println("Total weight: " + bestWeight);
            System.out.println("Total value: " + bestValue);
            System.out.println("Execution time: " + duration + " seconds");

        } catch (FileNotFoundException e) {
            System.out.println("Error: File not found. Please check the file path.");
        } catch (Exception e) {
            System.out.println("An error occurred: " + e.getMessage());
        }
    }

    private static void generateCombinations(List<Item> items, int[] vector, int index, int numItems, int capacity) {
        if (index == numItems) {
            int totalWeight = 0;
            int totalValue = 0;
            StringBuilder currentVector = new StringBuilder();
            for (int i = 0; i < numItems; i++) {
                if (vector[i] == 1) {
                    totalWeight += items.get(i).weight;
                    totalValue += items.get(i).value;
                }
                currentVector.append(vector[i]);
            }
            if (totalWeight <= capacity && totalValue > bestValue) {
                bestValue = totalValue;
                bestWeight = totalWeight;
                bestVector = currentVector.toString();
            }
        } else {
            vector[index] = 0;
            generateCombinations(items, vector, index + 1, numItems, capacity);
            vector[index] = 1;
            generateCombinations(items, vector, index + 1, numItems, capacity);
        }
    }
}
