# Plant-identification-system
## :small_blue_diamond:Introduction

* 大多人對於植物缺乏認識
    * 建立一套植物辨識系統，識別植物、瞭解其特徵及相關資訊
* 使用深度學習技術進行植物圖像分類
    * 採用的方法包括數據預處理、模型建立和訓練、結果評估
* 基於深度學習模型進行植物辨識應用
    * 用戶選擇一張圖片，並使用預先訓練的模型來辨識植物

## :small_blue_diamond:Method

### Dataset

選用包含各種植物圖片的公開數據集: PlantCLEF
* 涵蓋 20 種植物類別影像資料
* 訓練資料: 10,455 筆
* 驗證資料: 1,135 筆
* 測試資料: 30 筆


### Training 
![](https://github.com/jaifenny/Plant-identification-system/blob/main/picture/1.png)

➢ 圖像預處理

    歸一化像素值並進行標籤編碼 (LabelEncoder)

➢ 數據增強

    利用 ImageDataGenerator 進行圖像增強

    增加訓練數據的多樣性和提高模型的穩健性 (Robustness)

➢ 建立模型

    使用 MobileNetV2 作為預訓練的卷積神經網絡

    添加全局平均池化層和密集層進行分類

➢ 模型訓練與優化

    使用Adam優化器和分類交叉熵作為損失函數

    回調函數: 設置模型檢查點和動態調整學習率，保存最佳模型

    模型訓練: 在數據增強後的訓練集上進行模型訓練

➢ 模型評估

    模型載入: 從最佳檢查點載入模型權重

    驗證集上進行模型預測

    計算混淆矩陣和分類報告，評估模型性能

➢ 輸出模型

    plant_model.h5

### Application
![](https://github.com/jaifenny/Plant-identification-system/blob/main/picture/2.png)

➢ 應用程式介面

    使用 tkinter 建立圖形用戶界面 (GUI)
    顯示選擇的圖片和辨識結果
➢ 圖片選擇與顯示

    使用 filedialog 讓用戶從文件系統中選擇圖片
    調整圖片大小，顯示選擇的圖片在用戶界面上
➢ 植物辨識

    預處理圖像數據
    使用預先訓練的模型進行預測 (plant_model.h5)
➢ 顯示辨識結果

    根據預測結果顯示植物名稱和植物的相關資訊

## :small_blue_diamond:Results

### Test Dataset
➢ 使用訓練好的模型 (plant_model.h5) 對處理後的圖片進行預測，從預測結果中
獲取概率最高的類別標籤，比較預測與實際標籤

➢ 測試集準確率為 0.8，模型在測試數據上正確預測的比例

➢ 加權平均精確度為 0.51 (validation)，結合了各個類別精確度的綜合指標

➢ Summarize: 這兩個指標並不矛盾，即使模型在某些少見的類別上表現不佳（可
能因為數據不平衡或其他原因），但在測試集上整體的準確率仍然可以很高，這
可能是因為模型在大多數主要類別上的表現較好


## :small_blue_diamond:GUI

使用 tkinter建立圖形用戶界面 ，提供 "選擇照片" 和 "辨識" 兩個按鈕，用
於選擇圖片和啟動植物辨識

![](https://github.com/jaifenny/Plant-identification-system/blob/main/picture/3.png)


## References
[1] https://www.imageclef.org/PlantCLEF2022

[2] https://reurl.cc/K3ZbkM

[3] https://reurl.cc/ZyDAOa

[4] https://ithelp.ithome.com.tw/articles/10278264


