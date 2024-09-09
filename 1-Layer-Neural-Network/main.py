from collections import Counter
import math
import random
import re
import os
class Perceptron:
    "Initializes a new perceptron with a specific learning rate, target activation result, and number of attributes"
    def __init__(self, alpha, activating_result, number_of_attributes):
        self.alpha = alpha
        self.weights = []
        self.activating_result = activating_result
        self.__set_weights(number_of_attributes)

    "Initializes the weights of the perceptron, including a bias weight. Assigns random weights to each attribute and initializes a bias term to zero."
    def __set_weights(self, number_of_attributes):
        for i in range(number_of_attributes):
            self.weights.append(random.randint(0, 1))
        self.weights.append(0)

    "Computes the output of the perceptron based on input vector."
    def compute(self, vector):
        net = self.get_net(vector)
        if net >= 0:
            return 1
        return 0

    "Calculates the dot product of the weights and the input vector"
    def get_net(self, vector):
        _vector = vector + [-1]
        net = 0
        for i in range(len(_vector)):
            net += (float(_vector[i]) * self.weights[i])
        return net

    "The weights based on the difference between the desired output and the perceptron's prediction."
    def learn(self, good_result, vector):
        prev_result = self.compute(vector)
        _vector = vector + [-1]
        should_activate = 0
        if good_result == self.activating_result: should_activate = 1
        for i in range(len(self.weights)):
            self.weights[i] += ((should_activate - prev_result) * self.alpha * float(_vector[i]))


class NeuralNetwork:
    "Initializes multiple perceptrons, one for each class, with each perceptron responsible for recognizing a specific class."
    def __init__(self, alpha, classes, number_of_attributes):
        self.alpha = alpha
        self.classes = classes
        self.number_of_attributes = number_of_attributes
        self.perceptrons = self.__create_neural_network()

    "Creates a list of perceptrons, each tuned to one of the possible output classes."
    def __create_neural_network(self):
        network = []
        for i in range(len(self.classes)):
            network.append(Perceptron(self.alpha, self.classes[i], self.number_of_attributes))
        return network

    def compute_network_result(self, vector):
        _vector = vector
        results = []
        for perceptron in self.perceptrons:
            results.append(perceptron.get_net(_vector))
        print(self.classes)
        print(results)
        index_of_activated_perceptron = results.index(max(results))
        return self.perceptrons[index_of_activated_perceptron].activating_result

    def normalize_weights(self):
        for i in range(len(self.perceptrons)):
            v_len = self.vector_length(self.perceptrons[i].weights[:-1])
            for j in range(len(self.perceptrons[i].weights) - 1):
                self.perceptrons[i].weights[j] /= v_len

    def vector_length(self, vector):
        result = 0
        for e in vector:
            result += (e ** 2)
        result = math.sqrt(result)

        return result


class Trainer:
    def __init__(self, neural_network, train_set):
        self.neural_network = neural_network
        self.names_of_classes = neural_network.classes
        self.train_set = train_set
        random.shuffle(self.train_set)

    def train(self):
        for line in self.train_set:
            for percpetron in self.neural_network.perceptrons:
                percpetron.learn(line[-1], line[:-1])


class DataSetCreator:
    @staticmethod
    def create_vector_list(dir_name):
        vector_list = []
        rootdir = os.getcwd() + "/" + dir_name
        for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                language = os.path.basename(subdir)
                file = open(os.path.join(subdir, file), "r", encoding="utf-8")
                text = file.read().strip()
                vector = DataSetCreator.get_letters_count_vector(text)
                vector.append(language)
                vector_list.append(vector)
        return vector_list

    @staticmethod
    def get_letters_count_vector(text):
        vector = [0] * 26
        regex = re.compile('[^a-zA-Z]+')
        text = regex.sub('', text).lower()
        letter_counter = Counter(text)
        number_of_letters = letter_counter.total()
        for i in range(26):
            vector[i] = letter_counter[chr(i + ord('a'))] / number_of_letters
        return vector

    @staticmethod
    def get_names_of_classes(data):
        classes = []
        for line in data:
            if line[-1] not in classes:
                classes.append(line[-1])
        return classes


class UI:
    @staticmethod
    def input_text_to_test():
        text = input("Enter text to test:\n")
        return text

    def print_results(results):
        print("Test results: ", results)


class Controller:
    @staticmethod
    def start():
        data_set = DataSetCreator.create_vector_list("data")
        classes = DataSetCreator.get_names_of_classes(data_set)
        neural_network = NeuralNetwork(0.05, classes, len(data_set[0]) - 1)
        trainer = Trainer(neural_network, data_set)
        for i in range(100):
            print("training number: ", i)
            trainer.train()
        neural_network.normalize_weights()
        while (True):
            text_to_test = UI.input_text_to_test()
            vector_to_test = DataSetCreator.get_letters_count_vector(text_to_test)
            test_vector_len = neural_network.vector_length(vector_to_test)
            for i in range(len(vector_to_test)):
                vector_to_test[i] /= test_vector_len
            result = neural_network.compute_network_result(vector_to_test)
            UI.print_results(result)

Controller.start()