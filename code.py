# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
    
from tkinter import *    
    

def mlq():
    win.withdraw()
#    p1.update()
    p1.deiconify()
#    w.lower()
#    x.lower()
#    print("mlq")
    n=int(entry.get())
#    print(n)
    p = [i for i in range(n)]
#    print(p)
    bt=entry2.get().split()
    bt = list(map(int,bt))
#    print(bt)
    su=entry3.get().split()
    su = list(map(int, su))
#    print(su)
    wt=[i*0 for i in range(n)]
    tat=[i*0 for i in range(n)]
    plt.xlim([0, 50])
    plt.ylim([0, 100])
    plt.xticks(np.arange(sum(bt)+4, step=1))
    plt.yticks(np.arange(0, step=1))
    mng = plt.get_current_fig_manager()
    mng.resize(700,400)
    for i in range(n):
        for k in range(i+1,n):
            #for(k=i+1k<nk++)
            if su[i] > su[k]:
                temp=p[i]
                p[i]=p[k]
                p[k]=temp
                temp=bt[i]
                bt[i]=bt[k]
                bt[k]=temp
                temp=su[i]
                su[i]=su[k]
                su[k]=temp
    
    w.lower()
    x.lower()

    wtavg =  0
    wt[0] = 0
    tatavg =  bt[0]
    tat[0] = bt[0]
    
    for i in range(1,n):
        wt[i] =wt[i-1]+  bt[i-1]
        tat[i] =tat[i-1]+ bt[i]
        wtavg += wt[i]
        tatavg +=  tat[i]
         
    plt.annotate(("PROCESS  SYSTEM/USER  BURST TIME  WAITING TIME  TURNAROUND TIME"),(1,90))
    plt.xlabel("TIME")
    plt.annotate(("GANTT CHART"),(1,16))
    
    for i in range(n):
        plt.annotate(p[i],(3,85-i*6))
        plt.annotate(su[i],(9,85-i*6))
        plt.annotate(bt[i],(15,85-i*6))
        plt.annotate(wt[i],(22,85-i*6))
        plt.annotate(tat[i],(30,85-i*6))
#        plt.annotate(str(p[i])+str(su[i])+str(bt[i])+str(wt[i])+str(tat[i]),(x1+3,85-i*6))
        plt.broken_barh([(wt[i],bt[i])],(0,12),edgecolors='black',facecolor='white')
        plt.annotate("P"+str(p[i]),(tat[i]-2,5),size='13')
        if(i==n-1):
            plt.annotate("Average Waiting Time is",(1,35),)
            plt.annotate("Average Turnaround Time is",(1,30))
            plt.annotate(str(wtavg/n)+"ms",(15,35))
            plt.annotate(str(tatavg/n)+"ms",(15,30))       
            
        plt.waitforbuttonpress()
#        plt.draw()

    
    plt.draw()
    plt.close()
    exit(1)

def hrrn():
    print("hrrn")  
    win.withdraw()
    p2.update()
    p2.deiconify()    
    name=[i*0 for i in range(5)]
    at=[i*0for i in range(5)]
    bt=[i*0 for i in range(5)]
    ct=[i*0 for i in range(5)]
    wt=[i*0 for i in range(5)]
    tt=[i*0 for i in range(5)]
    completed=[i*0 for i in range(5)]
    ntt=[i*0 for i in range(5)]
    
    
    
    
    
    # Sorting Processes by Arrival Time 
    def sortByArrival():
        
         
        for i in range(0,n-1):
            for j in range(i+1,n):
                             
                if at[i] > at[j]:  
    
                    # Swap earlier process to front 
                    temp = at[i] 
                    at[i] = at[j] 
                    at[j] = temp
    
                    temp = bt[i] 
                    bt[i] = bt[j] 
                    bt[j] = temp
    
                    temp = ct[i] 
                    ct[i] = ct[j] 
                    ct[j] = temp
    
                    temp = wt[i] 
                    wt[i] = wt[j] 
                    wt[j] = temp
    
                    temp = tt[i] 
                    tt[i] = tt[j] 
                    tt[j] = temp
    
                    temp = completed[i] 
                    completed[i] = completed[j] 
                    completed[j] = temp
    
                    temp2 = ntt[i] 
                    ntt[i] = ntt[j] 
                    ntt[j] = temp2
    
                    temp3 = name[i] 
                    name[i] = name[j] 
                    name[j] = temp3
    
                     
    
    sum_bt = 0 
    avgwt = 0
    avgtt = 0 
    #n =int(input("Enter No of process\n"))
    n=int(entry7.get())
    c=0
    #arriv =[int(a) for a in input("Enter arrival time\n").split() ]
    #
    #burst =[int(b) for b in input("Enter burst time\n").split()]
    
#    arriv= [ 0, 2, 4, 6, 8] 
    
 
    burst=entry8.get().split()
    burst = list(map(int,burst))
        
    print(bt)
    arriv=entry9.get().split()
    arriv = list(map(int, arriv))
    for i in range(n):
          
        name[i] += c 
        c+=1
        at[i] = arriv[i] 
        bt[i] = burst[i] 
        completed[i] = 0 
        sum_bt += bt[i]
    
    plt.xlim([0, 50])
    plt.ylim([0, 100])
    plt.xticks(np.arange(sum(bt)+5, step=1))
    plt.yticks(np.arange(0, step=1))
    plt.xlabel("TIME")
    mng = plt.get_current_fig_manager()
    mng.resize(700,400)
    
#    fig= plt.figure(figsize=(10,10))
#    fig.set_size_inches([2,8],forward=True)    
#    fig.resize(500,500)
    sortByArrival() 
    plt.annotate("PROCESS  ARRIVAL TIME  BURST TIME  WAITING TIME  TURNAROUND TIME   RESPONSE RATIO",(1,90))
    #t=at[0]
    flag=0
    a=bt[0]
    x=1
    for t in range(n):
        
    #    for i in range(n):
            #(t = at[i] t < sum_bt):
        t=at[i]
     
        hrr = -9999 
        for i in range(n):
            if at[i] <= t and completed[i] != 1:
            
                temp = (bt[i] + (t - at[i])) / bt[i] 
                if hrr < temp:
                    hrr = temp 
                    loc = i 
                 
             
         
    
    # Up dating time value 
        t += bt[loc] 
    
    # Calculation of waiting time 
        wt[loc] = t -at[loc] - bt[loc] 
    
    # Calculation of Turn Around Time 
        tt[loc] = t - at[loc] 
    
    # Sum Turn Around Time for average 
        avgtt += tt[loc] 
    
    # Calculation of Normalized Time 
        ntt[loc] = (tt[loc] / bt[loc]) 
    
    # Updating Completion Status 
        completed[loc] = 1 
    
    # Sum Waiting Time for average 
        avgwt += wt[loc] 
    
    #    print("\n", name[loc],"\t\t", at[loc],"\t\t",bt[loc],"\t\t",wt[loc],"\t\t",tt[loc],"\t\t",ntt[loc]) 
    ##    for i in range(n):
    #    if flag==0:
    #        plt.broken_barh([(0,bt[i])],(0,1),edgecolors='black',facecolor='white')
    #    
    #        flag+=1
    #    else:
    ##        a=bt[i]
    #        plt.broken_barh([(a-1,bt[i])],(0,1),edgecolors='black',facecolor='white')
    ##        a=bt[i]
    #             
    #    plt.annotate("P"+str(name[i]),(bt[i],0.3),size='13')
    #    plt.waitforbuttonpress().
    #    plt.show(block=False) 
    #    for i in range(n):    
     
#    plt.annotate((name[loc],at[loc],bt[loc],wt[loc],tt[loc],ntt[loc]),(1,19-i*2 ))    
    for i in range(n):
       if flag==0:
           plt.broken_barh([(0,bt[i])],(0,25),edgecolors='black',facecolor='white')
           a=+bt[i] 
           flag+=1
       else:
    #       a+=bt[i]
           plt.broken_barh([(a,bt[i])],(0,25),edgecolors='black',facecolor='white')
           a+=bt[i]
       plt.annotate(name[i],(x+2,(80-i*6)))
       plt.annotate(at[i],(x+7,(80-i*6)))  
       plt.annotate(bt[i],(x+13,(80-i*6)))  
       plt.annotate(wt[i],(x+20,(80-i*6)))  
       plt.annotate(tt[i],(x+28,(80-i*6)))  
       plt.annotate(ntt[i],(x+38,(80-i*6)))       
       plt.annotate("P"+str(name[i]),(a-1.7,12),size='13')
       if(i==n-1):
            plt.annotate("Average waiting time:",(1,17)) 
            plt.annotate("Average Turn Around time:\n",(1,15))
            plt.annotate(avgwt / n,(15,18)) 
            plt.annotate(avgtt / n,(15,15))
       plt.waitforbuttonpress()
#       plt.show(block=False) 
#    3 5 8 10. 514
 
    plt.close() 
   
#    win=Tk()
#    w=Button(win,text='mlq',command=mlq)
#    w.pack()    
#    x=Button(win,text='hrrn',command=hrrn)
#    x.pack()
#    v = StringVar()
#    entry = Entry(win, textvariable=v)
#    entry.pack()
#    v1 = StringVar()
#    entry1 = Entry(win, textvariable=v1)
#    entry1.pack()
#    v2 = StringVar()
#    entry2 = Entry(win, textvariable=v2)
#    entry2.pack()
win=Tk()
p1=Tk()
p2=Tk()
p1.withdraw()
p1.geometry("400x400")
p2.withdraw()
p2.geometry("500x500")
win.geometry("500x500")
w=Button(win,text='Multi Level Queue Scheduling',command=mlq)

lm=Label(win,text="OS Mini Project\nGroup Members:\n1.)Hrithik Gaikwad\n2.)Zaid Siddhique\n3.)Nikhil Raote\n")
lm.pack()
lm.place(relx=0.5, rely=0.3, anchor=CENTER)  

lm1=Label(win,text="\nScheduling algorithm Simulator\n")
lm1.pack()
lm1.place(relx=0.5, rely=0.1, anchor=CENTER) 
l=Label(p1,text="Enter the number of processes")
l.pack()
l.place(relx=0.5, rely=0.25, anchor=CENTER)  

l1=Label(p1,text="Enter the burst time tof the processes seperated by a ','")
l1.pack()
l1.place(relx=0.5, rely=0.35, anchor=CENTER)

l2=Label(p1,text="Enter the value of processes User=1 or System=0")
l2.pack()
l2.place(relx=0.5, rely=0.45, anchor=CENTER)  

w.pack()
w.place(relx=0.5, rely=0.6, anchor=CENTER)    
x=Button(win,text='Highest Reponse Ratio Next Scheduling',command=hrrn)
x.pack()
x.place(relx=0.5, rely=0.7, anchor=CENTER)
x1=Button(p1,text='Begin MLQ Scheduling',command=mlq)
x1.pack()
x1.place(relx=0.5, rely=0.9, anchor=CENTER)
x2=Button(p2,text='Begin  HRRN Scheduling',command=hrrn)
x2.pack()
x2.place(relx=0.5, rely=0.9, anchor=CENTER)
l1=Label(p2,text="Enter the burst time of the processes seperated by a ','")
l1.pack()
l1.place(relx=0.5, rely=0.25, anchor=CENTER)
l2=Label(p2,text="Enter the no of processes")
l2.pack()
l2.place(relx=0.5, rely=0.15, anchor=CENTER) 
l2=Label(p2,text="Enter the arrival time of process")
l2.pack()
l2.place(relx=0.5, rely=0.35, anchor=CENTER) 
v = StringVar()
entry = Entry(p1, textvariable=v)
entry.pack()
entry.place(relx=0.5, rely=0.3, anchor=CENTER) 
v2 = StringVar() 
entry2 = Entry(p1, textvariable=v2)
entry2.pack()
entry2.place(relx=0.5, rely=0.4, anchor=CENTER) 
v7 = StringVar()
entry7 = Entry(p2, textvariable=v7)
entry7.pack()
entry7.place(relx=0.5, rely=0.2, anchor=CENTER)
v8 = StringVar()
entry8 = Entry(p2, textvariable=v8)
entry8.pack()
entry8.place(relx=0.5, rely=0.3, anchor=CENTER)

v9 = StringVar()
entry9 = Entry(p2, textvariable=v9)
entry9.pack()
entry9.place(relx=0.5, rely=0.4, anchor=CENTER)
v3 = StringVar()
entry3 = Entry(p1, textvariable=v3)
entry3.pack()
entry3.place(relx=0.5, rely=0.5, anchor=CENTER) 

win.mainloop()
