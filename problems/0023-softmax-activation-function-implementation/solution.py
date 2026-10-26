import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    max_score=max(scores)
    deno=0
    result=[]
    for i in scores:
        deno+=math.exp(i-max_score)
    for j in scores:
        soft=math.exp(j-max_score)/deno
        result.append(soft)
    return result
  