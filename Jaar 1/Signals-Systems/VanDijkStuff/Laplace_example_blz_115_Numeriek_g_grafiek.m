% Laplace_example_blz_115_Numeriek_g_grafiek.m
clc;clear;clf('reset');
t=0:0.01:10;
g=stepfun(t-3,0)-stepfun(t-4,0);
plot(t,g);
dim=[.2 .5 .3 .3];
str='g(t)=u(t-3)-u(t-4)';
annotation('textbox',dim,'String',str,'FitBoxToText','on');
xlabel('t');
ylabel('g(t)');