import cv2
font=cv2.FONT_HERSHEY_COMPLEX
font2=cv2.FONT_HERSHEY_SIMPLEX


img=cv2.imread('white.jpg')
print(img.shape)
img=cv2.resize(img,(1800,900))

img=cv2.rectangle(img,(180,20),(340,180),(200,50,100),-1)
img=cv2.rectangle(img,(180,184),(340,344),(200,50,100),-1)
img=cv2.putText(img,'1',(240,122),font,2,(255,255,255),2)
img=cv2.circle(img,(260,264),10,(255,255,255),-1)

img=cv2.rectangle(img,(230*2,10*2),(310*2,90*2),(0,200,0),-1)
img=cv2.rectangle(img,(230*2,92*2),(310*2,172*2),(0,200,0),-1)
img=cv2.putText(img,'2',(520,122),font,2,(255,255,255),2)
a=540
b=264
img=cv2.circle(img,(a+25,b),10,(255,255,255),-1)
img=cv2.circle(img,(a-25,b),10,(255,255,255),-1)

img=cv2.rectangle(img,(370*2,10*2),(450*2,90*2),(0,0,200),-1)
img=cv2.rectangle(img,(370*2,92*2),(450*2,172*2),(0,0,200),-1)
img=cv2.putText(img,'3',(800,122),font,2,(255,255,255),2)
a=370+450
img=cv2.circle(img,(a+30,b-30),10,(255,255,255),-1)
img=cv2.circle(img,(a,b),10,(255,255,255),-1)
img=cv2.circle(img,(a-30,b+30),10,(255,255,255),-1)

img=cv2.rectangle(img,(510*2,10*2),(590*2,90*2),(0,250,150),-1)
img=cv2.rectangle(img,(510*2,92*2),(590*2,172*2),(0,250,150),-1)
img=cv2.putText(img,'4',(1080,122),font,2,(255,255,255),2)
a=510+590
img=cv2.circle(img,(a+30,b-30),10,(255,255,255),-1)
img=cv2.circle(img,(a+30,b+30),10,(255,255,255),-1)
img=cv2.circle(img,(a-30,b-30),10,(255,255,255),-1)
img=cv2.circle(img,(a-30,b+30),10,(255,255,255),-1)

img=cv2.rectangle(img,(650*2,10*2),(730*2,90*2),(150,150,0),-1)
img=cv2.rectangle(img,(650*2,92*2),(730*2,172*2),(150,150,0),-1)
img=cv2.putText(img,'5',(1360,122),font,2,(255,255,255),2)
a=650+730
img=cv2.circle(img,(a+30,b-30),10,(255,255,255),-1)
img=cv2.circle(img,(a+30,b+30),10,(255,255,255),-1)
img=cv2.circle(img,(a,b),10,(255,255,255),-1)
img=cv2.circle(img,(a-30,b-30),10,(255,255,255),-1)
img=cv2.circle(img,(a-30,b+30),10,(255,255,255),-1)

img=cv2.rectangle(img,(790*2,10*2),(870*2,90*2),(250,0,50),-1)
img=cv2.rectangle(img,(790*2,92*2),(870*2,172*2),(250,0,50),-1)
img=cv2.putText(img,'6',(1640,122),font,2,(255,255,255),2)
a=790+870
img=cv2.circle(img,(a,b+25),10,(255,255,255),-1)
img=cv2.circle(img,(a,b-25),10,(255,255,255),-1)
img=cv2.circle(img,(a+50,b+25),10,(255,255,255),-1)
img=cv2.circle(img,(a+50,b-25),10,(255,255,255),-1)
img=cv2.circle(img,(a-50,b+25),10,(255,255,255),-1)
img=cv2.circle(img,(a-50,b-25),10,(255,255,255),-1)

img=cv2.rectangle(img,(870,560),(1030,720),(200,50,100),-1)
img=cv2.circle(img,(950,640),10,(255,255,255),-1)

img=cv2.rectangle(img,(870,398),(1030,558),(0,200,0),-1)
a=(870+1030)//2
b=(398+558)//2
img=cv2.circle(img,(a+25,b),10,(255,255,255),-1)
img=cv2.circle(img,(a-25,b),10,(255,255,255),-1)

img=cv2.rectangle(img,(708,560),(868,720),(0,0,200),-1)
a=(708+868)//2
b=(560+720)//2
img=cv2.circle(img,(a+30,b-30),10,(255,255,255),-1)
img=cv2.circle(img,(a,b),10,(255,255,255),-1)
img=cv2.circle(img,(a-30,b+30),10,(255,255,255),-1)

img=cv2.rectangle(img,(1032,560),(1192,720),(0,250,150),-1)
a=(1032+1192)//2
b=(560+720)//2
img=cv2.circle(img,(a+30,b-30),10,(255,255,255),-1)
img=cv2.circle(img,(a+30,b+30),10,(255,255,255),-1)
img=cv2.circle(img,(a-30,b-30),10,(255,255,255),-1)
img=cv2.circle(img,(a-30,b+30),10,(255,255,255),-1)

img=cv2.rectangle(img,(870,722),(1030,882),(150,150,0),-1)
a=(870+1030)//2
b=(722+882)//2
img=cv2.circle(img,(a+30,b-30),10,(255,255,255),-1)
img=cv2.circle(img,(a+30,b+30),10,(255,255,255),-1)
img=cv2.circle(img,(a,b),10,(255,255,255),-1)
img=cv2.circle(img,(a-30,b-30),10,(255,255,255),-1)
img=cv2.circle(img,(a-30,b+30),10,(255,255,255),-1)

img=cv2.rectangle(img,(546,560),(706,720),(250,0,50),-1)
a=(546+706)//2
b=(560+720)//2
img=cv2.circle(img,(a,b+25),10,(255,255,255),-1)
img=cv2.circle(img,(a,b-25),10,(255,255,255),-1)
img=cv2.circle(img,(a+50,b+25),10,(255,255,255),-1)
img=cv2.circle(img,(a+50,b-25),10,(255,255,255),-1)
img=cv2.circle(img,(a-50,b+25),10,(255,255,255),-1)
img=cv2.circle(img,(a-50,b-25),10,(255,255,255),-1)

img=cv2.putText(img,'SOUMITRA NAIK',(1450,745),font2,1,(0,0,0),2)
img=cv2.putText(img,'122CS0318',(1450,775),font2,1,(0,0,0),2)
img=cv2.putText(img,'version-  '+ cv2.__version__,(1450,810),font2,1,(0,0,0),2)


cv2.imwrite('final.png',img)

 