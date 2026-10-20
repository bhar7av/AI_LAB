"""Lab 3: Logistic regression from scratch for binary classification."""

import numpy as np


def sigmoid(values):
    # Clipping avoids overflow for very large positive or negative values.
    values = np.clip(values, -500, 500)
    return 1 / (1 + np.exp(-values))


def train_logistic_regression(X, y, learning_rate=0.1, epochs=5000):
    sample_count, feature_count = X.shape
    weights = np.zeros(feature_count)
    bias = 0.0

    for epoch in range(epochs):
        probabilities = sigmoid(X @ weights + bias)
        errors = probabilities - y

        # Small epsilon prevents log(0).
        eps = 1e-9
        loss = -np.mean(
            y * np.log(probabilities + eps)
            + (1 - y) * np.log(1 - probabilities + eps)
        )

        weights -= learning_rate * (X.T @ errors) / sample_count
        bias -= learning_rate * np.mean(errors)

        if epoch % 1000 == 0:
            print(f"Epoch {epoch:4d} | loss = {loss:.4f}")

    return weights, bias


def main():
    # Two simple features for a toy pass/fail classification example.
    X = np.array([
        [1, 2], [2, 1], [2, 3], [3, 2],
        [4, 4], [5, 4], [4, 5], [5, 5],
    ], dtype=float)
    y = np.array([0, 0, 0, 0, 1, 1, 1, 1], dtype=float)

    weights, bias = train_logistic_regression(X, y)
    probabilities = sigmoid(X @ weights + bias)
    predictions = (probabilities >= 0.5).astype(int)
    accuracy = np.mean(predictions == y) * 100

    print("\nPredicted probabilities:", np.round(probabilities, 3))
    print("Predicted classes:", predictions)
    print("Actual classes:   ", y.astype(int))
    print(f"Training accuracy: {accuracy:.1f}%")

    new_student = np.array([[3.5, 4.0]])
    probability = sigmoid(new_student @ weights + bias)[0]
    print(f"New example probability of class 1: {probability:.3f}")


if __name__ == "__main__":
    main()
