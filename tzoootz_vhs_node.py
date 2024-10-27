import numpy as np
from PIL import Image, ImageOps, ImageEnhance

class TZOOTZ_VHSNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_image": ("IMAGE",),
                "effect_strength": ("FLOAT", {"default": 0.5}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "apply_vhs_effect"
    CATEGORY = "TZOOTZ RESEARCH 2024®"

    def apply_vhs_effect(self, input_image, effect_strength):
        # Ensure input is a NumPy array and in uint8 format
        if isinstance(input_image, Image.Image):
            input_image = np.array(input_image)
        input_image = input_image.astype(np.uint8)  # Ensure uint8 data type

        # Remove any extra dimensions if present
        if input_image.ndim == 4:
            input_image = input_image[0]  # Remove batch dimension if exists
        elif input_image.ndim == 2:
            input_image = np.stack((input_image,) * 3, axis=-1)  # Convert grayscale to RGB

        # Apply a sample VHS effect (adding tint and noise for demonstration)
        effect_image = Image.fromarray(input_image, mode="RGB")
        
        # Example effect: Convert to grayscale and apply a color tint
        effect_image = ImageOps.colorize(effect_image.convert("L"), black="purple", white="orange")

        # Adjust brightness to simulate VHS effects
        enhancer = ImageEnhance.Brightness(effect_image)
        effect_image = enhancer.enhance(0.8 + 0.2 * effect_strength)

        # Final step: Convert effect_image to NumPy array for compatibility
        output_image = np.array(effect_image)

        return (output_image,)
