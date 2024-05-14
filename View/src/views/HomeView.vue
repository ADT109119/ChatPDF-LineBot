<template>
  <div class="max-w-4xl mx-auto sm:px-6 lg:px-8 p-2.5">
      <!-- <div class="mt-8 bg-white overflow-hidden shadow sm:rounded-lg p-6">
          <h2 class="text-2xl leading-7 font-semibold">
              Welcome to your Nuxt Application
          </h2>
          <p class="mt-3 text-gray-600">
              We recommend you take a look at the <a href="https://nuxtjs.org" target="_blank" class="button--doc text-green-500 hover:underline">Nuxt Documentation</a>, whether you are new or have previous experience with the framework.<br>
          </p>
          <p class="mt-4 pt-4 text-gray-800 border-t border-dashed">
              To get started, remove <code class="bg-gray-100 text-sm p-1 rounded border">components/Tutorial.vue</code> and start coding in <code class="bg-gray-100 text-sm p-1 rounded border">pages/index.vue</code>. Have fun!
          </p>
      </div> -->
      <searchBar></searchBar>
      <bottomTab></bottomTab>
  </div>
</template>

<script setup>
import searchBar from '@/components/searchBar.vue';
import bottomTab from '@/components/bottomTab.vue';
import { onMounted } from 'vue';
import { useStore } from 'vuex';

const store = useStore()
onMounted(async () => {
    let response = await fetch('/api/model');
    let jsondata = await response.json()
    // models.value = jsondata['data'];
    if(jsondata['status'] == 'success'){
        store.dispatch('setModels', jsondata['data']);
    }

});

</script>
