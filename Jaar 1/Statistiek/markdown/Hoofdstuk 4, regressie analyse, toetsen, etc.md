
# Hypothese toetsen
We hebben gemerkt dat verdelingen van stochastische vars minstens 1 parameter hebben.
Hypothesen zijn beweringen over de grootte van  een bepaalde parameters.


We willen onze hypoyhese toetsen door te kijken of onze bewering in een steekproef ook opgaat.
De bewering die getoetst wordt noemen we de $nulhypothese (H_0)$ en het complement van de te 
toetsen bewering noemen we de $alternative\ hypothese (H_1)$  
  

1. __Nulhypothese$(H_0)$:__ Status quo voor degene die het steekproefexperiment vericht. De hypothese die aanvaard zal worden, tenzij de gegevens overtuigend bewijs leveren dat de hypothese onjuist is.

2. __Alternatieve/ onderzoekshypothese $(H_1)$__: wordt alleen aanvaard als de gegevens overtuigend bewijs leveren van de juistheid ervan. We kunnen de volgende schema opstellen met betrekking tot beslissingen die genomen kunnen worden:

![image.png](attachment:image.png)

Een fout van de 1e soort: H0 verwerpen terwijl H0 juist is (kans $\alpha$) 

Een fout van de 2e soort: H0 aanvaarden terwijl H0 onjuist is (kans $\beta$)

Men zal meestal proberen de kans op een fout van de 1e soort zo klein mogelijk te laten zijn.
vb: stel dat de gemiddelde breuksterkte van rioolbuizen groter moet zijn dan 2400kg/strekkend meter. Elke fabrikant die dit product wilt verkopen i/d gemeente moet aantonen dat zijn product aan deze specificatie voldoet.  
Dus we willen vaststellen of de gem. breuksterkte groter is dan 2400kg/strekkend meter. Vanuit het standpunt van de gemeentebestuur, die de toetsen laat uitvoeren houden de hypothesen het volgende in:  

- $H_0 : \mu \leq 2400$ (buis voldoet niet aan specificaties)  
- $H_1 : \mu > 2400$ (buis voldoet aan de specificaties)
  

Om een beslissing te nemen berekenen we de uitkomst van een __toetsingsgrootheid(T)__.
Een toetsingsgrootheid is een steekproefgrootheid die wordt gebruikt om te beslissen of de 
nulhypothese verworpen moet worden. Via de toetsingsgrootheid T stellen we een beslissingscriteria op. Indien de  
gevonden steekproefwaarde v/d toetsingsgrootheid te veel afweikt van de beweerde waarde van $H_0$, zal men geneigd zijn de nulhypothese te verwerpen.  
Het __kritieke gebied__ wordt gevormt door alle waarden v/d toetsingsgrootheid waarvoor $H_0$ wordt verworpen  

Het kritieke gebied wordt bepaald op grond van een tevoren vastgeledge __onbetrouwbaarheidsdrempel, $\alpha$__ (Significantie-niveau of significance level).
bv. 1%, 5%, 10%

Er geld dus:
$\alpha$ = P(fout v\d 1e soort) = P(H0 onterecht verworpen) = $P(T \in K \mid H_0\text{ is juist})$  
K = kritieke gebied, T = toetsingsgrootheid  
  
  
  Conclusie: 
- Als de uitkomst v/d toetsingsgrootheid i/h kritieke gebeid valt, verwerpt $H_0$  
- Als de uitkomst v/ d toetsingsgrootheid niet i/h kritieke gebied valt, aanvaard $H_0$  


1. Er is altijd een kans dat H0 onterecht verworpen wordt, en deze kans is gelijk aan $\alpha$. Het aanvaarden van H0 wilt nog niet zeggen
dat de bewering in H0 juist is.
sinds: 
	- De beslissing is genomen voor een bepaalde steekproef
	- er is mischien een fout van de 2e soort
	- Een paremeterwaarde die slechts weinig afweikt v/d gestelde waarde in H0, zou mischien ook aangenomen worden met deze steekproef  
    
   
In bepaalde gevallen, afhankelijk v/d verdeling v/d toetsingsgrootheid, is het mogelijk om
achteraf nog wat te zegen over de kans op een fout van 2e soort.  

$\beta = P(\text{fout v.d 2e soort}) = P(H_0 \text { ten onterechte aanvaarden}) = P(T \not \in K \mid H_1 \text{ is juist})$

Het compllement van $\beta$ heet het __onderscheidend vermogen__. Dit is de kans dat de toets terecht leidt tot het verwerpen van 
de nulhypothese voor een bepaalde waarde van $\mu$ in de alternatieve hypothese. 
Het onderscheidend vermogen is: $1 - \beta = P(T \in K \mid H_1\ is\ juist)$



Toetsen in veelvoorkomende situaties:
![image.png](attachment:image.png)

## Own notes: TLDR
Er is een Toetsingsgrootheid T die wordt gebruikt om te beslissen wat te doen. Er zijn 3 mogelijkheden: 
$\alpha$ = kans op fout 1e soort (nulhypothese juist maar verworpen), $\beta$ = kans op 2e fout (nulhypothese is onjuist maar aanvaard) en de juiste beslissing. Het __kritieke gebied K__ wordt gevormt door alle waarden v/d toetsingsgrootheid waarvoor 𝐻0 wordt verworpen   
$\alpha = P(T \in K \mid H_0\text{ is juist})$   
 $1 - \beta = P(T \in K \mid H_1\ is\ juist)$  
$\beta = P(H_0 \text { ten onterechte aanvaarden}) = P(T \not \in K \mid H_1 \text{ is juist})$

Er zijn 3 typen toetsen:
- links eenzijdig  
- rechts eenzijdig  
- tweezeidig  

2 parameters kunnen getoest worden, nl verwachting $\mu$ en afweiking $\sigma$.


# Betrouwbaarheidsintervallen

## 1.Interval voor $\mu, \sigma^2$ bekend:  
	a. Tweezijdig (1- $\alpha$) 100%:
$$X_{avg} - {\sigma \cdot z_\alpha /2 \over \sqrt n} < \mu <  X_{avg} + {\sigma \cdot z_\alpha /2 \over \sqrt n}$$
    b. eenzijdig (1- $\alpha$) 100%:  
	$$\text{Links:} \mu > X_{avg} - {\sigma \cdot z_\alpha / 2 \over \sqrt n} \text{ Rechts:}\mu < X_{avg} + {\sigma \cdot z_\alpha / 2 \over \sqrt n}$$	
(Dus basically onthoudt die equation van tweezijdig, links en rechts zijn gewoon die delen ervan)
Gebruik kritieke waarde hypothese test(naast cum. normal bell curve)
![image.png](attachment:image.png)

## 2. __Interval voor $\mu, \sigma^2$ onbekend:__  
Bereken eerst $S^2$ of gebruik de gegeven steekrpoef std.

	a.  Tweezijdig:
$$\mu > X_{avg} - {S \cdot t_{n-1}\alpha/2 \over \sqrt n}$$

Links en rechts:
$$\mu > X_{avg} - {S \cdot t_{n-1}\alpha \over \sqrt n}\ en\ \mu < X_{avg} + {S \cdot t_{n-1}\alpha \over \sqrt n} $$
GEBRUIK T VERDELING TABEL

## 3. __Interval voor $\sigma^2$:__  
a. Tweezijdig (1 - $\alpha$) 100%:  
$${(n-1)S^2 \over \chi_{n-1}^2(0.5 \alpha)} < \sigma^2 <  {(n-1)S^2 \over \chi_{n-1}^2(1 - 0.5 \alpha)}$$  
b. Eenzijdig:  
Links: $\sigma^2 > {(n-1)S^2 \over \chi_{n-1}^2(\alpha)} \text{   rechts   } \sigma^2 <  {(n-1)S^2 \over \chi_{n-1}^2(1 - \alpha)}$

GEBRUIK CHI KWADRAAT TABEL

### OM

# STEFAN"S NOTES
# Toetsen & Hypothesen

$H_0 \Rightarrow$ Nulhypothese  
$H_1$v= Hypothese die getest wordt   
  
Er zijn 3 type toetsen:
- Links eenzijdig  
- Rechts eenzijdig
- tweezijdig

2 parameters die getest kunnen worden:
- De verwachting (gemiddeld, $\mu$)
- De variantie of afweiking ($\sigma\ of\ \sigma^2$)

Om een conclussie te kunnen trekken om de hypothesen te verwerpen of aanvaardenmoet er een criteria vastgelegd worden.   
Er moet een toetsingsgrootheid berekend worden, en dit noemen we __T__. Aan de hand van als T in de __Kritieke waarde K_ valt,
acepteren we $H_1$

$H_0$ verwerpen terwijl het juist is proberen we zo klein mogelijk te maken. Deze wordt ook wel
$\alpha$ genoemd, en is de significance level. Veelgebruikte waarden voor $\alpha$ zijn 0.01, 0.02, 0.05, 0.10.  

Indien de toetsingsgrootheid T binnen het kritiek gebied valt, verwerp $H_0$.

Er zijn de volgende situaties mogelijk:
1. toetsen van de verwachting mu  
	- std onbekend
	-std bekend
2. toetsen v'd variantie of std.



## Stappen
Stek: $\alpha = 0.01$  
Ok wil links eenzijdig toetsen.
Wat is de z-waarde die dus 0.01 geeft? $Z= -2.29$
Stel toetsingsgrootheid T valt in __WAIT FOR STEFAN__ $\Rightarrow$ Valt in het kritiek gebied, dan verwerp je $H_0$.

## VOORBEELD
Stel: $H_0 : \mu \leq 515 \\ H_1 : \mu > 515$  
Voer een hypothesetoets uit met de volgende info:  
- $\alpha = 0.05$  
- avg x = 540
- $\mu = 40$  
- $\sigma = 114$  
- Rechts eenzijdig : u > 515
Toetsingsgrootheden: ${\sqrt u (avg - \mu_0) \over \sigma} = 1.39$ (__WHY THIS? WHERE IT COME FROM? Is dit gegeven?__)
{0.05 : T = 1.645}

Sinds 1.39 $\in [0, 1.645], H_0$ 
__I GIVE UP< ASK LATER__ 



## Voorbeeld
Importeir A beweert dat bij het benzineverbruik van een bep. merk auto 0.6 l/km is. Autohandelaar B twijvelt daaraan.
De autohandelaar experimenteert dit met 2 autos en krijgt de volgende gegevens:  
- 0.65 0.36 0.62 0.58 0.67 0.68 0.66 0.57 0.67 0.59 0.64 0.68

Voer een hypothesetoest uit met de volgende info:
- $\alpha = 0.05$  
- $\mu = 12$  
- avg = 0.627  
- S = 0.04438




```python

```
