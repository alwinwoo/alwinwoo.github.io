# [Web Design - CSS](https://alwinwoo.github.io/pages/web_css.html)
[home](https://alwinwoo.github.io/) | [edit](https://github.com/alwinwoo/alwinwoo.github.io/edit/master/pages/web_css.md)

1. To enable w3-CSS, need to add in the following into your HTML or php file in the head section

```code
<link rel="stylesheet" href="https://www.w3schools.com/w3/css/4/w3.css">
```

# W3.CSS Colors

* w3-<color> for background
* w3-text-<color> for text
* w3-hover-<color> for color change
* w3-hover-text-<color> for hover change
  
```css
  Red, Orange, Yellow, Green, Blue, Purple
  Steel, Teal, Cobalt, Sienna
  Flame, Greenery, Marina, Primrose Yellow
  Neutral, Shaded, Navy, Tawny
  White, Gray or Grey, Black

<div class="w3-red w3-text-black w3-hover-black w3-hover-text-white">
  This is a warning.
</div>
```

# W3.CSS Sectioning

* w3-container for div, header, footer, article, section, blockquote, form etc.

* w3-panel for notes, quotes, alerts (16px top-bottom margin, 16px left-right padding)
```css
<div class="w3-panel w3-red w3-text-white">
  <h3>Warning</h3>
</div>

- w3-border / add (-left, right, top, bottom or 0)
- w3-border-<color>
- w3-hover-border-<color>
- w3-leftbar / rightbar / topbar / bottombar (no spacing)
- w3-xxlarge (?)
- w3-serif   (serif font)

<div class="w3-panel w3-blue w3-card-4 w3-round-xlarge">
  <p>text</p>
</div>

- w3-round (add -small, large, xlarge, xxlarge to change size)
```

* w3-card for nice cards (add -2 or 4 for 2/4 bordered shadow)

* w3-hover-shadow

```css
<div class="w3-card-4">
  <header class="w3-container w3-blue">
    My name
  </header>
    <img src="blah blah">
  <div class="w3-container w3-center">
    <p>text</p>
  </div>
  <footer class="w3-container w3-gray">
    Contact Me
  </footer>
</div>
```

* w3-table for tables
```css
<table class="w3-table w3-striped w3-border">
```
* w3-ul for lists
```css
<ul class="w3-ul w3-border">
  <li><h2>Names</h2></li>
  <li>Francis</li>
  ...
</ul>
```
* w3-tag or w3-badge for tags, labels etc.

* w3-tooltip

* W3 fonts

# Interactive + Alignment

* w3-button or w3-btn for buttons
* w3-display for top, left, middle, right, bottom etc.
* w3-input for forms

* css filters to search within a list, table, dropdown

* to close a panel
```css
<div class="w3-panel w3-display-container">
  <span onclick="this.parentElement.style.display='none'" class="w3-button w3-display-topright">X</span>
  <p>Click on the X to close the panel</p>
</div>
```

# For Pictures

* w3-modal for pop-up dialog in HTML

* image slideshows

* combine modals with slideshows to create lightbox

* styling images, add special effects

# For Navigation

* w3-dropdown display menus on hover, click

* w3 accordions to open sections

* tabs for multiple pages, or image gallery

* w3-bar to create a nav bar / with input / with dropdown

* w3-sidebar

* w3 page pagination





# References

* https://www.w3schools.com/w3css/default.asp
* https://bitsofco.de/sectioning-content-in-html5/
