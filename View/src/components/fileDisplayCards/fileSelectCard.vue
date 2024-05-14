<template>

    <div class="bg-gray-100 p-6 pb-2 shadow relative">
        <img :src="require(`@/assets/icon/${filetype}.svg`)">
        <span class="font-bold text-l mt-2 block truncate">{{ props.filename }}</span>
    </div>

</template>

<script setup>
import { defineProps } from 'vue'
// import switchButton from '@/components/switchButton.vue'
// import Swal from "sweetalert2";


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
    }
})


</script>