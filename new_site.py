import streamlit as st
from PIL import Image
st.title("WELCOME TO NYLA PERUVIAN RESTAURANT APP")
st.subheader("Make your order here")


st.write("See our menu")
st.selectbox("Menu", ["Peruvian Primer", "Ceviche", "Papas a la Huancaina", "Lomo Saltado", "Cuy", "Rocoto Relleno"])
st.text_area("Address")
st.number_input("Phone number", 0, 11)
st.number_input("number of orders", step=1)
st.sidebar.radio("Menu", ["Peruvian Primer", "Ceviche", "Papas a la Huancaina", "Lomo Saltado", "Cuy", "Rocoto Relleno"])
st.sidebar.selectbox("Mode of payment",["Paypal", "Visa", "Mastercard", "Verve"])
st.date_input("date you wish the food to be delivered")
st.warning("There will be no refunds for orders made under good condition. payments validates order and order cancellations are not allowed")
st.file_uploader("upload a file", type=["png", "jpg"])
img = Image.open("peruvian food.jpg")
st.sidebar.image(img, caption="your satisfaction, our concern")