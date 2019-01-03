import cv2
from numpy import array
from heapq import *
from numpy import*



image=cv2.imread('NewThinned.png',0)
image2=cv2.imread('NewThinned.png')
new_A=empty((image.shape[0],image.shape[1]),None)
#print(image[81,137], image[81,278])

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if image[i][j]>=100:
            new_A[i][j]=1
            image[i][j]=255
        else:
            new_A[i][j]=0
            image[i][j]=0

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def astar(array, start, goal):

    neighbors = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start:heuristic(start, goal)}
    oheap = []

    heappush(oheap, (fscore[start], start))
    while oheap:
        
        current = heappop(oheap)[1]
    
        if current == goal:
   
            data = []
            pos=0
             #print("Working2")
            while current in came_from:                                        
                data.append(current)
                pos=pos+1
                image2[current[0],current[1]]=[0,250,0]
                current = came_from[current]
            return data

        close_set.add(current)
        
        for i, j in neighbors:
             #print("For loop Working")
            neighbor = current[0] + i, current[1] + j            
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < array.shape[0]:
                 #print("1")
                if 0 <= neighbor[1] < array.shape[1]:       
                     #print("2")         
                    if array[neighbor[0]][neighbor[1]] >= 1:
                         #print("3",neighbor[0],neighbor[1])
                        if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                            continue
                        elif tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                            came_from[neighbor] = current
                            gscore[neighbor] = tentative_g_score
                            fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                            heappush(oheap, (fscore[neighbor], neighbor))                        
                else:
                    # array bound y walls
                     #print("Y walls")
                    continue

            else:
                # array bound x walls
                 #print("X walls")
                continue
                
            
                
                
            
                
                
    return False



#plug in the starting and ending coordinates in next line
print (astar(image,(634,115),(483,1232)))
cv2.imshow("img",image)
cv2.imshow("img2",image2)
cv2.waitKey(0)
