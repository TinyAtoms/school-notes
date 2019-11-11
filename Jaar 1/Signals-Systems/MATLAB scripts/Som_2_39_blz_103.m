% Som_2_39_blz_103.m
clc;clear;clf('reset');
T=0.1;   % stepsize 'numerieke rechthoeks regel'
t=0:T:17;
x=stepfun(t,0);
h=(0.6).^t.*stepfun(t,0);
y=T*conv(x,h);
t0=(0:340)*T;
plot(t0,y, t, h, t, x);
xlabel('Time(s)');
ylabel('Response y(t)');


