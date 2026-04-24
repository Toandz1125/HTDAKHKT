try:
    can_nang = input("Nhập cân nặng (kg): ").replace(",", ".") #Hỗ trợ cả chấm và phẩy khi người dùng ko biết nhập dấu phẩy hay dấu chấm khi nhập số thập phân
    chieu_cao = input("Nhập chiều cao (m): ").replace(",", ".")

    can_nang = float(can_nang)
    chieu_cao = float(chieu_cao)

    bmi = can_nang / (chieu_cao ** 2)

    print("Chỉ số BMI =", round(bmi, 2))

    if bmi < 18.5:
        print("Phân loại: Gầy")
    elif bmi < 25:
        print("Phân loại: Bình thường")
    else:
        print("Phân loại: Thừa cân")

except ValueError:
    print("Lỗi: Bạn phải nhập số, không được nhập chữ.")

except ZeroDivisionError:
    print("Lỗi: Chiều cao không được bằng 0.")