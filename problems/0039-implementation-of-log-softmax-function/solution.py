import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	# deno=0
	
	# for score in scores:
	# 	deno+=np.exp(score)
	# for score in scores:
	# 	out.append((np.exp(score))/deno)
	# return out
	scores=np.array(scores, dtype=float)
	max_score=np.max(scores)
	# for score in scores:
	n = np.log(np.sum(np.exp(scores-max_score)))
	l_s= (scores-max_score)-n
	
	return l_s