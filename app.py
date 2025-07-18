import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json
import google.generativeai as genai

# --- Configure Gemini API ---
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# --- Load Lottie animation ---
def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_career = load_lottie_file("assets/ready-for-career.json")

# --- Gemini AI Function ---
def generate_gemini_roadmap(experience, domain, goal):
    prompt = f"""
    I have {experience} years of experience in {domain}, and I want to become a {goal}.

    Create a career roadmap with:
    - Step-by-step guidance
    - Recommended tools, courses (free/paid)
    - Projects to build
    - Estimated time for each stage
    - Job titles to aim for
    """
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error: {e}"

# --- Streamlit Config ---
st.set_page_config(page_title="AIspire Roadmaps", page_icon="🎯", layout="centered")

# --- Hide Streamlit UI ---
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- Hover Header & Tags ---
st.markdown("""
<style>
.hover-box {
    text-align: center;
    margin-top: 10px;
    margin-bottom: 25px;
}

.hover-heading {
    font-size: 40px;
    font-weight: bold;
    color: #ffffff;
    padding: 20px;
    border-radius: 12px;
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    display: inline-block;
    transition: 0.3s;
}

.tag-container {
    display: none;
    margin-top: 10px;
}

.tag {
    display: block;
    background: #ff6a00;
    color: white;
    padding: 8px 20px;
    margin: 5px auto;
    border-radius: 20px;
    width: fit-content;
    text-align: center;
    transition: 0.3s;
    font-size: 18px;
    font-weight: 500;
    font-family: 'Inter', sans-serif;
}

.hover-box:hover .tag-container {
    display: block;
}
</style>

<div class="hover-box">
  <div class="hover-heading">🎯 AIspire Roadmaps</div>
  <div class="tag-container">
    <div class="tag">Data Science & Analytics</div>
    <div class="tag">Software Development</div>
    <div class="tag">Digital Marketing</div>
    <div class="tag">Banking & Finance</div>
    <div class="tag">Cybersecurity</div>
  </div>
</div>
""", unsafe_allow_html=True)

# --- Fading Subtitle ---
st.markdown("""
    <style>
    .fade-text {
        text-align: center;
        font-family: 'Roboto';
        font-size: 18px;
        margin-top: 15px;
        color: #cccccc;
    }
    </style>
    <div class="fade-text">From Vision to Victory — Let AI Lead the Way.</div>
""", unsafe_allow_html=True)

# --- Lottie Animation ---
with st.container():
    st_lottie(lottie_career, height=280, key="career-animation")

# --- Manual Roadmap Section ---
st.markdown("""
<div style='text-align: center; font-size: 34px; font-weight: bold; margin-top: 10px;'margin-bottom: 60px;'>
🧭 Generate Career Roadmap
</div>

""", unsafe_allow_html=True)


experience_level = st.selectbox("Select Your Experience Level", ["Select", "Beginner", "Intermediate", "Advanced"])
interest_area = st.selectbox("Select Your Interest Area", ["Select", "Data Science & Analytics", "Digital Marketing With AI", "Programming Courses", "Product Management", "Software Development", "Banking & Finance", "Cybersecurity Courses"])

def get_roadmap(experience, interest):
    if experience == "Beginner" and interest == "Data Science & Analytics":
        return "✅ Learn Python\n✅ Learn Pandas & Numpy\n✅ Study Statistics\n✅ Do small data projects\n✅ Learn Power BI / Tableau"
    elif interest == "Cybersecurity Courses":
        return "✅ Learn Networking Basics\n✅ Explore OWASP Top 10\n✅ Use Kali Linux Tools\n✅ Practice on TryHackMe\n✅ Get CompTIA or CEH"
    elif experience != "Select" and interest != "Select":
        return "✅ Explore foundational concepts\n✅ Take beginner-friendly courses\n✅ Build small projects\n✅ Contribute to GitHub\n✅ Read blogs & join communities"
    else:
        return ""

manual_roadmap = get_roadmap(experience_level, interest_area)
if manual_roadmap:
    st.markdown(f"<div class='roadmap-box'>{manual_roadmap.replace('✅', '✨')}</div>", unsafe_allow_html=True)

# --- Gemini AI Roadmap Generator Section ---
st.markdown("## 🤖 AI-Powered Roadmap by Gemini")

col1, col2 = st.columns(2)
with col1:
    exp_years = st.selectbox("Your Experience (years)", ["0", "1", "2", "3+", "5+"])
with col2:
    background = st.text_input("Your Background (e.g. BSc, Banking, Python learner)", placeholder="Type here...")
goal = st.text_input("Your Dream Role (e.g. Data Scientist, AI Engineer, PM)", placeholder="Type here...")

if st.button("Generate AI Roadmap ✨"):
    if not background or not goal:
        st.warning("Please fill in both Background and Dream Role.")
    else:
        with st.spinner("Talking to Gemini AI..."):
            ai_roadmap = generate_gemini_roadmap(exp_years, background, goal)
            st.markdown("### 🎯 AI Suggested Roadmap")
            st.markdown(f"<div class='roadmap-box'>{ai_roadmap}</div>", unsafe_allow_html=True)

# --- Roadmap Styling ---
st.markdown("""
    <style>
    .roadmap-box {
        margin-top: 20px;
        padding: 25px;
        border-radius: 15px;
        background: linear-gradient(135deg, #1c1c1c, #2b2b2b);
        color: white;
        font-size: 16px;
        text-align: left;
        line-height: 1.8;
        box-shadow: 0 8px 18px rgba(0,0,0,0.4);
        animation: fadeIn 2s ease-in-out;
        white-space: pre-wrap;
    }
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown("""
<div class="custom-footer">
    © 2025 <strong>Sourabh Ranbhise</strong> · AI Career Roadmap · 
    <a href="https://www.linkedin.com/in/sourabh-ranbhise-67a4ba257/" target="_blank">LinkedIn</a> |
    <a href="https://github.com/Sourabh301998" target="_blank">GitHub</a> ·
    <a href="mailto:sourabhranbhise301998@gmail.com" target="_blank">Contact</a> ·
    Powered by <strong>Gemini</strong>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-NH40E6EQ07"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-NH40E6EQ07');
</script>
""", unsafe_allow_html=True)