# Niko's Website
This is a website for Niko Darci-Maher's personal gallery of creative projects.

## Notes
* Each folder represents an individual project. All media related to each project is stored inside that project's folder.

* `niko.css` describes CSS styles for the entire site.

* The `index.html` file in the home folder describes the website front page. Images on this page should be roughly 1MB in size.

## Adding a new project

1. Create a directory inside `attofox.github.io` with a name for the project, e.g. `banana`.

2. Drop at least one image for the project into the project directory, and make a lower-res thumbnail image cropped to look good on the tile grid. Give the image files descriptive names.

3. Create a file called `blurb.html` inside the project directory, with this format:
```
Title
Project medium
Date [YYYY-MM-DD]
Blurb to be placed alongside the art piece, in HTML formatting (e.g. \<i>italics\</i> and line breaks \<br/>)
```

Example:
```
Banana House
Architectural Design
2017-5-25
I designed this house, inspired by a bunch of bananas, as my final project in my 12th grade Architecture class at Oakland Technical High School. 
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
architecture_banana.png,Banana House
topview.png,Top View 
sideview.png,Side View
downhillview.png,Downhill View 
sectionview.PNG,Section View
```

5. Run the python script (requires library yattag) to generate an index file for the project detail page:

```
python gen_detail_index.py <projectname>
```

Example:
```
python gen_detail_index.py banana
```

6. Add a new tile to the main `index.html` page linking to your new project detail page in the grid of image tiles. It goes inside the `<div class="frontpagetilegrid">` object, wherever you want it to land on the front page!

Example:
```{html}
<a href="banana/index.html" class="tile">
    <img src="banana/architecture_banana_thumbnail.png" alt="Banana House">
</a>
```