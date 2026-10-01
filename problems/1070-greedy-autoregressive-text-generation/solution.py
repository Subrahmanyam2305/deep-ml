import numpy as np

def generate_greedy(model, idx: list, max_new_tokens: int, context_size: int) -> list:
    # Your code here
    # model input is 1,T --> 1, T, vocab
    for i in range(max_new_tokens):
        input_tokens = np.array(idx[-context_size:]).reshape(1,-1)
        logits = model(input_tokens)
        next_token = int(np.argmax(logits[:,-1,:]))
        idx.append(next_token)
    return idx
