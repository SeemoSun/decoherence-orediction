
#A test for Gaussian SPECTRUM ALL

import numpy as np
import matplotlib.pyplot as plt
import math


def signal_generator(freq_cor,freq_spec,tlist):
    size = freq_cor.size
    t = tlist.size
    noise = np.zeros(t)
    rap = np.zeros(size)
    if size % 2 == 1:
        i=int((size-1)/2)
    else:  i=int(size/2)  
    rap1 = np.random.rand(i)
    rap[0:i] =rap1
    rap[size-i:size] = -np.flip(rap1)
    for tl in range(t):
        noise[tl]=np.sum((freq_spec)*np.cos(2*np.pi*freq_cor*tlist[tl]+2*np.pi*rap))
    return noise

def Gspectrum_generator(freq_cor,bandw,center,A):
    freq_spec = np.zeros(freq_cor.size)
    for i in range(center.size):
        freq_spec=freq_spec+ A[i]*np.exp(-((freq_cor-center[i])/bandw[i])**2)+A[i]*np.exp(-((freq_cor+center[i])/bandw[i])**2)
    return freq_spec


def Ispectrum_generator(freq_cor,A):
    freq_spec=A*1./np.abs(freq_cor)
    return freq_spec

def Spectrum_c_reader(f):
    f0 = open(f,'r')
    right = (np.genfromtxt(f0,delimiter=','))[:,0]
    left = -np.flip(right) 
    freq_cor = np.append(left,right[1:np.size(right)])
    return freq_cor

def Spectrum_i_reader(f):
    f0 = open(f,'r')
    right = 10**(((np.genfromtxt(f0,delimiter=','))[:,1])/20)
    left = np.flip(right)
    freq_spec=np.append(left,right[1:np.size(right)])
    return freq_spec

class test:
    fidelity=[]
    def __init__(self,test_time,pulse_mode,freq_cor,freq_spec,t_list):
        self.iteration = test_time
        self.pulse_mode=pulse_mode  # 0 is RP pulse, 1 is DDP pulse
        self.freq_cor = freq_cor
        self.freq_spec = freq_spec
        self.t_list = t_list
        self.d_t = t_list[t_list.size-1]/t_list.size
    def run(self,noise_tlist):
        t = (self.t_list).size
        t2= noise_tlist.size
        delta_t = noise_tlist[t2-1]/t2
        self.fidelity = np.zeros(t)
        for ts in range(self.iteration):
          noise = signal_generator(self.freq_cor,self.freq_spec,noise_tlist)
          #plt.plot(noise_tlist,noise)
          #plt.show()
          if self.pulse_mode==0:
            for i in range(t):
                fi = int((i-1)*self.d_t/delta_t+1)
                self.fidelity[i] = self.fidelity[i] + (np.cos(delta_t*np.sum(noise[0:fi]))+1)/2
          else:
            for i in range(t):
                fi = int((i-1)*self.d_t/delta_t+1)
                self.fidelity[i] = self.fidelity[i] + (np.cos(delta_t*np.sum(noise[0:i]-noise[i:2*i]))+1)/2
        self.fidelity = self.fidelity/self.iteration
    def deco_time(self,bound):
        tmax = (self.fidelity).size
        for i in range(tmax):
            if self.fidelity[i]<bound:
                return (i+1)*self.d_t
        return (tmax+1)*self.d_t
    def get_fidelity(self):
        c=self.fidelity
        return c
    def get_final_fidelity(self,noise_tlist):
        t=(self.t_list).size
        t2= noise_tlist.size
        delta_t = noise_tlist[t2-1]/t2
        fidel=0
        for ts in range(self.iteration):
           noise = signal_generator(self.freq_cor,self.freq_spec,noise_tlist)
          #plt.plot(noise_tlist,noise)
          #plt.show()
           if self.pulse_mode==0: fidel = fidel+(math.cos(delta_t*np.sum(noise[0:t]))+1)/2
           else: fidel =fidel + (math.cos(delta_t*np.sum(noise[0:t]-noise[t:2*t]))+1)/2
        return fidel/self.iteration

       
       
		
class t_spct_cordint:
	delta_t=0
	mode = 0
	t_cor =[]
	f_cor =[]
	def __init__(self,delta_t,grid_n,mode):
		self.delta_t = delta_t
		self.size = grid_n
		self.mode = mode
	def generate_cor(self):
		if self.mode ==0:
			self.t_cor = np.linspace(0,self.delta_t*(self.size-1),self.size)
			self.f_cor = np.linspace(-1/(2*self.delta_t*(self.size-1)),1/(2*self.delta_t*(self.size-1)),self.size)
		else: 
			self.f_cor = np.linspace(-self.delta_t*(self.size-1)/2,self.delta_t*(self.size-1)/2,self.size)
			self.t_cor = np.linspace(0,1/(self.delta_t*(self.size-1))*(self.size-1),self.size)
	def get_t_cor(self):
		return self.t_cor
	def get_f_cor(self):
		return self.f_cor
    

    #def plot_process(self)
	#def plot_deco_time(self)


# basic settings
# time unit is mili seconds, frequency unit is kHz



#test_time = 50

#rwtl = 100                          #simpling points on timeline in 2ms  
#rtl = np.linspace(0,0.00005,rwtl)   #different waiting time to use
#dwtl = 50
#dtl = np.linspace(0,0.000025,dwtl)
                                    #doing the experiment 200 times for average value  