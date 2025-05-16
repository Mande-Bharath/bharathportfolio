import streamlit as st

# ------------------ PAGE CONFIG ------------------ #
st.set_page_config(page_title="Bharath Mande | Portfolio", layout="wide")

# ------------------ HEADER SECTION ------------------ #
col1, col2 = st.columns([1, 3])

with col1:
    st.image("WhatsApp_Image_2024-05-16_at_17.31.52_egcf7b-Circle.jpg", width=200)

with col2:
    st.markdown("""
        <h1 style='margin-bottom: 0;'>Bharath Mande</h1>
        <h4 style='color: gray; margin-top: 0;'>Full-Stack Developer | CSE Student</h4>
        <p>
        📍 Bhadradri Kothagudem, Telangana, India  &nbsp; | &nbsp;
        📧 <a href="mailto:bharathytgmr@gmail.com">bharathytgmr@gmail.com</a>  &nbsp; | &nbsp;
        📞 7981659550  
        </p>
        <p>
        🔗 <a href="https://www.linkedin.com/in/mandebharath/" target="_blank">LinkedIn</a>  &nbsp; | &nbsp;
        🔗 <a href="https://github.com/bharathmande" target="_blank">GitHub</a>
        </p>
    """, unsafe_allow_html=True)

st.markdown("---")

# ------------------ ABOUT ------------------ #
st.subheader("👋 About Me")
st.write("""
I’m a passionate and goal-oriented full-stack developer currently training at Nxtwave.
With a strong foundation in computer science, I specialize in building responsive, 
user-focused web applications. I enjoy turning complex problems into simple, beautiful 
and intuitive designs.
""")

# ------------------ EDUCATION ------------------ #
st.subheader("🎓 Education")

st.markdown("""
- **Nxtwave Disruptive Technologies**  
  *Industry Ready Certification in Full-stack Development* (Jul 2023 – Present)

- **JBIET, Rangareddy**  
  *B.Tech in Computer Science Engineering* (2023 – 2027)  
  **CGPA:** 9.0

- **New Vision Junior College, Khammam**  
  *Intermediate (MPC)* (2021 – 2023)  
  **Percentage:** 96%

- **Triveni School, Bhadradri Kothagudem**  
  *SSC* (2020 – 2021)  
  **CGPA:** 10.0
""")

# ------------------ SKILLS ------------------ #
st.subheader("🛠️ Skills")

skills = {
    "Frontend": ["HTML", "CSS", "Bootstrap", "JavaScript", "React.js"],
    "Backend": ["Python", "Node.js", "Express.js"],
    "Database": ["SQLite"],
    "Other": ["C", "Java"]
}

for category, items in skills.items():
    st.markdown(f"**{category}:** " + ", ".join(items))

# ------------------ PROJECTS ------------------ #
st.subheader("💼 Projects")

projects = [
    {
        "title": "📦 E-Commerce Website",
        "description": "A responsive product showcase with video previews and Bootstrap carousels.",
        "link": "http://bharathecomme.ccbp.tech",
        "tech": "HTML, CSS, Bootstrap"
    },
    {
        "title": "🔍 Wikipedia Search App",
        "description": "A custom search interface using real-time API calls and intuitive layout.",
        "link": "http://bharath999.ccbp.tech",
        "tech": "HTML, CSS, JavaScript, REST API, Bootstrap"
    },
    {
        "title": "🍔 Tasty Kitchens (Swiggy/Zomato Clone)",
        "description": "A fully functional food ordering app with cart, login, protected routes and mock payments.",
        "link": "http://bharath304.ccbp.tech",
        "tech": "React.js, Bootstrap, React Slick, REST API, Figma"
    }
]

for proj in projects:
    with st.expander(proj["title"]):
        st.write(proj["description"])
        st.markdown(f"🔗 [Live Demo]({proj['link']})")
        st.code(proj["tech"])

# ------------------ ACHIEVEMENTS ------------------ #
st.subheader("🏆 Achievements")
st.markdown("""
- Participated in 3 national-level hackathons
- Won 2 by delivering innovative, real-world solutions
""")





