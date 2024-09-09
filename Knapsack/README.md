
# Brute-Force Knapsack Solver

![Screenshot_1](https://github.com/user-attachments/assets/661fff6a-621e-4573-b7c6-4436e4fe7bc6)


This project implements a brute-force solution to the classic knapsack problem, which explores all possible combinations of items to determine the most valuable subset that fits within a given weight capacity. The implementation strictly avoids predefined methods for generating characteristic vectors, ensuring all computations are done from scratch.


## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [Links](#links)
- [License](#license)
## About the Project

The knapsack problem is a combinatorial optimization problem where the goal is to maximize the total value of items packed in a knapsack without exceeding its weight capacity. This implementation generates all possible characteristic vectors representing potential solutions and identifies the optimal configuration.

## Features

- **Brute-Force Approach:** Generates all possible configurations of items to ensure finding the optimal solution.

- **Custom Vector Generation:** Characteristic vectors are generated manually, without relying on built-in methods.

- **Performance Optimization:** Designed to find the solution efficiently, with the goal of not exceeding 20 minutes for execution.

- **Output Information:** Prints the best characteristic vector, total weight, and total value of the selected items.

- **Optional Execution Time Display:** Measures and displays the time taken to compute the solution.


## Getting Started

To run this knapsack solver, follow these steps:

- **Clone the Repository:**
   ```sh
   git clone https://github.com/krookskala/Artificial-Intelligence-Tools-Projects/tree/main/Knapsack.git

   ```

- **Navigate to the Project Directory:**
    ```sh
    cd Knapsack

    ```

- **Compile the Java Files:**
    ```sh
    javac Knapsack.java Object.java

    ```

- **Run the Program:**
    ```sh
    java Knapsack

    ```




## Usage
1. **Prepare Input File:**
- Ensure your input file is formatted correctly: the first line should state the total capacity, followed by lines indicating each item's weight and value.

2. **Execute the Program:**
- Run the program and it will automatically read the input file, compute all possible combinations, and output the optimal solution.







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

