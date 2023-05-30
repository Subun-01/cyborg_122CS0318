'''
*********************************************************************************
*
*        		===============================================
*           		        CYBORG OPENCV TASK 2
*        		===============================================
*
*
*********************************************************************************
'''

# Author Name:		[SOUMITRA NAIK]
# Roll No:			[122CS0318]
# Filename:			task_2_SoumitraNaik.py
# Functions:		detect_arena_parameters
# 					[ detect_arena_parameters() ]


####################### IMPORT MODULES #######################
   ## You are free to make any changes in this section. ##
##############################################################
import cv2
import numpy as np
##############################################################
def detect_arena_parameters(maze_0):

		img = maze_0
		"""
		Purpose:
		---
		This function takes the image as an argument and returns a dictionary
		containing the details of the different arena parameters in that image

		The arena parameters are of four categories:
		i) traffic_signals : list of nodes having a traffic signal
		ii) horizontal_roads_under_construction : list of missing horizontal links
		iii) vertical_roads_under_construction : list of missing vertical links
		iv) medicine_packages : list containing details of medicine packages
		v)start_node : list containing the start node

		These four categories constitute the four keys of the dictionary

		Input Arguments:
		---
		`maze_image` :	[ numpy array ]
				numpy array of image returned by cv2 library
		Returns:
		---
		`arena_parameters` : { dictionary }
				dictionary containing details of the arena parameters
		
		Example call:
		---
		arena_parameters = detect_arena_parameters(maze_image)
		"""    
		# arena_parameters = {}

		##############	ADD YOUR CODE HERE	##############


		#traffic
		traffic=[]


		low=np.array([0,0,200])
		up=np.array([0,0,255])
		mask = cv2.inRange(img, low, up)
		result = cv2.bitwise_and(img, img, mask = mask)
		grey=cv2.cvtColor(result,cv2.COLOR_BGR2GRAY)

		xco={100:'A',200:'B', 300:'C', 400:'D', 500:'E', 600:'F', 700:'G'}
		yco={100:'1',200:'2', 300:'3', 400:'4', 500:'5', 600:'6', 700:'7'}


		contours,_ = cv2.findContours(grey, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		# print(contours)
		for cnt in contours:
			
			x,y,w,h=cnt
			# print(x)
			# print(y)
			xax=(x[0][0]+6)
			yax=(x[0][1]+6)
			z=str(xco[xax] + yco[yax])
			traffic.append(z)
		
			
		traffic.sort()


		#start
		start=[]
		low=np.array([0,200,0])
		up=np.array([0,255,0])
		mask = cv2.inRange(img, low, up)
		result = cv2.bitwise_and(img, img, mask = mask)
		grey=cv2.cvtColor(result,cv2.COLOR_BGR2GRAY)
		contours,_ = cv2.findContours(grey, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		for cnt in contours:
			approx=cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
            
			if len(approx)==4: 
				x1,y1,w1,h1=cv2.boundingRect(cnt)
				if w1==13:
					a = [str(xco[x1+6]+yco[y1+6])]
				


		#medicine
		pix=[]
		p=100
		for x in range(6):
			Shop_1=img[110:190,10+p:90+p]
			#   cv2.imshow("new",Shop_1)
			#   cv2.waitKey(0)
			gray=cv2.cvtColor(Shop_1,cv2.COLOR_BGR2GRAY)
			adaptive_thresh=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,5)
			contours2,hierarchy2=cv2.findContours(adaptive_thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)





			if len(contours2)==0:
				pass
			
			else:

					for cnt in contours2:
				

						approx=cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
						if len(approx)==4 :

								x2,y2,w2,h2=cv2.boundingRect(cnt)
								if w2==21:
									
									(b,g,r)=img[y2+120,x2+20+p]
									l1=(b,g,r)

									if l1==(255,255,0):
							
											u1=[f'Shop_{(p//100)}','Skyblue','Square',[x2+20+p,y2+120]]
											pix.append(u1)


									elif l1==(180,0,255):
											u2=[f'Shop_{(p//100)}','Pink','Square',[x2+20+p,y2+120]]
											pix.append(u2)


									elif l1==(0,127,255):
											u3=[f'Shop_{(p//100)}','Orange','Square',[x2+20+p,y2+120]]
											pix.append(u3)
						
									elif l1==(0,255,0):
											u4=[f'Shop_{(p//100)}','Green','Square',[x2+20+p,y2+120]]
											pix.append(u4)


						elif len(approx)==3:
									M=cv2.moments(cnt)
									cX=int(M['m10']/M['m00'])
									cY=int(M['m01']/M['m00'])
									(b,g,r)=img[cY+110,cX+10+p]
									l1=(b,g,r)
						
									if l1==(255,255,0):
							
										u5=[f'Shop_{(p//100)}','Skyblue','Triangle',[cX+10+p,cY+111]]
										pix.append(u5)

									elif l1==(180,0,255):
										u6=[f'Shop_{(p//100)}','Pink','Triangle',[cX+10+p,cY+111]]
										pix.append(u6)
									elif l1==(0,127,255):
										u7=[f'Shop_{(p//100)}','Orange','Triangle',[cX+10+p,cY+111]]
										pix.append(u7)
						
									elif l1==(0,255,0):
										u8=[f'Shop_{(p//100)}','Green','Triangle',[cX+10+p,cY+111]]
										pix.append(u8)

				
						else:

									(x, y), radius = cv2.minEnclosingCircle(cnt)
									center = (int(x), int(y))
									radius = int(radius)
									(b,g,r)=img[int(y)+110,int(x)+10+p]
									l1=(b,g,r)

				
									if l1==(255,255,0):

										u9=[f'Shop_{(p//100)}','Skyblue','Circle',[int(x)+10+p,int(y)+110]]
										pix.append(u9)

									elif l1==(180,0,255):
										u10=[f'Shop_{(p//100)}','Pink','Circle',[int(x)+10+p,int(y)+110]]
										pix.append(u10)


									elif  l1==(0,127,255):
										u11=[f'Shop_{(p//100)}','Orange','Circle',[int(x)+10+p,int(y)+110]]
										pix.append(u11)


						
									elif l1==(0,255,0):
										u12=[f'Shop_{(p//100)}','Green','Circle',[int(x)+10+p,int(y)+110]]
										pix.append(u12)
				


			p=p+100

		pix.sort()
		arena_parameters={'traffic_signals':traffic,'start_node':a,'medicine_packages_present':pix}
		##################################################
		return arena_parameters

