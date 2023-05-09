<template>
  <div>
    <GChart
      :data="chartData"
      :options="chartOptions"
      :type="'LineChart'"
    />
  </div>
</template>
  
<script>
import {GChart} from 'vue-google-charts/legacy'
import axios from 'axios'

export default {
  name: 'GoogleLineChart',
  components: {
    GChart,
  },
  data() {
    return {
      chartData: [],
      chartOptions: {
        title: 'Equity EPS Chart',
        curveType: 'function',
        legend: { position: 'bottom' },
        height: 400,
      },
      ticker: 'Ticker Name',
    }
  },
  mounted() {
    this.getData()
  },
  methods: {
    async getData() {
      try {
          let path = "http://" + window.location.hostname + ":5050/api/v1/equity_eps";
          const response = await axios.get(path)

          // const salesData = response.data
          // const chartData = [
          //   ['Year', 'Sales'],
          //   ...salesData.map((data) => [data.year, data.sales]),
          // ]

          const eps_data = response.data
          // Extract the stock symbol and data points from the response
          const ticker1 = Object.keys(eps_data)[0];
          const ticker2 = Object.keys(eps_data)[1];

          const data1 = eps_data[ticker1]
          const data2 = eps_data[ticker2]

          const chartData = []

          for (var i = 0; i < 4; i++) {
            const item = data1[i].concat(data2[i][1])
            chartData.push(item)
          }

          // Set the chart data
          this.chartData = [['Date', ticker1, ticker2], ...chartData];
      }
      catch (error){
          console.error(error);
      }
    },
  },
}
</script>
  