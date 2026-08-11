import streamlit as st
from bank import Bank

st.set_page_config(
    page_title="PRINCE BANK",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    .main-title {
        font-size: 42px;
        font-weight: 800;
        letter-spacing: 1px;
        margin-bottom: 0;
    }
    .subtitle {
        color: #777;
        font-size: 17px;
        margin-top: 0;
    }
    .card {
        padding: 22px;
        border-radius: 16px;
        border: 1px solid rgba(128,128,128,.2);
        margin-bottom: 18px;
    }
    .balance {
        font-size: 36px;
        font-weight: 800;
    }
</style>
""", unsafe_allow_html=True)


def login_form():
    st.sidebar.subheader("🔐 Secure Login")
    account = st.sidebar.text_input("Account Number")
    pin = st.sidebar.text_input("4-Digit PIN", type="password")

    if st.sidebar.button("Login", use_container_width=True):
        user = Bank.authenticate(account.strip(), pin)

        if user:
            st.session_state.logged_in = True
            st.session_state.account_no = account.strip()
            st.success("Login successful.")
            st.rerun()
        else:
            st.error("Invalid account number or PIN.")


def logout():
    st.session_state.logged_in = False
    st.session_state.account_no = None
    st.rerun()


st.sidebar.title("🏦 PRINCE BANK")
st.sidebar.caption("Secure • Simple • Professional")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "account_no" not in st.session_state:
    st.session_state.account_no = None


st.markdown('<p class="main-title">🏦 PRINCE BANK</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">Modern digital banking management system</p>',
    unsafe_allow_html=True
)

if not st.session_state.logged_in:
    login_form()

    tab1, tab2 = st.tabs(["Create Account", "About PRINCE BANK"])

    with tab1:
        st.header("Open a New Account")

        with st.form("create_account"):
            name = st.text_input("Full Name")
            age = st.number_input("Age", min_value=1, max_value=120, value=18)
            email = st.text_input("Email Address")
            pin = st.text_input("Create 4-Digit PIN", type="password")

            submitted = st.form_submit_button(
                "Create Account",
                use_container_width=True
            )

            if submitted:
                success, message, account = Bank.create_account(
                    name, int(age), email, pin
                )

                if success:
                    st.success(message)
                    st.info(
                        f"Your account number is **{account['accountNo']}**. "
                        "Please save it securely."
                    )
                else:
                    st.error(message)

    with tab2:
        st.header("Welcome to PRINCE BANK")
        st.write(
            "PRINCE BANK is a professional banking management project built "
            "with Python and Streamlit. It supports account creation, secure "
            "PIN authentication, deposits, withdrawals, profile updates, "
            "account details and account deletion."
        )

        col1, col2, col3 = st.columns(3)
        col1.metric("Security", "PIN Hashing")
        col2.metric("Storage", "JSON Database")
        col3.metric("Interface", "Streamlit")

else:
    account_no = st.session_state.account_no
    details = Bank.get_details(account_no, "")

    # Get the logged-in user without exposing the stored PIN.
    data = Bank._load_data()
    current_user = next(
        (u for u in data if u["accountNo"] == account_no), None
    )

    if not current_user:
        st.session_state.logged_in = False
        st.rerun()

    st.sidebar.success(f"Logged in as {current_user['name']}")
    if st.sidebar.button("Logout", use_container_width=True):
        logout()

    st.header(f"Welcome, {current_user['name']} 👋")

    col1, col2, col3 = st.columns(3)
    col1.metric("Account Number", current_user["accountNo"])
    col2.metric("Available Balance", f"₹{current_user['balance']:,.2f}")
    col3.metric("Account Status", "ACTIVE")

    st.divider()

    dashboard, deposit, withdraw, profile, delete = st.tabs(
        ["📊 Dashboard", "💰 Deposit", "💸 Withdraw", "👤 Profile", "⚠️ Delete"]
    )

    with dashboard:
        st.subheader("Account Overview")

        st.markdown(
            f"""
            <div class="card">
                <div>Current Balance</div>
                <div class="balance">₹{current_user['balance']:,.2f}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)
        with col1:
            st.write("**Account Holder**")
            st.write(current_user["name"])

            st.write("**Email**")
            st.write(current_user["email"])

        with col2:
            st.write("**Age**")
            st.write(current_user["age"])

            st.write("**Created On**")
            st.write(current_user.get("createdAt", "N/A"))

    with deposit:
        st.subheader("Deposit Money")

        with st.form("deposit_form"):
            pin = st.text_input("Enter PIN", type="password")
            amount = st.number_input(
                "Deposit Amount",
                min_value=1.0,
                max_value=10000.0,
                step=100.0
            )

            if st.form_submit_button("Deposit Money", use_container_width=True):
                success, message = Bank.deposit(
                    account_no, pin, float(amount)
                )

                if success:
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)

    with withdraw:
        st.subheader("Withdraw Money")

        with st.form("withdraw_form"):
            pin = st.text_input("Enter PIN", type="password")
            amount = st.number_input(
                "Withdrawal Amount",
                min_value=1.0,
                step=100.0
            )

            if st.form_submit_button("Withdraw Money", use_container_width=True):
                success, message = Bank.withdraw(
                    account_no, pin, float(amount)
                )

                if success:
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)

    with profile:
        st.subheader("Update Profile")

        with st.form("profile_form"):
            current_pin = st.text_input(
                "Current PIN",
                type="password"
            )
            new_name = st.text_input(
                "New Name",
                value=current_user["name"]
            )
            new_email = st.text_input(
                "New Email",
                value=current_user["email"]
            )
            new_pin = st.text_input(
                "New PIN (leave empty to keep current)",
                type="password"
            )

            if st.form_submit_button("Update Details", use_container_width=True):
                success, message = Bank.update_details(
                    account_no,
                    current_pin,
                    new_name,
                    new_email,
                    new_pin
                )

                if success:
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)

    with delete:
        st.subheader("Delete Account")
        st.warning(
            "Account deletion is permanent. Your balance must be ₹0 "
            "before the account can be deleted."
        )

        with st.form("delete_form"):
            pin = st.text_input("Enter PIN", type="password")
            confirmation = st.checkbox(
                "I understand that this action cannot be undone."
            )

            if st.form_submit_button("Delete Account", use_container_width=True):
                if not confirmation:
                    st.error("Please confirm account deletion.")
                else:
                    success, message = Bank.delete_account(
                        account_no, pin
                    )

                    if success:
                        st.success(message)
                        st.session_state.logged_in = False
                        st.session_state.account_no = None
                        st.rerun()
                    else:
                        st.error(message)
