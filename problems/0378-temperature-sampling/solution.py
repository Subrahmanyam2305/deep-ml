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
		res = np.zeros_like(logits)
		res[idx] = 1.0
		return res.tolist()
	temp_logits = logits/temperature
	shifted_logits = temp_logits - max(temp_logits) # when one no approaches infinity
	softmax = np.exp(shifted_logits) / np.sum(np.exp(shifted_logits))
	return softmax.tolist()
	