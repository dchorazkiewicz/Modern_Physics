# Mechanika klasyczna

## Opis ruchu (położenie, prędkość, przyspieszenie)

### Położenie 
Aby opisać ruch wystarczy abyśmy znali położenie ciała w danej chwili czasu. 
W mechanice klasycznej położenie ciała w przestrzeni trójwymiarowej opisuje się za pomocą
wektora $\vec{r}(t) = (x(t), y(t), z(t))$. W zależności od czasu położenie ciała zmienia się,
co można zapisać jako $\vec{r} = \vec{r}(t)$.

### Prędkość

[Prędkość](https://pl.wikipedia.org/wiki/Pr%C4%99dko%C5%9B%C4%87), [Velocity](https://en.wikipedia.org/wiki/Velocity)

Prędkość ciała to pochodna położenia ciała po czasie. W zapisie wektorowym prędkość ciała

$$
\vec{v}(t) = \frac{d\vec{r}(t)}{dt} = \left(\frac{dx(t)}{dt}, \frac{dy(t)}{dt}, \frac{dz(t)}{dt}\right)
$$


### Przyspieszenie

[Przyspieszenie](https://pl.wikipedia.org/wiki/Przyspieszenie), [Acceleration](https://en.wikipedia.org/wiki/Acceleration)


Przyspieszenie ciała to pochodna prędkości ciała po czasie. W zapisie wektorowym przyspieszenie ciała

$$
\vec{a}(t) = \frac{d\vec{v}(t)}{dt} = \left(\frac{dv_x(t)}{dt}, \frac{dv_y(t)}{dt}, \frac{dv_z(t)}{dt}\right)
$$

w zapisie drugiej pochodnej położenia ciała względem czasu

$$
\vec{a}(t) = \frac{d^2\vec{r}(t)}{dt^2} = \left(\frac{d^2x(t)}{dt^2}, \frac{d^2y(t)}{dt^2}, \frac{d^2z(t)}{dt^2}\right)
$$


## Prawa Newtona (I, II, III)

[Prawa dynamiki Newtona](https://pl.wikipedia.org/wiki/Zasady_dynamiki_Newtona), [Newton's laws of motion](https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion)

### I prawo dynamiki

Jeżeli na ciało nie działa żadna siła to ciało pozostaje w spoczynku lub porusza się ruchem jednostajnym prostoliniowym.

### II prawo dynamiki

Jeżeli na ciało działa siła to ciało porusza się z przyspieszeniem proporcjonalnym do siły i odwrotnie proporcjonalnym do masy ciała.

$$
\vec{F} = m\vec{a}
$$

### III prawo dynamiki

Jeżeli ciało A działa na ciało B siłą $\vec{F}_{AB}$ to ciało B działa na ciało A siłą $\vec{F}_{BA}$ o takiej samej wartości ale przeciwnie skierowaną.


## II prawo dynamiki w zapisie Hamiltona (numeryczne rozważania)

Równania Newtona są sformułowane dla położenia ciała w przestrzeni. W celu rozwiązania równań Newtona numerycznie można zastosować zapis Hamiltona. W zapisie Hamiltona równania ruchu ciała można zapisać jako równania różniczkowe zwyczajne pierwszego rzędu.

$$
\begin{aligned}
\frac{d\vec{r}(t)}{dt} &= \vec{v}((t)) \\
\frac{d\vec{v}(t)}{dt} &= \frac{\vec{F}(t, \vec{r}(t), \vec{v}(t))}{m}
\end{aligned}
$$

Zauważmy, że siła jest funkcją czasu, położenia ciała i prędkości ciała czyli może zmieniać się w czasie, w zależności od położenia ciała i w zależności od prędkości ciała.

**Przykład zmienności siły w czasie**

Drgania wymuszone są to drgania ciała pod wpływem siły zewnętrznej. Przykładem drgań wymuszonych jest ruch wahadła pod wpływem siły zewnętrznej. W przypadku drgań wymuszonych siła zewnętrzna jest funkcją czasu.

**Przykład zmienności siły w zależności od położenia ciała**

Praktycznie wszystkie siły działające na ciało są funkcją położenia ciała. Przykładem siły zależnej od położenia ciała jest siła grawitacyjna.

**Przykład zmienności siły w zależności od prędkości ciała**

Przykładem siły zależnej od prędkości ciała jest siła oporu powietrza. Siła oporu powietrza jest proporcjonalna do prędkości ciała.


Zapisując to za pomocą składowych wektorów

$$
\begin{aligned}
\frac{dx(t)}{dt} &= v_x(t) \\
\frac{dy(t)}{dt} &= v_y(t) \\
\frac{dz(t)}{dt} &= v_z(t) \\
\frac{dv_x(t)}{dt} &= \frac{F_x(t, x(t), y(t), z(t), v_x(t), v_y(t), v_z(t))}{m} \\
\frac{dv_y(t)}{dt} &= \frac{F_y(t, x(t), y(t), z(t), v_x(t), v_y(t), v_z(t))}{m} \\
\frac{dv_z(t)}{dt} &= \frac{F_z(t, x(t), y(t), z(t), v_x(t), v_y(t), v_z(t))}{m}
\end{aligned}
$$

Popatrzmy na składową $x$ równania ruchu w uproszczonym zapisie

$$
\begin{aligned}
\frac{dx}{dt} &= v_x \\
\frac{dv_x}{dt} &= \frac{F_x}{m}
\end{aligned}
$$

Mówiąc to prostymi słowami, aby obliczyć położenie ciała w chwili $t + \Delta t$ musimy znać położenie ciała w chwili $t$ oraz prędkość ciała w chwili $t$. Aby obliczyć prędkość ciała w chwili $t + \Delta t$ musimy znać siłę działającą na ciało w chwili $t$ oraz masę ciała. Czyli inaczej prędkość zmienia położenie ciała a przyspieszenie zmienia prędkość ciała.


## Praca 

[Praca](https://pl.wikipedia.org/wiki/Praca_(fizyka)), [Work_(physics)](https://en.wikipedia.org/wiki/Work_(physics))

Załóżmu, że na ciało działa siła $\vec{F}$ i ciało przesuwa się o wektor $\vec{r}$. Praca siły $\vec{F}$ jest równa iloczynowi skalarnemu siły $\vec{F}$ i przesunięcia $\vec{r}$.


<img src="https://upload.wikimedia.org/wikipedia/commons/1/12/Mehaaniline_t%C3%B6%C3%B6.png" alt="Praca_01" width="200"/>

W ogólnym przypadku musimy obliczyć całkę po drodze jaką pokonało ciało

$$
W = \int_{\vec{r}_1}^{\vec{r}_2} \vec{F} \cdot d\vec{r}
$$

[https://pl.wikipedia.org/wiki/Ca%C5%82ka_krzywoliniowa](https://pl.wikipedia.org/wiki/Ca%C5%82ka_krzywoliniowa)


## Siły zachowawcze

[Siła potencjalna](https://pl.wikipedia.org/wiki/Si%C5%82a_zachowawcza)

[Conservative force](https://en.wikipedia.org/wiki/Conservative_force)

Siła zachowawcza to siła, której praca nie zależy od drogi jaką pokonało ciało. W zapisie matematycznym siłę potencjalną można zapisać jako gradient funkcji potencjału.

Przyładem siły zachowawczej jest siła grawitacyjna

$$
\vec{F} = -\nabla U
$$

dla siły grawitacyjnej $ \vec{F} = -\frac{G M m}{r^2} \hat{r}$

mamy

$$
U = -\frac{G M m}{r}
$$

Poniżej znajduje się kod w sympy który oblicza gradient funkcji potencjału pola grawitacyjnego:

```python
import sympy as sp

x, y, z = sp.symbols('x y z')
U = -sp.Symbol('G') * sp.Symbol('M') * sp.Symbol('m') / sp.sqrt(x**2 + y**2 + z**2)
grad_U = sp.Matrix([sp.diff(U, x), sp.diff(U, y), sp.diff(U, z)])
grad_U
```

Więcej informacji na temat potencjału można znaleźć w artykule na wikipedii

[Potencjał](https://pl.wikipedia.org/wiki/Potencja%C5%82#:~:text=Potencjalne%20pola%20si%C5%82%20niezale%C5%BCnych%20od,w%20drug%C4%85%20w%20trakcie%20ruchu.)

## Energia kinetyczna i potencjalna, zachowanie energii mechanicznej

[Energia kinetyczna](https://pl.wikipedia.org/wiki/Energia_kinetyczna), [Kinetic energy](https://en.wikipedia.org/wiki/Kinetic_energy)

[Energia potencjalna](https://pl.wikipedia.org/wiki/Energia_potencjalna), [Potential energy](https://en.wikipedia.org/wiki/Potential_energy)

Policzmy wyrażenie 

$$\int_{\vec{r}_1}^{\vec{r}_2} \vec{F} \cdot d\vec{r}$$

w ogólnym przypadku


$$
\int_{\vec{r}_1}^{\vec{r}_2} \vec{F} \cdot d\vec{r} 
$$

$$\int_{\vec{r}_1}^{\vec{r}_2} m\vec{a} \cdot d\vec{r}  
$$

$$m \int_{\vec{r}_1}^{\vec{r}_2} \vec{a} \cdot d\vec{r}  
$$

$$m \int_{\vec{r}_1}^{\vec{r}_2} \frac{d\vec{v}}{dt} \cdot d\vec{r}  
$$

$$m \int_{\vec{r}_1}^{\vec{r}_2} \frac{d\vec{v}}{dt} \cdot \vec{v} \, dt  
$$

$$m \int_{\vec{v}_1}^{\vec{v}_2} \vec{v} \cdot d\vec{v}  
$$

$$ m \int_{\vec{v}_1}^{\vec{v}_2} v \, dv  
$$

$$ \frac{1}{2} m v^2_2 - \frac{1}{2} m v^2_1 = E_{k2} - E_{k1}
$$


gdzie wyrażenie $E_{k}$ nazwane jest energią kinetyczną ciała! Widać z powyższego wzoru, że praca siły jest równa zmianie energii kinetycznej ciała. Dodatkowo jeśli siła jest siłą potencjalną to praca siły jest równa zmianie energii potencjalnej ciała.

$$\int_{\vec{r}_1}^{\vec{r}_2} \vec{F} \cdot d\vec{r}$$

$$ \int_{\vec{r}_1}^{\vec{r}_2} (-\nabla U) \cdot d\vec{r}$$

$$= -\int_{\vec{r}_1}^{\vec{r}_2} \nabla U \cdot d\vec{r}$$

$$= -\left[U(\vec{r}_2) - U(\vec{r}_1)\right]$$

$$= U(\vec{r}_1) - U(\vec{r}_2)$$


gdzie wyrażenie $U$ nazwane jest energią potencjalną ciała! Widać z powyższego wzoru, że praca siły jest równa zmianie energii potencjalnej ciała.

Zachowanie energii mechanicznej ciała oznacza, że suma energii kinetycznej i potencjalnej ciała jest stała.

$$
E = E_k + U = \text{const}
$$

Daje to nam możliwość rozpatrywania ruchu ciała w kontekście energii ciała.

$$
E_{k1} + U_1 = E_{k2} + U_2
$$

[Zasada_zachowania_energii](https://pl.wikipedia.org/wiki/Zasada_zachowania_energii), [Conservation_of_energy](https://en.wikipedia.org/wiki/Conservation_of_energy)

### Przypadek siły grawitacyjnej

[Siła grawitacyjna](https://pl.wikipedia.org/wiki/Grawitacja), [Gravitational_force](https://en.wikipedia.org/wiki/Gravitational_force)

Dla siły grawitacyjnej $ \vec{F} = -\frac{G M m}{r^2} \hat{r}$ mamy

$$
\frac{mv_1^2}{2} - \frac{G M m}{r_1} = \frac{mv_2^2}{2} - \frac{G M m}{r_2} 
$$

gdzie $v_1$ i $v_2$ to prędkości ciała w chwilach $t_1$ i $t_2$ oraz $r_1$ i $r_2$ to odległości ciała od ciała centralnego w chwilach $t_1$ i $t_2$.

### Rrzut ukośny

[Rzut ukośny](https://pl.wikipedia.org/wiki/Rzut_uko%C5%9Bny_(fizyka)), [Projectile motion](https://en.wikipedia.org/wiki/Projectile_motion)

W odległościach niedalkich powierzchni ziemi przyspieszenie ziemskie jest stałe i wynosi $g = 9.81 \frac{m}{s^2}$. Dla takiego układu siłę grawitacyjną można zapisać jako

$$
\vec{F} = m\vec{g}
$$

zasadę zachowania  energii mechanicznej można zapisać jako

$$
\frac{mv_1^2}{2} + mgh_1 = \frac{mv_2^2}{2} + mgh_2
$$


## Zasada zachowania pędu

[Zasada zachowania pędu](https://pl.wikipedia.org/wiki/Zasada_zachowania_p%C4%99du), [Momentum Conservation](https://en.wikipedia.org/wiki/Momentum#Conservation)

Pęd zdefiniowany jest jako iloczyn masy ciała i prędkości ciała

$$
\vec{p} = m\vec{v}
$$

W układzie izolowanym pęd ciała jest stały

$$
\vec{p}_1 = \vec{p}_2
$$

### Przykład zderzenia dwóch ciał

Jeżeli ciało A o masie $m_A$ porusza się z prędkością $\vec{v}_{A1}$
i ciało B o masie $m_B$ porusza się z prędkością $\vec{v}_{B1}$ to po zderzeniu ciała A i B poruszają się z prędkościami  $\vec{v}_{A2}$ i $\vec{v}_{B2}$.

Zasada zachowania pędu mówi, że

$$
m_A \vec{v}_{A1} + m_B \vec{v}_{B1} = m_A \vec{v}_{A2} + m_B \vec{v}_{B2}
$$

[Zasada zachowania pędu](https://pl.wikipedia.org/wiki/Zasada_zachowania_p%C4%99du), [Momentum Conservation](https://en.wikipedia.org/wiki/Momentum#Conservation)


## Zasad zachowania momentu pędu

Moment pędu zdefiniowany jest jako iloczyn wektora położenia ciała i pędu ciała

$$
\vec{L} = \vec{r} \times \vec{p}
$$

W układzie izolowanym moment pędu ciała jest stały

$$
\vec{L}_1 = \vec{L}_2
$$


## Związek symetrii z zachowaniem wielkości fizycznych

W skróce można powiedzieć, że jeżeli układ fizyczny jest niezmienniczy względem pewnej transformacji to wielkość fizyczna jest zachowana. Zasada zachowania energii wynika z niezmienniczości układu względem przesunięcia w czasie. Zasada zachowania pędu wynika z niezmienniczości układu względem przesunięcia w przestrzeni. Zasada zachoawania momentu pędu wynika z niezmienniczości układu względem obrotu.


[Twierdzenie_Noether](https://pl.wikipedia.org/wiki/Twierdzenie_Noether), [Noether's Theorem](https://en.wikipedia.org/wiki/Noether%27s_theorem)

## Rzut ukośny, ruch po okręgu, oscylacje, układy oscylatorów -> zjawiska falowe

### Rzut ukośny

W tym problemie siła ma postać

$$
\vec{F} = 
\begin{pmatrix}
0 \\
0\\
-mg
\end{pmatrix}
$$

Zapisując równania ruchu dla rzutu ukośnego

$$
\begin{aligned}
\frac{d^2x}{dt^2} &= 0 \\
\frac{d^2y}{dt^2} &= 0\\
\frac{d^2z}{dt^2} &= -g/m
\end{aligned}
$$

można łatwo pokazać, że rozwiązaniem równań ruchu jest

$$
\begin{aligned}
x(t) &= v_{0x} t + x_0 \\
y(t) &= v_{0y} t + y_0 \\
z(t) &= -\frac{1}{2} g t^2 + v_{0z} t + z_0
\end{aligned}
$$

gdzie $v_{0x}$, $v_{0y}$, $v_{0z}$ to prędkości ciała w kierunkach $x$, $y$, $z$ w chwili $t=0$ oraz $x_0$, $y_0$, $z_0$ to położenie ciała w chwili $t=0$.

### Ruch po okręgu

Podejdźmy do problemu od strony matematycznej. Najpierw opiszmy ruch

$$
\begin{aligned}
x(t) &= R \cos(\omega t) \\
y(t) &= R \sin(\omega t)
\end{aligned}
$$

gdzie $R$ to promień okręgu a $\omega$ to prędkość kątowa ciała. Prędkość kątowa ciała to iloraz kąta obrotu ciała przez czas $\omega = \frac{\Delta \phi}{\Delta t}$ i wiąże się się z prędkością liniową ciała $v = R \omega$.

Policzmy prędkość ciała

$$
\begin{aligned}
v_x(t) &= -R \omega \sin(\omega t) \\
v_y(t) &= R \omega \cos(\omega t)
\end{aligned}
$$

Policzmy przyspieszenie ciała

$$
\begin{aligned}
a_x(t) &= -R \omega^2 \cos(\omega t) \\
a_y(t) &= -R \omega^2 \sin(\omega t)
\end{aligned}
$$

### Prędkość jest prostopadła do promienia okręgu


$$
\begin{aligned}
\vec{v}(t)\cdot \vec{r}(t) &= 
(-R \omega \sin(\omega t), R \omega \cos(\omega t)) \cdot (R \cos(\omega t), R \sin(\omega t)) \\
&= -R^2 \omega \sin(\omega t) \cos(\omega t) + R^2 \omega \sin(\omega t) \cos(\omega t) = 0
\end{aligned}
$$

### Przyspieszenie ciała skierowane do środka okręgu


Po pierwsze widzimy że:

$$
\begin{aligned}
a_x(t) &= -R \omega^2 \cos(\omega t) = -\omega^2 x(t)\\
a_y(t) &= -R \omega^2 \sin(\omega t) = -\omega^2 y(t)
\end{aligned}
$$

zapis wektorowy przyspieszenia ciała

$$
\vec{a}(t) = -\omega^2 \vec{r}(t)
$$

pamiętając o relacji między prędkością kątową a prędkością liniową $v = R \omega$
możemy to zapisać jako dobrze nam znaną zależność

$$
\vec{a}(t) = -\frac{v^2}{R} \vec{r}(t)
$$

## Oscylacje

Oscylacje to ruch ciała wokół położenia równowagi. Przykładem oscylacji jest ruch wahadła. W przypadku ruchu wahadła siła jest siłą sprężystości. W przypadku ruchu wahadła siła sprężystości jest proporcjonalna do odchylenia ciała od położenia równowagi.

### Jednowymiarowa sprężyna

Dla jednowymiarowej sprężyny siła sprężystości jest proporcjonalna do odchylenia ciała od położenia równowagi

$$
m\frac{d^2x}{dt^2} = -kx
$$

gdzie $k$ to stała sprężystości sprężyny. Rozwiązaniem równania powyżej jest

$$
x(t) = A \cos(\omega t + \phi)
$$

gdzie $A$ to amplituda oscylacji, $\omega$ to częstość oscylacji a $\phi$ to faza oscylacji.

### Wahadło matematyczne

Dla wahadła matematycznego siła jest siłą grawitacyjną. Dokładne równanie ruchu wahadła matematycznego można zapisać jako

$$  
\frac{d^2\theta}{dt^2} = -\frac{g}{l} \sin(\theta)
$$

ale dla małych kątów odchylenia $\sin(\theta) \approx \theta$ więc równanie ruchu wahadła matematycznego można zapisać jako

$$
\frac{d^2\theta}{dt^2} = -\frac{g}{l} \theta
$$

gdzie $l$ to długość wahadła. Rozwiązaniem równania powyżej jest

$$
\theta(t) = A \cos(\omega t + \phi)
$$

Bardziej skomplikowane układu oscylatorów można opisać za pomocą równań różniczkowych zwyczajnych drugiego rzędu. Przykładem takiego układu jest układ
podpora-spężyna-masa-sprężyna-masa-sprężyna-podpora:

$$
\begin{cases}
m_1 \ddot{x_1} = -k_1 (x_1 - l_0) - k_2 (x_2 - x_1 - l_0) \\
m_2 \ddot{x_2} = k_2 (x_2 - x_1 - l_0)- k_3 (x_2 - L + l_0)
\end{cases}
$$

układy tego typu można rozwiązać numerycznie co zostało pokazane w notatniku "Układy oscylatorów". Najważniejszą wnioskiem z tego notatnika jest to, że układy oscylatorów mogą wykazywać własności falowe!




 
