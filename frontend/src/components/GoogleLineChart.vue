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
          const ticker = Object.keys(eps_data)[0];
          const chartData = eps_data[ticker].map(point => [
          point[0],
          point[1],
          ]);

          // Set the chart data
          this.ticker = ticker
          this.chartData = [['Date', 'EPS'], ...chartData];
      }
      catch (error){
          console.error(error);
      }
    },
  },
}
</script>
  