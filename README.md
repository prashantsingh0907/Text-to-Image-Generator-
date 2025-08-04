# Text-to-Image-Generator Using Stable Diffusion v1.5
🖼️ Text-to-Image Generator | Stable Diffusion v1.5
A powerful and intuitive Text-to-Image Generator leveraging Stable Diffusion v1.5 to turn natural language prompts into vivid AI-generated visuals. Developed using both Streamlit for deployment and Gradio for GPU-powered inference via Google Colab.

✅ Developed as part of the AI/ML Internship at Brainwave Matrix Solutions

📌 Features
🔮 Natural Language → AI Image Generation
⚡ GPU acceleration with Google Colab
🧠 Powered by Hugging Face diffusers
🎛️ Clean and responsive Gradio UI
🌐 Lightweight Streamlit app for quick CPU-based deployment


🧠 Sample Prompts
"A futuristic city in the sky at golden hour"
"A majestic lion wearing sunglasses"
"Cyberpunk Tokyo street, rainy night, neon lights"
"An astronaut relaxing on Mars with a drink"


🧰 Tech Stack
Layer	Technology
Model	Stable Diffusion v1.5 (via Hugging Face Diffusers)
Frameworks	Gradio, Streamlit
Backend	Python 3.10+, PyTorch
Runtime	Google Colab (GPU), Local (CPU)


💻 Local Installation Guide
For CPU-based image generation using Streamlit.
1. Clone the Repository
git clone https://github.com/Prashantsingh0907/Text-to-Image-Generator
cd Brainwave__Matrix__Intern/text-to-image-app
2. Create a Virtual Environment
python -m venv venv
3. Activate the Virtual Environment
On Windows:
venv\Scripts\activate
On Mac/Linux:
source venv/bin/activate
4. Install Dependencies
pip install -r requirements.txt
5. Run the App
streamlit run app.py


📀 How to Run on Colab (Step-by-Step) (GPU)
For faster generation using CUDA acceleration and Gradio interface.

1. Open the app_colab.py in Colab by manually uploading the script.
2. If not already imported, you can fetch it via raw URL:
!wget https://raw.githubusercontent.com/Prashantsingh0907/Text-to-Image-Generator/main/app_colab.py
3. Then simply run:
!python app_colab.py
4. Wait for model loading (~1 minute on GPU).
5. A public Gradio live link will appear — click it to access the app in your browser.
☁️ Deployments


🚀 Streamlit Cloud (CPU)
Upload to GitHub
Connect with streamlit.io/cloud
Set app.py as the entry point




📁 Project Structure
text-to-image-app/
├── app.py # Streamlit version (CPU)
├── app_colab.py # Gradio + Colab (GPU)
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .gitignore # Git exclusions
✅ Task Completion
This project was successfully completed under the AI/ML Internship at Brainwave Matrix Solutions, as a demonstration of real-world application of generative models using Hugging Face Diffusers.

🏢 Brainwave Matrix Solutions

📅 August 2025

🎯 Deliverable: Text-to-Image Generator with dual deployment (CPU + GPU)

🙌 Acknowledgements
🤗 Hugging Face Diffusers

🧠 PyTorch + Transformers

🎨 Stability.AI for Stable Diffusion model

🖼️ Gradio and Streamlit for deployment

