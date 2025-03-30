import streamlit as st

#set title
st.title("Loan Qualifier Assistant")

#configure page settings
income = st.number_input("Annual Income (USD)", min_value=0, step=1000)
credit_score = st.number_input("Credit Score (300-850)", min_value=300, max_value=850)
debt_ratio = st.number_input("Debt Ratio (%)", min_value=0.0, max_value=100.0, step=0.1)

#check Eligibility
if st.button("Check Eligibility"):
 #rule1:Credit score must be at least 600
    if credit_score < 600:
        st.error("NO  Not eligible: Credit score must be at least 600.")
 #rule2:Debt ratio exceeds 40%
    elif debt_ratio > 40:
        st.error("NO Not eligible: Debt ratio exceeds 40%.")
   #rule3:Minimum annual income is $20,000
    elif income < 20000:
        st.error("NO Not eligible: Minimum annual income is $20,000.")
    #all rules pass
    else:
        st.success("YES Congratulations! You qualify for the loan!")
        st.balloons()  