#  OpenCV学习笔记仓库

- [OpenCV学习笔记仓库](#opencv学习笔记仓库)
  - [1. OpenCV读取图像](#1-opencv读取图像)
    - [1.1 imread函数](#11-imread函数)
    - [1.2 imshow函数](#12-imshow函数)
    - [1.3 imwrite函数](#13-imwrite函数)

## 1. OpenCV读取图像

> 对应文件：[01-TestCV.py](./01-TestCV.py)

### 1.1 imread函数

> 参数1：(字符串)图片文件路径
>
> 返回：(InputArray)图像对象

例子：

```python
import cv2 as cv

# 读取一张图片为图像对象
img = cv.imread('./imgs/test.jpg')
```

### 1.2 imshow函数

> 参数1：(字符串)窗口名
>
> 参数2：(IntputArray)图像对象
>
> 返回：空

例子：

```python
# 显示图像
cv.imshow('图像窗口', img)
# 等待用户输入
cv.waitKey(0)
# 销毁所有opencv的窗口
cv.destroyAllWindows()
```

### 1.3 imwrite函数

> 参数1：(字符串)文件名
>
> 参数2：(InputArray)图像对象
>
> 参数3：可选参数
>
> 返回：写入图像的结果(布尔型)

例子：

```python
# 保存一张图像
cv.imwrite('./imgs/img.png', img)
```

## 2. OpenCV读取摄像头

> 晚点写
