% Ex_2_1_conv_x_y_grafiek.m
clc;clear;clf('reset');
t=0:0.01:4;
z=2.*(t.^2).*sqrt(pi) +   sqrt(pi);
plot(t,z);
dim=[.2 .5 .3 .3];
str='z(t)= x(t)  conv  y(t)=2(t^2)sqrt(pi) +  sqrt(pi)';
annotation('textbox',dim,'String',str,'FitBoxToText','on');