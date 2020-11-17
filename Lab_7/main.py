from rn_like_network import Network

net = Network([2, 2, 1], learning_rate=3)

func = [0, 1, 1, 0]

net.train(max_epochs=10000, func=func)

net.load_and_run('network.pickle', func=[0, 1, 1, 0])
