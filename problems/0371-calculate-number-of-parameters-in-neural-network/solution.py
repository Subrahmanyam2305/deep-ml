def calculate_parameters(layers: list[dict]) -> int:
	"""
	Calculate the total number of trainable parameters in a neural network.

	Args:
		layers: List of dictionaries, each describing a layer.

	Returns:
		Total number of trainable parameters (int).
	"""
	# Your code here
	res = 0
	for layer in layers:
		if layer['type'] == 'dense':
			res += layer['input_size']*layer['output_size'] + layer['output_size']
			if not layer.get('bias', True):
				res -= layer['output_size']
		
		if layer['type'] == 'conv2d':
			res += layer['in_channels']*layer['out_channels']*layer['kernel_size']*layer['kernel_size'] + layer['out_channels']
			if  not layer.get('bias', True):
				res -= layer['out_channels']

	return res
