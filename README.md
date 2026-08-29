# Theo's Website
This is a website for Theo Darci-Maher's personal collection of creative projects.

## Notes
* Each folder represents an individual project or pieces connected to one another. All media related to each project is stored inside that project's folder.

* `theo.css` describes CSS styles for the entire site.

* The `index.html` file in the home folder describes the website front page. Images on this page should be roughly 1MB in size.

## Adding a new project

1. Create a directory inside `attofox.github.io` with a name for the project, e.g. `blue_bowls`.

2. Drop at least one image for the project into the project directory, and make a lower-res thumbnail image cropped to look good on the tile grid. Give the image files descriptive names.

3. Create a file called `blurb.html` inside the project directory, with this format:
```
Title
Project medium
Date
Blurb to be placed alongside the art piece, in HTML formatting (e.g. \<i>italics\</i> and line breaks \<br/>)
```

Example:
```
Blue Bowls
Ceramics
2024
Two bowls in a set, where the glaze changes from inside to out.
```

4. Create a file called `images.csv` inside the project folder, with this format (no quotes):
```
image1_filename,image1_alttext
image2_filename,image2_alttext
image3_filename,image3_alttext
etc...
```

Example:
```
main_iso.jpg,Isometric View of Two Red Ceramic Bowls
side_side.jpg,Side-by-side View of Two Red Ceramic Bowls
stack.jpg,Two stacked Red Ceramic Bowls
single.jpg,Single Red Ceramic Bowl
notes.jpg,Notes on these pieces
```

5. Run the python script (requires library yattag) to generate an index file for the project detail page:

```
python gen_detail_index.py <projectname>
```

Example:
```
python gen_detail_index.py blue_bowls
```

6. Add a new tile to the main `index.html` page linking to your new project detail page in the grid of image tiles. It goes inside the `<div class="frontpagetilegrid">` object, wherever you want it to land on the front page!

Example:
```{html}
<a href="blue_bowls/index.html" class="tile">
    <img src="blue_bowls/main_iso.jpg" alt="Blue Bowls Isoemtric Photo">
</a>
```