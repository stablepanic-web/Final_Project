
import numpy as np
from keras.models import Sequential
from keras.layers import Embedding, Flatten, Dense
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from keras.models import load_model

def train_sentiment_analysis_model(texts, labels, max_words, embedding_dim, num_epochs, batch_size):
    """
    Train a neural network model for sentiment analysis using word embeddings.

    Args:
        texts (list): List of text reviews.
        labels (list): List of corresponding sentiment labels (0 or 1).
        max_words (int): Maximum number of words to tokenize.
        embedding_dim (int): Dimension of word embeddings.
        num_epochs (int): Number of training epochs.
        batch_size (int): Batch size for training.
    """
    # 1. Tokenize the text data
    tokenizer = Tokenizer(num_words=max_words, oov_token="<OOV>")
    tokenizer.fit_on_texts(texts)
    sequences = tokenizer.texts_to_sequences(texts)
    
    # Find the maximum sequence length for padding
    max_len = max(len(seq) for seq in sequences) if sequences else 20
    
    # 2. Pad the sequences
    X_train = pad_sequences(sequences, maxlen=max_len, padding='post', truncating='post')
    y_train = np.array(labels)
    
    # 3. Build the neural network model
    model = Sequential([
        Embedding(input_dim=max_words, output_dim=embedding_dim, input_length=max_len),
        Flatten(),
        Dense(16, activation='relu'),
        Dense(1, activation='sigmoid')  # Binary classification
    ])
    
    # 4. Compile the model
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    
    # 5. Train the model
    print("Training model...")
    model.fit(X_train, y_train, epochs=num_epochs, batch_size=batch_size, verbose=1)
    
    # Save the model and tokenizer properties we'll need later
    model.save('sentiment_model.h5')
    
    return model, tokenizer, max_len

# --- Execution & Testing ---

# Example data: text reviews and sentiment labels
texts = [
    "I absolutely loved this movie! The acting was fantastic.",
    "Worst film I have ever seen in my entire life.",
    "Truly a masterpiece, highly recommend it to everyone.",
    "What a waste of time and money. Terrible plot.",
    "It was okay, but pretty boring and predictable.",
    "Amazing visuals and a brilliant performance by the lead."
]
labels = [1, 0, 1, 0, 0, 1]  # 1 = Positive, 0 = Negative

# Hyperparameters
MAX_WORDS = 1000
EMBEDDING_DIM = 16
NUM_EPOCHS = 10
BATCH_SIZE = 2

# Train the sentiment analysis model
model, tokenizer, max_len = train_sentiment_analysis_model(
    texts, labels, MAX_WORDS, EMBEDDING_DIM, NUM_EPOCHS, BATCH_SIZE
)

# Test the model
print("\n--- Testing the model ---")

# Load the trained model
loaded_model = load_model('sentiment_model.h5')

# Example new text reviews
new_reviews = [
    "The movie was absolutely amazing and wonderful!",
    "I hated it. It was a complete waste of time."
]

# Tokenize and pad the new text reviews
new_sequences = tokenizer.texts_to_sequences(new_reviews)
new_padded = pad_sequences(new_sequences, maxlen=max_len, padding='post', truncating='post')

# Use the trained model to predict sentiments
predictions = loaded_model.predict(new_padded)

# Convert the predictions to binary labels (0 or 1)
# Since sigmoid outputs a probability between 0 and 1, we threshold at 0.5
binary_predictions = [1 if prob >= 0.5 else 0 for prob in predictions]

# Print the predicted sentiments for new text reviews
for review, pred, prob in zip(new_reviews, binary_predictions, predictions):
    sentiment = "Positive" if pred == 1 else "Negative"
    print(f"\nReview: '{review}'")
    print(f"Predicted Sentiment: {sentiment} (Confidence Score: {prob[0]:.4f})")


#import streamlit as st
#import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")
