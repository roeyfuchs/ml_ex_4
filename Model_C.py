import torch
import torch.nn as nn
import torch.nn.functional as F


class Model_C(nn.Module):
    def __init__(self, image_size):
        super(Model_C, self).__init__()
        self.image_size = image_size
        self.bn1 = nn.BatchNorm1d(image_size)
        self.fc1 = nn.Linear(image_size, 100)  # first layer
        self.bn2 = nn.BatchNorm1d(100)
        self.fc2 = nn.Linear(100, 50)  # second layer
        self.fc3 = nn.Linear(50, 10)  # output


    def forward(self, x):
        x = x.view(-1, self.image_size)
        x = self.bn1(x)
        x = F.relu(self.fc1(x))
        x = self.bn2(x)
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return F.log_softmax(x, dim=1)
