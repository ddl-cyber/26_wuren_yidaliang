import torch
from torchvision import transforms, datasets
from torch.utils.data.dataloader import DataLoader
from net import mixed_net


def test_model(model_path, test_loader, device, class_names, dataset_name="Test"):
    """
    加载模型并对指定测试集进行验证，打印整体正确率和每一类的正确率
    """
    # 加载模型
    model = mixed_net()
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.to(device)
    model.eval()

    # 初始化计数器
    class_correct = list(0.0 for _ in range(len(class_names)))
    class_total = list(0.0 for _ in range(len(class_names)))

    total_correct = 0
    total = 0

    # 开始测试
    with torch.no_grad():
        for datas, labels in test_loader:
            datas, labels = datas.to(device), labels.to(device)
            outputs = model(datas)
            _, predicted = torch.max(outputs.data, dim=1)

            total += labels.size(0)
            total_correct += (predicted == labels).sum().item()

            for i in range(labels.size(0)):
                label = labels[i].item()
                class_correct[label] += (predicted[i] == labels[i]).item()
                class_total[label] += 1

    # 打印结果
    print(f"\n========== {dataset_name} 测试结果 ==========")
    overall_acc = 100.0 * total_correct / total if total > 0 else 0.0
    print(f"Overall Accuracy: {overall_acc:.2f}%")

    # 输出每个类别的正确率
    for i, name in enumerate(class_names):
        if class_total[i] > 0:
            acc = 100.0 * class_correct[i] / class_total[i]
            print(f"{name} Accuracy: {acc:.2f}%")
        else:
            print(f"{name} Accuracy: N/A")

    return overall_acc


if __name__ == "__main__":
    # ==================== 图像转换 ====================
    test_transforms = transforms.Compose([
        transforms.Resize([64, 64]),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])

    # ==================== 加载数据 ====================
    BATCH_SIZE = 1024
    testset1 = datasets.ImageFolder(root='dataset/test1', transform=test_transforms)
    testset2 = datasets.ImageFolder(root='dataset/test2', transform=test_transforms)
    test_loader1 = DataLoader(testset1, batch_size=BATCH_SIZE, shuffle=False, pin_memory=True)
    test_loader2 = DataLoader(testset2, batch_size=BATCH_SIZE, shuffle=False, pin_memory=True)

    # 类别名称（按字母顺序对应索引 0,1,2）
    class_names = ['blue', 'red', 'yellow']
    print(f'标签对应的ID: {testset1.class_to_idx}')

    # ==================== 设备选择 ====================
    if torch.cuda.is_available():
        device = torch.device("cuda")
    elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        device = torch.device("mps")
    else:
        device = torch.device("cpu")
    print(f"使用设备: {device}")

    # ==================== 调用测试函数 ====================
    # 默认加载最佳模型，可根据实际保存的模型名称修改
    model_path = "pth/model_best_100.00.pth"

    # 如果最佳模型不存在，尝试加载最终模型
    import os
    if not os.path.exists(model_path):
        model_path = "pth/model_final.pth"
        print(f"未找到默认最佳模型，尝试加载: {model_path}")

    if os.path.exists(model_path):
        test_model(model_path, test_loader1, device, class_names, dataset_name="Test1")
        test_model(model_path, test_loader2, device, class_names, dataset_name="Test2")
    else:
        print(f"错误：找不到模型文件 {model_path}，请先运行 net.py 进行训练。")
