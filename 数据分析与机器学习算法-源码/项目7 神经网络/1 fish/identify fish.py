# identify fish
import numpy as np
ty = ["鲢鱼", "鲤鱼"]  #   鲤鱼
ag = 1
maxinx = 0
while ag:
    bl = 0.0
    bl = float(input("输入鱼的身长 "))
    hl = 0.0
    hl = float(input("输入鱼的腮长 "))

    #weights：
    #[[-0.67, -0.14]
    # [1.34, -1.1]]
    #bias：
    #[0.02, -0.02]
    print("%5d%5d" % (bl, hl))
    maxinx = np.argmax((np.matmul([bl, hl], [[-0.67, -0.14], [1.34, -1.1]]) + [0.02, -0.02]))
    print(ty[maxinx])
    ag = int(input("again? press 1，Exit press 0 "))