import streamlit as st

st.title("Welcome to the tip calculator!")

# min_value = 0.0 // Aceita valores tipo float
# min_value = 0 // Entende que os valores serão inteiros
total_bill = st.number_input("What was the total bill? $", min_value=0.0, format="%.2f")
tip = st.selectbox("How much tipp would you like to give? 10, 12, or 15?", [10, 12, 15])
# tip = st.number_input("How much tipp would you like to give? 10, 12, or 15?", min_value=0, step=1)
total_peoples = st.number_input("How many people to split the bill? ", min_value=1, step=1)

if st.button("Perform Calculation"):
    # if tip not in [10, 12, 15]:
    #     print("Error! Choose between 10, 12, or 15.")
    
    # else:
    #     total = total_bill + (total_bill * tip / 100)
    #     each_person = total / total_peoples
    #     st.success(f"Each person should pay: ${round(each_person, 2)}")
    total = total_bill + (total_bill * tip / 100)
    each_person = total / total_peoples
    st.success(f"Each person should pay: ${round(each_person, 2)}")
