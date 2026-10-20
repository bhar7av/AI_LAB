"""Lab 6: A simple perceptron trained on the AND logic gate."""


def step_activation(value):
    return 1 if value >= 0 else 0


def train_perceptron(X, y, learning_rate=0.1, epochs=20):
    weights = [0.0 for _ in X[0]]
    bias = 0.0

    for epoch in range(epochs):
        mistakes = 0
        for features, target in zip(X, y):
            weighted_sum = sum(w * x for w, x in zip(weights, features)) + bias
            prediction = step_activation(weighted_sum)
            error = target - prediction

            if error != 0:
                mistakes += 1
            for index in range(len(weights)):
                weights[index] += learning_rate * error * features[index]
            bias += learning_rate * error

        print(f"Epoch {epoch + 1:2d}: mistakes = {mistakes}")
        if mistakes == 0:
            break

    return weights, bias


def predict(features, weights, bias):
    weighted_sum = sum(w * x for w, x in zip(weights, features)) + bias
    return step_activation(weighted_sum)


def main():
    # AND gate: only [1, 1] belongs to class 1.
    X = [[0, 0], [0, 1], [1, 0], [1, 1]]
    y = [0, 0, 0, 1]

    weights, bias = train_perceptron(X, y)
    print("\nLearned weights:", weights)
    print("Learned bias:", bias)
    print("\nPredictions:")
    for features, actual in zip(X, y):
        print(f"{features} -> predicted {predict(features, weights, bias)}, actual {actual}")


if __name__ == "__main__":
    main()
