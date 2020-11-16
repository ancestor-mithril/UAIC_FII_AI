from Network2 import Network

net = Network(learning_rate=0.1)

func = [0, 1, 1, 0]

net.train(max_epochs=10000, func=func)

print(net.feedForward([0, 0])[1])
