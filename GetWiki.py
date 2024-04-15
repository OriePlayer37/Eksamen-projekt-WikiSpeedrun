import requests
import re 

url = 'https://en.wikipedia.org/wiki/Religious_order'
r = requests.get(url)
html = r.text

SMainBodyPattern = r'<main id="content" class="mw-body" role="main[\s\S]*?</main>'

SMainBody = str(re.findall(SMainBodyPattern, html))

SReferenceListPattern =r'<h2><span class="mw-headline" id="References">References</span>'

SAdditionalCitationPattern = r'<table class="box-More_citations_needed plainlinks metadata ambox ambox-content ambox-Refimprove" role="presentation">[\s\S]*?</tbody></table>'

SMain = str(re.split(SReferenceListPattern, SMainBody, maxsplit=1))

SMain = str(re.split(SAdditionalCitationPattern, SMain))

