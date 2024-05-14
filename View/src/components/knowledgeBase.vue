<template>
    <div class="recentSearchList">
        <whiteBackground v-for="(item, index) in store.getters.knowledgebase" :key="index" :kb="item"></whiteBackground>
        <div class="text-gray-500 text-center text-xl pt-20" v-show="store.getters.knowledgebase.length == 0">您目前尚未創建知識庫</div>
    </div>
</template>

<script setup>
import { useStore } from 'vuex';
import whiteBackground from './whiteBackground.vue';

const store = useStore();

</script>
