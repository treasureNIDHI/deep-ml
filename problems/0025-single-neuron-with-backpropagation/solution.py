import numpy as np
import math
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	# Your code here
	mse_values=[]
	for epoch in range(epochs):
		probab=[]

		for feature in features:
			z=sum(f*w for f,w in zip(feature,initial_weights))+initial_bias
			sigmoid = 1 / (1+math.exp(-z))
			probab.append(sigmoid)
		summ=0.0
		
		for pred, true in zip(probab,labels):
			summ+=((pred-true)**2)
		mse=summ/len(probab)
		mse_values.append(mse)

		
		grad_w = np.zeros_like(initial_weights, dtype=float)
		grad_b = 0.0

		for feature, pred, true in zip(features, probab, labels):
			# Calculate delta
			delta=2*(pred - true)*pred*(1-pred)

			# Accumulate weight gradients
			for j, f in enumerate(feature):
				grad_w[j] += delta * f

			# Accumulate bias gradient
			grad_b += delta

		# Average both gradients
		grad_w/=len(probab)
		grad_b/=len(probab)

		# updated_weights = weights - learning_rate * grad_w
		# updated_bias = bias - learning_rate * grad_b
		updated_bias = []
		updated_weights=[]
		initial_weights = initial_weights - learning_rate * grad_w
		initial_bias = initial_bias - learning_rate * grad_b

	return initial_weights, initial_bias, mse_values



