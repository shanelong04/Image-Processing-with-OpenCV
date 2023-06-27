import cv2 as cv
import matplotlib.pyplot as plt

def cat_nguong(img, th):
    return img > th

def show_cat_nguong():
    fig = plt.figure(figsize=(16, 9))
    ax1, ax2 = fig.subplots(1, 2)

    img = cv.imread('keodan_dau.tif', 0) # Using 0 to read image in grayscale mode
    ax1.imshow(img, cmap='gray')
    ax1.set_title("Ảnh gốc")
    ax1.axis('off')

    y = cat_nguong(img, th=117)
    ax2.imshow(y, cmap='gray')
    ax2.set_title("Ảnh cắt ngưỡng")
    ax2.axis('off')
    plt.show()

if __name__ == '__main__':
    show_cat_nguong()