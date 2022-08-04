import streamlit as st

view = [300,200,100,500,600]

show_raw=st.checkbox('show raw data')
if show_raw ==True:
    st.write('# raw data')
    view

show_raw
st.write('# raw data')
st.write('# table')
st.table(view)
st.write('# bar graph')
st.bar_chart(view)
