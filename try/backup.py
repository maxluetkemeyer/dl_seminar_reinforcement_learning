n_epochs = 5
n_steps = 100
# 1. Initialize replay memory capacity.
# 2. Initialize the policy network with random weights.
# 3. Clone the policy network, and call it the target network.
# 4. For each episode:
for epoch in range(1, n_epochs + 1):
    print("Epoch {}/{}".format(epoch, n_epochs))
    # 1. Initialize the starting state.
    # 2. For each time step:
        # 1. Select an action. (Via exploration or exploitation)
        # 2. Execute selected action in an emulator.
        # 3. Observe reward and next state.
        # 4. Store experience in replay memory.
        # 5. Sample random batch from replay memory.
        # 6. Preprocess states from batch.
        # 7. Pass batch of preprocessed states to policy network.
        # 8. Calculate loss between output Q-values and target Q-values.
        # Requires a pass to the target network for the next state
        # 9. Gradient descent updates weights in the policy network to minimize loss.
        # After  time steps, weights in the target network are updated to the weights in the policy network.