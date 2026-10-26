# import numpy as np

# def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
# 	#Write your code here and return a python list after reshaping by using numpy's tolist() method
# 	a=np.array(a)
# 	if a.size != new_shape[0] * new_shape[1]:
#         return []
# 	else:
# 		reshaped_matrix=a.reshape(new_shape).tolist()
# 		return reshaped_matrix
import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    # Guard against empty matrices or missing rows
    if not a or not a[0]:
        return []
        
    try:
        arr = np.array(a)
        
        # Verify that total elements match the product of the new shape
        if arr.size != new_shape[0] * new_shape[1]:
            return []
            
        return arr.reshape(new_shape).tolist()
    except Exception:
        # Catch any structural irregularity (like jagged rows)
        return []