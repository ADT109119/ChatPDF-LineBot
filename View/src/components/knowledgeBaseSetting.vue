<template>

    <div>
        <div class="bg-white p-6 shadow mt-2 pt-4 pb-4">
            <span class="text-gray-600">知識庫</span>
            <br>
            <select class="w-full p-2 pl-0" v-model="selectKnowledgeBase">
                <option value="0" selected>創建知識庫</option>
                <option :value="item.id" v-for="(item, index) in knowledgeBase" :key="index">{{item.name}}</option>
            </select>
        </div>

        <div class="bg-white p-6 shadow mt-4">

            <div class="text-3xl text-gray-500 font-bold">
                基本設定:
            </div>
            <div class="mt-2" id="cityFilter">
                <basicSetting></basicSetting>
            </div>

            <hr>

            <div v-show="selectKnowledgeBase!= 0">
                <div class="text-3xl text-gray-500 font-bold mt-5 relative pb-4">
                    檔案列表:
                    <button type="button" id="addFileToKnowledgeBase" @click="OpenUploadWindow" class="text-white absolute right-2.5 top-0 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">添加檔案 +</button>
                </div>
                <div class="mt-2 grid grid-cols-2 gap-4">
                    <fileDisplayCard :filename="item.name" :filetype="item.filetype" :active="item.active" :fileid="item.id" :knowledgebaseid="selectKnowledgeBase" v-for="(item, index) in files" :key="index+'_'+selectKnowledgeBase"></fileDisplayCard>
                </div>

            </div>


        </div>

        <uploadWindow dkey="UPLOAD_KB"></uploadWindow>
        <fileSelectWindow></fileSelectWindow>
    </div>
</template>

<script setup>
import fileDisplayCard from '@/components/fileDisplayCards/fileDisplayCard.vue'
import basicSetting from './basicSetting.vue'
import uploadWindow from './uploadWindow.vue'
import fileSelectWindow from './fileSelectWindow.vue'
import { onMounted, ref, watch } from 'vue';
import { useStore } from 'vuex';

const knowledgeBase = ref([])
const selectKnowledgeBase = ref(0);
const files = ref();
const store = useStore();

onMounted(async() => {
    // console.log(text)
    readKB_List()
    document.addEventListener('refreshKB', ()=>{
        readData(selectKnowledgeBase.value)
    })

    document.addEventListener('refreshKB_List', ()=>{
        readKB_List()
    })

    document.addEventListener('delete_kb', ()=>{
        selectKnowledgeBase.value = 0;
        readKB_List()
    })

})

watch(selectKnowledgeBase, async(newValue) => {
    // console.log(newValue)
    if(newValue == 0)
        ChangeKnowledgeBase(store.getters.getSetting);
    else
        readData(newValue);
})

async function readKB_List(){
    let response = await fetch('/api/knowledge_base');
    let jsondata = await response.json()
    if(jsondata["status"] == "success"){
        knowledgeBase.value = jsondata["data"]
        store.dispatch("setKnowledgebase", jsondata["data"])
    }
}

async function readData(newValue){
    let response = await fetch(`/api/knowledge_base_setting/${newValue}`);
    let jsondata = await response.json()
    files.value = jsondata["data"]

    let response2 = await fetch(`/api/knowledge_base/${newValue}`);
    let jsondata2 = await response2.json()
    if(jsondata2['status'] == 'success')
        ChangeKnowledgeBase(jsondata2['data'])
    else
        ChangeKnowledgeBase(store.getters.getSetting)
}

function OpenUploadWindow(){
    const event = new CustomEvent('openUploadWindow', { detail: { display: true , dkey: "UPLOAD_KB" } });
    document.dispatchEvent(event);
}

function ChangeKnowledgeBase(data){
    const event = new CustomEvent('changeKnowledgeBase', { detail: { data: data } });
    document.dispatchEvent(event);
}

</script>

<style>

</style>