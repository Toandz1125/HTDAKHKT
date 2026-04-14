import pyodbc
import pandas as pd

# Kết nối SQL Server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=MAITOAN01;"
    "DATABASE=manager;"
    "Trusted_Connection=yes;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

cursor = conn.cursor()

# TODO 1: Tạo bảng employees nếu chưa tồn tại
cursor.execute("""
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='employees' AND xtype='U')
CREATE TABLE employees (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(100),
    age INT,
    department NVARCHAR(100)
)
""")
conn.commit()


# TODO 2: Vòng lặp nhập nhân viên
while True:
    name = input("Enter name (q to quit): ")

    if name.lower() == 'q':
        break

    age = int(input("Enter age: "))
    department = input("Enter department: ")

    cursor.execute(
        "INSERT INTO employees (name, age, department) VALUES (?, ?, ?)",
        (name, age, department)
    )

    conn.commit()


# TODO 3: Hiển thị bảng dạng DataFrame
query = "SELECT * FROM employees"
df = pd.read_sql(query, conn)

print("\nEmployee Table:")
print(df)


# TODO 4: Thống kê theo phòng ban
stats = df.groupby('department').agg(
    count=('name', 'count'),
    avg_age=('age', 'mean'),
    max_age=('age', 'max')
)

print("\nStatistics by Department:")
print(stats)

cursor.close()
conn.close()