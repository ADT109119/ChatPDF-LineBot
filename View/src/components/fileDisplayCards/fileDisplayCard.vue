<template>

    <div class="bg-gray-100 p-6 pb-2 shadow relative">
        <switchButton v-show="!props.nobutton" class="absolute right-2 top-3" :fileid="props.fileid" :knowledgebaseid="props.knowledgebaseid" :active="props.active" :callback="changeFileActive"></switchButton>

        <img :src="require(`@/assets/icon/${filetype}.svg`)">
        <span class="font-bold text-l mt-2 block truncate">{{ props.filename }}</span>
        <span class="absolute left-1 top-2" @click="delete_file">
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32"><path fill="currentColor" d="M12 12h2v12h-2zm6 0h2v12h-2z"/><path fill="currentColor" d="M4 6v2h2v20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8h2V6zm4 22V8h16v20zm4-26h8v2h-8z"/></svg>
        </span>
    </div>

</template>

<script setup>
import { defineProps } from 'vue'
import switchButton from '@/components/switchButton.vue'
import Swal from "sweetalert2";


const props = defineProps({
    filename: {
        type: String,
        required: true
    },
    filetype: {
        type: String,
        required: true
    },
    fileid: {
        type: Number,
        required: true
    },
    knowledgebaseid: {
        type: Number,
    },
    active: {
        type: Boolean,
        required: true
    },
    nobutton:{
        type: Boolean,
        default: false
    },
    nodelete:{
        type: Boolean,
        default: false
    }
})

async function changeFileActive(checked, fileid, knowledge_base_id){
    if(knowledge_base_id != undefined && !props.nobutton)
        fetch(`/api/knowledge_base_setting/${knowledge_base_id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                file_id: fileid,
                active: checked
            })
        })
        .then(res => res.json())
        .then(res => {
                console.log(res)
            })
        .catch(err => {
            console.log(err)
        })
}

async function delete_file(){
    if(props.fileid == undefined)
        return;

    if(props.nobutton){
        Swal.fire({
		title: "是否確定要刪除此檔案?",
		text: "刪除的檔案不可復原，並且此檔案會從全部知識庫中移除",
		icon: "warning",
		showCancelButton: true,
        confirmButtonColor: "#d33",
		confirmButtonText: "刪除",
        cancelButtonText: "取消",
	}).then(async(result) => {
		if (result.isConfirmed) {

            fetch(`/api/upload/${props.fileid}`, {
                method: 'DELETE',
            })
            .then(res => res.json())
            .then(res => {
                if(res.status == 'success'){
                    call_refresh();
                    Swal.fire({
                        title: '刪除成功!',
                        text: '檔案已成功刪除',
                        icon:'success',
                    })
                }else{
                    Swal.fire({
                        title: '錯誤',
                        icon: 'error',
                    })
                }
            })
            .catch(err => {
                console.log(err)
            })
        }
    })
    }else{
        fetch(`/api/knowledge_base_setting/${props.knowledgebaseid}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                file_id: props.fileid,
            })
        })
        .then(res => res.json())
        .then(res => {
            if(res.status == 'success'){
                call_refresh();
                Swal.fire({
                    title: '刪除成功!',
                    text: '檔案已從此知識庫刪除',
                    icon:'success',
                })
            }else{
                Swal.fire({
                    title: '錯誤',
                    icon: 'error',
                })
            }
        })
        .catch(err => {
            console.log(err)
        })
    }
}

function call_refresh(){
    const event = new CustomEvent("refreshKB")
    document.dispatchEvent(event);
}

// changeFileActive(true, 1)

</script>