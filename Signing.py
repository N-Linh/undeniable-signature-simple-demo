import init
import Solve

class Sign:
    y = 1
sign = Sign()
def signing():
    print("------Lập chữ ký------")
    sign.y = Solve.powerMode(init.doc.x, init.privateKey.a, init.publicKey.p)
    print("chữ ký trên văn bản x: y = sigk(x) = " + str(sign.y))