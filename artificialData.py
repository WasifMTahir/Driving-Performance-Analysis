data1 = np.array([[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
       [[0, 0], [0, 50], [0, 0], [0, 0], [10, 0], [20, 0], [30, 0], [40, 0], [30, 0], [20, 0]],
       [[10, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
       [[0, -50], [0, 0], [0, 0], [-10, 0], [-15, 0], [-25, 0], [-30, 0], [-50, 0], [-30, 0], [-10, 0]],
       [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],   
       [[0, -50], [0, 0], [-15, 0], [-30, 0], [-50, 0], [-35, 0], [-20, 0], [-5, 0], [5, 0], [0, 0]],
       [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],   
       [[0, 50], [0, 0], [5, 0], [15, 0], [20, 0], [30, 0], [45, 0], [60, 0], [40, 0], [20, 0]],
       [[10, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],   
       [[0, 0], [0, 0], [0, 0], [0, 50], [0, 0], [0, 0], [20, 0], [30, 0], [40, 0], [30, 0]],
       [[15, 0], [5, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],   
       [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],   
       [[0, 50], [0, 0], [0, 0], [10, 0], [25, 0], [40, 0], [55, 0], [75, 0], [50, 0], [25, 0]],
       [[10, 0], [-5, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
       [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],   
       [[0, 0], [0, 0], [0, 0], [0, -50], [0, 0], [0, 0], [0, 0], [-20, 0], [-45, 0], [-65, 0]],
       [[-30, 0], [-10, 0], [4, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]])
	   
data2 = np.array([[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
       [[0, 0], [0, 0], [0, 0], [0, 0], [10, 0], [20, 0], [30, 0], [40, 0], [30, 0], [20, 0]],
       [[10, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
       [[0, 0], [0, 0], [0, 0], [-10, 0], [-15, 0], [-25, 0], [-30, 0], [-50, 0], [-30, 0], [-10, 0]],
       [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],   
       [[0, 0], [0, 0], [-15, 0], [-30, 0], [-50, 0], [-35, 0], [-20, 0], [-5, 0], [5, 0], [0, 0]],
       [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],   
       [[0, 0], [0, 0], [5, 0], [15, 0], [20, 0], [30, 0], [45, 0], [60, 0], [40, 0], [20, 0]],
       [[10, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],   
       [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [20, 0], [30, 0], [40, 0], [30, 0]],
       [[15, 0], [5, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],   
       [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],   
       [[0, 0], [0, 0], [0, 0], [10, 0], [25, 0], [40, 0], [55, 0], [75, 0], [50, 0], [25, 0]],
       [[10, 0], [-5, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
       [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],   
       [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [-20, 0], [-45, 0], [-65, 0]],
       [[-30, 0], [-10, 0], [4, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]])
	   
data3 = np.array([[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
       [[0, 0], [0, -50], [0, 0], [0, 0], [10, 0], [20, 0], [30, 0], [40, 0], [30, 0], [20, 0]],
       [[10, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
       [[0, 50], [0, 0], [0, 0], [-10, 0], [-15, 0], [-25, 0], [-30, 0], [-50, 0], [-30, 0], [-10, 0]],
       [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],   
       [[0, 50], [0, 0], [-15, 0], [-30, 0], [-50, 0], [-35, 0], [-20, 0], [-5, 0], [5, 0], [0, 0]],
       [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],   
       [[0, -50], [0, 0], [5, 0], [15, 0], [20, 0], [30, 0], [45, 0], [60, 0], [40, 0], [20, 0]],
       [[10, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],   
       [[0, 0], [0, 0], [0, 0], [0, -50], [0, 0], [0, 0], [20, 0], [30, 0], [40, 0], [30, 0]],
       [[15, 0], [5, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],   
       [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],   
       [[0, -50], [0, 0], [0, 0], [10, 0], [25, 0], [40, 0], [55, 0], [75, 0], [50, 0], [25, 0]],
       [[10, 0], [-5, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
       [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],   
       [[0, 0], [0, 0], [0, 0], [0, 50], [0, 0], [0, 0], [0, 0], [-20, 0], [-45, 0], [-65, 0]],
       [[-30, 0], [-10, 0], [4, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]])