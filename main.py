

#Импорт необходимых модулей
import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
from matplotlib import pyplot as plt

import os
from os.path import join as pjoin
import pandas as pd
from torchvision.io import read_image
