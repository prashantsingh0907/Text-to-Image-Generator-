import torch
from diffusers import StableDiffusionPipeline
import gradio as gr

device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16 if device == "cuda" else torch.float32
)
pipe.to(device)

def generate_image(prompt):
    image = pipe(prompt).images[0]
    return image

gr.Interface(
    fn=generate_image,
    inputs=gr.Textbox(label="Enter your prompt", placeholder="e.g. A futuristic city on Mars"),
    outputs=gr.Image(type="pil"),
    title="🎨 Text-to-Image Generator",
    description="A text-to-image generator using Stable Diffusion v1.5 and Gradio",
).launch(share=True)
