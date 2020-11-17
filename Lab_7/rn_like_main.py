from rn_like_network import Network

net = Network([2, 2, 1], learning_rate=0.2)

print("Starting training...")
net.train(max_epochs=10000, func=[0, 1, 1, 0])

net.load_and_run('network.pickle', func=[0, 1, 1, 0])
