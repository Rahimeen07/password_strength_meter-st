import streamlit as st
import re

def check_password_strength(password):
    """Check the strength of the password and return reasons for weakness."""
    reasons = []
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    if length < 8:
        reasons.append("Password is too short (minimum 8 characters).")
    if not has_upper:
        reasons.append("Password should contain at least one uppercase letter.")
    if not has_lower:
        reasons.append("Password should contain at least one lowercase letter.")
    if not has_digit:
        reasons.append("Password should contain at least one digit.")
    if not has_special:
        reasons.append("Password should contain at least one special character (e.g., @, #, $, etc.).")

    if len(reasons) == 0:
        return "Strong", []
    elif length < 10:
        return "Weak", reasons
    elif has_upper and has_lower and has_digit and has_special:
        return "Very Strong", []
    elif (has_upper and has_lower and has_digit) or (has_upper and has_lower and has_special):
        return "Medium", []
    else:
        return "Weak", reasons

# Streamlit application
st.title("Password Strength Meter")

password = st.text_input("Enter Password", type="password")

if st.button("Check Strength"):
    strength, reasons = check_password_strength(password)
    st.write(f"Password Strength: **{strength}**")

    if reasons:
        st.write("Reasons for Weakness:")
        for reason in reasons:
            st.write(f"- {reason}")
    else:
        st.write("Your password meets all the strength requirements!")

st.write("### Password Requirements:")
st.write("- At least 8 characters long")
st.write("- At least one uppercase letter")
st.write("- At least one lowercase letter")
st.write("- At least one digit")
st.write("- At least one special character (e.g., @, #, $, etc.)")