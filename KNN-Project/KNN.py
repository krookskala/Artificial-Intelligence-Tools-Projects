import math

def load_data(file_path):
    features = []
    labels = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip().split(',')
            feat = [float(x) for x in line[:-1]]
            label = line[-1]
            features.append(feat)
            labels.append(label)
    return features, labels

def euclidean_distance(vec1, vec2):
    distance = 0
    for i in range(len(vec1)):
        distance += (vec1[i] - vec2[i]) ** 2
    return math.sqrt(distance)

def get_neighbors(train_features, train_labels, test_instance, k):
    distances = [(euclidean_distance(test_instance, train_features[i]), i) for i in range(len(train_features))]
    distances.sort()
    return [i for _, i in distances[:k]]

def predict_label(train_features, train_labels, test_instance, k):
    neighbors = get_neighbors(train_features, train_labels, test_instance, k)
    labels = [train_labels[i] for i in neighbors]
    return max(set(labels), key=labels.count)

def calculate_accuracy(true_labels, predicted_labels):
    correct = sum(1 for true, pred in zip(true_labels, predicted_labels) if true == pred)
    total = len(true_labels)
    return (correct / total) * 100

if __name__ == "__main__":
    try:
        while True:
            try:
                train_file_path = input("\033[1;35mEnter The Path To The Training File: \033[0m")
                train_features, train_labels = load_data(train_file_path)
                break
            except FileNotFoundError:
                print("\033[1;31mError: File Does Not Exist.\033[0m")

        while True:
            try:
                k = int(input("\033[1;35mEnter The Number Of Nearest Neighbors (k): \033[0m"))
                if k <= 0:
                    raise ValueError("\033[1;31m(k) Must Be A Positive Integer.\033[0m")
                break
            except ValueError as e:
                print(f"\033[1;31mError: {e}\033[0m")

        while True:
            print("\n\033[1;35mMenu:\033[0m")
            print("\033[1;35m|=======================================================================|")
            print("\033[1;35m| (a) Classification Of All Observations From The Test Set              |")
            print("\033[1;35m| (b) Classification Of An Observation Provided By The User             |")
            print("\033[1;35m| (c) Change k                                                          |")
            print("\033[1;35m| (d) Exit                                                              |")
            print("\033[1;35m|=======================================================================|")

            option = input("Choose An Option: ")

            if option == 'a':
                try:
                    test_file_path = input("Enter The Path To The Test File: ")
                    test_features, test_labels = load_data(test_file_path)
                    predictions = [predict_label(train_features, train_labels, x_test, k) for x_test in test_features]
                    acc = calculate_accuracy(test_labels, predictions)
                    print("Accuracy:", acc, "%")

                    print("\n\033[1;35mTest Results:\033[0m")
                    for i in range(len(test_features)):
                        predicted_label = predictions[i]
                        true_label = test_labels[i]
                        if predicted_label == true_label:
                            print("\033[1;32mPredicted label:", "---> " +  predicted_label, "\033[0m")
                        else:
                            print("\033[1;31mPredicted label:", "---> " + predicted_label, "\033[0m(Expected: \033[1;34m" + true_label + "\033[0m)")
                except FileNotFoundError:
                    print("Error: Test File Not Found!")

            elif option == 'b':
                try:
                    observation = [float(x) for x in input("Enter The Observation (Comma-Separated Values): ").split(',')]
                    prediction = predict_label(train_features, train_labels, observation, k)
                    print("Predicted Label:", prediction)
                except ValueError:
                    print("Error: Please Enter Comma-Separated Values.")

            elif option == 'c':
                while True:
                    try:
                        new_k = int(input("Enter The New Value Of (k): "))
                        if new_k <= 0:
                            raise ValueError("(k) Must Be A Positive Integer.")
                        k = new_k
                        break
                    except ValueError as e:
                        print(f"Error: {e}")

            elif option == 'd':
                print("Exiting Program...")
                break

            else:
                print("Invalid Option! Please Choose Again.")

    except KeyboardInterrupt:
        print("\nProgram Interrupted By User...")