import os
import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder

# 設定檔案路徑
model_path = r'C:\Users\owner\Desktop\plant_model.h5'  # plant_model.h5 的實際路徑
label_file = r'C:\Users\owner\Desktop\圖型識別\project\PlantCLEF_Subset\PlantCLEF_Subset\labels_info.txt'  # labels_info.txt 的實際路徑

# 載入標籤及相關資訊
labels_info = {}
with open(label_file, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip().split(':')
        label = line[0].strip()
        info = line[1].strip()
        labels_info[label] = info

# 載入標籤
labels = list(labels_info.keys())

# 加載最佳模型
model = load_model(model_path)

class PlantRecognitionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("植物辨識應用")
        
        self.label = Label(self.master, text="按下 '選擇照片' 按鈕選擇一張照片，然後按下 '辨識' 按鈕進行植物辨識。")
        self.label.pack()

        self.choose_button = Button(self.master, text="選擇照片", command=self.choose_image)
        self.choose_button.pack()

        self.recognize_button = Button(self.master, text="辨識", command=self.recognize_plant)
        self.recognize_button.pack()

        self.image_label = Label(self.master)
        self.image_label.pack()

        self.result_label = Label(self.master, text="")
        self.result_label.pack()

    def choose_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            self.load_and_display_image(file_path)

    def load_and_display_image(self, file_path):
        img = Image.open(file_path)
        img = img.resize((300, 300), Image.BICUBIC)
        img = ImageTk.PhotoImage(img)
        self.image_label.config(image=img)
        self.image_label.image = img
        self.image_path = file_path

    def recognize_plant(self):
        if hasattr(self, 'image_path'):
            img = load_img(self.image_path, target_size=(224, 224))
            img_array = img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = img_array / 255.0

            # 進行預測
            prediction = model.predict(img_array)
            predicted_label = labels[np.argmax(prediction)]
            plant_info = labels_info.get(predicted_label, "無相關資訊")

            # 顯示辨識結果
            result_text = f"辨識結果：{predicted_label}\n相關資訊：{plant_info}"
            self.result_label.config(text=result_text)
        else:
            self.result_label.config(text="請先選擇照片")

if __name__ == "__main__":
    root = Tk()
    app = PlantRecognitionApp(root)
    root.mainloop()
