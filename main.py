import matplotlib.pyplot as plt

from thread import SummingThread

NUM_PROCESSES = 2

xdata = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.8, 2.1, 2.5] 
ydata = [0.0, 0.7, 0.2, 0.4, 0.3, 0.4, 0.8, 0.9, -0.1]

def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out


def devide_array(array, num):
    chunks = chunkIt(array, num)
    for i in range(1,len(chunks)-1):
        chunks[i].insert(0,chunks[i-1][-1])
        chunks[i].append(chunks[i+1][0])
    
    if num >2:
        chunks[len(chunks)-1].insert(0,chunks[i-1][-1])
        chunks[0].append(chunks[1][1])
    else: 
        chunks[1].insert(0,chunks[0][-1])
        chunks[0].append(chunks[1][1])
    return chunks

a =devide_array(xdata, NUM_PROCESSES)
b =devide_array(ydata, NUM_PROCESSES)


threading1 = []
for i in range(NUM_PROCESSES):
    threading1.append(SummingThread(a[i],b[i]))
for i in range(NUM_PROCESSES):
    threading1[i].start()
for i in range(NUM_PROCESSES):
    threading1[i].join()

plt.plot(xdata, ydata)
max_x_vals = []
max_y_vals = []
for i in range(NUM_PROCESSES):
    max_x_vals =  threading1[i].max_x_vals
    max_y_vals = threading1[i].max_y_vals
    plt.scatter(max_x_vals, max_y_vals, color='red')
  
plt.show()





