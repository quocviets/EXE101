import streamlit as st
from PIL import Image

# Cấu hình trang
st.set_page_config(page_title="MamaCare", page_icon="👶", layout="wide")

# Biến lưu trữ tài khoản (giả lập bằng session_state)
if 'users' not in st.session_state:
    st.session_state.users = {}

# Biến lưu trữ trạng thái đăng nhập
if 'logged_in_user' not in st.session_state:
    st.session_state.logged_in_user = None

# Tải hình ảnh
image_1 = Image.open(r"C:\\Users\\lequo\\Downloads\\UI\\UI\\1.png")
image_2 = Image.open(r"C:\\Users\\lequo\\Downloads\\UI\\UI\\2.png")

# CSS để tạo phong cách
st.markdown("""
    <style>
    .main-title {
        font-size: 50px;
        color: #FF4B4B;
        text-align: center;
        font-weight: bold;
    }
    .section-title {
        font-size: 35px;
        color: #FF6F61;
        margin-top: 40px;
        margin-bottom: 20px;
    }
    .form-field {
        background-color: #FFE5E5;
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Hiển thị tên đăng nhập nếu đã đăng nhập thành công
if st.session_state.logged_in_user:
    st.markdown(f"<p style='text-align:right;'>Xin chào, {st.session_state.logged_in_user}!</p>", unsafe_allow_html=True)

# Thanh điều hướng ở sidebar
st.sidebar.title("Điều hướng MamaCare")
pages = ["Trang chủ", "Giới thiệu", "Đăng nhập", "Đăng ký"]
page_selection = st.sidebar.radio("Đi tới", pages)

# Trang: Trang chủ
if page_selection == "Trang chủ":
    st.markdown('<h1 class="main-title">MamaCare - Chăm sóc mẹ sau sinh</h1>', unsafe_allow_html=True)
    st.image(image_1, caption="MamaCare - Chăm sóc mẹ sau sinh", use_column_width=True)
    
    # Văn bản giới thiệu
    st.markdown("""
    <div class="section-title">Chào mừng đến với MamaCare</div>
    Chúng tôi cung cấp dịch vụ chăm sóc tận tâm và chuyên nghiệp cho các mẹ và bé sau sinh. 
    Đội ngũ chăm sóc của chúng tôi luôn sẵn sàng hỗ trợ bạn trong giai đoạn quan trọng này.

    ### Dịch vụ của chúng tôi:
    - **Chăm sóc sau sinh** cho các mẹ
    - **Chăm sóc em bé** và hỗ trợ nuôi dưỡng
    - **Hỗ trợ tinh thần** và hướng dẫn cho con bú
    """, unsafe_allow_html=True)

    # Biểu mẫu đặt lịch
    st.markdown('<div class="section-title">Đặt lịch chăm sóc viên</div>', unsafe_allow_html=True)
    with st.form(key="booking_form"):
        name = st.text_input("Tên của bạn")
        email = st.text_input("Email của bạn")
        service = st.selectbox("Chọn dịch vụ", ["Chăm sóc sau sinh", "Chăm sóc em bé", "Hỗ trợ nuôi dưỡng"])
        date = st.date_input("Ngày mong muốn")
        time = st.time_input("Giờ mong muốn")
        submit_button = st.form_submit_button("Gửi")

    # Tin nhắn xác nhận
    if submit_button:
        st.success(f"Cảm ơn {name}! Chúng tôi đã nhận yêu cầu của bạn cho dịch vụ {service} vào ngày {date} lúc {time}. Chúng tôi sẽ liên hệ với bạn qua email {email} sớm nhất có thể.")

# Trang: Giới thiệu
elif page_selection == "Giới thiệu":
    st.markdown('<h1 class="main-title">Giới thiệu về MamaCare</h1>', unsafe_allow_html=True)
    st.image(image_2, caption="Chúng tôi quan tâm đến mẹ và bé", use_column_width=True)
    st.write("""
    Tại MamaCare, chúng tôi cam kết mang đến dịch vụ chăm sóc tốt nhất cho các mẹ sau khi sinh. 
    Đội ngũ chăm sóc của chúng tôi đều là những chuyên gia giàu kinh nghiệm, sẵn sàng hỗ trợ cả về thể chất và tinh thần cho các mẹ và bé.

    ### Vì sao chọn MamaCare?
    - **Chăm sóc chuyên nghiệp**: Tất cả nhân viên chăm sóc của chúng tôi đều được cấp chứng chỉ.
    - **Sẵn sàng 24/7**: Chúng tôi sẵn sàng hỗ trợ bạn mọi lúc.
    - **Được các gia đình tin tưởng**: Hàng trăm gia đình đã tin tưởng và sử dụng dịch vụ của chúng tôi.

    Liên hệ ngay để biết thêm về dịch vụ của chúng tôi và cách chúng tôi có thể hỗ trợ bạn trong hành trình chăm sóc sau sinh!
    """)

# Trang: Đăng nhập
elif page_selection == "Đăng nhập":
    st.markdown('<h1 class="main-title">Đăng nhập</h1>', unsafe_allow_html=True)
    
    # Biểu mẫu đăng nhập
    with st.form(key="login_form"):
        email = st.text_input("Email")
        password = st.text_input("Mật khẩu", type="password")
        login_button = st.form_submit_button("Đăng nhập")
    
    # Xác thực đăng nhập cơ bản
    if login_button:
        if email in st.session_state.users and st.session_state.users[email]['password'] == password:
            st.session_state.logged_in_user = st.session_state.users[email]['username']
            st.success(f"Chào mừng bạn trở lại, {st.session_state.logged_in_user}!")
        else:
            st.error("Thông tin đăng nhập không chính xác. Vui lòng thử lại.")

# Trang: Đăng ký
elif page_selection == "Đăng ký":
    st.markdown('<h1 class="main-title">Đăng ký</h1>', unsafe_allow_html=True)
    
    # Biểu mẫu đăng ký
    with st.form(key="signup_form"):
        username = st.text_input("Tên đăng nhập")
        email = st.text_input("Email")
        password = st.text_input("Mật khẩu", type="password")
        signup_button = st.form_submit_button("Đăng ký")
    
    # Xác nhận đăng ký
    if signup_button:
        if email in st.session_state.users:
            st.error("Email này đã tồn tại. Vui lòng chọn email khác.")
        else:
            st.session_state.users[email] = {'username': username, 'password': password}
            st.success(f"Đăng ký thành công! Bạn có thể đăng nhập bằng email: {email}")

# Footer (Tùy chọn)
st.markdown("""
<hr style="border:2px solid #FF6F61">
<p style="text-align:center;">© 2024 MamaCare. website đang trong quá trình thử nghiệm.</p>
""", unsafe_allow_html=True)
