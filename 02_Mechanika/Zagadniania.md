# Mechanika klasyczna

## Opis ruchu (położenie, prędkość, przyspieszenie)

### Położenie 
Aby zdefiniować ruch wystarczy abyśmy znali położenie ciała w danej chwili czasu. 
W mechanice klasycznej położenie ciała w przestrzeni trójwymiarowej opisuje się za pomocą
wektora $\vec{r}(t) = (x(t), y(t), z(t))$. W zależności od czasu położenie ciała zmienia się,
co można zapisać jako $\vec{r} = \vec{r}(t)$.

### Prędkość

Prędkość ciała to pochodna położenia ciała po czasie. W zapisie wektorowym prędkość ciała

$$
\vec{v}(t) = \frac{d\vec{r}(t)}{dt} = \left(\frac{dx(t)}{dt}, \frac{dy(t)}{dt}, \frac{dz(t)}{dt}\right)
$$


### Przyspieszenie

Przyspieszenie ciała to pochodna prędkości ciała po czasie. W zapisie wektorowym przyspieszenie ciała

$$
\vec{a}(t) = \frac{d\vec{v}(t)}{dt} = \left(\frac{dv_x(t)}{dt}, \frac{dv_y(t)}{dt}, \frac{dv_z(t)}{dt}\right)
$$

w zapisie drugiej pochodnej położenia ciała względem czasu

$$
\vec{a}(t) = \frac{d^2\vec{r}(t)}{dt^2} = \left(\frac{d^2x(t)}{dt^2}, \frac{d^2y(t)}{dt^2}, \frac{d^2z(t)}{dt^2}\right)
$$


## Prawa Newtona (I, II, III)

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

Załóżmu, że na ciało działa siła $\vec{F}$ i ciało przesuwa się o wektor $\vec{r}$. Praca siły $\vec{F}$ jest równa iloczynowi skalarnemu siły $\vec{F}$ i przesunięcia $\vec{r}$.

![Praca_01](https://upload.wikimedia.org/wikipedia/commons/7/73/Mehaaniline_t%C3%B6%C3%B6.png)


## Siły potencjalne

## Energia kinetyczna i potencjalna, zachowanie energii mechanicznej

## Zasada zachowania pędu

## Związek symetrii z zachowaniem wielkości fizycznych

## Rzut ukośny, ruch po okręgu, oscylacje, układy oscylatorów -> zjawiska falowe
 
