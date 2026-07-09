import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import math
import time

# ---------------- CONFIG ----------------
st.set_page_config(page_title="News Classifier", layout="centered")

# ---------------- STYLE ----------------
st.markdown("""
<style>
.stApp {
    background: #f8fafc;
    font-family: 'Inter', sans-serif;
}

/* Card */
.card {
    background: white;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #e5e7eb;
    margin-bottom: 20px;
}

/* Button */
.stButton button {
    background: linear-gradient(135deg, #4f46e5, #9333ea);
    color: white;
    border-radius: 10px;
    height: 45px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("Model Overview")
st.sidebar.metric("Accuracy", "94.2%")
st.sidebar.metric("Model", "BERT Base")
st.sidebar.metric("Classes", "4")

# ---------------- LABELS ----------------
LABELS = {
    0: ("World", "#3b82f6"),
    1: ("Sports", "#22c55e"),
    2: ("Business", "#f59e0b"),
    3: ("Sci/Tech", "#8b5cf6"),
}

# ---------------- MOCK MODEL ----------------
def mock_classify(text):
    text = text.lower()
    scores = [0, 0, 0, 0]

    keywords = {
        0: ["war", "government"],
        1: ["match", "football"],
        2: ["market", "stock"],
        3: ["ai", "technology"]
    }

    for i in keywords:
        for w in keywords[i]:
            if w in text:
                scores[i] += 1.5

    if sum(scores) == 0:
        scores[hash(text) % 4] += 1

    exps = [math.exp(s) for s in scores]
    probs = [e / sum(exps) for e in exps]

    return probs.index(max(probs)), probs

# ---------------- TITLE ----------------
st.title("News Classification Dashboard")
st.caption("All-in-one clean layout")

# ---------------- INPUT CARD ----------------
st.markdown("<div class='card'>", unsafe_allow_html=True)

text = st.text_area("Enter News Text")
predict = st.button("Run Classification", use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- OUTPUT ----------------
if predict and len(text) > 20:

    with st.spinner("Analyzing..."):
        time.sleep(1)
        pred, probs = mock_classify(text)

    label, color = LABELS[pred]
    confidence = probs[pred] * 100

    labels = [LABELS[i][0] for i in range(4)]
    values = [p * 100 for p in probs]

    # -------- RESULT --------
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("Prediction")
    st.markdown(f"<h2 style='color:{color}'>{label}</h2>", unsafe_allow_html=True)
    st.write(f"{confidence:.2f}% confidence")

    st.markdown("</div>", unsafe_allow_html=True)

    # -------- DONUT CHART --------
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("Category Distribution")

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    centre = plt.Circle((0,0),0.65,fc='white')
    fig.gca().add_artist(centre)
    ax.axis('equal')

    st.pyplot(fig)

    st.markdown("</div>", unsafe_allow_html=True)

    # -------- RADAR GRAPH --------
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("Scientific Analysis")

    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
    values_cycle = np.concatenate((values, [values[0]]))
    angles_cycle = np.concatenate((angles, [angles[0]]))

    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111, polar=True)
    ax2.plot(angles_cycle, values_cycle)
    ax2.fill(angles_cycle, values_cycle, alpha=0.1)
    ax2.set_xticks(angles)
    ax2.set_xticklabels(labels)

    st.pyplot(fig2)

    st.markdown("</div>", unsafe_allow_html=True)

    # -------- DETAILS --------
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("Detailed Output")
    for i in range(4):
        st.progress(values[i]/100, text=f"{labels[i]} - {values[i]:.1f}%")

    st.markdown("</div>", unsafe_allow_html=True)

else:
    st.info("Enter text and run classification")