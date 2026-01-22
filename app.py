import streamlit as st

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b


st.title(" Calculator Application")
st.write("This is a basic calculator built using Python and Streamlit")


num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)


operation = st.selectbox(
    "Select Operation",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

if operation == "Addition":
    result = add(num1, num2)

elif operation == "Subtraction":
    result = subtract(num1, num2)

elif operation == "Multiplication":
    result = multiply(num1, num2)

elif operation == "Division":
    result = divide(num1, num2)


st.subheader("Result:")
st.write(result)
