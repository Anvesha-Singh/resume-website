from pathlib import Path

import streamlit as st
from PIL import Image

# PATH SETTINGS
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "STEP_resume.pdf"
profile_pic = current_dir / "assets" / "pfp-modified.png"

# GENERAL SETTINGS
PAGE_TITLE = "Resume"
PAGE_ICON = "🐧"
NAME = "Anvesha Singh"
DESCRIPTION = """
WE '23 | Pursuing B.Tech in CSE at VIT Chennai
"""
EMAIL = "anveshasingh1412@gmail.com"
NUMBER = "+91 7862007499"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=300)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    st.write("📞", NUMBER)
    st.write("[LinkedIn](https://www.linkedin.com/in/anvesha-singh-330ba9260)‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎[GitHub](https://github.com/Anvesha-Singh)")


# --- EDUCATION ---
st.write('\n')
st.subheader("Education")
st.write("- __🏫 Vellore Institute of Technology, Chennai__")
st.write("_Sep. 2022 – July 2026(Expected)_")
st.write("Bachelor of CSE with Specialization in AI and Robotics; CGPA: 9.14")


# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
- **Languages:** C, C++, Python, Java, HTML, CSS
- **Soft Skills:**  Leadership, Event and Time Management, Teamwork, Communication, Adaptable
- **Tools:** Github, Google Colab, Figma, Arduino, Visual Studio Code
"""
)


# --- PROJECTS ---
st.write('\n')
st.subheader("Projects")
st.write("---")

# --- PROJECT 1
st.write("🌟","[__CaseFlowPro__](https://github.com/Anvesha-Singh/CaseFlowPro_beta)")
st.write("_September 2023_")
st.write(
    """
- ► Created a web-app that can be used by Judges to organise their workflow implementing DCM.
- ► A Smart India Hackathon Project under the Ministry of Law Category.
- ► Took responsibility for the research, design and presentation of the project.
"""
)

# --- PROJECT 2
st.write('\n')
st.write("🌟","[__VIT Achievements Page__](https://github.com/Anvesha-Singh/Bhagwan-Bharose)")
st.write("_February 2023_")
st.write(
    """
- ► Developed a website for displaying the achievements made by VIT students and faculty.
- ► Final project for the Web Development Workshop and Competition organised by Spoken Tutorial IIT
Bombay.
- ► Was responsible for the front-end using HTML and CSS.
"""
)

# --- PROJECT 3
st.write('\n')
st.write("🌟","[__Nonograms__](https://github.com/Anvesha-Singh/Nonograms)")
st.write("_May 2023_")
st.write(
    """
- ► Programmed a bot that can solve Nonograms on its own given the blank spaces and clues.
- ► Team project assigned to us at the Women Engineers Bootcamp by TalentSprint.
- ► Was tasked with coding the base strategies and a few advanced methods for the bot to solve the Nonogram.
"""
)


# --- KEY COURSES TAKEN ---
st.write('\n')
st.subheader("KEY COURSES TAKEN")
st.write("---")

# --- COURSE 1
st.write("📖","Women Engineers BootCamp 2023")
st.write(
    """
- ► Participated in a 3 Week physical Bootcamp conducted from May 2023 at IIIT Hyderabad, Telangana.
- ►  Learnt self-learning skills, computational and analytical skills, clean-coding techniques, working on projects
in teams, and Corporate Skills.
"""
)

# --- COURSE 2
st.write('\n')
st.write("📖","Internet of Things and Space BootCamp")
st.write(
    """
- ► 1 Week physical Bootcamp conducted from December 2023 at Hyderabad by ECE Dept., B V Raju
Institute of Technology.
- ► Practical understanding of Wireless Communication Tech like Node MCU, Rasperry Pi, ESP32
Microcontroller, ThinkSpeak through MATLAB, Live streaming satellite data.
"""
)


# --- Accomplishments ---
st.write('\n')
st.subheader("Accomplishments")
st.write("---")
st.write("🏆","**Google WE Scholar:** Selected in the Top 200 out of 23 thousand applicants for Women Engineers Scholarship Program by TalentSprint sponsored by Google.")


# --- POSITIONS OF RESPONSIBILITY ---
st.write('\n')
st.subheader("Positions of Responsibility")
st.write("☘️"," __Treasurer__ ")
st.write("_IEEE Computer Society, VIT Chennai_")
st.write("_Oct 2023 – Present_")
st.write("Organised a Competitive Coding event with 400+ college student participants called BitWars Algorithm ShowDown as the Student Coordinator.")