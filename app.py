import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
from io import BytesIO

@st.cache_resource
def load_model():
    st.info("Loading model... this may take a minute")
    try:
        pipe = StableDiffusionPipeline.from_pretrained(
            "CompVis/stable-diffusion-v1-4",
            torch_dtype=torch.float32
        )
        pipe.to("cpu")
        st.success("Model loaded!")
        return pipe
    except Exception as e:
        st.error(f"Failed to load model: {e}")
        return None

def image_to_bytes(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()

st.title("🎨 Text-to-Image Generator")
prompt = st.text_input("Enter your prompt", "A fantasy forest with glowing mushrooms")

if st.button("Generate"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        pipe = load_model()
        if pipe:
            with st.spinner("Generating image..."):
                try:
                    image = pipe(prompt).images[0]
                    st.image(image, caption=prompt)
                    st.download_button("Download Image", image_to_bytes(image), "generated.png")
                except Exception as e:
                    st.error(f"Generation error: {e}")
        else:
            st.error("Model not available")
