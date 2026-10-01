import numpy as np

def temperature_sampling(logits: np.ndarray, temperature: float) -> list:
	"""
	Compute temperature-scaled softmax probabilities from logits.
	
	Args:
		logits: 1D numpy array of raw model output scores
		temperature: float controlling distribution sharpness
	
	Returns:
		List of probabilities after temperature scaling
	"""
	# Your code here
	if temperature == 0:
		idx = np.argmax(logits)
		res = np.zeros(logits.shape)
		res[idx] = 1
		return res
	temp_logits = logits/temperature
	softmax = np.exp(temp_logits) / np.sum(np.exp(temp_logits))
	return softmax
	