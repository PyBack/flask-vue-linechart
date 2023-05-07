<template>
  <div>
    <h1>Equity EPS Line Chart Page</h1>
    <GoogleLineChart />
  </div>
</template>

<script>
import GoogleLineChart from '@/components/GoogleLineChart.vue';
export default {
    name: 'GoogleLineChartView',
    components: {
        GoogleLineChart
    }

};
</script>

<style>
</style>
