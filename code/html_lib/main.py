from jinja2 import Template
html = '''

## test


<div style="width: 380px;"><canvas id="chart1"></canvas></div>
<p>
<script>
// ボタンをクリック
window.onload = function(){
  DrawChart(); // グラフを再描画
}

// グラフ描画処理
function DrawChart() {
	var ctx = document.getElementById('chart1').getContext('2d');
	window.myChart = new Chart(ctx, {
	  type: 'line',
	  data: {
	    labels: ['3','5','10','Half','30','Full'],
	    datasets: [{
	      label: 'VDOT40',
	      data: [843,1448,3003,6659,9687,13785],
	      borderColor: '#f88',
	    }, {
	      label: 'VDOT50',
	      data: [693,1197,2481,5495,8002,11449],
	      borderColor: '#484',
	    }, {
	      label: 'VDOT60',
	      data: [590,1023,2122,4689,6828,9805],
	      borderColor: '#48f',
	    }],
	  },
	  options: {
	    y: {
	      min: 0,
	      max: 15000,
	    },
	  },
	});
}
</script>


## test done

'''


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
    return Template(escape_xml(html))

print ()
