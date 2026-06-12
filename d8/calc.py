import streamlit as st

st.title("Simple Calculator")

st.write("Enter your Choice :")
st.write("1> Addition")
st.write("2> Subtraction")
st.write("3> Multiplication")
st.write("4> Division")

opp = st.number_input("Enter Choice :")

num1 = st.number_input("Enter 1st number :")
num2 = st.number_input("Enter 2nd number :")

if st.button("Submit"):
    if opp == 1:
        st.write("Result is ", num1 + num2)
    elif opp == 2:
        st.write("Result is ", num1 - num2)
    elif opp == 3:
        st.write("Result is ", num1 * num2)
    elif opp == 4:
        if num2 != 0:
            st.write("Result is ", num1 / num2)
        else:
            st.error("Not divided by zero")
    else:
        st.error("Invalid choice")
st.balloons()
    
