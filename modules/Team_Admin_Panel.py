import json
import streamlit as st

def role_editor():
    st.subheader("🔐 Role & Access Manager")

    # Load user roles from file
    with open("./data/user_roles.json", "r") as f:
        user_roles = json.load(f)

    editable_roles = {}
    for email, data in user_roles.items():
        col1, col2 = st.columns([3, 2])
        with col1:
            st.text(email)
        with col2:
            role_options = ["admin", "coach", "athlete", "guest"]
            current_role = data.get("role", "guest")
            default_index = role_options.index(current_role) if current_role in role_options else role_options.index("guest")

            new_role = st.selectbox(
                "Role", 
                role_options, 
                index=default_index, 
                key=email
            )
            editable_roles[email] = new_role

    if st.button("💾 Save Role Changes"):
        for email, new_role in editable_roles.items():
            user_roles[email]["role"] = new_role
        with open("./data/user_roles.json", "w") as f:
            json.dump(user_roles, f, indent=4)
        st.success("Roles updated successfully.")
