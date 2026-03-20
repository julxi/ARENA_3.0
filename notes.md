# 1.3.1

- alone first half of notebook uses 52GB disk

- bias/center mising in MMProbe?
    - makes sense to me
    - when added boost accuracy
    - cross-dada transfer worse

- in 3 Causal interventions / batch-aware intervention hook:
    - what is the purpose of # scale the direction?
    - In my notebook `direction = scaled_direction`

- in 4 probing for deception - exercise - construct instructed-pairs
    - there is a hint about splitting statements but the code is already provided
    - also defenisve coding len(words) > 5, the authors don't want the last words to capture intent
- exercise DeceptionSteeringHook : discussion
    - "it may only be a classification feature. This is consistent with the Geometry of Truth paper's finding that LR directions have high accuracy but low causal effect" <- the exercise uses mm

# 1.3.2 Function vectors

| can we steer a model to produce different outputs / have a different behaviour, by intervening on the model's forward pass using vectors found by non gradient descent-based methods?

_haven't we just seen that in 1.3.1?_
