import threading


class SummingThread(threading.Thread):
    def __init__(self,arrX,arrY):
        super(SummingThread, self).__init__()
        self.arrX=arrX
        self.arrY=arrY
        self.max_x_vals = []
        self.max_y_vals = []


    def run(self):
        max_indices=[]
        for i in range(1,len(self.arrY)-1):   
           if self.arrY[i]>self.arrY[i-1] and self.arrY[i]>self.arrY[i+1]:
               max_indices.append(i)
        for j in max_indices:
           self.max_x_vals.append(self.arrX[j])
           self.max_y_vals.append(self.arrY[j])




