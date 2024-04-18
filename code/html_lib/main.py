from jinja2 import Template


def escape_xml(html):
	escape_dict = [
		#{
		#	"key" : '"',
		#J	"value" : "&quot;"
		#},
		#{
		#	"key" : "'",
		#	"value" : "&apos;"
		#},
		{
			"key" : "<",
			"value" : "&lt;"
		},
		{
			"key" : ">",
			"value" : "&gt;"
		},
		#{
		#	"key" : "&",
		#	"value" : "&amp;"
		#}
	]
	for row in escape_dict:
		html = html.replace(row["key"], row["value"])
	return html

def get_template():
	with open("./template.html") as f:
		html = f.read()
		return Template(escape_xml(html))

print ()
