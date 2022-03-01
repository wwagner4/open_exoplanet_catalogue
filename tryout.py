from typing import IO
from xml.etree.ElementTree import parse
import urllib.request
import gzip
import io

url = "https://github.com/OpenExoplanetCatalogue/oec_gzip/raw/master/systems.xml.gz"
read = urllib.request.urlopen(url).read()
bytes_io = io.BytesIO(read)
file = gzip.GzipFile(fileobj=bytes_io)
oec = parse(file)

# Output mass and radius of all planets
for planet in oec.findall(".//planet")[0:10]:
    print(planet)
    print(planet.findtext("mass"), planet.findtext("radius"))
