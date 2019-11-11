% Laplace_example_blz_115_Numeriek_x_conv_g_g.m
clc;clear;clf('reset');
T=0.01;   % stepsize numerieke integratie
          % rechthoeks regel bij conv(olutie)
t=0:T:5;
g=stepfun(t-3,0)-stepfun(t-4,0);
x=T*conv(g,g);
t0=(0:1000)*T;
plot(t0,x);
dim=[.2 .5 .3 .3];
str='x(t)=conv(g(t),g(t)=r(t-6)-2r(t-7)+r(t-8)';
annotation('textbox',dim,'String',str,'FitBoxToText','on');
xlabel('t');
ylabel('x(t)');
