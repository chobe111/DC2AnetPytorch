from torch import tensor
from torchvision.io import decode_jpeg, decode_image
import torch
import torch.nn as nn


def decode_name(input: tensor.Tensor) -> str:
    """
    input: tensor shape 1 * N dtype ascii int
    return: ascii int list to string
    """

    int_arr = list(input.numpy())
    chr_arr = list(map(chr, int_arr))
    name = ""
    for i in chr_arr:
        name += i

    return name
