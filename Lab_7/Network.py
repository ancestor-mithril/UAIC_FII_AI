import numpy as np
import os
import pickle


class Network:
    def __init__(self, layers, learning_rate):
        self.num_layers = len(layers)
        self.layer_sizes = layers
        self.learning_rate = learning_rate

        self.biases = [np.random.normal(size=(layers[i + 1], 1)) for i in
                       range(self.num_layers - 1)]

        self.weights = [np.random.normal(size=(layers[i + 1], layers[i])) for i in
                        range(self.num_layers - 1)]

    def save(self, filename):

        if os.path.exists(filename):
            os.remove(filename)

        with open(filename, 'wb') as file:
            pickle.dump(self, file, protocol=pickle.HIGHEST_PROTOCOL)
            file.close()

    def load(self, filename):
        if not os.path.exists(filename):
            raise Exception(filename + 'not found.')
        with open(filename, 'rb') as file:
            network = pickle.load(file)

            self.learning_rate = network.learning_rate
            self.num_layers = network.num_layers
            self.layer_sizes = network.layer_sizes
            self.biases = network.biases
            self.weights = network.weights

            file.close()

    def load_and_run(self, filename, func):
        self.load(filename)
        correct = 0
        for i in range(10000):
            inp = [np.random.randint(0, 2), np.random.randint(0, 2)]
            out = func[inp[0] * 2 + inp[1]]
            net_out = np.argmax(self.feedForward(inp)[1][-1])

            if out == net_out:
                correct += 1

        print("Total accuracy:{}/10000".format(correct))

    def train(self, max_epochs, func):

        for j in range(max_epochs):
            inp = [np.random.randint(0, 2), np.random.randint(0, 2)]
            out = func[inp[0] * 2 + inp[1]]

            nabla_b = [np.zeros(b.shape) for b in self.biases]
            nabla_w = [np.zeros(w.shape) for w in self.weights]

            delta_nabla_b, delta_nabla_w = self.backprop(inp, out)

            nabla_b = [nabla_b[i] + delta_nabla_b[i] for i in range(len(nabla_b))]
            nabla_w = [nabla_w[i] + delta_nabla_w[i] for i in range(len(nabla_w))]

            self.weights = [self.weights[i] - (nabla_w[i] * self.learning_rate) for i in range(len(self.weights))]
            self.biases = [self.biases[i] - (nabla_b[i] * self.learning_rate) for i in range(len(self.biases))]

        self.save('network.pickle')

    def backprop(self, x, y):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]

        z_values, activations = self.feedForward(x)

        y = np.array([[1] if y == i else [0] for i in range(2)])

        delta = (activations[-1] - y) * sigmoid_prime(activations[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())

        for l in range(2, self.num_layers):
            z = z_values[-l]
            delta = np.dot(self.weights[-l + 1].transpose(), delta) * sigmoid_prime(z)
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l - 1].transpose())

        return nabla_b, nabla_w

    def feedForward(self, x):

        x = np.array([x]).transpose()
        zs = []
        xs = [x]

        for i in range(0, self.num_layers - 1):
            z = np.dot(self.weights[i], x) + self.biases[i]
            zs.append(z)
            x = sigmoid(z)
            xs.append(x)
        return zs, xs


def sigmoid(z):
    """The sigmoid function."""
    return 1.0 / (1.0 + np.exp(-z))


def sigmoid_prime(z):
    """Derivative of the sigmoid function."""
    return sigmoid(z) * (1 - sigmoid(z))
