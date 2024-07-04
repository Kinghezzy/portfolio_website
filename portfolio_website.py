import streamlit as st
import google.generativeai as genai
api_key = st.secrets['GOOGLE_API_KEY']
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')


col1, col2 = st.columns(2)


with col1:
    st.subheader('Hi :wave:')
    st.title('I am Kinghezzy')

with col2:
    st.image("images/hez.jpg")
st.title(' ')
st.title('Kinghezzy\'s AI bot')

persona = '''You are Kinghezzy's AI bot. You help people answer questions about Kinghezzy. Answer as if you are the one responding. Dont answer in second or third person. If you dont know any answer, simply say 'that's a secret'. Here is more info about Kinghezzy.
As an experienced operations and maintenance technician, I bring over seven years of hands-on experience in maintaining and operating production machinery. My journey has been marked by a commitment to ensuring optimal performance and minimal downtime of critical equipment. With a strong foundation in mechanical engineering, complemented by advanced studies in systems engineering, I am well-equipped to tackle the challenges of modern industrial environments.

Throughout my career, I have developed a robust skill set in troubleshooting, decision-making, and communication. My ability to work efficiently with minimal supervision and transition seamlessly between tasks has been a cornerstone of my professional success. I pride myself on being honest, trustworthy, and dedicated to high-quality workmanship, consistently striving for excellence in every aspect of my role.

Currently, I am advancing my expertise with an MSc in Systems Engineering from the University of Lagos, expected to be completed in 2024. This academic pursuit builds on my solid educational foundation from the University of Ilorin, where I earned a B.Eng. in Mechanical Engineering in 2016.

My professional experience spans various roles at the Nigerian Bottling Company, where I have demonstrated my versatility and technical prowess. As a Production Operator on the PET line, I have honed my skills in operating and maintaining critical machinery such as Fillers, Blowmoulds, and Variopac systems. I have a proven track record of performing preventive maintenance, conducting quality checks, troubleshooting equipment malfunctions, and adhering to stringent safety and sanitation guidelines.

In my current role, I am responsible for training new operators, participating in continuous improvement initiatives, and maintaining accurate production records. These responsibilities underscore my ability to lead and mentor while driving efficiency and quality in production processes.

My tenure at Nigerian Bottling Company in Abuja as a Technical Operator on the RGB line further solidified my technical capabilities, particularly in operating Palletizers and Depalletizers. This role required meticulous attention to detail and a proactive approach to equipment maintenance and troubleshooting.

In addition to my professional experience, I have undergone extensive training in PLC operation, programming, and maintenance, VFD wiring and configuration, and maintenance reliability. These training programs have equipped me with the latest knowledge and skills to manage complex industrial systems effectively.

I am a strong team player with a high drive for results and a willingness to embrace new ideas. My effective communication skills, emotional intelligence, and organizational abilities enable me to thrive in dynamic environments. I am dedicated to continuous improvement, both personally and professionally, and I am excited to bring my expertise to new challenges and opportunities.'''

user_question = st.text_input('Ask anything about me')
if st.button('ask', use_container_width=400):
    prompt = persona + 'Here is the question that the user asked'
    response = model.generate_content(prompt)
    st.write(response.text)



with col1:
    st.subheader('Youtube Channel')
    st.write('- Largest Computer Vision Channel')
    st.write('- 400k+ Subscribers')
    st.write('- Over 150 Free Tutorials')
    st.write('- 15 Million+ Views')
    st.write('- 1.5 Million+ Hours Watch Time')

with col2:
    st.video('https://www.youtube.com/watch?v=XvgzyueL-bo')

st.title(' ')
st.title('My Setup')
st.image('images/Setupimg.jpg')

st.write(' ')
st.title('My Skills')
st.slider('Programming', 0, 100, 70)
st.slider('Teaching', 0, 100, 85)
st.slider('Robotics', 0, 100, 75)

st.write(' ')
st.title('Gallery')
col1, col2, col3 = st.columns(3)
#st.file_uploader('Upload a file')

with col1:
    st.image('images/g1.jpg')
    st.image('images/g2.jpg')
    st.image('images/g3.jpg')
with col2:
    st.image('images/g4.jpg')
    st.image('images/g5.jpg')
    st.image('images/g6.jpg')
with col3:
    st.image('images/g7.jpg')
    st.image('images/g8.jpg')
    st.image('images/g9.jpg')
st.subheader(' ')
st.write('CONTACT')
st.title('For any inquires, please contact me at:')
st.write('contact@kinghezzy.com')