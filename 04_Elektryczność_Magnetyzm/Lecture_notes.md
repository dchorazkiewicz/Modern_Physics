# Elektrostatyka

## Prawo Coulomba

[Prawo Coulomba](https://pl.wikipedia.org/wiki/Prawo_Coulomba), [Coulomb's law](https://en.wikipedia.org/wiki/Coulomb%27s_law)

mówi, że siła oddziaływania między dwoma ładunkami elektrycznymi jest wprost proporcjonalna do iloczynu tych ładunków i odwrotnie proporcjonalna do kwadratu odległości między nimi. To prawo jest analogiczne do prawa grawitacji.

Porównajmy wzór na siłę grawitacji i wzór na siłę elektrostatyczną:

$$
F_g = G \frac{m_1 m_2}{r^2}
$$

$$
F_e = k \frac{q_1 q_2}{r^2}
$$

### Siła wypadkowa

Siła wypadkowa to suma wszystkich sił działających na dany obiekt. W przypadku sił elektrostatycznych siła wypadkowa to suma wszystkich sił elektrostatycznych działających na dany ładunek.

$$
\vec{F} = k \frac{q Q_1}{r_1^2} \hat{r_1} + k \frac{q Q_2}{r_2^2} \hat{r_2} + \ldots
$$


## Pole elektryczne

[Pole elektryczne](https://pl.wikipedia.org/wiki/Pole_elektryczne), [Electric field](https://en.wikipedia.org/wiki/Electric_field)

Pole elektryczne to pole wektorowe, które opisuje siłę, z jaką ładunek elektryczny działa na inne ładunki w przestrzeni. Pole elektryczne jest zdefiniowane jako siła elektryczna na jednostkowy dodatni ładunek.


$$
\vec{E} = \frac{\vec{F}}{q}
$$

## Pole eketryczne pochodzące od ładunków punktowych

Pole elektryczne pochodzące od ładunku punktowego $Q$ w odległości $r$ od niego jest równe:

$$
\vec{E} = k \frac{Q}{r_1^2} \hat{r_1}+ k \frac{Q}{r_2^2} \hat{r_2} + \ldots
$$


## Potencjał elektryczny

[Potencjał elektryczny](https://pl.wikipedia.org/wiki/Potencja%C5%82_elektryczny), [Electric potential](https://en.wikipedia.org/wiki/Electric_potential)

Potencjał elektryczny to wielkość skalarna, która opisuje energię potencjalną ładunku elektrycznego w danym punkcie przestrzeni. Potencjał elektryczny jest zdefiniowany jako praca wykonana przez siłę elektrostatyczną na jednostkowy dodatni ładunek, aby przenieść go z nieskończoności do danego punktu.

$$
V(\vec{r}) = \int_{\infty}^{\vec{r}} \vec{E} \cdot d\vec{l}
$$

zatem

$$
\vec{E} = - \nabla V
$$

Jeśli potencjał elektryczny jest znany, to pole elektryczne można obliczyć jako gradient potencjału!

# Magnetyzm

[Magnes](https://pl.wikipedia.org/wiki/Magnes), [Magnet](https://en.wikipedia.org/wiki/Magnet)

# Równania Maxwella

### Prawo Gaussa

[Prawo Gaussa](https://pl.wikipedia.org/wiki/Prawo_Gaussa), [Gauss's law](https://en.wikipedia.org/wiki/Gauss%27s_law)

$$
\oint \vec{E} \cdot d\vec{A} = \frac{Q}{\varepsilon_0}
$$

Prawo Gaussa mówi, że strumień pola elektrycznego przez dowolną zamkniętą powierzchnię jest równy ładunkowi elektrycznemu wewnątrz tej powierzchni podzielonemu przez przenikalność elektryczną próżni.

### Prawo Gaussa dla pola magnetycznego

Prawo Gaussa dla pola magnetycznego mówi, że strumień magnetyczny przez dowolną zamkniętą powierzchnię jest równy zeru.

$$
\oint \vec{B} \cdot d\vec{A} = 0
$$

Praktycznie oznacza to, że nie istnieją źródła pola magnetycznego.


### Prawo Faradaya

[Prawo Faradaya](https://pl.wikipedia.org/wiki/Prawo_Faradaya), [Faraday's law](https://en.wikipedia.org/wiki/Faraday%27s_law_of_induction)

Prawo Faradaya mówi, że siła elektromotoryczna indukowana w dowolnym obwodzie zamkniętym jest równa szybkości zmian strumienia magnetycznego przez powierzchnię ograniczoną przez ten obwód.

$$
\oint \vec{E} \cdot d\vec{l} = - \frac{d\Phi_B}{dt}
$$


### Prawo Ampère'a

[Prawo Ampère'a](https://pl.wikipedia.org/wiki/Prawo_Amp%C3%A8re%E2%80%99a), [Ampère's circuital law](https://en.wikipedia.org/wiki/Amp%C3%A8re%27s_circuital_law)

Prawo Ampère'a mówi, że całkowita siła magnetyczna wokół dowolnej zamkniętej krzywej jest równa całkowitemu prądowi przepływającemu przez tę krzywą.

$$
\oint \vec{B} \cdot d\vec{l} = \mu_0 I
$$


### Równania Maxwella

[Równania Maxwella](https://pl.wikipedia.org/wiki/R%C3%B3wnania_Maxwella), [Maxwell's equations](https://en.wikipedia.org/wiki/Maxwell%27s_equations)

Próżniowe równania Maxwella:

$$
\nabla \cdot \vec{E} = \frac{\rho}{\varepsilon_0}
$$

$$
\nabla \cdot \vec{B} = 0
$$

$$
\nabla \times \vec{E} = - \frac{\partial \vec{B}}{\partial t}
$$

$$
\nabla \times \vec{B} = \mu_0 \vec{J} + \mu_0 \varepsilon_0 \frac{\partial \vec{E}}{\partial t}
$$

gdzie:

- $\vec{E}$ to pole elektryczne,
- $\vec{B}$ to pole magnetyczne,
- $\rho$ to gęstość ładunku elektrycznego,
- $\varepsilon_0$ to przenikalność elektryczna próżni,
- $\mu_0$ to przenikalność magnetyczna próżni,
- $\vec{J}$ to gęstość prądu elektrycznego.