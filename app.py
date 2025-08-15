import streamlit as st
from hello import Bank

st.set_page_config(page_title="SuvRams Bank", layout="wide")
st.title("🏦 SuvRams Bank")
st.caption("Your Trusted Digital Banking Partner")
menu = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Create Account", "Deposit", "Withdraw", "Show Details", "Update Info", "Delete Account"]
)


if menu == "Dashboard":
    st.subheader("📊 Bank Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Customers", "124")
    col2.metric("Total Balance", "₹8,40,000")
    col3.metric("Transactions Today", "56")

    st.info("💡 Tip: Use your Account Number & PIN for all operations. Keep your PIN secure.")


elif menu == "Create Account":
    st.subheader("📄 Create New Account")
    name = st.text_input("Your Name")
    age = st.number_input("Your Age", min_value=0, step=1)
    email = st.text_input("Your Email")
    pin = st.text_input("4-digit PIN", type="password")
    
    if st.button("Create Account", use_container_width=True):
        if name and email and pin:
            user, msg = Bank.create_account(name, int(age), email, int(pin))
            st.success(msg)
            st.balloons()
            if user:
                st.subheader("✅ Account Created")
                col1, col2 = st.columns(2)
                col1.metric("Name", user["name"])
                col1.metric("Age", user["age"])
                col2.metric("Email", user["email"])
                col2.metric("Account Number", user["accountNo."])
        else:
            st.warning("⚠ Please fill all fields")
elif menu == "Deposit":
    st.subheader("💰 Deposit Money")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)
    
    if st.button("Deposit", use_container_width=True):
        success, msg = Bank.deposit(acc_no, int(pin), int(amount))
        if success:
            st.success(msg)
            st.snow()
        else:
            st.error(msg)


elif menu == "Withdraw":
    st.subheader("💸 Withdraw Money")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)
    
    if st.button("Withdraw", use_container_width=True):
        success, msg = Bank.withdraw(acc_no, int(pin), int(amount))
        if success:
            st.success(msg)
            st.snow()
        else:
            st.error(msg)


elif menu == "Show Details":
    st.subheader("📂 Account Details")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show Details", use_container_width=True):
        user = Bank.find_user(acc_no, int(pin))
        if user:
            st.subheader("💳 Account Information")
            st.write(f"**Name:** {user['name']}")
            st.write(f"**Age:** {user['age']}")
            st.write(f"**Email:** {user['email']}")
            st.write(f"**Balance:** ₹{user['balance']}")
            st.write(f"**Account Number:** {user['accountNo.']}")
        else:
            st.error("❌ No account found")


elif menu == "Update Info":
    st.subheader("✏ Update Your Info")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")
    
    name = st.text_input("New Name (Optional)")
    email = st.text_input("New Email (Optional)")
    new_pin = st.text_input("New PIN (Optional)")

    if st.button("Update Info", use_container_width=True):
        success, msg = Bank.update_user(acc_no, int(pin), name, email, new_pin)
        st.success(msg) if success else st.error(msg)


elif menu == "Delete Account":
    st.subheader("🗑 Delete Account")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete Account", use_container_width=True):
        success, msg = Bank.delete_user(acc_no, int(pin))
        st.success(msg) if success else st.error(msg)
