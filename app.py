import streamlit as st
st.title("      Тест по География")

with st.form("quiz"):
    q1 = st.radio("1. Коя е най-голямата държава по площ?", ["Китай", "САЩ", "Русия", "Канада"])
    q2 = st.radio("2. Кой океан е най-голям?", ["Атлантически", "Индийски", "Северен ледовит", "Тихи"])
    q3 = st.radio("3. Кой е най-високият връх в света?", ["К2", "Еверест", "Килиманджаро", "Монблан"])
    q4 = st.text_input("4.Кой е най-големият континент по площ ?")
    q5 = st.text_input("5.Коя е най-дългата река в света ?")
    q6 = st.text_input("6. Коя държава има най-голямо население в света?")
    q7 = st.text_input("7.Кой е най-големият пустинен район в света?")
    q8 = st.text_input("8. Кой пролив разделя Европа от Азия при Истанбул?")
    q9 = st.text_input("9. Коя е столицата на Франция?")
    q10= st.number_input("10. Колко континента има на Земята?", min_value=0, step=1)
    
    submitted = st.form_submit_button("Провери")

if submitted:
    points = 0
    
    if q1 == "Русия": points += 1
    if q2 == "Тихи": points += 1
    if q3 == "Еверест": points += 1
    if q4 == "Азия": points += 1
    if q5 == "Нил": points += 1
    if q6 == "Индия": points += 1
    if q7 == "Сахара": points += 1
    if q8 == "Босфорът": points += 1
    if q9== "Париж": points += 1
    if q10 == 7: points += 1

    if points == 10:
        st.success(f"Отличен! Верни отговори: {points}/10")
    elif points >= 5:
        st.info(f"Добър резултат: {points}/10")
    else 
        st.error(f"Слаб: {points}/10")
      
