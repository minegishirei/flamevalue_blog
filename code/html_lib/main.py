from jinja2 import Template
html = '''

## test


<div style="width: 380px;"><canvas id="chart1"></canvas></div>
<p>
<script>
// ボタンをクリック
window.onload = function(){
	data1 = {{ money_countlist['lower'] }}
	data2 = {{ money_countlist['upper'] }}
  DrawChart(data1, data2); // グラフを再描画
}

// グラフ描画処理
function DrawChart(data1, data2) {
	var ctx = document.getElementById('chart1').getContext('2d');
	window.myChart = new Chart(ctx, {
	  type: 'line',
	  data: {
	    labels: ['3','5','10','Half','30','Full'],
	    datasets: [{
	      label: 'VDOT40',
	      data: data1,
	      borderColor: '#f88',
	    }, {
	      label: 'VDOT50',
	      data: data2,
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
