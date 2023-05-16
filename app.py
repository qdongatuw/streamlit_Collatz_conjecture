import streamlit as st


def calculation(x):
    if x % 2 == 0:
        return x/2
    return x * 3 + 1

def generate_list(n):
    l = []
    l.append(n)
    if n == 1:
        return l
    while True:
        last = calculation(l[-1])
        l.append(last)
        if last == 1:
            break
    return l

st.sidebar.write('Hi Mason!')
st.write('<h1 style="font-size: 24px; font-family: Arial;">Collatz conjecture</h1>', unsafe_allow_html=True)

st.sidebar.text_input('Input a number:', ini_numer)

l = generate_list(int(ini_numer))

st.write(f'{ini_numer}: {len(l)} steps.')

st.line_chart(l)
st.dataframe(l)