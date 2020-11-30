import init
import Solve
import Verify
import Signing

def disavowal(docX, signY, e1, e2, c, d):
    print("------giao thức từ chối------")
    print("chọn ngẫu nhiên f1, f2 với 1 <= f1, f2 < (p - 1)/2:")
    f1 = int(input("nhập f1: "))
    f2 = int(input("nhập f2: "))
    C = Solve.powerMode(signY, f1, init.publicKey.p)*Solve.powerMode(init.publicKey.beta, f2, init.publicKey.p) % init.publicKey.p
    print("bên kiểm thử tính C và gửi cho bên ký: C =" + str(C))
    D = Solve.powerMode(C, Solve.ext_gcd(int((init.publicKey.p-1)/2), init.privateKey.a), init.publicKey.p)
    print("bên ký tính D và gửi cho bên kiểm thử: D = " + str(D))
    check = Solve.powerMode(docX, f1, init.publicKey.p)*Solve.powerMode(init.publicKey.alpha, f2, init.publicKey.p) % init.publicKey.p

    print("bên kiểm tính 'check' thử xác minh xem có trùng với D không, check = " + str(check))
    if(check == D): print(" => chữ ký y trên x hợp lệ")
    else:
        print("không trùng => thực hiện bước cuối cùng là kiểm tra tính phù hợp")
        print("bên kiểm thử kết luận y là giả mạo khi và chỉ khi:")
        print("(d.alpha^-e2)^f1 == (D.alpha^-f2)^e1 (mod p)")
        check1 = Solve.powerMode(d, f1, init.publicKey.p)*Solve.ext_gcd(init.publicKey.p, pow(init.publicKey.alpha,e2*f1)) % init.publicKey.p
        check2 = Solve.powerMode(D, e1, init.publicKey.p)*Solve.ext_gcd(init.publicKey.p, pow(init.publicKey.alpha, f2*e1)) % init.publicKey.p
        if(check1 == check2):
            print(str(check1) + " == " + str(check2))
            print("=> chữ ký y trên x không hợp lệ")