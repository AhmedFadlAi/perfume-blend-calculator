
import streamlit as st

st.set_page_config(page_title="حاسبة تركيبة العطر", page_icon="🌿")
st.title("حاسبة تركيبة عطر أحمد")

st.markdown("""
أدخل حجم العطر اللي عايز تحضره ونسبة تركيز الزيوت العطرية، وهتشوف الكميات المطلوبة لكل مكون.
""")

# مدخلات المستخدم
total_volume_ml = st.number_input("أدخل الحجم الكلي للعطر (بالمليليتر):", min_value=10, max_value=500, value=100)
concentration_percent = st.slider("اختر نسبة تركيز الزيوت العطرية (%):", 5, 30, 20)

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
    st.write(f"- {name}: {percent}% = {amount_ml} مل")

st.markdown(f"""
### الكحول المطلوب:
**{alcohol_volume} مل**
""")
