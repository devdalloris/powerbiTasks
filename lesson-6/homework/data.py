import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import uuid
import io

# Define lists for generating data
job_titles = [
    "AI Architect", "Machine Learning Specialist", "Deep Learning Specialist",
    "Data Scientist", "Computer Scientist", "Business Intelligence Analyst",
    "Cloud Specialist", "Web Developer", "Software Developer", "Mobile Developer",
    "DevOps Engineer", "Help Desk Professional", "Desktop Support Professional",
    "Cloud Administrator", "Cyber Security Professional", "System Administrator"
]

# Salary ranges per job title (based on realistic U.S. IT job market data for 2025)
salary_ranges = {
    "AI Architect": (120000, 200000),
    "Machine Learning Specialist": (110000, 180000),
    "Deep Learning Specialist": (115000, 185000),
    "Data Scientist": (100000, 160000),
    "Computer Scientist": (95000, 150000),
    "Business Intelligence Analyst": (80000, 130000),
    "Cloud Specialist": (90000, 150000),
    "Web Developer": (75000, 120000),
    "Software Developer": (85000, 140000),
    "Mobile Developer": (80000, 130000),
    "DevOps Engineer": (100000, 160000),
    "Help Desk Professional": (50000, 80000),
    "Desktop Support Professional": (55000, 85000),
    "Cloud Administrator": (85000, 140000),
    "Cyber Security Professional": (95000, 160000),
    "System Administrator": (70000, 110000)
}

# Skills tailored to job titles
skills_by_job = {
    "AI Architect": ["Python, TensorFlow, PyTorch, AWS", "Machine Learning, Deep Learning, NLP", "Big Data, Hadoop, Spark"],
    "Machine Learning Specialist": ["Python, Scikit-learn, TensorFlow", "Machine Learning, NLP, Pandas", "R, SQL, Apache Spark"],
    "Deep Learning Specialist": ["Python, PyTorch, Keras", "Deep Learning, Computer Vision, NLP", "TensorFlow, GPU Optimization"],
    "Data Scientist": ["Python, R, SQL", "Tableau, Power BI, Pandas", "Machine Learning, Statistical Analysis"],
    "Computer Scientist": ["C++, Python, Algorithms", "Java, Data Structures", "Linux, Research"],
    "Business Intelligence Analyst": ["SQL, Tableau, Power BI", "ETL, Data Warehousing", "Excel, Looker"],
    "Cloud Specialist": ["AWS, Azure, GCP", "Terraform, Kubernetes", "Docker, Cloud Security"],
    "Web Developer": ["JavaScript, React, Node.js", "HTML, CSS, Angular", "MongoDB, Django"],
    "Software Developer": ["Java, Python, C#", "Spring, .NET, Git", "SQL, REST APIs"],
    "Mobile Developer": ["Swift, Kotlin, Flutter", "React Native, Firebase", "iOS, Android SDK"],
    "DevOps Engineer": ["Docker, Kubernetes, Jenkins", "AWS, Terraform, CI/CD", "Ansible, Bash"],
    "Help Desk Professional": ["ITIL, ServiceNow, Windows", "Troubleshooting, Customer Support", "Ticketing Systems"],
    "Desktop Support Professional": ["Windows, Active Directory", "Hardware Troubleshooting", "Office 365, VPN"],
    "Cloud Administrator": ["AWS, Azure, Linux", "Cloud Monitoring, IAM", "VMware, Network Security"],
    "Cyber Security Professional": ["Wireshark, Splunk, CISSP", "Penetration Testing, Firewalls", "SIEM, Network Security"],
    "System Administrator": ["Linux, Windows Server", "Active Directory, VMware", "Network Administration, Bash"]
}

companies = [
    "TechCorp", "Innovate Solutions", "DataDriven Inc.", "CloudWave Technologies",
    "SecureSystems", "NextGen Analytics", "WebWorks", "MobileMavens", "AI Pioneers",
    "GlobalTech", "SmartSolutions", "CyberGuard", "InfoSys", "TechTrend Innovations",
    "FutureProof Tech"
]

locations = [
    "San Francisco, CA", "New York, NY", "Austin, TX", "Seattle, WA", "Boston, MA",
    "Chicago, IL", "Los Angeles, CA", "Denver, CO", "Atlanta, GA", "Remote",
    "Phoenix, AZ", "Portland, OR", "Miami, FL", "Dallas, TX", "Houston, TX"
]

# Job description templates with placeholders for skills
job_description_templates = {
    "AI Architect": "Design and implement AI solutions using {skills}. Lead model development and collaborate with teams to deploy scalable systems.",
    "Machine Learning Specialist": "Develop and optimize ML models with {skills}. Conduct experiments and integrate models into production.",
    "Deep Learning Specialist": "Build deep neural networks specializing in {skills}. Optimize for performance in computer vision or NLP.",
    "Data Scientist": "Analyze datasets and build predictive models using {skills}. Provide actionable insights to drive business decisions.",
    "Computer Scientist": "Research and develop algorithms with {skills}. Contribute to innovative tech projects and publish findings.",
    "Business Intelligence Analyst": "Create dashboards and perform data analysis with {skills}. Support strategic decision-making.",
    "Cloud Specialist": "Design and manage cloud infrastructure using {skills}. Ensure scalability and high availability.",
    "Web Developer": "Build responsive web applications with {skills}. Collaborate with designers to optimize user experience.",
    "Software Developer": "Develop and test software applications using {skills}. Write clean code and work with cross-functional teams.",
    "Mobile Developer": "Create mobile apps for iOS and Android using {skills}. Ensure seamless user experience and API integration.",
    "DevOps Engineer": "Automate CI/CD pipelines and manage infrastructure with {skills}. Ensure system reliability and scalability.",
    "Help Desk Professional": "Provide technical support and resolve user issues using {skills}. Maintain IT service management systems.",
    "Desktop Support Professional": "Support end-user hardware and software with {skills}. Troubleshoot issues and ensure security.",
    "Cloud Administrator": "Manage cloud environments and monitor performance using {skills}. Implement security best practices.",
    "Cyber Security Professional": "Protect systems from threats using {skills}. Conduct vulnerability assessments and implement protocols.",
    "System Administrator": "Maintain servers and network infrastructure with {skills}. Ensure system uptime and security."
}

# Generate data
np.random.seed(42)
n_rows = 2000

data = {
    "Job ID": [str(uuid.uuid4()) for _ in range(n_rows)],
    "Job Title": np.random.choice(job_titles, n_rows),
    "Company": np.random.choice(companies, n_rows),
    "Location": np.random.choice(locations, n_rows),
    "Salary": [0] * n_rows,
    "Skills": [""] * n_rows,
    "Post Date": [(datetime(2025, 4, 19) - timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d") for _ in range(n_rows)],
    "Job Description": [""] * n_rows
}

# Assign salaries, skills, and job descriptions
for i, title in enumerate(data["Job Title"]):
    # Assign salary based on job title
    salary_min, salary_max = salary_ranges[title]
    data["Salary"][i] = round(np.random.uniform(salary_min, salary_max), 2)
    
    # Assign skills based on job title
    data["Skills"][i] = random.choice(skills_by_job[title])
    
    # Assign job description with skills incorporated
    data["Job Description"][i] = job_description_templates[title].format(skills=data["Skills"][i])

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel in memory using openpyxl
output = io.BytesIO()
with pd.ExcelWriter(output, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="IT_Job_Demands", index=False)

# Get the Excel file content
excel_content = output.getvalue()
excel_content
# ... (rest of the code remains the same until the Excel-saving part)

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel file locally
output_path = "IT_Job_Demands_Corrected.xlsx"  # Change this to your desired path, e.g., "C:/Users/YourName/Desktop/IT_Job_Demands_Corrected.xlsx"
with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="IT_Job_Demands", index=False)

print(f"File saved to: {output_path}")
print("Hello")
