from yattag import Doc
from yattag import indent
import pandas as pd
import sys

# project folder name is the first and only command line argument to the script
project = sys.argv[1]

# import project-specific information from manually generated blurb and image files
# blurb file format explained in README
blurb_file = open(project + '/blurb.html', 'r')
blurb_lines = blurb_file.readlines()
detail_title = blurb_lines[0][:-1]
detail_medium = blurb_lines[1][:-1]
detail_date = blurb_lines[2][:-1]
detail_blurb = ''.join([str(line) for line in blurb_lines[3:]])
image_df = pd.read_csv(project + '/images.csv', header = None)
detail_images = list(image_df[0])
detail_images_alt = list(image_df[1])

# instantiate a doc object with its useful tag and text methods
doc, tag, text = Doc().tagtext()

# add necessary first tags
doc.asis('<!DOCTYPE html>')
doc.asis('<html lang="en">')
with tag('html'):
    # add the header with meta information, css link, and favicon
    with tag('head'):
        doc.stag('meta', name = 'description', content = "Niko's Website")
        doc.stag('meta', charset = 'utf-8')
        doc.stag('meta', name = 'viewport', content = 'width=device-width, initial-scale=1')
        doc.stag('meta', name = 'author', content = "Niko Darci-Maher")
        with tag('title'):
            text('Niko Darci-Maher')
        doc.stag('link', rel = 'stylesheet', href = '../niko.css')
        doc.stag('link', rel = 'icon', type = 'image/x-icon', href = '../favicon.png')
    # add the document body
    with tag('body'):
        with tag('div', ('class', 'wrapper')):
            # link back to homepage
            with tag('div', ('class', 'page-header-detail')):
                with tag('a', href = '../index.html'):
                    with tag('h1'):
                        text('ndm')
            # text and media columns
            with tag('div', ('class', 'page-main')):
                with tag('div', ('class', 'detailcolumns')):
                    # text column with title, two subtitles, blurb
                    with tag('div', ('class', 'detailcolumn-text')):
                        with tag('h2'):
                            text(detail_title)
                        with tag('h3'):
                            text(detail_medium)
                            doc.stag('br')
                            text(detail_date)
                        with tag('p'):
                            # blurb goes in as-is... needs to be in html syntax
                            doc.asis(detail_blurb)
                    # media column with a tile for each image in the input list
                    with tag('div', ('class', 'detailcolumn-media')):
                        for i in range(0, len(detail_images)):
                            with tag('div', ('class', 'detailcolumn-media-tile')):
                                doc.stag('img', src = detail_images[i], alt = detail_images_alt[i])

# generate output HTML text with automatic tab indenting
html_document = indent(doc.getvalue(), indentation = '\t')

# write the new HTML file in this project's directory
with open(project + '/index.html', 'w') as f:
    f.write(html_document)