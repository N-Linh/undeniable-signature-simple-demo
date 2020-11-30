import Solve
import random
class PublicKey:
    p = 1
    alpha = 1
    beta = 1
class PrivateKey:
    a = 1
class Doc:
    x = 1
publicKey = PublicKey()
privateKey = PrivateKey()
doc = Doc()
def init():
    print("------Khởi tạo giá trị------")
    p = int(input("nhập số nguyên tố p:"))
    while not Solve.isPrime(p):
        p = int(input("nhập lại số nguyên tố p:"))
    publicKey.p = p

    g = Solve.primRoots(p)[0]
    publicKey.alpha = g*g
    a = int(input("nhập số a với 1 <= a <= (p-1)/2: "))
    privateKey.a = a
    publicKey.beta = Solve.powerMode(publicKey.alpha, privateKey.a, publicKey.p)

    print("khóa công khai: K(p, alpha, beta) : K(" + str(publicKey.p) + ", " + str(publicKey.alpha) + ", " + str(publicKey.beta) + ")")
    print("khóa bí mật a K(a) : K(" + str(privateKey.a) + ")")
    x = int(input("nhập văn bản x:"))
    doc.x = x
