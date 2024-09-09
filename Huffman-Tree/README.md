
# Huffman Coding Implementation

![Screenshot_1](https://github.com/user-attachments/assets/9ec19777-1884-4503-b580-5ed95fcb26cc)


This project implements Huffman coding, an efficient method for compressing data. The implementation includes the creation of a Huffman tree using a custom-built priority queue to organize and prioritize nodes based on their frequency.


## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [Links](#links)
- [License](#license)
## About the Project

Huffman coding is a popular algorithm for lossless data compression. This project takes alphanumeric sequences as input and outputs Huffman codes for each symbol and the encoded sequence. The priority queue used to build the Huffman tree is implemented from scratch, with options for different data structures like naive arrays or binary search trees.

## Features

- **Custom Priority Queue:** Implemented from scratch to support the efficient creation of Huffman trees.

- **Dynamic Huffman Tree Creation:** Builds the tree based on the frequency of each symbol in the input.

- **Encoding and Decoding:** Encodes an input sequence into Huffman codes and decodes back to the original sequence.

- **Detailed Output:** Prints the Huffman code for each symbol and the encoded sequence.

- **Graphical Tree Representation:** (Optional) Generates a visual representation of the Huffman tree.


## Getting Started

To run the Huffman coding project, follow these steps:

- **Clone the Repository:**
   ```sh
   git clone https://github.com/krookskala/Artificial-Intelligence-Tools-Projects/tree/main/Huffman-Tree.git

   ```

- **Navigate to the Project Directory:**
    ```sh
    cd Huffman-Tree

    ```

- **Compile the Java Files:**
    ```sh
    javac Huffman.java Node.java PriorityQueue.java

    ```

- **Run the Program:**
    ```sh
    java Huffman

    ```




## Usage
1. **Input Sequence:**
- Provide an alphanumeric sequence when prompted to see its Huffman encoding and the encoded sequence.

2. **View Huffman Codes and Tree:**
- After running the program, it will display the Huffman codes for each symbol and the optional tree diagram.







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

