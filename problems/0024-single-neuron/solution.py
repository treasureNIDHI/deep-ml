import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	probab=[]
	for feature in features:
		z= sum(w*f for w,f in zip(weights,feature))+bias
		sig= 1/(1+math.exp(-z))
		probab.append(sig)

	summ=0.0
	mse=0.0
	for pred, true in zip(probab,labels):
		summ+=(pred-true)**2
	mse=summ/len(probab)
	return probab,mse
	