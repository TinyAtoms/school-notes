
# Hoofdstuk 3, Stochastische variabelen

Een stochast is een _kans_ variabele. DWZ dat de uikomst van deze van toeval afhangt

VB:
Je hebt een vaas met 5Z en 8W ballen, en je trekt 3 ballen zonder teruglegging. 
Je kan de volgende stochastische vars/ definieren:
1. x = aantal witte ballen die je trekt.
2. {1,2,3} = uitkomstenruimte van x.

__ER wordt een onderscheid gemaakt tussen__  
1. discrete stochastische variabelen (x is integer)
2. continue stochastische vars. De waarde van x correspodeert met alle punten in een gegeven interval. voorbeeld:  
    a. tijdsduur tussen binnenkomen 2 klanten. $0 \leq x \leq \infty $  
    b. Hoeveeel water er is in een 0.5l container. $0 \leq x \leq 0.5L$


```python

```

## Discrete stochastische variabelen

### 1. Binominale verdeling

__Eigenschappen:__  
1. Het experiment bestaat uit n identieke deelexperimenten
2. Maar 2 mogelijke uitkomsten per experiment. (JA/NEE)(Success/Misslukking) 
4. er is een verwachting (p of mu ($\mu$)), de kans op S/M voor 1 deelexperiment  
    A. P(S) = p  
    B. P(M) = q of q = 1 - p (voor als p > 0.5 is)  
6. n is aantal deelexperimenten
7. c is gewenste aantal S uitkomsten
8. Je moet het __altijd__ in de form van $X \leq k$ zetten omdat je de cumulatieve bin. waarde wilt  
    a. $P(X \lt k) = P(X \leq k - 1)$  
    b. $P(X \gt k) = 1 -  P(X \leq k)$  
    c. $P(X \leq k) = 1 -  P(X \leq k - 1)$  
    d. $P(X = k) = P(X \leq k) -  P(X \leq k - 1)$
9. Schrijfwijze is B(n,p,c)
8. $Bin(n,p,c) = \sum_{k=0}^c {n \choose k}  p^k  (1-p)^{n-k}$, zonder c soms


VB:
Je hebt 10 muntworpen. Je wilt weten wat de kans is dat er 6 of minder worpen zijn die Kruis zijn.  
p = 0.5, n = 10, c = 6.   
(antwoord is 0.8281, kijk in bin. tabel)  
Als je wilt weten wat de kans is dat er minstens 6 K worpen zijn.  
Dan kan je het anders formuleren(je kijkt altijd naar P(X <= some getal)).
Je wilt weten wat de kans is dat er hoogstens 4 M worpen zijn.  
p = 0.5, n = 10, c = 4
antw is 0.377



```python

```

## Poisson verdeling
Deze is bruikbaar voor het beschrijven van aantal gebeurtenissen dat in een bepaalde tijdsperiode/volume/gebied zal voorkomen. 
Het heeft de volgende eigenschappen:
1. het experiment bestaat uit het tellen van het aantal keren dat een bep. gebeurtenis voorkomt in een bep. tijdsinterval of gebied.  
2. er s een verwachtingswaarde bekend. (mu, $\mu$) Dit is meestal een gemiddelde over een lang periode.
3. De kans dat een gebeurtenis voorkomt is even groot voor alle gebieden of tijdsintervallen van gelijke grootte.
4. Het moet altijd in de form $P(X \leq k)$, zie hoe dit gedaan wordt bij cum. bin. verdeling
5. scrijfwijze is P($\lambda, c$) (meestal zonder  c)


vb berkening mu. Premie voor huisverzekering is USD 300. als er brand uitbreekt betaalt Asuria  USD200k. De kans op brand is 0.0002
wat is de verwachte winst/verlies voor Asuria als ze 1k premies verkopen?   

| brand | -$199.7k 	| 0.0002 |  

| geen brand | $300 | 0.9998 |

$\mu$ = (-199.7k * 0.0002) + (0.3k * .9998) = 260 

per 1000 premies = 1k * $260 = $260k




```python

```

# Continue stochastische variabelen

Deze variabelen kunnen alle mogelijke waarden in een interval aannemen.
De belangrijkste verdeling is de normaal of gaussian verdeling $N(\mu, \sigma^2)$.   
Het is de meest voorkomende kasverdeling, is symmetrisch rond de verwachting $\mu$ en de spreiding wordt bepaald door de std. $\sigma$
![image.png](attachment:image.png)
De kansverdeling van vele stochastische variabelen blijke een normale verdeling te volgen,  of althans, veel te  lijken op een normale verdeling.   
Het gaat om situaties waarbij de verdeling  symmetrisch geconcentreerd is   rond een centrale waard $\mu$ en de afweikingen van deze waarde steeds  
onwaarschijnlijker worden, naarmate de afweiking groter wordt. De normale verdeling wordt vaak gebruikt bij natuurlijk voorkomende verschijnselen en medische laboratorium testen.  

De A onder de bell curve geeft de kanswaarden aan, mar het is niet zo eenvoudig mod dit voor een bep. interval te berekenen, dus gebruiken we een tabel.  Hoewel er infinite aantal bell curves zijn(inf aantal $\mu\ en\ \sigma$), 
gebruiken we maar 1 standaard tabel die voor elke bell curve gebruikt kan worden.


Voor de standaard normale verdeling geldt: $\mu=0$ en $\sigma^2 = 1$, dus 
$$f(z) = {e^{-0.5z^2} \over \sqrt{2 \pi}}$$

## IMPORTANT AF
Je kan de tabel alleen gebruiken als $\mu = 0$ en $\sigma^2 = 1$. Is dit niet zo, dan moet het __gestandardiseerd__ worden.  
Om een normaal verdeelde variabele __x__ (random $\mu$ en $\sigma$) srandaard te maken moeten we eerst de waarde van x omrekenen naar een 
z-score. De z-score wordt zo berekend:
$$z = {x- \mu \over \sigma}$$


```python

```

## Benadering van binominale en poisson verdelingen

Soms zijn de bin. en poisson tabellen niet toepasbaar (zeer grote waarden van c, mu, enz)
Dan wordt de normale verdeling gebuikt voor het benaderen van de waarden.  
__Voor Binominale verdelingen geld het volgende__:    
1.$\mu = n \cdot p$  
2. $variantie\ \sigma^2 = n \cdot p \cdot q$  
3. $std\ \sigma = \sqrt {n p q}$  
__voor Poisson verdeling geldt:__ 
1. $verwachting\ \mu = \lambda$  
2. variantie $\sigma^2 = \lambda$
3. std $\sigma = \sqrt \lambda$  

Voor grote waarde van n geldt: (* means it needs correction because bin and pois are discrete and normal is continuous)  
binominale benadering: $X \sim Bin(n,p) \approx X^* \sim N(np, npq) \approx N(\mu, \sigma^2) $  
poisonn benadering: $X \sim P(\lambda) \approx X^* \sim N(\lambda, \lambda) \approx N(\mu, \sigma^2)$ 

(No idea what to do with these things below)  
Voor X ~ Bin(n, p) met grote n en X ~ P($\lambda$) met grote $\lambda$:  
$P(k_1 \leq X \leq k_2) \approx P(k_1 - 0.5 \lt X \lt k_2 + 0.5) $  
$P(X\leq k_2) = P(X^* \lt k_2 + 0.5) $  
$P(X \lt k_2) = P(X^* \lt k_2 - 0.5)$  
$P(x \geq k_2) = P(X^* \gt k_2 - 0.5)$  
$P(X \gt k_2) = P(X^* \gt k_2 + 0.5)$  



```python

```

## Exponentiele verdeling(wachttijdsverdeling)

![image.png](attachment:image.png)

Deze berekent de kans van het tijdsinterval tussen opeenvolgende random gebeurtenissen.
vb: tijdsinterval tussen opeenvolgende klanten bij een restaurant.  

Kansdichtheidfunctie : $$f(x) = \lambda e^{- \lambda x}$$  
Verwachting $\mu = {1 \over \lambda}$  
variantie $\sigma^2 = {1 \over \lambda^2}$  
std $\sigma = {1 \over \lambda}$  
  
  __VB__: tijdsinterval(in days) tussen opeenvolgende transacties worden bepaald door een exp. verdeling met $\lambda = 0.5$.  
  Wat is de kans dat de verkoper meer dan 5 dagen geen auto verkoopt?  
  
  $A = P(X\geq 5) = e^{-0.5 \cdot 5} = e ^{-2.5} = 0.0821$


```python

```

## De Chi-kwadraat verdeling (Notatie $X \sim X_n^2$)

Als $U_1, U_2, \ldots, U_n$ onafhankelijke vars. zijn met $U_i \sim N(0,1) $  
We zeggen dat $X = \sum_{i=1}^n U_i^2 = U_1^2 + U_2^2 + \ldots + U_n^2 +$ een 
chi-kwadraat verdeling heeft met __n__ vrijheidsgraden.

__Eigenschappen__:
- Verwachting $\mu = n$  
- Variantie $\sigma^2 = 2n$  
- Als $ X_m^2$ en $X_n^2$ onafhankelijk zijn, dan $X_m^2 + X_n^2 X_{m+n}^2$



```python

```

## De Student of T-verdeling ($T_n \sim t_n$)

Als __U ~ N(0,1)__ en $V \sim X^2_n$ is met U en V onafhankelijk.  
We zeggen dan dat $T_n = {U \over \sqrt{v/n}}$ een studentverdeling heeft met n 
vrijheidsgraden.

__Eigenschappen:__  
- De verdeling is symmetriesch ten opzichte van 0.
- Verwachting = 0


```python

```

## Som 31
We werpen één maal met een zuivere dobbelsteen; X = aantal geworpen ogen. Bepaal de kansfunctie, de verdelingsfunctie, de verwachting en variantie van X.


### Oplossing
verwachting $\mu = (1+2+3+4+5+6)/6 = 3.5$    
varientie $\sigma^2 =  \sum{(x_i - \mu)^2 \over n} = {\sum x_i^2 \over 6} - \mu^2 =  2.92 $

Kansfunctie:
$
  P(x) =
\begin{cases}
\frac 1 6,  & \text{voor p(1)} \\
\frac 1 6,  & \text{voor p(2)} \\
\frac 1 6,  & \text{voor p(3)} \\
\frac 1 6,  & \text{voor p(4)} \\
\frac 1 6,  & \text{voor p(5)} \\
\frac 1 6,  & \text{voor p(6)} \\
\end{cases}
$

Verdelingsfunctie:
$
  F(x) =
\begin{cases}
\frac 1 6,  & \text{voor F(1)} \\
\frac 2 6,  & \text{voor F(2)} \\
\frac 3 6,  & \text{voor F(3)} \\
\frac 4 6,  & \text{voor F(4)} \\
\frac 5 6,  & \text{voor F(5)} \\
\frac 6 6,  & \text{voor F(6)} \\
\end{cases}
$


```python

```

# Som 33 
In een loterij is op elk lot een prijs te winnen van 2, 3 of 4 gulden; de kansen op deze prijzen zijn even groot. Laat X = uitkering bij 2 gekochte loten.
a.	Bepaal Ux en de kansfunctie van X.
b.	Bereken de verwachting en de variantie van X.
a. 
```
uitkomsten
2+2 = 4 
2+3 = 5
2+4 = 6
3+2 = 5
3+3 = 6
3+4 = 7
4+2 = 6
4+3 = 7
4+4 = 8

4 = 1/9
5 = 2/9
6 = 3/9
7 = 2/9
8 = 1/9
```

$U_x = \{4,5,6,7,8\}$  

verwachting $\mu = {1 \over 9} \cdot 4 + {2 \over 9} \cdot 5 + {3 \over 9} \cdot 6 + {2 \over 9} \cdot 7 + {1 \over 9} \cdot 8 = 6 $, dus je moet, on average, $6 winnen per 2 lot.

variantie $\sigma^2 = {\sum(x - \mu)^2 \over n} = 1.3333$



```python

```

# Som 34
Een groep bestaat uit 3 dames en 4 heren en aselect worden 2 personen uitgekozen om onderhandelingen te voeren. De kans op succesvolle onderhandelingen is 0,6 als 2 dames worden gekozen, 0,3 bij één dame en één heer, 0,1 als 2 heren worden gekozen.
a.	Bereken de verwachting van de kans op succesvolle onderhandelingen.
b.	Wat is deze verwachting als een bepaalde heer bij voorbaat in de afvaardiging zit ?

## Oplossing

a. 
```
P(FF) = 3/7 * 2/6 = 1/7 
P(FM) = 2(3/7 * 4/6)= 4/7
P(MM) = 4/7*3/6 = 2/7
```

$E(x) = {1 \over 7} \cdot 0.6 + {4 \over 7} \cdot 0.3 + {2 \over 7} \cdot 0.1 = 0.2857$
b. 
dan zijn er MM en MF  
P(MM) = 4/7  
P(MF) = 3/7  
verwachting $E(x) ={4 \over 7} \cdot 0.1 + {3 \over 7} \cdot 0.3 = 0.1857  $


```python

```

# Som 35
Een loterij heeft 100 loten, die 1 gulden per stuk kosten. Drie verschillende nummers hebben een prijs : één van 50 en twee van 10 gulden. De winst W = uitkering – inzet.  
a.	wat is mijn verwachte winst als ik 1 lot koop ?  
b.	wat is mijn verwachte winst als ik 2 loten koop ?  
c.	wat is mijn verwachte winst als ik 100 loten koop ?  

## Oplossing
```
P(49) = 1/100
P(9) = 2/100
P(-1) = 97/100
```
Verwachting $\mu = {48+16-194 \over 100 } = -0.30$  
b. 2 * -1.30 = -0.60  
c. 100 * -1.30 = -30  



```python

```

# Som 36
Gegeven de kansdichtheidsfuncties van X:
$$f_1(x) = 
\begin{cases}
ax,  & \text{op [0,1]} \in \\
0,  & \text{elders} \\
\end{cases}
$$

$$f_2(x) = 
\begin{cases}
{1 \over 3}x^2,  & \text{op [0,b]}\in \\
0,  & \text{elders} \\
\end{cases}
$$


```python

```

# Som 42
Een fabrikant koopt machine-onderdelen bij een ander bedrijf waarvan hij weet dat 10% niet voldoet.   
Bepaal de kans dat van 20 afgeleverde er hoogstens 2 niet voldoen.

## Oplossing
gebruik poisson verdeling.  

$\mu =0.1 \cdot 20 = 2, \\ c=2\\ P(x\leq 2)= 0.6767$

of gebruik binominaal:
$p = 0.1,\\ c=2,\\ n=20\\ P(x\leq 2) =0.6769$



```python

```

# Som 43
Van de Surinaamse bevolking is 40% van Hindoestaanse afkomst. Wat is de kans op meer dan 4 Hindoestanen in een steekproef van 10?

## Oplossing
p = 0.4
n = 10
x = aantal hindustanen
vind P(x>4) = 1 - P(x<= 4) = 1 - 0.6331 = 0.3669



```python

```

# Som 44
Bij een speelbank mag men na 5 gulden betaald te hebben, 10 keer met een zuivere dobbelsteen werpen. 
Bij iedere worp van minstens 4 betaalt de bank 1 gulden uit. Wat is de kans dat een speler winst maakt ?


## Oplossing
winst = 4 of minder keren lager dan 4 scoren.
P(worp < 4) = 50%
n = 10
c = 4
aflezen uit tabel: 0.377


```python

```

# Som 45
Bij het telegraferen treden storingen op, waardoor letters verminkt overkomen. Veronderstel dat de kans dat een  
letter verminkt overkomt 0,9 is en dat de storingen onafhankelijk van elkaar optreden. Men telegrafeert een zin  
van 64 letters, bestaande uit woorden van 4 letters.  
a.	wat is de kans dat een woord ongestoord ontvangen wordt ?  
b.	wat is de kans dat in de overgeseinde zin niet meer dan 4 letters verminkt ontvangen worden ?  

## Oplossing
a.
een woord = 4 letters, de kans dat een woord verstoord overkomt = $0.9^4 =0.6561$ 
er zijn 16 woorden, en 1 van ze moet goed overeenkomen.
dus wat is de kans dat 15 of minder verstoord komen?
sinds 0.656 niet in de tabel voorkomt, kunnen we 1 - B(16, 1 - 0.656, 15) doen, wat 1 - B(16, 0.3439, 15) is

P(meer dan 1 woord ongestoord) $\approx 1 - B(16, 0.3439, 15) = 1 - $
__SHIT, komt niet in tabel. groter dan 0.997, dus de kans is kleiner dan 0.003__


```python

```

# Som 46 
Als 100 mensen elk eenzelfde kans van 1/50 hebben om een bepaalde ziekte te krijgen, wat is dan de kans dat  
a.	precies 5 mensen de ziekte krijgen  
b.	meer dan 5 mensen de ziekte krijgen   
b
x = zieke mensen
verwaching 
$\mu = 100 \times 1/50  =2 \\
P(x> 5) = 1 -  P(x\leq 5) = 1 - 0.9834 = 0.0166
$

a. P precies 5 mensen  = $P(x\leq 5) - p(x\leq 4) = 0.9834 - 0.9437  = 0.03 $



```python

```

# Som 47
Bij keuring van rollen weefseldoek van 40m lengte, bleek gemiddeld 1 weeffout voor te komen. Een afnemer heeft belangstelling voor rollen van 60 m met hoogstens 1 weeffout( de zogenaamde A-kwaliteit).  
a.	Hoe groot is het percentage rollen van 60m met A-kwaliteit ?  
b.	Hoe groot zou U de lengte van de rollen kiezen, opdat het percentage rollen met hoogstens 1 weeffout per rol, 90% bedraagt ?  

## oplossing
a. verwachting = $\mu = 60/40 * 1 = 1.5$
c = 1

a kwaliteit is kans dat er 1 of minder fouten zijn in een 60 m rol. dus c = 1, $\mu$ = 1.5
P(x<1) = 0.5578

Percentage van rollen met a kwaliteit can 60 m = 55.78%


```python

```

# som 48
Er komen gemiddeld 4 telefoongesprekken per minuut via een centrale binnen.  
a.	Wat is de kans op meer dan 3 gesprekken in 15 seconden ?  
b.	Wat is de kans op minstens 3 gesprekken in 15 seconden ?  


## Oplossing
x = telefoongesprekken per 15 sec  
$\mu = 1 tel/min$  
a. $P(x>3) = 1 - P(x\leq 3) = 1 - 0.981 =  0.019$  
b $ P(x\geq 3) = 1 - P(x \leq 2) = 1 - 0.9197 = 0.0803$



```python


```

# Som 49
Het aantal zieke bomen per ha, X bedraagt gemiddeld 10. 
Bereken P(X <= 8) en P(6<=X<=12).

## Oplossing
P(x<=8) = 0.3328  
x(6<=x<=12) = p(x<=12) - p(x<=6) = 0.7916 - 0.1301 = 0.6615



```python

```

# som 50
Bij bepaalde stoffen is het aantal zwakke plekken op rollen van 12m lengte, Poisson verdeeld met een gemiddelde van 1,2.  
a.	Wat is de kans dat een aselect gekozen rol hoogstens 2 zwakke plekken heeft ?  
b.	Wat is de kans dat zo’n rol geen zwakke plek heeft ?  
c.	Wat is de kans dat er in een doos met 5 rollen (aselect gekozen) precies 2 rollen één zwakke plek, en de andere 3 rollen géén zwakke plek hebben ?  


## Oplossing
$\mu = 1.2$  
a. 0.8795  
b. 0.3012  
c. p(x=2) = p(x<=2) - p(x<=1) = 0.9785 - 0.6626 = 0.316 __FOUT__

![image.png](attachment:image.png)


```python

```

# Som 51
Het aantal storingen per dag aan een machine bedraagt gemiddeld 2  
a.	Wat is de kans dat op een willekeurige dag meer dan 3 storingen optreden  
b.	Wat is de kans dat op 2 dagen samen, meer dan 6 storingen optreden ?  
c.	Wat is de kans dat er in een willekeurige week met 7 werkdagen, meer dan 2 dagen zijn, waarop het aantal storingen meer dan 3 is ?  

## Oplossing

Gebruik poisson
a. $\mu = 2, P(x>3) = 1 - P(x\leq 3) = 1 - 0.857 = 0.143$  
b. $\mu = {4 storingen \over 2 d}, P(X>6) = 1 - P(x\leq 6) = 1 - 0.8893 = 0.1103$  
c. $P(x\leq3) = 0.143, \\ c = 3 (x<=3),\\ n = 7, \\Bin(7,0.143, 3) \approx 0.9898 $  
c is gedaan met formule, niet met tabel



```python

```

# Som 52
In een bepaald bedrijf bedraagt het aantal dodelijke ongevallen per maand gemiddeld 0.5 .  
a.	Hoeveel van zulke ongevallen zullen er naar verwachting plaatsvinden in een willekeurig jaar ?  
b.	Wat is de kans op minstens 1 dodelijk ongeval in een willekeurige maand ?  


## Oplossing
x = aantal doden per tijdsperiode
a. verwachting $\mu = 0.5 * 12 = 6 \text {gevallen per jaar}$  
b. $P(X\geq 1) = 1 - P(X\leq 0) = 1 -  0.6065 = 0.3935$  



```python

```

# Som 53
 Op een ronde schijf zit in het midden een draaibare pijl bevestigd. Laat X = uitwijkingshoek ten opzichte van O, dan Ux = [0, 2pi>.  
Bereken P(0.5 pi < X < 3/2 pi).
Bereken met behulp van de definitie, de verwachting en de variantie van X en controleer hiermee de formules op bladzijde 26 van het dictaat.


## Oplossing
verwachting $\mu = \pi$
# TODO!!!!!!!!!!!!!!!!!!!!



```python

```

# Som 55
Laat $ X \sim N(\mu = 1, \sigma^2 = 4).$ Bepaal  
a.	$P(X < 2),\\ P( X \geq 0), \\ P(0,88 < X < 1,58), \\P( |X| < 2)$    
  
  
b.	p zodat $P(X < p) = 0,50,\\ P(X < p) = 0,80. \\ P(X > p) = 0,90.$


## Oplossing
$\sigma = 2$

### a.   
$z = {2-1 \over 2 = 0.5},$
$P(x<2) = P(z<0.5)= 0.6915 $

  
$z = {0 - 1 \over 2},$
$P(x\geq 0) = 1 - P(X \leq 0) =1-  P(z < -0.5) = 1 - 0.3085 = 0.6915 $

$z_1 = {.88 - 1 \over 2} = -0.06,\  z_2 = {1.58 - 1 \over 2} = 0.29 $  
P(0.88 < x < 1.58) = P(-0.06 < z < 0.29) =  P(z < 0.29) - P(z< -0.06) = 0.6141 - 0.4761 = 0.14  
  
  
### b
$P(X<z) = 0.5 \Rightarrow  z=0 \Rightarrow 0 = {p - 1 \over 2} \Rightarrow p = 1$  
$P(X<z) = 0.8 \Rightarrow  z=0.85 \Rightarrow 0.85 = {p - 1 \over 2} \Rightarrow p = 2.7$  


```python

```

# Som 56
![image.png](attachment:image.png)
## Oplossing a

Bin(20, 0.5, 12) = 0.8684  
Poisson: 
$\mu = 20 \cdot 0.5 = 10$
P(x<=12) = 0.7916  
 
__normale benadering vsanuit poisson:__  
$\mu = \lambda$  
std $\sigma = \sqrt \lambda$  
$\mu = 10,\ \sigma = \sqrt 10 = 3.162$  
P(x<=12) =  P(X < 12.5) = P(z<= 0.79) = 0.7852

__Normale benadering vanuit binominaal__  
$\mu = n \cdot p = 10$  
$\sigma = \sqrt {n p q} = \sqrt {20 \cdot 0.5 \cdot 0.5} = \sqrt 5 = 2.236$  
P(x<=12) = P(x< 12.5) = P(z < 1.12) = 0.8686 


## HUH! I expected them to come the same ish. OK




# Som 57
Een zaal biedt plaats aan 900 personen. Vereniging X weet dat 1 op de 6 genodigden niet komt opdagen, zodat er plaatsen leeg zullen blijven als precies 900 personen worden uitgenodigd. Bereken de kans dat er méér dan 900 personen verschijnen indien er 1080, resp. 1000 mensen worden uitgenodigd. 

verwachting: $\mu = 166.666/1000 = 180/1080$

Benadering vanuit Poisson:  
$X ~ P(\mu = 166.666, n=1000)$:  

$\mu = 166.666, \sigma = \sqrt {166.66} = 12.9$  

P(x < 100) = P(x< 99.5) = P(z < -5.2)  $\approx 0$  
z = ${99.5 - 166.66 \over \sqrt{166.66}} = -5.2$



```python

```

# Som 58
58. Bij de massafabrikage van een bepaald produkt voldoet gemiddeld 5% niet aan bepaalde eisen. Bepaal de kans om in een steekproef van    
a.	50 produkten méér dan 6% slechte exemplaren aan te treffen  
b.	1000 produkten méér dan 6% slechte exemplaren aan te treffen.  

## Oplossing a
$\mu = 50 * 0.05 = 2.5$  
$P(x>6\%) =P(x>3) =1 - P(x<= 3) = 1 - 0.7576 = 0.2424$  

## OPlossing b
Doe met $X \sim P(\lambda=50)$  
$\mu = 0.05 * 1000 = 50 $  
$\sigma = \sqrt{50} = 7.071$    
$z = {60.5 - 50 \over 7.071} = 1.41$  
P(x>60) = 1 - P(x<= 60) = 1 - P(x < 60.5) = 1 -  P(z < 1.41) = 1 - 0.9251 = 0.0749





```python

```

# Som 59
59. Het netto vulgewicht van pakken waspoeder is normaal verdeeld met een standaardafwijking $\sigma$ = 2 gr. Op welk gemiddelde moet de machine worden afgesteld opdat hoogstens 1% van de pakken een netto vulgewicht heeft van minder dan 100 gr?


## Oplossing
$ P(z< a) \leq 0.01 \Rightarrow a \leq -2.32$  
$-2.32 = {100 - \mu \over 2} \Rightarrow -4.64 = 100 - \mu \Rightarrow \mu = 104.64$  
Gemiddelde moet gezet worden op 104.64gr



```python

```

# Som 60  
De lengte van bepaalde onderdelen is normaal verdeeld met een gemiddelde van 551mm. Geëist wordt dat de lengte minimaal 548,6 mm is en er blijkt 2,3% van de onderdelen te worden afgekeurd.
a.	Hoe groot is $\sigma$?  
b.	Hoe groot is het afkeuringspercentage als ook onderdelen afgekeurd worden die  langer zijn dan 552,6 mm?    

## Oplossing   a
$\mu = 551$  
$P(z<a) = 0.023 \Rightarrow a = -2$  
$-2 = {548.6 - 551 \over \sigma} = {-2.4 \over \sigma} \Rightarrow  \sigma = 1.2$

## Oplossing b
$P( 548.6 \geq x | x \geq 552.6) =0.023 + P(x> 552.6) = 0.023  + (1 - P(x< 552.6) ) = 0.023 + (1 - P(z < 1.33) = 0.023 + 0.0918 = 0.1148 = 11.48\% $  
$z = {552.6 - 551 \over 1.2} = 1.33$



```python

```

![image.png](attachment:image.png)

## Oplossing a
kans dat de waarde binnen de eisen valt:  
x = weerstand  
$z_1 = {45-50 \over 1.52} = -3.29, z_2 = {55-50\over 1.52} = 3.29$
P(45<x<55) = P(-3.29 < z < 3.29) = P(z<3.29) - P(z<-3.29) = 0.9995 - 0.0005 = 0.999  
Kans buiten de eisen  = 0.001
Kans dat er geen foute exemplaren zijn in een pak van 100 stuks:  
X = aantal foute exemplaren  
$P(X\leq 0) = Bin(100, 0.001,0 ) = {100 \choose 0} \cdot 0.001^0 \cdot 0.999^{100}  = 0.9047$



```python

```
