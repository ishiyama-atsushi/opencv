<<<<<<< HEAD
import cv2

def main():
    # 入力画像の読み込み
    img = cv2.imread("Lenna.jpg")

    # カスケード型識別器の読み込み
    cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 顔領域の探索
    face = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

    # 顔領域を赤色の矩形で囲む
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x + w, y+h), (0,0,300), 4)

    # 結果を出力
    cv2.imwrite("result.jpg",img)


if __name__ == '__main__':
    main()
=======
import os
import cv2

# 特徴量ファイルをもとに分類器を作成
#classifier = cv2.CascadeClassifier('lbpcascade_animeface.xml')#アニメの時はこっち
classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# 顔の検出
image = cv2.imread('Lenna.jpg')
# グレースケールで処理を高速化
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces = classifier.detectMultiScale(gray_image)
print(faces)
output_dir = 'faces'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for i, (x,y,w,h) in enumerate(faces):
    # 一人ずつ顔を切り抜く
    face_image = image[y:y+h, x:x+w]
    output_path = os.path.join(output_dir,'{0}.jpg'.format(i))
    cv2.imwrite(output_path,face_image)

cv2.imwrite('/faces/face.jpg',image)
>>>>>>> 3160156c97aa01396fd236074cdbe5a2cd7f9201
