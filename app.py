import streamlit as st
st.title("      Тест по География")

with st.form("quiz"):
    q1 = st.radio("1. Коя е най-голямата държава по площ?", ["Китай", "САЩ", "Русия", "Канада"])
    q2 = st.radio("2. Кой океан е най-голям?", ["Атлантически", "Индийски", "Северен ледовит", "Тихи"])
    q3 = st.radio("3. Кой е най-високият връх в света?", ["К2", "Еверест", "Килиманджаро", "Монблан"])
    q4 = st.text_input("4. Коя е столицата на Франция?")
    q5 = st.number_input("5. Колко континента има на Земята?", min_value=0, step=1)
    
    submitted = st.form_submit_button("Провери")

if submitted:
    points = 0
    
    if q1 == "Русия": points += 1
    if q2 == "Тихи": points += 1
    if q3 == "Еверест": points += 1
    if q4.strip().lower() in ["париж", "paris"]: points += 1
    if q5 == 7: points += 1

    if points == 5:
        st.success(f"Отличен! Верни отговори: {points}/5")
    elif points >= 3:
        st.info(f"Добър резултат: {points}/5")
    else:
        st.error(f"Опитай пак: {points}/5")
      
