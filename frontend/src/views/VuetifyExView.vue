<template>
    <div id="app">
      <MyComponent /><br>
      <v-btn>Success</v-btn><br>
      <v-btn>Error</v-btn><br>
      <v-btn>Warning</v-btn><br>
      <v-btn>Info</v-btn>
    </div>
  </template>

  <script>
  import MyComponent from '@/components/VuetifyExample.vue';
  export default {
    name: 'VutifyExample',
    components: {
        MyComponent
    }
  };
  </script>
  
  <style>
  /* 스타일을 필요에 따라 추가합니다. */
  </style>
  