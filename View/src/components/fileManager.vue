<template>

    <div class="bg-white p-6 shadow mt-2">

        <div class="text-3xl text-gray-500 font-bold mt-5 relative pb-4">
            檔案列表:
            <button type="button" id="addFileToKnowledgeBase" @click="OpenUploadWindow" class="text-white absolute right-2.5 top-0 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">添加檔案 +</button>
        </div>
        <div class="mt-2 grid grid-cols-2 gap-4">
            <fileDisplayCard nobutton="true" :filename="item.name" :filetype="item.filetype" :active="true" :fileid="item.id" v-for="(item, index) in files" :key="index"></fileDisplayCard>
        </div>


        <uploadWindow onlyupload="true" dkey="ALL_FILE"></uploadWindow>

    </div>

</template>

<script setup>
import fileDisplayCard from '@/components/fileDisplayCards/fileDisplayCard.vue'
import uploadWindow from './uploadWindow.vue'
import { onMounted, ref } from 'vue';
import { useStore } from 'vuex';

const store = useStore();
// const selectKnowledgeBase = ref(0);
const files = ref([]);

onMounted(async() => {
    // console.log(text)
    readData()
    document.addEventListener('refreshKB', ()=>{
        readData()
    })
})

async function readData(){
    let response = await fetch('/api/upload');
    let jsondata = await response.json()
    files.value = jsondata["data"]
    store.dispatch('setFiles', files.value)
}

function OpenUploadWindow(){
    const event = new CustomEvent('openUploadWindow', { detail: { display: true, dkey: "ALL_FILE" } });
    document.dispatchEvent(event);
}

</script>

<style>

</style>