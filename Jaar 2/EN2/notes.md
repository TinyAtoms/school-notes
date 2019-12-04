## Sinusoid to phasor

$A sin(\omega t + \theta) = A cos(\omega t + 90 + \theta) = A \angle (\theta + 90)$  
$B cos(w t + \theta) = B \angle \theta$  

## Phasor to sinusoid 

$(-r + j4)A 5 \angle 126.87 = 5 cos(wt + 126...)$  
$j8e^{-20} = j8 \angle-20 = (1\angle90)(9\angle-20) = 8 \angle 70$   
The $(1\angle 90)$ is omdat vermenigvuldigen met j gewoon roteren met 90 is.

# Differentieeren
$$
{dv \over dt} \rightarrow j \omega V
$$

# integreren
$$
\int v dt = {1\over j\omega} V = -j {1 \over \omega} V  
$$
(delen door j is vermenigvuldigen met -j)

# Rotatie van phasors met 90
$$
A = r e^{j \theta} \rightarrow Aj = r e^{j (\theta  + 90)}
$$
Basically, vermenigvuldigen met j is phase shiften met 90 graden.

# Solving of diffEqs with phasors, example
$$
\begin{aligned}
4 \Bbb{}{I} + 8 \int i dt - 3 {di \over dt} &= 50 cos( 2 t + 75) \\
4 I + 8 {1 \over j \omega} I - 3 j \omega I &= 50 \angle 75 \\
\text{since t is 2, and dividing by j is multiplying with -j,} \\
4 I - 4 I j - 6 I j &=  50 \angle 75 \\
I (4 - 10j) &= 50 \angle 75 \\
I = {50 \angle 75 \over 4 - 10j} &= 4,64 \angle 143
\end{aligned}
$$

# Phasor relationships

| element 	| Freq domain 	| Time domain 	|
|---------	|-------------	|-------------	|
| R       	|$\mathbb{V} = R \mathbb{I}$| V = Ri|
| L       	|$\mathbb{V} = jwL \mathbb{I}$|v = L ${di \over dt}$|
| C       	|$\mathbb{V} = {I\over jwC}$|i = C $dV \over dt$|


# Impedance
$$
\begin{aligned}
    Impedance(\mathcal{Z}) &= \mathbb{V \over I} = (Z_r + Z_L +Z_C ) \Omega \\
    \text{where:} \\
    \mathcal{Z_R} &= R \\
    \mathcal{Z_L} &= j\omega L \\
    \mathcal{Z_C} &= {1 \over j \omega C}
\end{aligned}
$$
We can alsso express z in complex rectangular form ($R + j x$) where x = reactance.  
Or we could just express it as $Z = |z| \angle \theta$
