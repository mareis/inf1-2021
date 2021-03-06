# Test deg selv 1

## 1.1 Filstruktur

---

Lag følgende filstruktur:

<img src="img/filstruktur.png" width="150px">

## 2.1

---

I index.html:

- Endre "title" til "Test deg selv 1".
- Lag en overskrift (<a href="https://www.w3schools.com/tags/tag_hn.asp">h1</a>) "Test deg selv 1" i <a href="https://www.w3schools.com/tags/tag_body.asp">body</a>.
- Lag en mindre overskrift (<a href="https://www.w3schools.com/tags/tag_hn.asp">h2</a>) "2.1".
- Lag en linje under med <a href="https://www.w3schools.com/tags/tag_hr.asp">hr</a>.
- Ta skjermbilde av filstrukturen til "Test_deg_selv"-mappen og legg det i img-mappen.
- bruk <a href="https://www.w3schools.com/tags/tag_img.asp">img-tagen</a> til å legge in skjermbildet på nettsiden.

## 2.2

---

I index.html:

- Lag en overskrift (<a href="https://www.w3schools.com/tags/tag_hn.asp">h2</a>) "2.2".
- Lag en linje under med <a href="https://www.w3schools.com/tags/tag_hr.asp">hr</a>.
- Lag en liste med <a href="https://www.w3schools.com/tags/tag_ul.asp">ul</a> der du lister opp komponentene vi har snakket om i timen.

## 2.3

---

I index.html:

- Lag en overskrift (<a href="https://www.w3schools.com/tags/tag_hn.asp">h2</a>) "2.3".
- Lag en linje under med <a href="https://www.w3schools.com/tags/tag_hr.asp">hr</a>.
- Lag en overskrift (<a href="https://www.w3schools.com/tags/tag_hn.asp">h3</a>) med teksten HTML.
- Lag to paragrafer (<a href="https://www.w3schools.com/tags/tag_p.asp">p</a>) med litt informasjon om <a html="https://en.wikipedia.org/wiki/HTML">HTML</a>.

## 3.1

---

I index.html:

- Legg til en <a href="https://www.w3schools.com/tags/tag_link.asp">link-tag</a> i <a href="https://www.w3schools.com/tags/tag_head.asp">head</a> for å koble til main.css i css-mappen din.

```html
<link rel="stylesheet" href="ccs/main.css" />
```

I main.css:

- Bytt farger
  - body-bagrunn: #9DD9D2 <a href="https://www.w3schools.com/cssref/pr_background-color.asp">tips</a>
  - h1: #392F5A <a href="https://www.w3schools.com/cssref/pr_text_color.asp">tips</a>
  - h2: #FF8811
  - p: #506B75

## 3.2

---

I index.html:

- Lag en overskrift (<a href="https://www.w3schools.com/tags/tag_hn.asp">h2</a>) "3.2".
- Lag en linje under med <a href="https://www.w3schools.com/tags/tag_hr.asp">hr</a>.
- Legg til en <a href="https://www.w3schools.com/tags/tag_div.asp">div-tag</a> med class="boks".

I main.css:

- Referer til til div-tagen og gjør følgende:

  - Bredde: 300px
  - Høyde: 150px
  - Bakgrunnsfarge: #392F5A
  - Ramme:

  ```css
  border: 10px solid #221c35;
  ```

  - Rund av kantene på boksen
  - Bruk <a href="https://www.w3schools.com/cssref/pr_margin.asp">margin</a> og test med 100px og auto. Hva skjer. Forklar i en p-tag inne i div-tagen i index.html.
  - Legg på <a href="https://www.w3schools.com/cssref/pr_padding.asp"> padding</a>. Prøv med ulike verdier (5px, 10px, 20px). Hva skjer? Forklar i en p-tag under den andre p-tagen i div-boksen.

eks:

```css
.boks {
  width: 300px;
  border: 10px solid #221c35;
}
.boks p {
  color: #fff8f0;
}
```

## 3.3

---

I index.html:

- Legg til en div rundt alt du har gjort inne i body som koden under.

```html
<body>
  <div class="hoved">...Resten av koden din...</div>
</body>
```

I main.css:

- sett bredden til div-en, med klasse hoved, til 600px bredde.

```css
.hoved {
  width: 800px;
  margin: auto;
}
```

- Velg fargen #FFF8F0 på bakgrunnen til hoved og legg til 20px padding.
