# LAB 03 – LOGIN TESTING USING SELENIUM

## Mục tiêu
Thực hiện kiểm thử tự động (Automation Testing) chức năng **Đăng nhập (Login)** bằng **Python + Selenium + Pytest**.  
Yêu cầu: **6 test case chạy được**, **locator gọn & chính xác**, **ảnh chụp kết quả**, **README hướng dẫn**.

---

## 📂 Cấu trúc thư mục
```
lab03-selenium/
├─ site/
│  ├─ login.html
│  ├─ forgot.html
│  ├─ signup.html
│  └─ dashboard.html
├─ tests/
│  └─ test_login.py
├─ screenshots/
│  ├─ login_success.png
│  ├─ wrong_password.png
│  ├─ empty_fields.png
│  ├─ forgot_password.png
│  ├─ signup_link.png
│  └─ social_buttons.png
│  └─ ketqua.png
|─ README.md
└─ test_cases_lab03.txt
```


```
.venv/
.pytest_cache/
__pycache__/
*.pyc
```

---

## Các bước thực hiện test
**1. Chuẩn bị môi trường**

- Cài Python 3.x (tick “Add Python to PATH”).

- Mở CMD tại thư mục dự án:

cd /d E:\lab03-selenium
-->python -m venv .venv
-->.venv\Scripts\activate
-->pip install selenium webdriver-manager pytest


- Khởi chạy web server cục bộ

- Mở một CMD khác (giữ cửa sổ này mở suốt lúc test):

-->cd /d E:\lab03-selenium
-->python -m http.server 8000


- Kiểm tra trang chạy: mở trình duyệt vào http://localhost:8000/site/login.html.

- Chạy bộ test Selenium (6 test case)

- Quay về cửa sổ CMD có (venv):

-->cd /d E:\lab03-selenium
-->.venv\Scripts\activate
-->pytest -q


- **Kết quả mong đợi:**

......
*6 passed in XXs*



## 🔎 Locator sử dụng
- Username: `By.ID, "username"`  
- Password: `By.ID, "password"`  
- Nút LOGIN: `By.ID, "submit"`  
- Link Forgot: `By.LINK_TEXT, "Forgot password?"`  
- Link Sign Up: `By.LINK_TEXT, "SIGN UP"`  
- Nút mạng xã hội: `By.CSS_SELECTOR, ".circle"`  


## Danh sách 6 Test Case
1. **Login thành công** → điều hướng `dashboard.html`  
2. **Sai mật khẩu** → thông báo “Sai tài khoản hoặc mật khẩu”  
3. **Bỏ trống ô nhập** → thông báo “Vui lòng nhập đầy đủ (required)”  
4. **Forgot password** → điều hướng `forgot.html`  
5. **SIGN UP** → điều hướng `signup.html`  
6. **Hiển thị 3 nút social** → tồn tại đủ 3 phần tử `.circle`


---

## Thông tin sinh viên
- Họ tên: Hồ Thị Mai Linh
- Lớp: D23CQPTTK01-N
- Môn: Nhập môn công nghệ phần mềm
- Giảng viên hướng dẫn: Châu Văn Vân
- Bài: LAB 03 – Login Testing using Selenium
