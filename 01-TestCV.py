import cv2 as cv

# 读取一张图片
img = cv.imread('./imgs/test.jpg')
# 显示图像
cv.imshow('图像窗口', img)
# 等待用户输入
cv.waitKey(0)
# 销毁所有opencv的窗口
cv.destroyAllWindows()
# 保存一张图像
cv.imwrite('./imgs/img.png', img)