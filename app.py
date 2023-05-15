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

st.sidebar.write('Collatz conjecture')

num_list = list(range(1, 100))
ini_numer = st.sidebar.selectbox('Select a number:', num_list)

l = generate_list(ini_numer)

st.line_chart(l)
