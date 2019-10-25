import sys
import torch
from utils import timer
import matplotlib.pyplot as plt


ckpt_path = sys.argv[1]
ckpt = torch.load(ckpt_path)
weights = ckpt['Classifier']['weight']
norm = weights.abs() / weights.abs().sum()
plt.plot(norm.cpu())
plt.savefig('weights.png')
