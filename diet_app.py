import pandas as pd
import streamlit as st

def get_diet_recommendation(age_group, gender, activity_level):
    data = {
        "年齡": [
            "1-3", "1-3", "1-3", "1-3", "4-6", "4-6", "4-6", "4-6",
            "7-8", "7-8", "7-8", "7-8", "9-12", "9-12", "9-12", "9-12",
            "13-15", "13-15", "13-15", "13-15", "16-18", "16-18", "16-18", "16-18"
        ],
        "性別": ["男", "男", "女", "女", "男", "男", "女", "女", "男", "男", "女", "女", "男", "男", "女", "女", "男", "男", "女", "女", "男", "男", "女", "女"],
        "活動強度": ["稍低", "適度", "稍低", "適度", "稍低", "適度", "稍低", "適度", "稍低", "適度", "稍低", "適度",
                    "稍低", "適度", "稍低", "適度", "稍低", "適度", "稍低", "適度", "稍低", "適度", "稍低", "適度"],
        "熱量 (大卡)": [1150, 1350, 1150, 1350, 1550, 1800, 1400, 1650, 1800, 2100, 1650, 1900, 2050,
                      2350, 1950, 2250, 2400, 2800, 2050, 2350, 2500, 2900, 1900, 2250],
        "全榖雜糧類 (碗)": [1.5, 2, 1.5, 2, 2.5, 3, 2, 3, 3, 3.5, 2.5, 3, 3, 4, 3, 3.5, 4, 4.5, 3, 4, 4, 4.5, 3, 3.5],
        "豆魚蛋肉類 (份)": [2, 3, 2, 3, 3, 4, 3, 3, 5, 6, 4, 5.5, 6, 6, 6, 6, 6, 8, 6, 6, 7, 9, 5.5, 6],
        "乳品類 (杯)": [2, 2, 2, 2, 2, 2, 2, 2, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 2, 1.5, 1.5, 1.5, 2, 1.5, 1.5],
        "蔬菜類 (份)": [2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 3, 3, 4, 4, 3, 4, 5, 5, 4, 4, 5, 5, 3, 4],
        "水果類 (份)": [2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 3, 3, 4, 3, 3.5, 4, 4, 3, 4, 4, 4, 3, 3.5],
        "油脂與堅果種子類 (份)": [4, 4, 4, 4, 4, 5, 4, 4, 5, 6, 5, 5, 6, 6, 5, 6, 7, 8, 6, 6, 7, 8, 5, 6]
    }
    df = pd.DataFrame(data)
    result = df[(df["年齡"] == age_group) & (df["性別"] == gender) & (df["活動強度"] == activity_level)]
    
    if result.empty:
        return "查無對應的飲食建議，請確認輸入條件是否正確。"
    else:
        return result.to_dict(orient='records')[0]

# 建立 Streamlit 應用
st.title("兒童與青少年每日飲食建議量查詢")

age_group = st.selectbox("請選擇年齡範圍:", ["1-3", "4-6", "7-8", "9-12", "13-15", "16-18"])
gender = st.radio("請選擇性別:", ["男", "女"])
activity_level = st.selectbox("請選擇活動強度:", ["稍低", "適度"])

if st.button("查詢飲食建議"):
    recommendation = get_diet_recommendation(age_group, gender, activity_level)
    if isinstance(recommendation, str):
        st.write(recommendation)
    else:
        st.write("### 每日飲食建議量")
        for key, value in recommendation.items():
            st.write(f"**{key}**: {value}")
