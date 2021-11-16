import os
import cv2
import glob
# 特徴量ファイルをもとに分類器を作成
classifier = cv2.CascadeClassifier('lbpcascade_animeface.xml')#アニメの時はこっち
#classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")#実際の顔の時はこっち
# 顔の検出

image1 = glob.glob('./samples/*')
number = 0
for j in range(11):
    #image = cv2.imread('.samples/{num:06d}.jpg'.format(num = j))
    image = cv2.imread(image1[j])
    # グレースケールで処理を高速化

    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = classifier.detectMultiScale(gray_image)
    print(faces)
    print(type(faces))
    output_dir = 'faces'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


    if type(faces) is not tuple:
        for i in range(faces.shape[0]):
            # 一人ずつ顔を切り抜く
            x = faces[i][0]
            y = faces[i][1]
            w = faces[i][2]
            h = faces[i][3]
            face_image = image[y:y+h, x:x+w]
            output_path = os.path.join(output_dir,'{num:06d}.jpg'.format(num = number))
            cv2.imwrite(output_path,face_image)
            cv2.imwrite('/faces/face.jpg',image)
            number+=1
