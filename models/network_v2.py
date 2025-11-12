import torch
import torch.nn as nn
#import albumentations as A
import numpy as np
import torch
import torchvision
import torch.nn as nn 
import torchvision.transforms as T
import torchvision.models as models
from torch.utils.data import DataLoader, Dataset
from torchsummary import summary
import torch.optim as optim
class NetworkV2(nn.Module):
    def __init__(self, base, num_classes, num_makes, num_types, freeze_layers=25):
        super().__init__()
        self.base = base

        # --- Freeze the first N layers of ResNet ---
        # Flatten all submodules of the base model
        child_modules = list(self.base.children())
        layer_count = 0
        for child in self.base.children():
            layer_count += 1
            if layer_count <= freeze_layers:
                for param in child.parameters():
                    param.requires_grad = False

        # --- Adjust for ResNet vs MobileNet ---
        if hasattr(base, 'fc'):
            in_features = self.base.fc.in_features
            self.base.fc = nn.Sequential()  # Remove original FC
        else:  # mobile net v2
            in_features = self.base.last_channel
            self.base.classifier = nn.Sequential()

        # --- Define output heads ---
        self.brand_fc = nn.Sequential(
            nn.Dropout(0.2),
            nn.Linear(in_features, num_makes)
        )

        self.type_fc = nn.Sequential(
            nn.Dropout(0.2),
            nn.Linear(in_features, num_types)
        )

        self.class_fc = nn.Sequential(
            nn.Dropout(0.2),
            nn.ReLU(),
            nn.Linear(in_features + num_makes + num_types, num_classes)
        )

    def forward(self, x):
        out = self.base(x)
        brand_fc = self.brand_fc(out)
        type_fc = self.type_fc(out)
        concat = torch.cat([out, brand_fc, type_fc], dim=1)
        fc = self.class_fc(concat)
        return fc, brand_fc, type_fc