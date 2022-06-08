class QValues():
    @staticmethod
    def get_current(policy_net, states, actions):
        # return predicted q values for specific state-actions pairs
        y_pred = policy_net(states, training=False)
        return policy_net(states).gather(dim=1, index=actions.unsqueeze(-1))

    @staticmethod
    def get_next(target_net, next_states):
        return target_net(next_states)
        # for each next_state we want max q value among all actions
        pass
        final_state_locations = next_states.flatten(start_dim=1).max(dim=1)[0].eq(0).type(torch.bool)
        non_final_state_locations = (final_state_locations == False)
        non_final_states = next_states[non_final_state_locations]
        batch_size = next_states.shape[0]
        values = torch.zeros(batch_size).to(QValues.device)
        values[non_final_state_locations] = target_net(non_final_states).max(dim=1)[0].detach()
        return values
        