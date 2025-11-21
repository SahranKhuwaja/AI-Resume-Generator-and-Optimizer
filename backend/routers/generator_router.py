from flask import Blueprint, request
from services.langchain_service import generate_resume

generator_router = Blueprint('resumeGenerator', __name__)

@generator_router.post('/generate')
def generator():
    return generate_resume("""Job description

Role: AI & ML Engineer/ Research (Freshers)

Vacancies: 15
Location: Mandaveli, Chennai
Batch: 2025

Education: Bachelors or Masters in Computer Science, Artificial Intelligence, Data Science, Machine Learning, Mathematics, or Statistics.


Key Responsibilities:

Design and develop compiler frameworks that optimize AI model execution at the kernel, graph, and operator levels.
Architect scalable transformer-based infrastructures for distributed multi-node training and efficient inference.
Build end-to-end AI pipelines including graph optimizations, memory scheduling, and compute distribution.
Collaborate with research teams to translate mathematical models into optimized execution graphs and intermediate representations (IRs).
Implement custom kernels, quantization strategies, and low-level performance optimizations in C/C++ and CUDA.
Analyze and tune runtime performance bottlenecks focusing on parallelization, vectorization, and memory management.
Develop domain-specific compiler passes for tensor operations, automatic differentiation, and operator fusion.
Conduct systematic experiments to explore scaling laws, precision formats, and architectural optimizations for improved computational efficiency.

Required Skills & Qualifications:

Strong proficiency in C and C++ (mandatory).
Experience or strong interest in compiler construction, runtime systems, and code generation.
Proficiency or willingness to learn CUDA and Rust for high-performance computing and systems-level development.
Solid foundation in Mathematics calculus, probability, statistics, and linear algebra.
Deep understanding of computer architecture, operating systems, data structures, and memory management.
Analytical mindset with strong debugging and performance profiling abilities.
Ability to thrive in a fast-paced, research-oriented environment with cross-functional collaboration.

What We Offer:

A dynamic and innovative work environment with a AI research-driven team.
Mentorship, learning, and growth opportunities in AI infrastructure and systems research.
Competitive compensation with performance-based advancement and technical ownership.
Opportunity to work on compiler-level AI framework design and large-scale foundation model optimization.
Access to multi-node GPU clusters and next-gen compute environments for experimentation.
Important: Please read the guidelines clearly before applying: https://blubridge.ai/join-our-team

Role: Machine Learning Engineer
Industry Type: Analytics / KPO / Research
Department: Data Science & Analytics
Employment Type: Full Time, Permanent
Role Category: Data Science & Machine Learning
Education
UG: B.Tech/B.E. in Computers
PG: M.Tech in Any Specialization, MS/M.Sc(Science) in Maths
Doctorate: Any Doctorate
Key Skills
Skills highlighted with ‘‘ are preferred keyskills
C++Artificial IntelligenceMachine Learningfresher
TensorflowCNatural Language ProcessingNeural NetworksAIDeep LearningPytorchData SciencePattern RecognitionAimlPythonMl""", 
"""
    Juan Jose Carin 
Data Scientist 
 
Mountain View, CA 94041 
 650-336-4590 | juanjose.carin@gmail.com 
 linkedin.com/in/juanjosecarin | juanjocarin.github.io 
 
Professional Profile 
Passionate about data analysis and experiments, mainly focused on user behavior, experience, and engagement, with a solid 
background in data science and statistics, and extensive experience using data insights to drive business growth. 
Education
 2016 University of California, Berkeley Master of Information and Data Science GPA: 3.93
 
 
 
Relevant courses: 
• Machine Learning 
• Machine Learning at Scale 
• Storing and Retrieving Data 
• Field Experiments 
• Applied Regression and Time Series 
Analysis 
• Exploring and Analyzing Data 
• Data Visualization and 
Communication 
• Research Design and Applications for 
Data Analysis 
2014 Universidad Politécnica de Madrid M.S. in Statistical and Computational Information Processing GPA: 3.69
 
 
 
Relevant courses:  
• Data Mining 
• Multivariate Analysis 
• Time Series 
• Neural Networks and Statistical 
Learning 
• Regression and Prediction Methods 
• Optimization Techniques 
• Monte Carlo Techniques 
• Numerical Methods in Finance 
• Stochastic Models in Finance 
• Bayesian Networks
 2005 Universidad Politécnica de Madrid M.S. in Telecommunication Engineering GPA: 3.03
 Focus Area: Radio communication systems (radar and mobile). 
Fellowship: First year at University, due to Honors obtained last year at high school. 
Skills 
 Programming / Statistics Big Data Visualization Others 
Proficient: R, Python, SQL Hadoop, Hive, MrJob Tableau Git, AWS 
Intermediate: SPSS, SAS, Matlab Spark, Storm  Bash 
Basic: EViews, Demetra+  D3.js Gephi, Neo4j, QGIS 
Experience 
DATA SCIENCE 
Jan. 2016 – Mar. 2016 Data Scientist 
 CONENTO  Madrid, Spain (working remotely) 
• Designed and implemented the ETL pipeline for a predictive model of traffic on the main roads in 
eastern Spain (a project for the Spanish government). 
• Automated scripts in R to extract, transform, clean (incl. anomaly detection), and load into MySQL 
data from multiple data sources: road traffic sensors, accidents, road works, weather.
 Jun. 2014 – Sep. 2014 Data Scientist  
 CONENTO Madrid, Spain 
• Designed an experiment for Google Spain (conducted in October 2014) to measure the impact of 
YouTube ads on the sales of a car manufacturer's dealer network. 
• A matched-pair, cluster-randomized design, which involved selecting the test and control groups 
from a sample of 50+ cities in Spain (where geo-targeted ads were possible) based on their sales
wise similarity over time, using wavelets (and R). 
MANAGEMENT – SALES (Electrical Eng.) 
Feb. 2009 – Aug. 2013 Head of Sales, Spain & Portugal – Test &Measurement dept.
 YOKOGAWA Madrid, Spain 
• Applied analysis of sales and market trends to decide the direction of the department. 
• Led a team of 7 people. 
 
Juan Jose Carin 
Data Scientist 
Mountain View, CA 94041 
650-336-4590 | juanjose.carin@gmail.com 
linkedin.com/in/juanjosecarin | 
juanjocarin.github.io 
• Increased revenue by 6.3%, gross profit by 4.2%, and operating income by 146%, and achieved a 30% 
ratio of new customers (3x growth), by entering new markets and improving customer service and 
training.
 SALES (Electrical Eng. & Telecom.) 
Apr. 2008 – Jan. 2009 
Sales Engineer – Test & Measurement dept. 
YOKOGAWA 
• Promoted to head of sales after 5 months leading the sales team. 
Sep. 2004 – Mar. 2008 Sales & Application Engineer 
AYSCOM 
Madrid, Spain 
Madrid, Spain 
• Exceeded sales target every year from 2005 to 2007 (achieved 60% of the target in the first 3 months 
of 2008). 
EDUCATION
 Jul. 2002 – Jun. 2004 
Projects  
Tutor of Differential & Integral Calculus, Physics, and Digital Electronic Circuits
 ACADEMIA UNIVERSITARIA 
• Highest-rated professor in student surveys, in 4 of the 6 terms. 
• Increased ratio of students passing the course by 25%. 
Madrid, Spain 
See juanjocarin.github.io for additional information
 2016 
2015 
2015 
2015 
2015 
2015 
2014 
2014 
SmartCam 
Capstone 
Python, OpenCV, TensorFlow, AWS (EC2, S3, DynamoDB) 
A scalable cloud-based video monitoring system that features motion detection, face counting, and image recognition.
 Implementation of the Shortest Path and PageRank algorithms with the Wikipedia graph dataset 
Machine Learning at Scale 
Using a graph dataset of almost half a million nodes. 
Forest cover type prediction 
Machine Learning 
Hadoop MrJob, Python, AWS EC2, AWS S3
 Python, Scikit-Learn, Matplotlib 
A Kaggle competition: predictions of the predominant kind of tree cover, from strictly cartographic variables such as elevation 
and soil type, using random forests, SVMs, kNNs, Naive Bayes, Gradient Descent, GMMs, …
 Redefining the job search process 
Storing and Retrieving Data 
Hadoop HDFS, Hive, Spark, Python, AWS EC2, Tableau
 A pipeline that combines data from Indeed API and the U.S. Census Bureau to select the best locations for data scientists 
based on the number of job postings, housing cost, etc.
 A fresh perspective on Citi Bike 
Data Visualization and Communication 
An interactive website to visualize NYC Citi Bike bicycle sharing service.
 Investigating the effect of competition on the ability to solve arithmetic problems 
Field Experiments 
Tableau, SQLite
 R 
A randomized controlled trial in which 300+ participants were assigned to a control group or one of two test groups to 
evaluate the effect of competition (being compared to no one or someone better or worse). 
Prediction of customer churn for a mobile network carrier 
Data Mining 
Predictions from a sample of 45,000+ customers, using tree decisions, logistic regression, and neural networks. 
Different models of Harmonized Index of Consumer Prices (HICP) in Spain 
Time Series 
SAS
 SPSS, Demetra+
 Forecasts based on exponential smoothing, ARIMA, and transfer function (using petrol price as independent variable) models. 

""")