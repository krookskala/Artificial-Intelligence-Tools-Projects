import java.util.*;
import java.io.File;
import java.util.Scanner;

public class Perceptron {
    static class InputVector {
        private String type;
        private double[] values;

        public InputVector(String type, double[] values) {
            this.type = type;
            this.values = values;
        }

        public String getType() {
            return type;
        }

        public double[] getValues() {
            return values;
        }
    }

    private List<InputVector> testList, trainList;
    private double[] weights;
    private double bias, alpha;
    private int epochs;

    public Perceptron(String trainingPath, String testPath, double alpha, int epochs) {
        this.epochs = epochs;
        trainList = DataSet.readFile(trainingPath);
        testList = DataSet.readFile(testPath);
        configurePerceptron();
        this.alpha = alpha;
    }

    private void configurePerceptron(){
        bias = (Math.random()*2)-1;
        weights = new double[DataSet.vectorLength];
        for (int i = 0; i < weights.length; i++) {
            weights[i] = (Math.random()*2)-1;
        }
    }

    private int output(InputVector vector){
        // Output = w1*x1 + w2*x2 + ... + wn*xn - bias
        double net = 0;
        for (int i = 0; i < vector.getValues().length; i++) {
            net = net + vector.getValues()[i]*weights[i];
        }
        return net-bias >= 0 ? 1 : 0;
    }

    public void learn(){
        for (int epoch = 0; epoch < epochs; epoch++) {
            Collections.shuffle(trainList);
            int errorsTotal = 0;
            for(InputVector vector : trainList){
                int output = output(vector);
                int actualDeterminant = 0;

                for (Map.Entry<String,Integer> entry : DataSet.determinationValues.entrySet()){
                    if(entry.getKey().equals(vector.getType())){
                        actualDeterminant = entry.getValue();
                    }
                }
                int error = actualDeterminant - output;
                errorsTotal+=error;

                //Update weights and bias according to delta rule
                for (int j = 0; j < DataSet.vectorLength; j++) {
                    // w' = w + alpha(d-y)x
                    weights[j] += alpha*vector.getValues()[j]*error;
                }
                bias += error*alpha;
            }
            if (errorsTotal == 0) break;
            System.out.printf("Epoch %d, Accuracy: %.2f%%\n", epoch+1, calculateAccuracy(testList)*100);
        }
    }

    private double calculateAccuracy(List<InputVector> vectors) {
        int correct = 0;
        for (InputVector vector : vectors) {
            int predicted = output(vector);
            int actual = DataSet.determinationValues.get(vector.getType());
            if (predicted == actual) {
                correct++;
            }
        }
        return correct / (double) vectors.size();
    }

    public void run(boolean displayAccuracy){
        List<String> predictions = new ArrayList<>();
        double total = 0;
        double correct = 0;
        for(InputVector vector : testList){
            int output = output(vector);
            String predictedType = null;
            for (Map.Entry<String, Integer> entry : DataSet.determinationValues.entrySet()){
                if (output == entry.getValue()){
                    predictedType = entry.getKey();
                    break;
                }
            }
            predictions.add(predictedType);
            if (vector.getType().equals(predictedType)){
                correct++;
            }
            total++;
        }
        showTestResults(testList, predictions);
        if (displayAccuracy){
            System.out.printf("Accuracy: %.2f%%\n", (correct / total) * 100);
        }
    }

    public void showTestResults(List<InputVector> testList, List<String> predictions) {
        for (int i = 0; i < testList.size(); i++) {
            InputVector vector = testList.get(i);
            String predictedLabel = predictions.get(i);
            String trueLabel = vector.getType();

            if (predictedLabel.equals(trueLabel)) {
                System.out.println("\033[1;32mPredicted Label: " + predictedLabel + "\033[0m (Expected: \033[1;34m" + trueLabel + "\033[0m)");
            } else {
                System.out.println("\033[1;31mPredicted Label: " + predictedLabel + "\033[0m (Expected: \033[1;34m" + trueLabel + "\033[0m)");
            }
        }
    }

    public void predictFromConsoleInput(Scanner scanner) {
        while (true) {
            System.out.println("\n\033[1;35mPlease Provide The Attribute Values Separated By Commas (e.g., 5.1,3.5,1.4,0.2) Or Type 'exit' To Quit:\033[0m");
            String input = scanner.nextLine();

            if ("exit".equalsIgnoreCase(input.trim())) {
                break;
            }

            String[] attrsString = input.split(",");
            double[] attributes = new double[attrsString.length];
            boolean isValidInput = true;

            try {
                for (int i = 0; i < attrsString.length; i++) {
                    attributes[i] = Double.parseDouble(attrsString[i].trim());
                }
            } catch (NumberFormatException e) {
                System.out.println("\033[1;31mError: Please Enter Valid Numbers Separated By Commas.\033[0m");
                isValidInput = false;
            }

            if (isValidInput) {
                int predictionIndex = output(new InputVector(null, attributes));
                String predictedLabel = getLabelByIndex(predictionIndex);
                System.out.println("Predicted Label: \033[1;32m" + predictedLabel + "\033[0m");
            }
        }
    }

    private String getLabelByIndex(int index) {
        for (Map.Entry<String, Integer> entry : DataSet.determinationValues.entrySet()) {
            if (entry.getValue() == index) {
                return entry.getKey();
            }
        }
        return "Unknown";
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String trainingPath = "", testPath = "";
        double alpha = 0;
        int epochs = 0;

        while (true) {
            System.out.println("\033[1;35mEnter The Path To The Training Data: \033[0m");
            trainingPath = scanner.nextLine();
            if (!new File(trainingPath).exists()) {
                System.out.println("\033[1;31mError: The Specified File Was Not Found Or Could Not Be Read.\033[0m");
                continue;
            }
            break;
        }

        while (true) {
            System.out.println("\033[1;35mEnter The Path To The Test Data: \033[0m");
            testPath = scanner.nextLine();
            if (!new File(testPath).exists()) {
                System.out.println("\033[1;31mError: The Specified File Was Not Found Or Could Not Be Read.\033[0m");
                continue;
            }
            break;
        }

        while (true) {
            System.out.println("\033[1;35mEnter The Learning Rate: \033[0m");
            try {
                alpha = Double.parseDouble(scanner.nextLine());
                if (alpha <= 0) throw new NumberFormatException();
                break;
            } catch (NumberFormatException e) {
                System.out.println("\033[1;31mError: Learning Rate Must Be A Positive Number.\033[0m");
            }
        }

        while (true) {
            System.out.println("\033[1;35mEnter The Number Of Epochs: \033[0m");
            try {
                epochs = Integer.parseInt(scanner.nextLine());
                if (epochs <= 0) throw new NumberFormatException();
                break;
            } catch (NumberFormatException e) {
                System.out.println("\033[1;31mError: Please Enter A Valid Integer.\033[0m");
            }
        }

        Perceptron perceptron = new Perceptron(trainingPath, testPath, alpha, epochs);
        perceptron.learn();
        perceptron.run(true);
        perceptron.predictFromConsoleInput(scanner);
        scanner.close();
    }
}