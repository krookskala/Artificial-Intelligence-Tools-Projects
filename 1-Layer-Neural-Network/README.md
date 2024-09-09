
# Language Recognition Neural Network

![Screenshot_1](https://github.com/user-attachments/assets/ed478bf9-dad9-4752-a592-6b7110a23f3c)

This project implements a one-layer neural network that recognizes the language of a given text based on the proportion of ASCII characters in the text. The network dynamically adjusts to the number of languages present in the training dataset.


## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [Links](#links)
- [License](#license)
## About the Project

This neural network model identifies the language of input texts by analyzing the frequency of ASCII characters. The network architecture consists of as many neurons as there are unique languages in the training data, which it determines automatically.

## Features

- **Dynamic Neural Architecture:** Automatically adjusts to the number of languages based on the training data.

- **Input Vectorization:** Converts text into a frequency vector of ASCII characters.

- **Training with Delta Rule:** Utilizes the delta rule for training, with an option to normalize weight vectors after each step.

- **Language Identification:** Employs a maximum selector mechanism to determine the most likely language.


## Getting Started

To use this language recognition system, follow these steps:

- **Clone the Repository:**
   ```sh
   git clone https://github.com/krookskala/Artificial-Intelligence-Tools-Projects/tree/main/1-Layer-Neural-Network.git

   ```

- **Navigate to the Project Directory:**
    ```sh
    cd 1-Layer-Neural-Network

    ```

- **Prepare the Data:**
    - Create folders named according to language codes (e.g., en, de) in the data directory.
    - Place at least 10 text files containing a few paragraphs of ASCII-representable language text in each folder.

- **Run the Script:**
    ```sh
    python main.py

    ```




## Usage
1. **Train the Network:**
- Automatically trains on the texts found in the language folders.

2. **Classify Text:**
- Enter a short ASCII text through the command line interface to classify its language.






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

