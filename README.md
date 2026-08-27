# Niko's Website
This is a website for Niko Darci-Maher's personal gallery of creative projects.

## Notes
* Each folder represents an individual project. All media related to each project is stored inside that project's folder.

* `niko.css` describes CSS styles for the entire site.

* The `index.html` file in the home folder describes the website front page. Images on this page should be roughly 1MB in size.

* To generate the detail page for a project, use `gen_detail_index.py`, with that project's folder name as a command line argument. This script writes a new `index.html` into the corresponding project folder.

* `gen_detail_index.py` requires two files to be present inside the project folder to work correctly:
1. A text file called `blurb.html` with the following format:<br/>
Title<br/>
Project medium<br/>
Date [YYYY-MM-DD]<br/>
Blurb to be placed alongside the art piece, in HTML formatting (e.g. \<i>italics\</i> and line breaks \<br/>)

2. A csv file called `images.csv` with the following format (no quotes):<br/>
image1_filename,image1_alttext<br/>
image2_filename,image2_alttext<br/>
image3_filename,image3_alttext<br/>
etc...