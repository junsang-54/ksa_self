arr = np.arange(6).reshape(2,3)   # arr = ([[0,1,2], [3,4,5]])
arr_0 = np.delete(arr, n, axis=0)   # arr배열에서 n번째 행 제거
arr_1 = np.delete(arr, n, axis=1)   # arr배열에서 n번째 열 제거
