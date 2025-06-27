from fpdf import FPDF
from datetime import datetime

# Replacing special characters like en-dashes with simple hyphens to avoid Unicode issues
def clean_text(text):
    return text.replace("–", "-").replace("’", "'")

# Cleaned content sections
career_objective = clean_text("""Motivated and technically-inclined fresher with a Diploma and B.Tech in Mechanical Engineering, 
equipped with strong foundational IT knowledge and hands-on training in DevOps and desktop support. 
Eager to begin my career as a Desktop Support Engineer, contribute to IT infrastructure maintenance, 
and grow into advanced technical roles.""")

education = clean_text("""B.Tech in Mechanical Engineering
Kallam Haranadha Reddy Institute of Technology, Guntur
2019 - 2023

Diploma in Mechanical Engineering
State Board of Technical Education, Andhra Pradesh
2016 - 2019""")

technical_skills = clean_text("""- Operating Systems: Windows 10/11, Linux (Ubuntu, Kali Basic)
- Software & Tools: MS Office, Remote Desktop Tools, Ticketing Systems
- Networking: Basic LAN setup, IP addressing, routers & switches
- DevOps Exposure: Git, GitHub, Docker (basics), Linux terminal
- Other: System Troubleshooting, Printer/Scanner Configuration""")

training_projects = clean_text("""PMKVK DevOps Training (SYNCHROSERVE Global Solutions Pvt. Ltd.)
- Trained on DevOps tools and basic system/network administration
- Exposure to real-time software development and deployment pipelines
- Learned troubleshooting commands, user management in Linux

Grocery Delivery Platform (React + Node.js Project)
- Built a web platform with authentication, order management
- Experience working with GitHub and version control""")

core_competencies = clean_text("""- Desktop & laptop setup, configuration, and maintenance
- First-level user support (hardware, OS, and basic networking)
- User account & permission management (Windows/Linux)
- Troubleshooting peripheral devices (printers, scanners)
- Asset tracking and ticket-based service documentation""")

strengths = clean_text("""- Quick learner with strong troubleshooting instincts
- Team player with effective communication skills
- Committed to long-term career growth in IT Support and Systems Engineering
- Fluent in English, Hindi, Telugu""")

# Dynamically insert today's date (June 27, 2025)
declaration = clean_text(f"""I hereby declare that the information provided above is true to the best of my knowledge.

Shaik Abdul Rahiman
Date: {datetime(2025, 6, 27).strftime('%B %d, %Y')}
Location: Guntur, Andhra Pradesh""")

# Create a new PDF instance
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Helvetica", "B", 14)
pdf.cell(0, 10, "SHAIK ABDUL RAHIMAN", ln=True, align="C")
pdf.set_font("Helvetica", "", 11)
pdf.cell(0, 10, "Phone: 75692206048 | Email: abdulrehamanshaik46@gmail.com", ln=True, align="C")
pdf.cell(0, 10, "Location: Guntur, Andhra Pradesh | GitHub: github.com/username | LinkedIn: linkedin.com/in/username", ln=True, align="C")
pdf.ln(10)

# Add sections with double-line separator
def add_section(title, content):
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 10, title, ln=True)
    pdf.set_font("Helvetica", "", 11)
    pdf.multi_cell(0, 10, content)
    pdf.set_font("Helvetica", "", 10)  # Slightly smaller font for separator
    pdf.cell(0, 10, "=========", ln=True, align="L")  # Add double-line separator
    pdf.ln(2)

add_section("Career Objective", career_objective)
add_section("Education", education)
add_section("Technical Skills", technical_skills)
add_section("Training & Projects", training_projects)
add_section("Core Competencies", core_competencies)
add_section("Strengths", strengths)
add_section("Declaration", declaration)

# Save the final cleaned PDF
final_pdf_path = "Shaik_Abdul_Rahiman_Resume_Final.pdf"  # Adjust path based on your environment
try:
    pdf.output(final_pdf_path)
    print(f"PDF successfully generated at: {final_pdf_path}")
except Exception as e:
    print(f"Error generating PDF: {e}")

# Output the final path
final_pdf_path
