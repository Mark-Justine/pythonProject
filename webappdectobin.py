import streamlit as st
import dectobin as db
import bintodec as bd

st.markdown("<h1 style='text-align: center;'>Decimal To Binary Converter</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: red;'>Vice Versa</h2>", unsafe_allow_html=True)
st.subheader('By: :blue[_Mark Justine B. Cabales_]')

print(st.session_state)

option = st.selectbox(
    'What kind of conversion do you want to perform?',
    ('Binary To Decimal', 'Decimal To Binary'))
st.write('Converting:', option)
if option == 'Binary To Decimal':
    binary = st.text_input("Please enter a Binary Number:")
    con_button = st.button("Convert", key = "con_bun")

    if con_button:
        result = ""
        try:
            bin_num = str(binary)
            result = bd.binary_to_decimal(bin_num)
            if result == None:
                result = 'Error, please input a valid binary number.'
        except ValueError:
            result = 'Error, please input a valid binary number.'

        st.subheader(f'Result: :blue[{result}]')

elif option == 'Decimal To Binary':
    num = st.text_input("Please enter a Decimal Integer Number:" )
    con_button = st.button("Convert", key="con_bun")

    if con_button:
        result = ""
        try:
            dec_num = int(num)
            result = db.decimal_to_binary(dec_num)
        except ValueError:
            result = 'Error, please input a valid decimal integer number.'

        st.subheader(f'Result: :blue[{result}]')

