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

# Tạo biến trạng thái để theo dõi mục nào đang được chọn
if 'page' not in st.session_state:
    st.session_state.page = 'gioi-thieu'

# Hàm để thay đổi nội dung khi nhấn vào các mục trong thanh điều hướng
def change_page(page):
    st.session_state.page = page

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
    .header {
        background-color: #FDEFF1;
        padding: 10px 20px;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }
    .header h2 {
        color: #D63384;
        font-family: Arial, sans-serif;
        font-size: 24px;
        font-weight: bold;
        margin: 0;
    }
    .sub-header {
        font-family: Arial, sans-serif;
        font-size: 18px;
        font-weight: normal;
        color: #666666;
        margin-top: 5px;
        margin-bottom: 0;
    }
    .nav-bar {
        display: flex;
        justify-content: center;
        background-color: #F8BBD0;
        padding: 10px;
        margin-top: 10px;
        border-radius: 10px;
    }
    .nav-item {
        margin: 0 15px;
        font-family: Arial, sans-serif;
        font-size: 16px;
        color: #0073C6;
        text-transform: uppercase;
        cursor: pointer;
        text-decoration: none;
        position: relative;
        font-weight: bold;
    }
    .nav-item:hover {
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True)

# Hiển thị tên đăng nhập nếu đã đăng nhập thành công
if st.session_state.logged_in_user:
    st.markdown(f"<p style='text-align:right;'>Xin chào, {st.session_state.logged_in_user}!</p>", unsafe_allow_html=True)

# Phần header (tiêu đề và sub-header)
st.markdown("""
    <div class="header">
        <h2>Mamacare</h2>
        <h3 class="sub-header">Nhận Trách Nhiệm, Trao Yêu Thương</h3>
    </div>
""", unsafe_allow_html=True)

# Thanh điều hướng với các nút trong cùng một trang
col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)

with col1:
    if st.button("Giới Thiệu"):
        change_page('gioi-thieu')

with col2:
    if st.button("Dịch Vụ"):
        change_page('dich-vu')

with col3:
    if st.button("Blog"):
        change_page('blog')

with col4:
    if st.button("Tuyển Dụng"):
        change_page('tuyen-dung')

with col5:
    if st.button("Hợp Tác"):
        change_page('hop-tac')

with col6:
    if st.button("Trợ Giúp"):
        change_page('tro-giup')

with col7:
    if st.button("Đăng Nhập"):
        change_page('dang-nhap')

with col8:
    if st.button("Đăng Ký"):
        change_page('dang-ky')

# Hiển thị nội dung dựa trên trạng thái của trang
if st.session_state.page == 'gioi-thieu':
    st.header("Giới Thiệu")
    st.image(image_2, caption="Chúng tôi quan tâm đến mẹ và bé", use_column_width=True)
    st.markdown("""
        **Mamacare** là nền tảng cung cấp dịch vụ chăm sóc sức khỏe tại nhà cho trẻ em và người cao tuổi. 
        Chúng tôi luôn hướng đến việc mang lại sự tiện lợi và an tâm cho các bậc phụ huynh và gia đình.

        ### Vì sao chọn MamaCare?
        - **Chăm sóc chuyên nghiệp**: Tất cả nhân viên chăm sóc của chúng tôi đều được cấp chứng chỉ.
        - **Sẵn sàng 24/7**: Chúng tôi sẵn sàng hỗ trợ bạn mọi lúc.
        - **Được các gia đình tin tưởng**: Hàng trăm gia đình đã tin tưởng và sử dụng dịch vụ của chúng tôi.
    """)

elif st.session_state.page == 'dich-vu':
    st.header("Dịch Vụ")
    st.image(image_1, caption="MamaCare - Chăm sóc mẹ sau sinh", use_column_width=True)
    st.markdown("""
        **Các dịch vụ của Mamacare** bao gồm:
        - Điều dưỡng tại nhà
        - Chăm sóc người cao tuổi
        - Dịch vụ phục hồi chức năng
        - Chăm sóc trẻ em tại nhà
    """)

elif st.session_state.page == 'blog':
    st.header("Blog")
    st.markdown("""
        Chào mừng bạn đến với Blog của Mamacare. Tại đây, bạn có thể tìm thấy những bài viết về:
        - Cách chăm sóc sức khỏe cho trẻ em
        - Phục hồi chức năng sau bệnh tật
        - Các bài viết tư vấn từ các chuyên gia y tế hàng đầu
    """)

elif st.session_state.page == 'tuyen-dung':
    st.header("Tuyển Dụng")
    st.markdown("""
        Mamacare đang tìm kiếm các ứng viên tài năng để gia nhập đội ngũ điều dưỡng và chăm sóc sức khỏe.
        - Vị trí: Điều dưỡng viên
        - Lương: Cạnh tranh
        - Thời gian làm việc: Linh hoạt
    """)
elif st.session_state.page == 'hop-tac':
    st.header("Hợp Tác")
    st.markdown("""
        Mamacare đang tìm kiếm các đối tác để mở rộng dịch vụ. Nếu bạn quan tâm đến việc hợp tác, hãy liên hệ với chúng tôi để biết thêm chi tiết.
    """)

elif st.session_state.page == 'tro-giup':
    st.header("Trợ Giúp")
    st.markdown("""
        Các câu hỏi thường gặp:
        1. Làm sao để đặt lịch chăm sóc tại nhà?
        2. Làm sao để đánh giá chất lượng dịch vụ?
        3. Tôi có thể yêu cầu nhân viên chăm sóc theo nhu cầu không?
    """)

# Trang đăng nhập
elif st.session_state.page == 'dang-nhap':
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

# Trang đăng ký
elif st.session_state.page == 'dang-ky':
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
