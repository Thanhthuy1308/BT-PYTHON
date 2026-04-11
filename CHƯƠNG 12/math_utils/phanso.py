def cong_phan_so(p1, p2):
    tu = p1[0] * p2[1] + p2[0] * p1[1]
    mau = p1[1] * p2[1]
    return (tu, mau)

def tru_phan_so(p1, p2):
    tu = p1[0] * p2[1] - p2[0] * p1[1]
    mau = p1[1] * p2[1]
    return (tu, mau)

def nhan_phan_so(p1, p2):
    return (p1[0] * p2[0], p1[1] * p2[1])

def chia_phan_so(p1, p2):
    return (p1[0] * p2[1], p1[1] * p2[0])