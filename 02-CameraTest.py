import cv2 as cv

# 摄像头视频捕获器
cap = cv.VideoCapture(0)

while True:
    # 读取一帧(frame)图像
    ret, frame = cap.read()
    # 显示当前帧
    cv.imshow('帧', frame)
    # 判断是否需要退出程序
    if (cv.waitKey(1) & 0xFF) == ord('q'):
        break

# 释放视频捕获器
cap.release()
# 销毁所有窗口
cv.destroyAllWindows()