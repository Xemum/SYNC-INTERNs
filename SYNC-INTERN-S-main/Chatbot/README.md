## Chatbot README

This repository contains a simple implementation of a chatbot using Python and TensorFlow/Keras.

### Files and Usage

- **intents.json**: This file contains the intents for the chatbot. Each intent consists of a tag, patterns, and responses.
- **main.py**: This is the main Python script that loads the intents, preprocesses the data, trains the neural network model, and interacts with the user.
- **words.pkl** and **classes.pkl**: These files store the preprocessed words and classes respectively, using Python's pickle module.
- **chatbot_model.h5**: This file stores the trained neural network model using the HDF5 format.

To use the chatbot:

1. Make sure you have all the required Python packages installed. You can install them using pip:

   ```
   pip install numpy nltk tensorflow
   ```

2. Ensure you have the NLTK data downloaded. You can download it using the following commands in Python:

   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('wordnet')
   ```

3. Run the `main.py` script:

   ```
   python main.py
   ```

4. Interact with the chatbot by typing messages. Type "exit" to end the conversation.

### Model Training

The chatbot uses a neural network model implemented with TensorFlow/Keras. Here's a brief overview of the model architecture:

- Input Layer: Dense layer with ReLU activation function.
- Dropout Layer: Dropout layer to prevent overfitting.
- Hidden Layer: Dense layer with ReLU activation function.
- Output Layer: Dense layer with softmax activation function.

The model is compiled using the SGD optimizer with adjusted parameters and categorical cross-entropy loss function.

### Interaction Loop

The `main.py` script starts an interaction loop where the chatbot prompts the user with "Bot: Hello! How can I assist you today?" and waits for user input. It then processes the input, predicts the intent using the trained model, and generates a response based on the predicted intent. If the intent cannot be determined with sufficient confidence, the chatbot asks the user to rephrase the input.

### License

This code is provided under the MIT License. Feel free to modify and distribute it according to your needs.