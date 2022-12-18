# BCM Dev Notes

JuiceBoxBuilder-Lite (installed)
https://www.juicebox.net
https://www.juicebox.net/support

Set up a juicebox gallery and dropped in some images.
Builder dumps them into the specified gallery directory with juicebox structure/code
Can then access through mac simple http browser run in the toplevel juicebox directory
i.e.

(base) brucemoxon@tigrisbrucis debugdatasets % ls ~/Desktop/juicebox_gallery
config.xml	images		index.html	jbcore		thumbs

(nst-doodle) (base) brucemoxon@tigrisbrucis juicebox_gallery % python3 -m http.server 8000
Serving HTTP on :: port 8000 (http://[::]:8000/) ...

Then hit http://localhost:8000


imdims.py - report image dims for an image file (JPG, PNG, GIF)

open (and display) an image from URL
https://www.geeksforgeeks.org/how-to-open-an-image-from-the-url-in-pil/

(nst-doodle) (base) brucemoxon@tigrisbrucis Neural-Style-Transfer % pip install pillow
Requirement already satisfied: pillow in /Users/brucemoxon/DEV/pythonenvs/nst-doodle/lib/python3.9/site-packages (9.3.0)

See also
https://www.programcreek.com/python/example/81585/urllib.request.urlretrieve

# smugmug integration

For smugmug, links to images are effectively to a web service returning html, not an image.
Can set download links, but looks like need to allow downloads for the site, then restrict for
one or all galleries (?)

smugmug does have an api, with some examples of python apps abstracting and calling the apis

https://api.smugmug.com/api/v2/doc/tutorial/oauth/web.html
https://api.smugmug.com/api/v2/doc/tutorial/oauth/non-web.html

need to get an api key ...
https://api.smugmug.com/api/v2/doc/tutorial/api-key.html
