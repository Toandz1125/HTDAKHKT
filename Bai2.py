def tach_tu(van_ban):
    van_ban = van_ban.replace(",", "").replace(".", "")
    danh_sach_tu = van_ban.lower().split()
    return danh_sach_tu

text = input("Nhập đoạn văn bản: ")

words = tach_tu(text)

print("Danh sách từ:", words)
print("Tổng số từ:", len(words))

dem = {}

for word in words:
    if word in dem:
        dem[word] += 1
    else:
        dem[word] = 1

max_lan = max(dem.values())

tu_nhieu_nhat = []

for word, count in dem.items():
    if count == max_lan:
        tu_nhieu_nhat.append(word)

print("Từ xuất hiện nhiều nhất:", tu_nhieu_nhat)
print("Số lần xuất hiện:", max_lan)