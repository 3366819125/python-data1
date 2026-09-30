from ultralytics import YOLO

# 加载模型，第一次会自动下载
model = YOLO("yolov8n.pt")

# 检测图片，可以换成你自己图片路径
results = model(r"C:\Users\马玲\Pictures\青协总结会.jpg")

# 遍历结果
for r in results:
    r.show()    # 弹窗直接显示检测图片
    r.save()    # 保存到runs文件夹