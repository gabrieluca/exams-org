import cv2
import numpy as np

from Normalize_and_crop import normalize_crop

img = cv2.imread("database_files/exams/NM7510_P3_C_2019_2/NM7510_P3_pacote_C_2_sem_2019-34.png",1) 
template = cv2.imread('database_files/track_markers/template.png',cv2.IMREAD_GRAYSCALE)
template2 = cv2.imread('database_files/track_markers/template2.png',cv2.IMREAD_GRAYSCALE)

def main():
 
    img1, img2 = normalize_crop(img,template,template2)
    img_qdr = img1[8:300, 8:1900]
    img_res = img_qdr[5:500, 40:1900]
    img_res = cv2.cvtColor(img_res, cv2.COLOR_BGR2GRAY)

    # Normalize and threshold image
    res, im = cv2.threshold(img_res, 164, 255, cv2.THRESH_BINARY_INV)

    # Fill everything that is the same colour (black) as top-left corner with white
    cv2.floodFill(im, None, (0, 0), 255)

    # Fill everything that is the same colour (white) as top-left corner with black
    cv2.floodFill(im, None, (0, 0), 0)

    imgFI = cv2.bitwise_not(im)

    # morphology operation
    kernel = np.ones((1, 1), np.uint8)
    im = cv2.dilate(im, kernel, iterations=1)
  
    img_qdr = cv2.resize(img_qdr, (800, 200))
    cv2.imshow("Dados do cabecalho:", img_qdr)

        
    cv2.imshow("RA-1)", imgFI[80:150,230:290])
    cv2.waitKey(0)
    cv2.imshow("RA-2)", imgFI[80:150,290:360])
    cv2.waitKey(0)
    cv2.imshow("RA-3)", imgFI[80:150,390:450])
    cv2.waitKey(0)
    cv2.imshow("RA-4)", imgFI[80:150,460:520])
    cv2.waitKey(0)
    cv2.imshow("RA-5)", imgFI[80:150,520:590])
    cv2.waitKey(0)
    cv2.imshow("RA-6)", imgFI[80:150,610:680])
    cv2.waitKey(0)
    cv2.imshow("RA-7)", imgFI[80:150,690:760])
    cv2.waitKey(0)
    cv2.imshow("RA-8)", imgFI[80:150,760:830])
    cv2.waitKey(0)
    cv2.imshow("RA-9)", imgFI[80:150,860:920])
    cv2.waitKey(0)
    cv2.imshow("Sequencial-1)", imgFI[70:150,1000:1070])
    cv2.waitKey(0)
    cv2.imshow("Sequencial-2)", imgFI[70:150,1070:1140])
    cv2.waitKey(0)
    cv2.imshow("Sequencial-3)", imgFI[70:150,1140:1210])
    cv2.waitKey(0)
    cv2.imshow("Pacote)", imgFI[70:150,1280:1360])
    cv2.waitKey(0)

    #img1, img2 = normalize_crop(img,template,template2)
    img_qdr = img1[182:280, 5:1900] #Nome e ass
    img_res = img_qdr[5:500, 40:1900]
    img_res = cv2.cvtColor(img_res, cv2.COLOR_BGR2GRAY)

    # Normalize and threshold image
    res, im = cv2.threshold(img_res, 190, 255, cv2.THRESH_BINARY_INV)

    # Fill everything that is the same colour (black) as top-left corner with white
    cv2.floodFill(im, None, (0, 0), 255)

    # Fill everything that is the same colour (white) as top-left corner with black
    cv2.floodFill(im, None, (0, 0), 0)

    imgFI = cv2.bitwise_not(im)

    # morphology operation
    kernel = np.ones((2, 2), np.uint8)
    im = cv2.dilate(im, kernel, iterations=1)


    #img_qdr = cv2.resize(img_qdr, (900, 120))  
    #cv2.imshow("Dados do cabecalho:", img_qdr)

    cv2.imshow("Nome)", imgFI[3:280,80:660
    ])
    cv2.waitKey(0)

    #img1, img2 = normalize_crop(img,template,template2)
    img_qdr = img1[180:280, 697:1900] #Nome e ass
    img_res = img_qdr[5:500, 40:1900]
    img_res = cv2.cvtColor(img_res, cv2.COLOR_BGR2GRAY)

    # Normalize and threshold image
    res, im = cv2.threshold(img_res, 164, 255, cv2.THRESH_BINARY_INV)

    # Fill everything that is the same colour (black) as top-left corner with white
    cv2.floodFill(im, None, (0, 0), 255)

    # Fill everything that is the same colour (white) as top-left corner with black
    cv2.floodFill(im, None, (0, 0), 0)

    imgFI = cv2.bitwise_not(im)

    # morphology operation
    kernel = np.ones((2, 2), np.uint8)
    im = cv2.dilate(im, kernel, iterations=1)
    
    #img_qdr = cv2.resize(img_qdr, (800, 200))
    #cv2.imshow("Dados do cabecalho:", img_qdr)

    cv2.imshow("Assinatura)", imgFI[0:280,100:1900])
    cv2.waitKey(0)
    
        
main()
