<template>
    <div class="inline-flex items-center">
        <div class="relative inline-block w-8 h-4 rounded-full cursor-pointer">
            <input v-model="checked" :id="'switch' + props.fileid" type="checkbox"
            class="absolute w-8 h-4 transition-colors duration-300 rounded-full appearance-none cursor-pointer peer bg-blue-gray-100 checked:bg-gray-900 peer-checked:border-gray-900 peer-checked:before:bg-gray-900"
            :checked="props.active" />
            <label :htmlFor="'switch' + props.fileid"
            class="before:content[''] absolute top-2/4 -left-1 h-5 w-5 -translate-y-2/4 cursor-pointer rounded-full border border-blue-gray-100 bg-white shadow-md transition-all duration-300 before:absolute before:top-2/4 before:left-2/4 before:block before:h-10 before:w-10 before:-translate-y-2/4 before:-translate-x-2/4 before:rounded-full before:bg-blue-gray-500 before:opacity-0 before:transition-opacity hover:before:opacity-10 peer-checked:translate-x-full peer-checked:border-gray-900 peer-checked:before:bg-gray-900">
            <div class="inline-block p-5 rounded-full top-2/4 left-2/4 -translate-x-2/4 -translate-y-2/4"
                data-ripple-dark="true"></div>
            </label>
        </div>
    </div>
</template>

<script setup>
import { defineProps, watch, ref } from 'vue'
const props = defineProps({
    fileid:{
        type: Number,
        required: true
    },
    active:{
        type: Boolean,
        default: false
    },
    knowledgebaseid:{
        type: Number,
        required: true
    },
    callback:{
        type: Function,
        default: (val) => {console.log(val)}
    }
})

const checked = ref(props.checked)

watch(() => checked.value, (val) => {
    props.callback(val, props.fileid, props.knowledgebaseid)
})

</script>