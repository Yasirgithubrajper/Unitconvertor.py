
import streamlit as st
 #title
st.title_Types("unit convertor")
 #unit conversion
 conversion_types = ["length","weight","temperature"]
 # user se conversion karwana/
  conversion_chioce =st.seclectbox.("choose conversion Types:,""conversion_types")
 #length conversion
 if conversion_chioce == "length":
    length_units =["Meters","Kilometers","Feet","Inches","Centimeters"]
    input_value =st.number_input("Enter Your Lenght Value:",main_value=0.0, Format ="%.2f")
    from_unit =st.seclectbox("From Unit:",length_units)
    to_unit =seclectbox("To Unit:",length_units)
    #conversion Dictionaries
    length_conversion={"Meters":1,
    "Kilometers":1000,
    "Feet":0.345,
    "Inches":0.034,
    "Centimeters":0.05,}
    #conversion Logic
    if st.button("convert"):
        result =input_value =(length_conversion[from_unit] / length_conversion[to_unit])
        st.success(f'{input_value} {from_unit} is equal to {result:.2f}, {to_unit}')
        
        #weight conversion
        elif conversion_chioce == "weight":
            weight_units=["Kilograms","Grams","Pounds","Ounces",]
            input_value =st.number_input("Enter your Weight value:",main_value =0.0,
            From = "%.2f")
            from_unit =st.seclectbox("from unit:", weight_units)
            to_unit =seclectbox("To unit:",weight_units)
            #conversion Dictionnaries
            weight_conversion={"Kilograms":1,
    "Grams":0.001,
    "Pounds":0.45355,
    "Ounces":0.02834,
    }
    #conversion logic
    if st.button("convert"):
        result =input_value =(weight_conversion[from_unit] / weight_conversion[to_unit])
        st.success(f'{input_value}{from_unit} is equal to {result:.2f}{to_unit}')

        #temperature conversion
        elif conversion_chioce =="Temperature":
            temperature_units=["Celsius","Fahrenhit","Kelvin",]
            input_value =st.number_input("Enter your Temperature value:",main_value =0.0,
            From = "%.2f")
            from_unit =st.seclectbox("from unit:", temperature_units)
            to_unit =seclectbox("To unit:",temperature_units)
            def convert_temperature(value,from_unit == "Celsius"):
                if from_unit == "Celsius":
                    if to_unit=="Fahrenhit":
                        return(value * 9/5) + 32
                    elif to_unit == "Kelvin":
                        return value + 273
                elif from_unit == "Fahrenhit":
                    if to_unit == "Celsius":
                        return (value - 32) * 5/9
                elif to_unit == "Kelvin":
                    return(value-32)* 5/9 +273
            elif from_unit == "Kelvin":
                if to_unit == "Celsius":
                    return value -273
                elif to_unit == "Fahrenhit":
                    return (value -273) * 9/5 + 32
                return value
            if st.button("convert"):
                result = convert_temperature(input_value, from_unit, to_unit)
                st.success(f'{input_value:.2f} {from_unit} is equal to {result:.2f} {to_unit}')
        


