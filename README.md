# decoherence-orediction
This is a simple python module used for dynamical coupling and ramsey pulse sequence with noise presence

## Usage:

 import dep 

## Functions:
 - signal_generator(freq_cor,freq_spec,tlist)
 
   take 3 args, data type being arrays: freq_cor,freq_spec,tlist; output an array of noise intenstiy according to the "tlist" simpling points.
 
 - Gspectrum_generator(freq_cor,bandw,center,A)
 
    take 4 args, data type being arrays: freq_cor,bandw,center,A; output an array of noise spectrum intensity with Gaussian shape at designated frequency center(value at "center" list) with designated width(value at "bandw" list) and intensity(value at "A" list),according to the "freq_cor" sampling points.
  
 - Ispectrum_generator(freq_cor,A)
 
    take 2 args, data type being arrays:freq_cor,data type being float:A ; output an array of noise spectrum intenstiy with 1/f shape with designated amplitude according to the "freq_cor" sampling points.
    
 - Spectrum_c_reader(f)
 
    take 1 args, data type being string:f; open txt file with name 'f'; output an array of frequency coordinate.
   
 - Spectrum_i_reader(f)
 
    take 1 args, data type being string:f; open txt file with name 'f'; output an array of spectrum intensity.
 
 ## Classes:
 ### test
 Attributes:
 
 - fidelity: array, record the population at spin up state after a dynamical decoupling/ramsey pulse sequence.
 
 - test_time: int, repetition times
 
 - pulse_mode: int, 0(1) refer to Ramsey(dynamical decoupling) pulse sequence
 
 - freq_cor: array, noise spectrum coordinate
 
 - freq_spec: array, noise spectrum intensity
 
 - t_list: time sampling points during experiment 
 
Functions:

 - def __init__(self,test_time,pulse_mode,freq_cor,freq_spec,t_list) 
   
   initialize a test objective
   
 - run(self,noise_tlist)
 
   be called from an ojective in "test" class, take in 1 args, data type being arrays:noise_tlist, for expressing the timeline of how noise spectrum is measured.
   
   no output directly, simulation results stored in "fidelity" list.
   
 - deco_time(self,bound):
 
   be called from an ojective in "test" class, take in 1 args, data type being float: bound, for expressing the lowest fidelity(population) you can accept as non-decoherent. 
   
   return to the time point in "t_list" that fidelity drops to be lower than "bound"
 
 - get_fidelity(self):
   
   be called from an ojective in "test" class, take in 0 args, return to the fidelity list according to experiemnt time.
   
  - get_final_fidelity(self,noise_tlist):
  
    the function is equal to return to the last value in the list of fidelity, but without calculating throughout the whole process.
    
 ### t_spct_cordint
 
 Attributes:
 
  - delta_t: float, could be time sampling spacing if you input a time list; could be frequency sampling spacing if you input a frequency coordiante

  - mode: int, 0(1) from time list(frequency coordinate) to get frequecny coordinate(time list) for reliable FFT result.

  - t_cor: array, time list

  - f_cor: array, frequency coordinate

Functions:

  - def __init__(self,delta_t,grid_n,mode)
     
    initialize an t_spct_cordint obejct, by returning to a list with length __grin_d__, spacing __delta_t__, and mode 0(1) if you input a time list(frequency coordinate)

  - generate_cor(self)

    call from a t_spct_cordint object
    
    From time list(frequency coordinate) to get frequecny coordinate(time list) for reliable FFT result

  - get_t_cor(self)
  
    call from a t_spct_cordint object, return to the time list you wanted(corresponding to your frequency coordinate)

  - get_f_cor(self)

    call from a t_spct_cordint object, return to the frequency coordinate you wanted(corresponding to your time list)
 
 
  
