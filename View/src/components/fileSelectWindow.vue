<template>

    <div class="fileSelectWindowBackground" @click="displayChange" v-show="display">
        <div class="fileSelectWindow shadow rounded-lg p-6 bg-white relative">
            <h2 class="font-bold text-gray-600 text-3xl">選擇檔案</h2>
            <hr>
            <div class="grid grid-cols-2 h-full gap-4 mt-4 overflow-y-auto">
                <fileSelectCard @click="addFileToKnowledgeBase(item.id)" :filename="item.name" :filetype="item.filetype" :fileid="item.id" :key="index" v-for="(item, index) in store.getters.files"></fileSelectCard>
            </div>
            <span class="absolute right-4 top-2 text-4xl closeButton cursor-pointer" @click="displayChange">×</span>
        </div>
    </div>

</template>

<script setup>
import { onBeforeUnmount, onMounted, ref } from 'vue';
import Swal from 'sweetalert2';
import fileSelectCard from '@/components/fileDisplayCards/fileSelectCard.vue';
import { useStore } from 'vuex';

const store = useStore();

const knowledge_base_id = ref(0);
const display = ref(false);
function displayChange(e){
    if(e.target.className == 'fileSelectWindowBackground' || e.target.className.includes("closeButton"))
        display.value = false;
}

onMounted(() => {
    document.addEventListener("openSelectFileWindow", ()=>{
        display.value = true;
    })

    document.addEventListener("changeKnowledgeBase", (e)=>{
        knowledge_base_id.value = e.detail.data.id;
    })
});

onBeforeUnmount(() => {
    document.removeEventListener("openSelectFileWindow", ()=>{
        display.value = false;
    })
    document.removeEventListener("changeKnowledgeBase", (e)=>{
        knowledge_base_id.value = e.detail.data.id;
    })
});

async function addFileToKnowledgeBase(id){
    await fetch(`/api/knowledge_base_setting/${knowledge_base_id.value}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({"file_id":id})
    })
    display.value = false;
    Swal.fire({
        title: "添加成功",
        text: "文件已添加至知識庫",
        icon: "success"
    })
    const event = new CustomEvent('refreshKB', { detail: { data: '' } });
    document.dispatchEvent(event);
}

</script>

<style>

.fileSelectWindowBackground{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0,0,0,0.5);
    z-index: 999;
}

.fileSelectWindow{
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%,-50%);
    width: 80%;
    aspect-ratio: 1/1;
    max-height: 70%;
    background-color: #fff;
    z-index: 1000;
}

</style>