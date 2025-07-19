import json
import streamlit as st

def role_editor():
    st.subheader("🔐 Role & Access Manager")
    
    with open("./data/user_roles.json", "r") as f:
        roles = json.load(f)

    editable_roles = {}
    for email, data in roles.items():
        col1, col2 = st.columns([3, 2])
        with col1:
            st.text(email)
        with col2:
            roles = ["admin", "coach", "athlete", "guest"] 
            current_role = data.get("role", "guest")
            default_index = roles.index(current_role) if current_role in roles else roles.index("guest")

new_role = st.selectbox("Role", roles, index=default_index, key=email)
= st.selectbox("Role", ["admin", "coach", "athlete", "guest"], index=["admin", "coach", "athlete", "guest"].index(data["role"]), key=email)
            editable_roles[email] = new_role

    if st.button("💾 Save Role Changes"):
        for email, new_role in editable_roles.items():
            roles[email]["role"] = new_role
        with open("./data/user_roles.json", "w") as f:
            json.dump(roles, f, indent=4)
        st.success("Roles updated successfully.")
