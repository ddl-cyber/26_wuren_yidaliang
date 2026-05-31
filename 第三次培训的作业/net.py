import torch
from torch import nn
from torchvision import transforms, datasets
from torch.utils.data.dataloader import DataLoader
import torch.optim as optim
import torch.nn.functional as F
from torchinfo import summary
import os


class mixed_net(nn.Module):
    """
    混合神经网络，用于锥桶图像分类（3类：blue, red, yellow）
    网络层数统计（不含激活函数、BatchNorm、Dropout、Flatten）：
        卷积层 + 池化层 + 全局平均池化 + 全连接层 = 4 + 4 + 1 + 1 = 10层，全连接层为1层（<=3层）
    """
    def __init__(self):
        super(mixed_net, self).__init__()

        # 第1层：卷积层
        # 输入: [B, 3, 64, 64]，输出: [B, 32, 64, 64]
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1)
        self.bn1 = nn.BatchNorm2d(32)
        # 第2层：最大池化
        # 输入: [B, 32, 64, 64]，输出: [B, 32, 32, 32]
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)

        # 第3层：卷积层
        # 输入: [B, 32, 32, 32]，输出: [B, 64, 32, 32]
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        self.bn2 = nn.BatchNorm2d(64)
        # 第4层：最大池化
        # 输入: [B, 64, 32, 32]，输出: [B, 64, 16, 16]
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)

        # 第5层：卷积层
        # 输入: [B, 64, 16, 16]，输出: [B, 128, 16, 16]
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1)
        self.bn3 = nn.BatchNorm2d(128)
        # 第6层：最大池化
        # 输入: [B, 128, 16, 16]，输出: [B, 128, 8, 8]
        self.pool3 = nn.MaxPool2d(kernel_size=2, stride=2)

        # 第7层：卷积层
        # 输入: [B, 128, 8, 8]，输出: [B, 256, 8, 8]
        self.conv4 = nn.Conv2d(128, 256, kernel_size=3, stride=1, padding=1)
        self.bn4 = nn.BatchNorm2d(256)
        # 第8层：最大池化
        # 输入: [B, 256, 8, 8]，输出: [B, 256, 4, 4]
        self.pool4 = nn.MaxPool2d(kernel_size=2, stride=2)

        # 第9层：全局平均池化（替换Flatten+两层全连接，大幅减少参数量，提升泛化能力）
        # 输入: [B, 256, 4, 4]，输出: [B, 256, 1, 1]
        self.gap = nn.AdaptiveAvgPool2d(1)

        # 第10层：全连接层（输出层）
        # 输入: [B, 256]，输出: [B, 3]
        self.fc = nn.Linear(256, 3)

    def forward(self, x):
        """
        前向传播
        """
        x = self.pool1(F.relu(self.bn1(self.conv1(x))))  # [B, 3, 64, 64] -> [B, 32, 32, 32]
        x = self.pool2(F.relu(self.bn2(self.conv2(x))))  # [B, 32, 32, 32] -> [B, 64, 16, 16]
        x = self.pool3(F.relu(self.bn3(self.conv3(x))))  # [B, 64, 16, 16] -> [B, 128, 8, 8]
        x = self.pool4(F.relu(self.bn4(self.conv4(x))))  # [B, 128, 8, 8] -> [B, 256, 4, 4]
        x = self.gap(x)                                   # [B, 256, 4, 4] -> [B, 256, 1, 1]
        x = x.view(x.size(0), -1)                         # [B, 256, 1, 1] -> [B, 256]
        x = self.fc(x)                                    # [B, 256] -> [B, 3]
        return x


def evaluate_model(net, test_loader, criterion, device):
    """
    评估模型在测试集上的 Loss 和 Accuracy
    """
    net.eval()
    test_loss = 0.0
    correct = 0
    total = 0
    with torch.no_grad():
        for datas, labels in test_loader:
            datas, labels = datas.to(device), labels.to(device)
            outputs = net(datas)
            loss = criterion(outputs, labels)
            test_loss += loss.item()
            _, predicted = torch.max(outputs.data, dim=1)
            total += predicted.size(0)
            correct += (predicted == labels).sum().item()
    accuracy = 100.0 * correct / total if total > 0 else 0.0
    avg_loss = test_loss / len(test_loader)
    return avg_loss, accuracy


def evaluate_detailed(net, test_loader, device, class_names):
    """
    详细评估：打印 Overall Accuracy 和每一类的 Accuracy
    """
    net.eval()
    class_correct = list(0.0 for _ in range(len(class_names)))
    class_total = list(0.0 for _ in range(len(class_names)))
    total_correct = 0
    total = 0

    with torch.no_grad():
        for datas, labels in test_loader:
            datas, labels = datas.to(device), labels.to(device)
            outputs = net(datas)
            _, predicted = torch.max(outputs.data, dim=1)
            total += labels.size(0)
            total_correct += (predicted == labels).sum().item()

            for i in range(labels.size(0)):
                label = labels[i].item()
                class_correct[label] += (predicted[i] == labels[i]).item()
                class_total[label] += 1

    overall_acc = 100.0 * total_correct / total if total > 0 else 0.0
    print(f"Overall Accuracy: {overall_acc:.2f}%")
    for i, name in enumerate(class_names):
        if class_total[i] > 0:
            acc = 100.0 * class_correct[i] / class_total[i]
            print(f"{name} Accuracy: {acc:.2f}%")
        else:
            print(f"{name} Accuracy: N/A")


if __name__ == "__main__":
    # ==================== 图像转换与数据增强 ====================
    # 训练集：加入数据增强，提升泛化能力
    train_transforms = transforms.Compose([
        transforms.Resize([64, 64]),
        transforms.RandomHorizontalFlip(p=0.5),          # 随机水平翻转
        transforms.RandomRotation(degrees=15),           # 随机旋转±15度
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),  # 颜色抖动
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])

    # 测试集：不做数据增强，仅做归一化
    test_transforms = transforms.Compose([
        transforms.Resize([64, 64]),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])

    # ==================== 超参数设置 ====================
    BATCH_SIZE = 256
    EPOCH = 200
    LR = 0.01

    # ==================== 加载数据 ====================
    trainset = datasets.ImageFolder(root='dataset/train', transform=train_transforms)
    testset1 = datasets.ImageFolder(root='dataset/test1', transform=test_transforms)
    testset2 = datasets.ImageFolder(root='dataset/test2', transform=test_transforms)

    print(f"训练集图片数量: {len(trainset)}")
    print(f"测试集1图片数量: {len(testset1)}")
    print(f"测试集2图片数量: {len(testset2)}")

    train_loader = DataLoader(trainset, batch_size=BATCH_SIZE, shuffle=True, pin_memory=True)
    test_loader1 = DataLoader(testset1, batch_size=BATCH_SIZE, shuffle=False, pin_memory=True)
    test_loader2 = DataLoader(testset2, batch_size=BATCH_SIZE, shuffle=False, pin_memory=True)

    # 类别名称与索引映射（按字母顺序：blue->0, red->1, yellow->2）
    class_names = ['blue', 'red', 'yellow']
    print(f'标签对应的ID: {trainset.class_to_idx}')

    # ==================== 创建网络 ====================
    if torch.cuda.is_available():
        device = torch.device("cuda")
    elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        device = torch.device("mps")
    else:
        device = torch.device("cpu")
    print(f"使用设备: {device}")

    net = mixed_net().to(device)

    # 打印网络信息
    summary(net, input_size=(1, 3, 64, 64), device=device)

    # ==================== 设置优化器、损失函数、学习率调度 ====================
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=LR, momentum=0.9, weight_decay=5e-4)
    # 学习率衰减：每30个epoch乘以0.5，帮助收敛
    scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=30, gamma=0.5)

    # ==================== 开始训练 ====================
    print("\n========== 开始训练 ==========")
    best_acc1 = 0.0
    no_improve_epochs = 0      # 连续未提升的epoch数
    patience = 200              # 早停耐心值：连续20个epoch验证准确率不提升则停止
    os.makedirs("pth", exist_ok=True)

    for epoch in range(EPOCH):
        net.train()
        train_loss = 0.0
        mid_point = len(train_loader) // 2

        for batch_id, (datas, labels) in enumerate(train_loader):
            datas, labels = datas.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = net(datas)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            train_loss += loss.item()

            # 在一个epoch中，训练完前半部分，打印一次train Loss
            if batch_id == mid_point - 1 and mid_point > 0:
                avg_loss = train_loss / (batch_id + 1)
                print(f"Epoch [{epoch + 1}/{EPOCH}] 前半部分 train Loss: {avg_loss:.5f}")

        # 训练完一个epoch，打印后半部分（整个epoch）的train Loss
        avg_train_loss = train_loss / len(train_loader)
        print(f"Epoch [{epoch + 1}/{EPOCH}] 后半部分 train Loss: {avg_train_loss:.5f}")

        # 学习率调度步进
        scheduler.step()

        # 训练完一个epoch，打印验证集的test Loss和Accuracy
        test1_loss, test1_acc = evaluate_model(net, test_loader1, criterion, device)
        test2_loss, test2_acc = evaluate_model(net, test_loader2, criterion, device)
        print(f"Epoch [{epoch + 1}/{EPOCH}] test1 Loss: {test1_loss:.5f} Accuracy: {test1_acc:.2f}%")
        print(f"Epoch [{epoch + 1}/{EPOCH}] test2 Loss: {test2_loss:.5f} Accuracy: {test2_acc:.2f}%")

        # 保存最佳模型（以test1准确率为准）
        if test1_acc > best_acc1:
            best_acc1 = test1_acc
            best_path = f"pth/model_best_{best_acc1:.2f}.pth"
            torch.save(net.state_dict(), best_path)
            print(f"*** 最佳模型已更新并保存至: {best_path} ***")
            no_improve_epochs = 0  # 重置早停计数器
        else:
            no_improve_epochs += 1
            print(f"*** 验证准确率未提升，早停计数: {no_improve_epochs}/{patience} ***")

        print("-" * 60)

        # 早停判断
        if no_improve_epochs >= patience:
            print(f"\n>>> 早停触发：连续 {patience} 个 epoch 验证准确率未提升，停止训练。")
            break

    # ==================== 所有epoch训练结束后，详细评估 ====================
    print("\n========== 训练结束，最终详细评估 ==========")
    print(f"\n>>> Test1 详细结果:")
    evaluate_detailed(net, test_loader1, device, class_names)
    print(f"\n>>> Test2 详细结果:")
    evaluate_detailed(net, test_loader2, device, class_names)

    # 同时保存最终模型
    final_path = "pth/model_final.pth"
    torch.save(net.state_dict(), final_path)
    print(f"\n最终模型已保存至: {final_path}")
