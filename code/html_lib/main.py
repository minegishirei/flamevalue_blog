from jinja2 import Template
html = '''


<h2>{{ name }}の評価</h2>

<div>
<canvas id="abilityChart"></canvas>
</div>

<script>
	var LABEL_MASTER = [
		{
			"key" : "money",
			"name" : "下限年収"
		},
		{
			"key" : "overtime",
			"name" : "上限年収"
		},
		{
			"key" : "qiita_score",
			"name" : "フォロワー数(Qiita)"
		},
		{
			"key" : "remote",
			"name" : "リモート率"
		},
		{
			"key" : "count",
			"name" : "求人件数"
		}
	]
	var labelname = "{{ name }}"
	var score_100 = {{ score_100 }}
	console.log(score_100)
	var data = LABEL_MASTER.map((row)=>(score_100[row.key]))
	var labels = LABEL_MASTER.map((row)=>row.name)

    var ctx = document.getElementById("abilityChart");
    var myRadarChart = new Chart(ctx, {
        type: 'radar', 
        data: { 
            labels: labels,
            datasets: [{
                label: labelname,
                data: data,
                backgroundColor: 'RGBA(225,95,150, 0.5)',
                borderColor: 'RGBA(225,95,150, 1)',
                borderWidth: 1
            }]
        },
        options: {
            title: {
                display: true,
                text: '言語評価チャート'
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




<h2>{{ name }}の評価</h2>


<table>
	<tr>
		<td>
			下限年収
		</td>
		<td>
			{{　basic["money"] }} 万円 / 年
		</td>
	</tr>
	<tr>
		<td>
			上限年収
		</td>
		<td>
			{{ basic["overtime"] }} 万円 / 年
		</td>
	</tr>
	<tr>
		<td>
			フォロワー数(Qiita)
		</td>
		<td>
			{{ basic["qiita_score"] }} 人
		</td>
	</tr>
	<tr>
		<td>
			リモート率
		</td>
		<td>
			{{ basic["remote"] }} %
		</td>
	</tr>
	<tr>
		<td>
			求人件数
		</td>
		<td>
			{{ basic["count"] }} 件
		</td>
	</tr>
</table>











<h2>{{ name }}の年収分布</h2>

<div><canvas id="chart1"></canvas></div>
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
