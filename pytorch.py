#PYTORCH CHEATSHEET

#Imports
import torch
# Check the version of pytorch installed in your computer
print(f"PyTorch version: {torch.__version__}")
# Can also import the common abbreviation "nn" for "Neural Networks"
from torch import nn
# Almost everything in PyTorch is called a "Module" (you build neural networks by stacking together Modules)
module = nn.Linear(in_features=1,out_features=1)
print(type(module))


#Data imports
# Import PyTorch Dataset (you can store your data here) and DataLoader (you can load your data here)
from torch.utils.data import Dataset, DataLoader


#Creating tensors
# Create a single number tensor (scalar)
scalar = torch.tensor(7)
# Create a random tensor
random_tensor = torch.rand(size=(3, 4)) # this will create a tensor of size 3x4 but you can manipulate the shape how you want
# Multiply two random tensors
random_tensor_1 = torch.rand(size=(3, 4))
random_tensor_2 = torch.rand(size=(3, 4))
random_tensor_3 = random_tensor_1 * random_tensor_2 # PyTorch has support for most math operators in Python (+, *, -, /)


#Computer vision
# Base computer vision library
import torchvision
# Other components of TorchVision (premade datasets, pretrained models and image transforms)
from torchvision import datasets, models, transforms


#Text and natural language processing (NLP)
# Base text and natural language processing library
import torchtext
# Other components of TorchText (premade datasets, pretrained models and text transforms)
from torchtext import datasets, models, transforms


#Audio and speech
# Base audio and speech processing library
import torchaudio
# Other components of TorchAudio (premade datasets, pretrained models and text transforms)
from torchaudio import datasets, models, transforms

