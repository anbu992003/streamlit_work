import streamlit as st
import time


st.write("Hello ,let's learn how to build a streamlit app together")


st.title ("this is the app title")


st.header("this is the header")


st.markdown("this is the markdown")


st.subheader("this is the subheader")


st.caption("this is the caption")


st.code("x=2021")


st.latex(r''' a+a r^1+a r^2+a r^3 ''')




st.success("You did it !")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))



st.title('LOAN PREDICTION :')      
st.image('loan_image.jpg')    
st.markdown('Dataset :')    
data=pd.read_csv('loan_dataset.csv')    
st.write(data.head())    
st.markdown('Applicant Income VS Loan Amount ')    
st.bar_chart(data[['ApplicantIncome','LoanAmount']].head(20))

