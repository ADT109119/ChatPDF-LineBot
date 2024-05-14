<template>

    <div class="uploadWindowBackground" @click="displayChange" v-show="display">
        <div class="uploadWindow shadow rounded-lg p-6 bg-white relative">
            <h2 class="font-bold text-gray-600 text-3xl">上傳檔案</h2>
            <hr>
            <div class="grid grid-rows-2 h-full gap-4 mt-4">
                <label v-show="!props.onlyupload" class="bg-gray-200 rounded p-6 text-center" @click="openSelectFileWindow">
                    <div class="flex h-full justify-center items-center">
                        <img class="h-full" :src="require('@/assets/icon/pdf.svg')">
                        <img class="h-full" :src="require('@/assets/icon/csv.svg')">
                        <img class="h-full" :src="require('@/assets/icon/txt.svg')">
                    </div>
                    <div>選擇已有檔案</div>
                </label>
                <label :for="`uploadFile_${dkey}`" class="bg-gray-200 rounded p-6 text-center">
                    <div v-show="progressbar == 0" class="flex h-full justify-center items-center">
                        <img class="h-full" :src="require('@/assets/icon/upload.svg')">
                    </div>
                    <div>
                        上傳新檔案
                    <div v-show="progressbar != 0">
                        <progress :value="progressbar" max="100" style="width: 100%;"></progress>
                        <span>{{ progresspercent }}</span>
                    </div>
                </div></label>

                <input ref="uploader" @change="uploadFile" type="file" :id="`uploadFile_${dkey}`" hidden>
            </div>
            <span class="absolute right-4 top-2 text-4xl closeButton cursor-pointer" @click="displayChange">×</span>
        </div>
    </div>

</template>

<script setup>
import { onMounted, ref, defineProps } from 'vue';
import Swal from 'sweetalert2';

const props = defineProps({
    dkey:{
        type: String,
        default: ""
    },
    onlyupload: {
        type: Boolean,
        default: false
    }
})

const knowledge_base_id = ref(0);
const display = ref(false);
function displayChange(e){
    if(e.target.className == 'uploadWindowBackground' || e.target.className.includes("closeButton"))
        display.value = false;
}

onMounted(() => {
    document.addEventListener("openUploadWindow", (e)=>{
        if(props.dkey == e.detail.dkey)
            display.value = true;
    })

    document.addEventListener("changeKnowledgeBase", (e)=>{
        knowledge_base_id.value = e.detail.data.id;
    })
});

const uploader = ref()
const progresspercent = ref("0%")
const progressbar = ref(0)
async function uploadFile(e){
    const file = e.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/api/upload', true);

    xhr.upload.addEventListener("progress", (progressEvent) => {
        const percent = Math.round((progressEvent.loaded / progressEvent.total) * 100);
        progressbar.value = percent;
        progresspercent.value = `${percent}%`;
    });

    xhr.onload = () => {
        if (xhr.status === 200) {
            const jsondata = JSON.parse(xhr.responseText);
            e.target.value = ''; // 清空文件輸入框

            if (jsondata['status'] === 'success') {
                progressbar.value = 0;
                progresspercent.value = "0%";
                Swal.fire({
                    title: "上傳成功",
                    text: "文件已成功上傳",
                    icon: "success"
                })
                if(!props.onlyupload)
                    addFileToKnowledgeBase(jsondata['file_id']);
            }
        }else{
            const errorMessage = JSON.parse(xhr.responseText).detail;
            Swal.fire({
                title: "上傳失敗",
                text: errorMessage,
                icon: "error"
            })
        }
    };

    xhr.onerror = (e) => {
        alert("上傳失敗")
        alert(e)
        Swal.fire({
            title: "上傳失敗",
            text: e,
            icon: "error"
        })
    };

    xhr.send(formData);
}

async function addFileToKnowledgeBase(id){
    await fetch(`/api/knowledge_base_setting/${knowledge_base_id.value}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({"file_id":id})
    })
    display.value = false;
    const event = new CustomEvent('refreshKB', { detail: { data: '' } });
    document.dispatchEvent(event);
}

async function openSelectFileWindow(){
    const event = new CustomEvent('openSelectFileWindow', { detail: { data: '' } });
    await document.dispatchEvent(event);
    display.value = false;
}

</script>

<style>

.uploadWindowBackground{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0,0,0,0.5);
    z-index: 999;
}

.uploadWindow{
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