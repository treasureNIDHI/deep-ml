import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# scores=np.array(scores, dtype=float)
	# max_score=np.max(scores)
	# # for score in scores:
	# n = np.log(np.sum(np.exp(scores-max_score)))
	# l_s= (scores-max_score)-n
	
	# return l_s
	scores=np.array(scores,dtype=float)
	max_score = np.max(scores)
	log = np.log(np.sum(np.exp(scores-max_score)))
	log_softmax = (scores-max_score) - log
	return log_softmax