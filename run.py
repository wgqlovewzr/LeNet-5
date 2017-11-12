from lenet import LeNet5
import torch.nn as nn
import torch.optim as optim
import torch.functional as F
from torch.autograd import Variable
from torchvision.datasets.mnist import MNIST
import torchvision.transforms as transforms
from torch.utils.data import DataLoader


def main():
    data_train = MNIST('./data/mnist',
                       download=True,
                       transform=transforms.Compose([
                           transforms.Scale((32, 32)),
                           transforms.ToTensor(),
                       ]))
    data_train_loader = DataLoader(data_train, batch_size=1024, shuffle=True, num_workers=8)

    net = LeNet5()
    criterion = nn.NLLLoss()
    optimizer = optim.SGD(net.parameters(), lr=2e-3)

    for e in range(10):
        for i, samples in enumerate(data_train_loader):
            images, labels = samples
            images, labels = Variable(images), Variable(labels)
            output = net(images)
            loss = criterion(output, labels)
            print('Epoch %d, Batch: %d, Loss: %f' % (e, i, loss.data[0]))

            loss.backward()
            optimizer.step()


if __name__ == '__main__':
    main()