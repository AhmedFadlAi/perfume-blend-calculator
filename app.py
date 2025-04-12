import streamlit as st
from PIL import Image

st.set_page_config(page_title="Nashiq - حاسبة العطور", page_icon="🌿")

# اللوجو
logo = Image.open("ChatGPT Image 12 أبريل 2025، 09_47_47 م")
st.image(logo, use_column_width=True)

# العنوان الأساسي
st.markdown("""
    <h1 style='text-align: center; color: #d4af37; font-family:serif;'>Nashiq</h1>
    <h3 style='text-align: center; color: #ffffff;'>حاسبة تركيبة عطر فخم ومنعش</h3>
    <hr style='border: 1px solid #d4af37;'>
""", unsafe_allow_html=True)

# خلفية داكنة
st.markdown("""
    <style>
        body {
            background-color: #1c1c1c;
            color: white;
        }
        .stSlider > div > div {
            color: #d4af37 !important;
        }
    </style>
""", unsafe_allow_html=True)

# مدخلات المستخدم
total_volume_ml = st.number_input("🧪 أدخل الحجم الكلي للعطر (بالمليليتر):", min_value=10, max_value=500, value=100)
concentration_percent = st.slider("💧 اختر نسبة تركيز الزيوت العطرية (%):", 5, 30, 20)

# المكونات الأساسية
ingredients = {
    "برغموت": 6,
    "ماندرين أخضر": 5,
    "زنجبيل": 4,
    "نعناع": 2,
    "كحول عطري": 8,
    "لافندر": 10,
    "قرفة": 6,
    "عسل أبيض": 7,
    "جوزة الطيب": 2,
    "ياسمين": 2,
    "Iso E Super": 8,
    "خشب الصندل": 10,
    "فول التونكا": 10,
    "مسك أبيض": 5,
    "فانيلا": 3,
    "Ambroxan": 7,
    "مثبت إضافي": 5
}

# الحساب
oil_volume_ml = (concentration_percent / 100) * total_volume_ml
alcohol_volume = round(total_volume_ml - oil_volume_ml, 2)

st.subheader("تفصيل المكونات:")

for name, percent in ingredients.items():
    amount_ml = round((percent / 100) * oil_volume_ml, 2)
    st.markdown(f"<div style='color:#d4af37;'>- {name}: {percent}% = <strong>{amount_ml} مل</strong></div>", unsafe_allow_html=True)

st.markdown(f"""
    <br>
    <div style='background-color:#333;padding:15px;border-radius:10px;'>
        <h4 style='color:#d4af37;'>الكحول المطلوب:</h4>
        <p style='color:white;font-size:18px;'><strong>{alcohol_volume} مل</strong></p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <br>
    <hr style='border: 1px solid #d4af37;'>
    <p style='text-align:center;color:gray;'>هذا العطر تم تطويره بواسطة <strong>أحمد فاضل</strong> – مشروع Nashiq 💎</p>
""", unsafe_allow_html=True)
