import numpy as np

array_1d = np.array(np.arange(0, 8))
array_2d = np.array([np.arange(0, 8, 2), np.arange(1, 8, 2), np.arange(1, 8, 2)])


eye_array = np.eye(4, k=1)
print(eye_array)
eye_array[eye_array == 0] = 2
print(eye_array)
eye_array[eye_array < 2] = 9
print(eye_array)
eye_array[1:] = 3
print(eye_array)
eye_array[:, -1] = 4
print(eye_array)
eye_array[3, 0] = 5
print(eye_array)