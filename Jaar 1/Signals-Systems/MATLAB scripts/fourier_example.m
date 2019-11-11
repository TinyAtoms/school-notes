t = 0:0.1:10;
N = 50;

T = 5;
w= (2 * pi)/T;
result = zeros(1, 101);
for n=1:N
    an = (sin(n*w)*4)/ (n * w);
    bn = (1-cos(n*w)*4)/(n*w);
    fill = n.*w.*t;
     result = result + cos(fill) .* an + sin(fill) .* an;
end
result = result + 2;
plot(t, result)