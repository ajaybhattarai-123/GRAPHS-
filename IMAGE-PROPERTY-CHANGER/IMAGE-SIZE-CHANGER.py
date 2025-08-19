'''THIS CODE CHANGE THE DPI, IMAGE SIZE OF THE PROVIDED IMAGE, AND IS VERY USEFUL FOR RESEARCH PURPOSER BEFORE SUBMITTING TO THE JOURNAL'''
##CREATED BY ER. AJAY BHATTARAI ###
import cv2
import numpy as np
from PIL import Image, ImageEnhance
import rembg
import os
from io import BytesIO
'''
this code is very useful for the researrch purpose, as various types of images should be submitted in different journals
thus this helps to change dpi, file size and the image size'''
def enhance_image(
    image_path,
    output_size=None,  # Desired output dimensions (width, height)
    dpi=None,          # DPI for saved image
    file_size_kb=None,  # Target file size in KB
    sharpen_factor=2.0,  # Sharpness enhancement
    contrast_factor=1.5,  # Contrast enhancement
    denoise_strength=10   # Denoising strength
):
    # Load image using Pillow to preserve metadata
    try:
        original_image = Image.open(image_path)
    except Exception as e:
        print(f"Error loading image: {e}")
        return

    # Preserve original DPI if not specified
    original_dpi = original_image.info.get('dpi', (72, 72))
    target_dpi = dpi or original_dpi

    # Remove background
    image_no_bg = rembg.remove(original_image)
    
    # Composite on white background
    white_bg = Image.new('RGBA', image_no_bg.size, (255, 255, 255, 255))
    composite_image = Image.alpha_composite(white_bg, image_no_bg).convert('RGB')
    
    # Resize if output_size is specified
    if output_size:
        composite_image = composite_image.resize(output_size, Image.LANCZOS)
    
    # Enhance sharpness
    enhancer = ImageEnhance.Sharpness(composite_image)
    enhanced_image = enhancer.enhance(sharpen_factor)
    
    # Enhance contrast
    enhancer = ImageEnhance.Contrast(enhanced_image)
    enhanced_image = enhancer.enhance(contrast_factor)
    
    # Convert to OpenCV for denoising
    cv_image = cv2.cvtColor(np.array(enhanced_image), cv2.COLOR_RGB2BGR)
    denoised_image = cv2.fastNlMeansDenoisingColored(
        cv_image, None, 
        denoise_strength, denoise_strength, 7, 21
    )
    
    # Convert back to Pillow
    final_image = Image.fromarray(cv2.cvtColor(denoised_image, cv2.COLOR_BGR2RGB))
    
    # Save with size/DPI options
    output_path = os.path.splitext(image_path)[0] + "_enhanced.png"
    save_image_with_options(final_image, output_path, target_dpi, file_size_kb)
    print(f"Enhanced image saved at {output_path}")

def save_image_with_options(image, output_path, dpi, target_size_kb=None):
    """Save image with DPI and file size options"""
    format = "PNG"  # Default format for transparency support
    
    if target_size_kb:
        quality = 95
        while quality > 10:
            buffer = BytesIO()
            image.save(buffer, format=format, dpi=dpi, quality=quality)
            size_kb = len(buffer.getvalue()) / 1024
            
            if size_kb <= target_size_kb:
                with open(output_path, "wb") as f:
                    f.write(buffer.getvalue())
                return
            quality -= 5
        
        # Fallback to smallest possible size
        image.save(output_path, format=format, dpi=dpi, quality=10)
    else:
        image.save(output_path, format=format, dpi=dpi)

# Example usage
if __name__ == "__main__":
    input_path = r"C:\Users\ajayb\OneDrive\Pictures\MY-PIC\PROFILE-1.png"
    
    # User-configurable parameters
    enhance_image(
        image_path=input_path,
        output_size=(800, 600),  # Desired width/height
        dpi=(300, 300),          # Target DPI
        file_size_kb=500,        # Target file size (KB)
        sharpen_factor=1.8,      # Reduce if too sharp
        contrast_factor=1.3,     # Reduce if too contrasty
        denoise_strength=8       # Reduce if losing details
    )