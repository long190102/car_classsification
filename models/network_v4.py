import torch.nn as nn


class NetworkV4(nn.Module):
    def __init__(self, base, num_classes, num_makes, num_types):
        super().__init__()
        self.base = base

        if hasattr(base, 'fc'):
            in_features = self.base.fc.in_features
            self.base.fc = nn.Sequential()
        else:  # mobile net v2
            in_features = self.base.last_channel
            self.base.classifier = nn.Sequential()


        self.type_fc = nn.Sequential(
            nn.Dropout(0.2),
            nn.ReLU(),
            nn.Linear(in_features, num_types)
        )
        # self.class_fc = nn.Sequential(
        #     nn.Dropout(0.2),
        #     nn.Linear(in_features, num_classes)
        # )

    def forward(self, x):
        out = self.base(x)
        type_fc = self.type_fc(out)

        return type_fc