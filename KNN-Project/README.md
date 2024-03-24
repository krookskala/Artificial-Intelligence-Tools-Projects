
# K Nearest Neighbors (kNN) Algorithm Implementation

![Screenshot_1](https://github.com/krookskala/Artificial-Intelligence-Tools-Projects/assets/86527375/6b52b7ee-e923-474a-b750-62d20bbb3289)

This project implements the k-Nearest Neighbors (kNN) algorithm for classification tasks. It includes a Python implementation of the algorithm along with user interaction capabilities for loading data, specifying the number of nearest neighbors (k), and performing classification tasks.


## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [Links](#links)
- [License](#license)
## About the Project

The kNN algorithm is a simple yet effective method for classification tasks, where the class of a given observation is determined by the majority class among its k nearest neighbors in the feature space. This project provides a Python implementation of the kNN algorithm, allowing users to load data from CSV files, specify the value of k, and perform classification tasks.

## Features

- Load data from CSV files, where each line represents an observation with features and labels.
- Calculate distances between data points using the Euclidean distance metric.
- Predict the label for a given observation based on the majority label of its k nearest neighbors.
- User interaction capabilities for specifying the path to the training file, choosing the number of nearest neighbors (k), and performing classification tasks.



## Getting Started

To get started with the kNN project, follow these steps:

- **Clone the Repository:**
   ```sh
   git clone https://github.com/krookskala/Artificial-Intelligence-Tools-Projects/tree/main/KNN-Project.git

   ```

- **Navigate to the Project Directory:**
    ```sh
    cd kNN-Project

    ```

- **Install Dependencies (if any):**
    - If additional dependencies are required, install them using pip or conda. For example:
    ```sh
    pip install numpy

    ```

- **Prepare Data:**
    - Organize your data into CSV files where each row represents a single observation, and the last column contains the class label.

- **Run the Script:**
   - Execute the Python script knn.py to start the program.
    ```sh
    python knn.py

    ```

    


## Usage
1. **Input Data:**
- Provide the path to the training file when prompted.
- Specify the number of nearest neighbors (k) to be used for classification

2. **Classification Options:**
- **Classification of Test Set:** Provide the path to the test file for classification and view accuracy metrics.
- **Classification of Single Observation:** Enter a single observation through the console for classification.
- **Change k:** Adjust the value of k for dynamic classification.
- **Exit:** Terminate the program.

3. **View Results:**
- Analyze the classification results and accuracy metrics provided after each classification task.





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

