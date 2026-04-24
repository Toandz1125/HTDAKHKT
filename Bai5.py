import matplotlib.pyplot as plt

kho_hang = {
    "Balo": 150,
    "Tui xach": 80,
    "Vali": 120
}

vi_da = int(input("Nhập số lượng Ví da: "))
kho_hang["Vi da"] = vi_da

kho_hang["Balo"] -= 30

print("Kho hàng sau cập nhật:")
for ten, so_luong in kho_hang.items():
    print(f"{ten}: {so_luong}")

labels = kho_hang.keys()
sizes = kho_hang.values()

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Tỷ trọng hàng hóa trong kho")
plt.show()