from Mat import Mat


R = Mat([[3, 2, 3, 0], [2, 5, 4, 0], [1, 3, 2, 0], [1, 2, 3, 0]], slu=3)

R[0] = R[0]/3
R[1] = R[1] - 2*R[0]
R[2] = R[2] - R[0]
R[3] = R[3]-R[0]
R[1] = 3*R[1]/11
R[2] = R[2]-7*R[1]/3
R[3] = R[3]-4*R[1]/3
R[2] = -11*R[2]/3
R[3] = R[3]-14*R[2]/11

print(R)