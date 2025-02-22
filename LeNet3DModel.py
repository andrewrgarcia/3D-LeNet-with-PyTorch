# Besmei Taala
# Amir Hossein Karami
# Subject: I want to make the LeNet Model 3D
# Fork by Andrew Garcia, 2023

from torch.autograd import Variable
import torch
import torch.nn as nn
import torch.nn.functional as F


# input: (N = batch_size, C = 1, L = 32, L = 32, L = 32)
# output: (N, num_classes)
L =32
num_classes = 5


class LeNet3D(nn.Module):
    def __init__(self):
        super(LeNet3D, self).__init__()

        self.conv1 = nn.Conv3d(1, 6, kernel_size=(5, 5, 5))
        self.pool = nn.MaxPool3d(2, 2)
        self.conv2 = nn.Conv3d(6, (L//2), kernel_size=(5, 5, 5))
        self.fc1 = nn.Linear((L//2) * 5 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, num_classes)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        print(x.size())
        x = self.pool(F.relu(self.conv2(x)))
        print(x.size())
        x = x.view(-1, (L//2) * 5 * 5 * 5)
        # x = x.view(x.size(0), -1) 
        print(x.size())
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x



model = LeNet3D()


# Test the model:
x = Variable(torch.randn(10, 1, L, L, L)) # (N_samples,C_channels,D=L,H=L,W=L)
print(x)
y = model(x)
print(y)



