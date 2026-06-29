# pages/06_ 📝_單元10-5：會考模擬賽.py
import streamlit as st

# ==========================================
# 1. 網頁全域設定
# ==========================================
st.set_page_config(page_title="單元10-5：會考模擬賽", layout="wide")

# 初始化答題索引與紀錄（確保多頁面切換時不互相衝突）
if 'quiz_idx' not in st.session_state:
    st.session_state.quiz_idx = 0
if 'mock_answered_list' not in st.session_state:
    st.session_state.mock_answered_list = {}

st.header("🏆 單元 10-5：乘法公式與多項式實戰模擬特訓場")
st.markdown("##### 💡 這裡彙整了講義與歷屆會考最經典的 5 大代表題型。請在下方輸入答案，系統會即時幫你批改並給予詳細解析！")
st.markdown("---")

# ==========================================
# 2. 題庫資料庫定義
# ==========================================
questions = [
    {
        "id": 1,
        "type": "填空題",
        "title": "【會考減C必備】利用乘法公式計算 $306 \\times 294$ 的值為何？",
        "hint": "提示：將兩數看成對稱中心的加減：(300 + 6)(300 - 6)，利用平方差公式展開。",
        "correct_ans": 89964,
        "solution": r"$$306 \times 294 = (300+6)(300-6) = 300^2 - 6^2 = 90000 - 36 = \mathbf{89964}$$"
    },
    {
        "id": 2,
        "type": "填空題",
        "title": "【會考達B穩固】若 $a-b=5$，$ab=6$，則 $a^2+b^2$ 的值為何？",
        "hint": "提示：利用差的平方公式變形：a² + b² = (a - b)² + 2ab。",
        "correct_ans": 37,
        "solution": r"$$a^2+b^2 = (a-b)^2 + 2ab = 5^2 + 2(6) = 25 + 12 = \mathbf{37}$$"
    },
    {
        "id": 3,
        "type": "填空題",
        "title": "【邁向 A++ 特訓】展開多項式 $(2x-3)^2 - (3x+4)(3x-4)$ 後，其常數項的值為何？",
        "hint": "提示：(2x-3)² 的常數項是 +9；(3x+4)(3x-4) 的常數項是 -16。注意中間是「減法」與負負得正！",
        "correct_ans": 25,
        "solution": r"展開式為 $(4x^2 - 12x + 9) - (9x^2 - 16) = 4x^2 - 12x + 9 - 9x^2 + 16 = -5x^2 - 12x + 25$。因此常數項為 $\mathbf{25}$。"
    },
    {
        "id": 4,
        "type": "填空題",
        "title": "【幾何素養題】有一長方形紙片，長為 47，寬為 20。若在內部挖去一個底為 14、高為 7 的三角形，則剩餘的紙片面積為何？",
        "hint": "提示：剩餘面積 = 長方形總面積 - 三角形面積。三角形面積公式為 (底×高)/2。",
        "correct_ans": 891,
        "solution": r"長方形面積 = $47 \times 20 = 940$。三角形面積 = $\frac{14 \times 7}{2} = 49$。剩餘面積 = $940 - 49 = \mathbf{891}$。"
    },
    {
        "id": 5,
        "type": "填空題",
        "title": "【歷屆試題精選】求多項式 $6x^2 + 4x$ 除以 $2x^2$ 後，所得的「餘式」為何？",
        "hint": "提示：注意是除以 2x²。因為被除式的一次項 4x 的次數（1次）已經小於除式的次數（2次），所以 4x 無法再被除，直接變成餘式。",
        "correct_ans": "4x",
        "solution": r"利用多項式除法原理：$6x^2 + 4x = 3 \times (2x^2) + 4x$。因為餘式 $4x$ 的次數為 1，小於除式的次數 2，故商式為 3，餘式為 $\mathbf{4x}$。"
    }
]

# ==========================================
# 3. 畫面與邏輯渲染
# ==========================================
q = questions[st.session_state.quiz_idx]

st.subheader(f"📝 挑戰第 {st.session_state.quiz_idx + 1} 題 / 共 {len(questions)} 題")
st.markdown(f"### {q['title']}")
st.caption(f"📌 題型分類：{q['type']}")

# 思考提示摺疊面板
with st.expander("🔍 顯示解題思考關鍵提示"):
    st.info(q['hint'])

# 根據答案型態給予輸入框
if isinstance(q['correct_ans'], int):
    user_input = st.number_input("請在下方輸入你的計算答案（整數）：", step=1, value=0, key=f"mock_q_{q['id']}")
else:
    user_input = st.text_input("請在下方輸入你的計算答案（包含未知數如 4x）：", key=f"mock_q_{q['id']}").strip().lower()

# 提交答案與即時批改邏輯
if st.button("🚀 提交本題答案並檢查"):
    cleaned_input = str(user_input).replace(" ", "")
    cleaned_correct = str(q['correct_ans']).replace(" ", "")

    if cleaned_input == cleaned_correct:
        st.balloons()
        st.success("🎉 太厲害了！完全正確！你成功看穿了這個會考考題陷阱！")
        st.session_state.mock_answered_list[st.session_state.quiz_idx] = True
    else:
        st.error("❌ 喔不！計算有一點小失誤，或者符號漏掉了。再仔細看一次提示挑戰看看！")
        st.session_state.mock_answered_list[st.session_state.quiz_idx] = False

    # 顯示詳細解析
    st.markdown("#### 📘 本題完整正向思考解析：")
    st.success(q['solution'])

# 切換題目導覽按鈕
st.markdown("---")
cb1, cb2 = st.columns(2)
with cb1:
    if st.button("⬅️ 上一題") and st.session_state.quiz_idx > 0:
        st.session_state.quiz_idx -= 1
        st.rerun()
with cb2:
    if st.button("下一題 ➡️") and st.session_state.quiz_idx < len(questions) - 1:
        st.session_state.quiz_idx += 1
        st.rerun()

# 成就結算進度條
st.markdown("---")
correct_count = sum(1 for v in st.session_state.mock_answered_list.values() if v)
st.write(f"📈 當前實戰賽進度：已答對 {correct_count} / {len(questions)} 題")
st.progress(correct_count / len(questions))

# 側邊欄腳註
st.sidebar.markdown("### 🏰 闕老師的數學進化基地")
st.sidebar.caption("單元 10-5 副本：會考模擬賽")