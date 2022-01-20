import torch.cuda
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset
import numpy as np

device = 'cuda' if torch.cuda.is_available() else 'cpu'


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(6*48, 1024)   # 6*48 ulazni
        self.fc2 = nn.Linear(1024, 512)    # 3 skrivena po 64
        self.fc3 = nn.Linear(512, 256)
        # self.fc4 = nn.Linear(64, 6*8)   # 48 izlazni
        self.fc4 = nn.Linear(256, 1)

    def forward(self, x):
        x = F.leaky_relu(self.fc1(x))   # samo relu?
        x = F.leaky_relu(self.fc2(x))
        x = F.leaky_relu(self.fc3(x))
        x = self.fc4(x)
        return F.relu(x)


'''
class CubeTrainDataset(Dataset):
    def __init__(self):
        data = np.load(.....)
        self.inputs = data['arr_0']
        self.outputs = data['arr_1']
        print(f'Data loaded, {self.inputs.shape}, {self.outputs.shape}')

    def __len__(self):
        return self.inputs.shape[0]

    def __getitem__(self, index):
        return self.inputs[index], self.outputs[index]
'''