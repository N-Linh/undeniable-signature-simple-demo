import init
import Signing
import Solve
import Disavowal

def verify():
    print("------Giao thức kiểm thử------")
    signY = int(input("nhập chữ ký nhận được: "))
    print("thông báo x với chữ ký y: x = " + str(init.doc.x))
    print("kiểm thử với khóa công khai là: K(p, alpha, beta) : K(" + str(init.publicKey.p) + ", " + str(init.publicKey.alpha) + ", " + str(init.publicKey.beta) + ")")
    print("chọn ngẫu nhiên e1, e2 với 1 <= e1, e2 <= p - 1:")
    e1 = int(input("nhập e1:"))
    e2 = int(input("nhập e2:"))
    c = Solve.powerMode(signY, e1, init.publicKey.p)*Solve.powerMode(init.publicKey.beta, e2, init.publicKey.p) % init.publicKey.p
    print("bên kiểm thử tính c và gửi cho bên ký: c = y^e1.beta^e2 mod p = " + str(c))
    d = Solve.powerMode(c, int(Solve.ext_gcd((init.publicKey.p - 1)/2, init.privateKey.a)), init.publicKey.p)
    print("bên ký tính d gửi cho bên kiểm thử: d = c^(a^-1 mod q) mod p = " + str(d))
    check = Solve.powerMode(init.doc.x, e1, init.publicKey.p)*Solve.powerMode(init.publicKey.alpha, e2, init.publicKey.p) % init.publicKey.p
    print("bên kiểm thử kiểm tra d = (x^e1 * alpha^e2 mod p) hay không, check = " + str(check))
    if(check == d): print("trùng d => chữ ký hợp lệ")
    else:
        print("không trùng d => thực hiện bước giao thức từ chối")
        Disavowal.disavowal(init.doc.x, signY, e1, e2, c, d)