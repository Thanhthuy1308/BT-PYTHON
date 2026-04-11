import math_utils

def main():
    # Thử nghiệm phân số
    p1 = (1, 5) # 1/2
    p2 = (1, 7) # 1/3
    kq_cong = math_utils.cong_phan_so(p1, p2)
    print(f"Tổng phân số: {kq_cong[0]}/{kq_cong[1]}")

    # Thử nghiệm hình học
    r = 5
    print(f"Diện tích hình tròn bán kính {r}: {math_utils.dien_tich_tron(r):.2f}")
    
    dai, rong = 10, 5
    print(f"Chu vi hình chữ nhật ({dai}x{rong}): {math_utils.chu_vi_hcn(dai, rong)}")

if __name__ == "__main__":
    main()