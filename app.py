import streamlit as st
from data_loader import get_currency_rates

st.title("Конвертер валют")

try:
    rates = get_currency_rates()
    currencies = list(rates.keys())
    amount = st.number_input("Введите сумму:", min_value=0.0, value=100.0)
    from_cur = st.selectbox("Из валюты:", currencies)
    to_cur = st.selectbox("В валюту:", currencies)

    if st.button("Конвертировать"):
        amount_in_rub = amount * rates[from_cur]["value"] / rates[from_cur]["nominal"]
        result = amount_in_rub * rates[to_cur]["nominal"] / rates[to_cur]["value"]
        st.success(f"{amount} {from_cur} = {result:.2f} {to_cur}")

except Exception as e:
    st.error(f"Ошибка загрузки или обработки данных: {e}")
