from jinja2 import Template
html = '''


<h2>{{ name }}の評価</h2>

<canvas id="abilityChart"></canvas>


<script>
    var ctx = document.getElementById("abilityChart");
    var myRadarChart = new Chart(ctx, {
        type: 'radar', 
        data: { 
            labels: ["英語", "数学", "国語", "理科", "社会"],
            datasets: [{
                label: 'Aさん',
                data: [92, 72, 86, 74, 86],
                backgroundColor: 'RGBA(225,95,150, 0.5)',
                borderColor: 'RGBA(225,95,150, 1)',
                borderWidth: 1,
                pointBackgroundColor: 'RGB(46,106,177)'
            }, {
                label: 'Bさん',
                data: [73, 95, 80, 87, 79],
                backgroundColor: 'RGBA(115,255,25, 0.5)',
                borderColor: 'RGBA(115,255,25, 1)',
                borderWidth: 1,
                pointBackgroundColor: 'RGB(46,106,177)'
            }]
        },
        options: {
            title: {
                display: true,
                text: '試験成績'
            },
            scale:{
                ticks:{
                    suggestedMin: 0,
                    suggestedMax: 100,
                    stepSize: 10,
                    callback: function(value, index, values){
                        return  value +  '点'
                    }
                }
            }
        }
    });
</script>


<h2>{{ name }}の年収分布</h2>

<div style="width: 380px;"><canvas id="chart1"></canvas></div>
<p>
<script>
// ボタンをクリック
window.onload = function(){
	labels = ['100万', '200万', '300万','400万', '500万', '600万', '700万', '800万', '900万', '1000万']
	data1 = {{ money_countlist['lower'] }}
	data2 = {{ money_countlist['upper'] }}
  DrawChart(labels, data1, data2); // グラフを再描画
}

// グラフ描画処理
function DrawChart(labels, data1, data2) {
	var ctx = document.getElementById('chart1').getContext('2d');
	window.myChart = new Chart(ctx, {
	  type: 'bar',
	  data: {
	    labels: labels,
	    datasets: [{
	      label: '下限年収 (件)',
	      data: data1,
		  backgroundColor: '#9BD0F5'
	    }, {
	      label: '上限年収 (件)',
	      data: data2,
		  backgroundColor: '#FFB1C1'
	    }]
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
