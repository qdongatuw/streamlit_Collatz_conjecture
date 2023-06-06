import streamlit as st


def calculation(x):
    if x % 2 == 0:
        return x/2
    return x * 3 + 1

def cacalculation_neg(x):
    if x % 2 == 0:
        return x/2
    return x * 3 - 1

def generate_list(n):
    l = []
    l.append(n)
    if abs(n)== 1:
        return l
    if n >= 0:
        while True:
            last = calculation(l[-1])
            l.append(last)
            if last == 1:
                return l
    else:
        while True:
            last = cacalculation_neg(l[-1])
            l.append(last)
            if last == -1:
                return l
    

st.set_page_config(page_title="Collatz conjecture")


st.sidebar.header('Hi Mason!')
st.title('Collatz conjecture')

ini_numer = st.sidebar.number_input('Input a number:', value=2048)
if abs(ini_numer) > 1000000000000:
    st.info('The number is just too big.')
    st.stop()
l = generate_list(round(ini_numer))

st.write(f'{ini_numer}: {len(l)} steps.')

st.line_chart(l)
st.dataframe(l, width=600)