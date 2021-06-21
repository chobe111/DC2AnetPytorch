from torchvision.io import decode_jpeg, image
import torch
import torch.nn as nn

def decode_image(input: torch.Tensor) -> torch.Tensor:
    return decode_jpeg(input, mode=image.ImageReadMode.GRAY)
    
