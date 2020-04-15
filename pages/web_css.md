# [Web Design - CSS](https://alwinwoo.github.io/pages/web_css.html)
[home](https://alwinwoo.github.io/) | [edit](https://github.com/alwinwoo/alwinwoo.github.io/edit/master/pages/web_css.md)

To enable w3-CSS, need to add in the following into your HTML or php file in the head section

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
```

# W3.CSS Sectioning

* w3-container for div, header, footer, article, section, blockquote, form etc
* w3-display-container
  * w3-display (add -top, left, middle, right, bottom, -topleft, bottomright) in display-container

* w3-panel for notes, quotes, alerts (16px top-bottom margin, 16px left-right padding)
* w3-card for nice cards (add -2 or 4 for 2/4 bordered shadow)

```css
<div class="w3-panel w3-red w3-text-white">
  <h3>Warning</h3>
  This is a warning.
</div>

<div class="w3-red w3-text-black w3-hover-black w3-hover-text-white">
  <h3>Warning</h3>
  This is a warning.
</div>
```

# W3.CSS Responsive Layout
* w3-row or w3-row-padding (8px LR padding)
  * w3-half, third, twothird, quarter, threequarter
  * use style="width:xx%" possible as well
  * w3-rest (used best with fixed px in same w3-row -> it will occupy the rest - must be the last element)
    * use w3-left, right, center (to align within the container)
    * otherwise can use nested divs
  * w3-col (add -s, m or l for different screen sizes, 1 to 12 max per w3-row eg. w3-col1 or w3-col s4 m6)

```css
<div class="w3-row">
  <div class="w3-col" style="width:20%"><p>20%</p></div>
  <div class="w3-col" style="width:60%"><p>60%</p></div>
  <div class="w3-col" style="width:20%"><p>20%</p></div>
</div>
```

# For Decoration

* w3-round (add -small, large, xlarge, xxlarge to change size)

* w3-border / add (-left, right, top, bottom or 0)
* w3-border-<color>
* w3-hover-border-<color>
* w3-hover-shadow

* w3-leftbar / rightbar / topbar / bottombar (no spacing)
* w3-xxlarge (?)
* w3-serif   (serif font)

```css
<div class="w3-panel w3-blue w3-card-4 w3-round-xlarge">
  <p>text</p>
</div>

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

* W3 fonts

# Interactive + Alignment

* w3-button or w3-btn for buttons
* w3-input for forms

* w3-tooltip

* css filters to search within a list, table, dropdown

```javascript
<div class="w3-container">
  <h2>Filter List</h2>
  <p>Search for a name in the input field.</p>

  <input class="w3-input w3-border w3-padding" type="text" placeholder="Search for names.." id="myInput" onkeyup="myFunction()">
  <ul class="w3-ul w3-margin-top" id="myUL">
    <li>Adele</li>
    <li>Agnes</li>
    <li>Billy</li>
    <li>Bob</li>
    <li>Calvin</li>
    <li>Christina</li>
    <li>Cindy</li>
  </ul>
</div>

<script>
function myFunction() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  ul = document.getElementById("myUL");
  li = ul.getElementsByTagName("li");
  for (i = 0; i < li.length; i++) {
    txtValue = li[i].textContent || li[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = "";
    } else {
      li[i].style.display = "none";
    }
  }
}
</script>
```

* w3-modal for pop-up dialog in HTML
* to close a panel
```css
<div class="w3-panel w3-display-container">
  <span onclick="this.parentElement.style.display='none'" class="w3-button w3-display-topright">X</span>
  <p>Click on the X to close the panel</p>
</div>
```

# For Pictures

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

# For Social

* Open Graph - https://ogp.me/
* Laravel - https://hackernoon.com/how-to-fetch-open-graph-metadata-in-laravel-2d5d674904d7
* PHP OG extractor (old) - https://github.com/scottmac/opengraph
* Automating OG with PHP - https://computermentor.net/makingawebsite/tutorials-php/automating-open-graph.php

* extract metadata (working) - https://github.com/baj84/MetaData/blob/master/metadata.class.php

# Embed video / music into website

  - Video
  ```code
  <div style="position: fixed; z-index: -99; width: 100%; height: 100%">
    <iframe frameborder="0" height="100%" width="100%"
      src="https://youtube.com/embed/ID?autoplay=1&controls=0&showinfo=0&autohide=1">
    </iframe>
  </div>
  ```

  - Music
  ```code
  <embed height="0" width="0"
    src="http://youtube.googleapis.com/v/VIDEO_ID&autoplay=1&loop=1" />
  ```

  - <https://www.labnol.org/internet/youtube-video-background/27933/>


# References

* https://www.w3schools.com/w3css/default.asp
* https://bitsofco.de/sectioning-content-in-html5/
