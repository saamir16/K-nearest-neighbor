import streamlit as st


# Enter weight:
# select hieght format:
# radion btn: cms, inch, feet, meter
# selected input  box
# button: calculate BMI

# Your BMI idx is ...
# based upon BMI:  underweight, overweight, normal
#  cm: bmi  = weight /((height/100)**2)
#  meter: bmi  = weight /((height)**2)
#  ft: bmi  = weight /((height/3.28)**2)

# BMI <16 :extreme underweight
# 16<BMI<18.5 : underweight
# 18.5<BMI<25 : healthy
# 25<BMI<30: overweight
# BMI >30:Extremely overweight
bmi = None
weight = st.number_input("Enter your weight")
unit = st.radio("Select unit", ("cms","inch","feet","meter"))
height = st.number_input("Enter your height")
if st.button("Calculate BMI"):
    if height > 0: 
        if unit == "cms":
            bmi = weight / ((height / 100) ** 2)
        elif unit == "inch":
            bmi = weight / ((height * 0.0254) ** 2)  
        elif unit == "feet":
            bmi = weight / ((height / 3.28) ** 2)  
        elif unit == "meter":
            bmi = weight / (height ** 2)

        # Display BMI
        st.write(f"### Your BMI is: **{bmi:.2f}**")

        # BMI Classification
        if bmi < 16:
            st.error("You are **Extremely Underweight** 😞")
        elif 16 <= bmi < 18.5:
            st.warning("You are **Underweight** 🥦")
        elif 18.5 <= bmi < 25:
            st.success("You are **Healthy** 🎉")
        elif 25 <= bmi < 30:
            st.warning("You are **Overweight** ⚠️")
        else:
            st.error("You are **Extremely Overweight** 🚨")
    else:
        st.error("Please enter a valid height greater than 0!")