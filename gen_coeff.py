import numpy as np
import scipy.signal as signal
import pylab as pl

# Calculate the coefficients for a pure fixed point
# integer filter

# sampling rate
fs = 24000

# cutoffs
f1 = 300
f2 = 2700

# scaling factor in bits
q = 14
# scaling factor as facor...
scaling_factor = 2**q

# let's generate a sequence of 2nd order IIR filters
#sos = signal.butter(2,[f1/fs*2,f2/fs*2],'pass',output='sos')
sos = signal.cheby1(3,0.2,[f1/fs*2,f2/fs*2],'bandpass',output='sos')

sos = np.round(sos * scaling_factor)

# print coefficients
for biquad in sos:
    for coeff in biquad:
        print(int(coeff),",",sep="",end="")
    print(q)

# plot the frequency response
b,a = signal.sos2tf(sos)
w,h = signal.freqz(b,a)
pl.plot(w/np.pi/2*fs,20*np.log(np.abs(h)))
pl.xlabel('frequency/Hz');
pl.ylabel('gain/dB');
pl.ylim(top=1,bottom=-20);
pl.xlim(left=250, right=12000);
pl.show()
