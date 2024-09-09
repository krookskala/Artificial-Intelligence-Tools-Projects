
# Perceptron Algorithm Implementation

![Screenshot_1](https://github.com/user-attachments/assets/f7a04fb9-c0fb-4f2b-b96d-6847b67585c5)

This project implements the Perceptron algorithm for binary classification tasks. It includes a Java implementation of the algorithm along with user interaction capabilities for loading data, specifying training parameters, and performing classification tasks.


## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [Links](#links)
- [License](#license)
## About the Project

The Perceptron algorithm is a type of artificial neural network that is used as the simplest form of a feedforward network: linear binary classifier. This project provides a Java implementation of the Perceptron algorithm, allowing users to load data, configure the learning rate and epochs, and perform binary classification tasks.

## Features

- Load data from specified file paths for training and testing.
- Configure learning parameters such as the learning rate and number of epochs.
- Train the Perceptron using the delta rule and update weights based on prediction errors.
- Print accuracy metrics on the test set after each training epoch.
- Shuffle training data optionally at the end of each epoch to enhance learning.
- After training, continuously accept user input for new observations and provide classifications, or allow the user to exit the program.
- Designed to work with any number of numerical attributes and a binary decision attribute.


## Getting Started

To start using the Perceptron project, follow these steps:

- **Clone the Repository:**
   ```sh
   git clone https://github.com/krookskala/Artificial-Intelligence-Tools-Projects/tree/main/Perceptron.git

   ```

- **Navigate to the Project Directory:**
    ```sh
    cd Perceptron

    ```

- **Compile the Java Files:**
    ```sh
    javac Perceptron.java DataSet.java

    ```

- **Run the Program:**
    ```sh
    java Perceptron

    ```




## Usage
1. **Input Data:**
- Provide paths to the training and test data files as command-line arguments or through prompts in the program.
- Set the learning rate and number of epochs.

2. **Operation Options:**
- **Classify Test Set:** Automatically classify the data in the test set after training and view accuracy metrics.
- **Classify New Observation:** Manually enter new observations for on-the-fly classification.
- **Adjust Parameters:** Modify learning rate or epochs dynamically.
- **Exit:** Terminate the program.

3. **View Results:**
- The program displays classification results and updates on the accuracy after each epoch.





## Contributing

Contributions are welcome!

If you find any issues or have ideas for improvements, feel free to open an issue or submit a pull request.

Please make sure to follow the project's code of conduct.

1. **Fork the repository**
2. **Create your feature branch (git checkout -b feature/YourFeature)**
3. **Commit your changes (git commit -am 'Add some feature')**
4. **Push to the branch (git push origin feature/YourFeature)**
5. **Open a pull request**


## Links

[![Gmail](https://img.shields.io/badge/ismailsariarslan7@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](ismailsariarslan7@gmail.com)

[![instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/ismailsariarslan/)

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ismailsariarslan/)
## License

The code in this repository is licensed under the [MIT License.](https://choosealicense.com/licenses/mit/)

