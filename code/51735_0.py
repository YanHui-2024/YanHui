class Noise(nn.Module):
    def forward(self, image):
        return image.new_empty(2, 1, 3, 4).normal_()