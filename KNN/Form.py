import streamlit as st

def main():
    st.title("User Information Form")
    
    with st.form("user_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        age = st.number_input("Age", min_value=0, step=1)
        feedback = st.text_area("Feedback")
        
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            st.success(f"Thank you, {name}! Your response has been recorded.")

if __name__ == "__main__":
    main()
