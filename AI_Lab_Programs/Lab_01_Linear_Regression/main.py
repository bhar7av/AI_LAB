"""
Lab 1: Linear Regression with Gradient Descent
A small from-scratch example using house size and bedroom count.
"""

import numpy as np


def train_linear_regression(features, prices, learning_rate=0.01, epochs=3000):
    """Train a two-feature linear regression model with gradient descent."""
    # Scaling makes the two features easier to work with together.
    feature_mean = features.mean(axis=0)
    feature_std = features.std(axis=0)
    feature_std[feature_std == 0] = 1
    scaled_features = (features - feature_mean) / feature_std

    sample_count = len(prices)
    weights = np.zeros(scaled_features.shape[1])
    bias = 0.0

    for epoch in range(epochs):
        predictions = scaled_features @ weights + bias
        errors = predictions - prices

        # The 1/2 factor keeps the derivative neat.
        cost = np.sum(errors ** 2) / (2 * sample_count)
        weight_gradient = scaled_features.T @ errors / sample_count
        bias_gradient = np.sum(errors) / sample_count

        weights -= learning_rate * weight_gradient
        bias -= learning_rate * bias_gradient

        if epoch % 500 == 0:
            print(f"Epoch {epoch:4d} | cost = {cost:.4f}")

    model = {
        "weights": weights,
        "bias": bias,
        "mean": feature_mean,
        "std": feature_std,
    }
    return model


def predict(model, new_features):
    """Predict prices for one or more houses."""
    scaled = (new_features - model["mean"]) / model["std"]
    return scaled @ model["weights"] + model["bias"]


def main():
    # Columns: size in square feet, bedrooms. Prices are in lakh rupees.
    X = np.array([
        [1000, 2],
        [1500, 3],
        [2000, 3],
        [2500, 4],
        [3000, 5],
        [1800, 3],
    ], dtype=float)
    y = np.array([20, 30, 40, 50, 60, 36], dtype=float)

    model = train_linear_regression(X, y)
    test_house = np.array([[2200, 3]], dtype=float)
    predicted_price = predict(model, test_house)[0]

    print("\nLearned weights:", model["weights"])
    print("Learned bias:", round(float(model["bias"]), 4))
    print(f"Predicted price for a 2200 sq. ft., 3-bedroom house: ₹{predicted_price:.2f} lakh")


if __name__ == "__main__":
    main()
