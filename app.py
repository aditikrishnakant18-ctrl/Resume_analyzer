import streamlit as st
import PyPDF2


st.set_page_config(page_title = "Smart Resume Analyzer", layout="centered")
st.title("Smart Resume Analyzer")
st.caption("Upload your resume and get instant feedback for your target role")

st.markdown("---")

# Roles and skills
role_skills = {
    "Full stack developer": ["html", "css", "javascript", "react", "node", "database"],
    "Frontend developer": ["html", "css", "javascript", "react", "responsive design"],
    "Backend developer": ["python", "django", "flask", "api", "database"],
    "Software engineering": ["python", "dsa", "oops", "git", "dbms"],
    "Data analyst": ["python", "sql", "excel", "pandas", "numpy"],
    "Data scientist": ["python", "machine learning", "statistics", "pandas", "numpy", "model"],
    "Python developer": ["python", "functions", "oops", "git", "sql"],
    "AI/ML": ["python", "machine learning", "pandas", "numpy", "model"],
    "Cybersecurity": ["networking", "security", "linux", "ethical hacking"],
    "UI/UX Designer": ["figma", "wireframing", "prototyping", "user research"],
    "Graphic Designer": ["photoshop", "illustrator", "creativity", "branding"],
}
   


# Dropdown
target_role = st.selectbox(
    "Select Target Role",
    list(role_skills.keys())
)

# Upload resume
uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    st.success("Resume uploaded successfully!")

    # Read PDF
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    resume_text = ""

    for page in pdf_reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text

    # Show extracted text
    st.subheader(" Extracted Resume Text")
    st.text_area("Resume Content", resume_text, height=250)

    # Analyze button
    if st.button("Analyze Resume"):

        resume_text = resume_text.lower()
        required_skills = role_skills[target_role]

        matched_skills = []
        missing_skills = []

        # Skill matching
        for skill in required_skills:
            if skill in resume_text:
                matched_skills.append(skill)
            else:
                missing_skills.append(skill)

        # Match percentage
        match_percentage = (len(matched_skills) / len(required_skills)) * 100

        # Results
        st.subheader("Analysis Result")
        st.write(f"**Target Role:** {target_role}")
        st.write(f"Matched Skills: {len(matched_skills)} / {len(required_skills)}")
        st.write(f"**Matched Skills:** {', '.join(matched_skills) if matched_skills else 'None'}")
        st.write(f"**Missing Skills:** {', '.join(missing_skills) if missing_skills else 'None'}")
        st.write(f"**Match Percentage:** {match_percentage:.2f}%")

        # Progress bar
        st.progress(int(match_percentage))

        # Suggestions
        if missing_skills:
            st.subheader(" Suggestions to Improve")
            for skill in missing_skills:
                st.write(f"- Improve your knowledge or add projects related to **{skill}**")

        # Feedback
        st.subheader(" Feedback")

        if match_percentage >= 80:
            st.success("Your resume is strong and well aligned with the selected role. Add real-world projects to stand out more.")

        elif match_percentage >= 50:
            st.warning("Your resume has a good base but needs improvement. Add projects or certifications for missing skills.")

        else:
            st.error("Your resume needs improvement. Focus on building core skills and adding relevant projects.")
            
st.markdown("---")
st.caption("Made by Aditi Krishna kant")