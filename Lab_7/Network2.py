import numpy as np


class Network:
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate
        self.input_size = 2
        self.hidden_size = 2
        self.output_size = 1

        self.hidden_weights = np.random.uniform(-0.1, 0.1, size=(self.hidden_size,self.input_size))
        self.output_weights = np.random.uniform(-0.1, 0.1, size=(self.output_size,self.hidden_size))

        self.hidden_biases = [-1] * self.hidden_size
        self.output_biases = [-1] * self.output_size

        # print("Hidden weights:", self.hidden_weights)
        # print("Output weights:", self.output_weights)
        # print("HB:", self.hidden_biases)
        # print("OB:", self.output_biases)

    def train(self, max_epochs, func):
        for j in range(max_epochs):
            inp = [np.random.randint(2), np.random.randint(2)]
            out = func[inp[0]*2 + inp[1]]

            ys, net_out = self.feedForward(inp)

            # mse = (out-net_out)**2
            # print("MSE?: ", mse)

            delta_output_weights, delta_hidden_weights = self.backprop(ys, out, net_out)

            self.hidden_weights += delta_hidden_weights
            self.output_weights += delta_output_weights

            # print("1 iteration")
            # print(self.hidden_weights, self.output_weights)

    def feedForward(self, inp):
        activated_values = [np.array([[inp[0], inp[0]], [inp[1], inp[1]]])]

        Sum = np.dot(inp, self.hidden_weights)

        hidden_sum = sigmoid(Sum + self.hidden_biases)

        activated_values.append(hidden_sum)

        output = np.dot(hidden_sum, self.output_weights.T)

        output_sum = sigmoid(output + self.output_biases)

        return activated_values, output_sum

    def backprop(self, ys, out, net_out):
        # print("YS:", ys)
        delta = sigmoid_prime(net_out) * (out - net_out)

        delta_output_weights = (self.learning_rate * delta[0]) * ys[-1]

        # print("DOW:", delta_output_weights)

        delta_hidden = sigmoid_prime(ys[-1]) * sum(delta * self.hidden_weights)
        # print("DH:", delta_hidden)

        delta_hidden_weights = (self.learning_rate * delta_hidden) * ys[-2]
        # print("DHW:", delta_hidden_weights)

        return delta_output_weights, delta_hidden_weights

def sigmoid(z):
    """The sigmoid function."""
    return 1.0 / (1.0 + np.exp(-z))


def sigmoid_prime(z):
    """Derivative of the sigmoid function."""
    return sigmoid(z) * (1 - sigmoid(z))
