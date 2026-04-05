from realesrgan import RealESRGAN
from PIL import Image
import torch

# load model once (VERY IMPORTANT)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = RealESRGAN(device, scale=2)
model.load_weights("https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x2.pth")


def restore_image(input_path, output_path):
    """
    Enhance image using Real-ESRGAN AI model
    """

    image = Image.open(input_path).convert("RGB")

    # AI enhancement
    restored = model.predict(image)

    restored.save(output_path)