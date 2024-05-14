<template>
    <div class="max-w-4xl w-full mx-auto sm:px-6 lg:px-8">
        <div class="mt-2 mb-4 bg-white overflow-hidden shadow sm:rounded-lg p-6">
            <h2 class="text-2xl leading-7 font-semibold">
                知識庫名稱: {{ props.kb.name }}
            </h2>
            <p class="mt-3 text-gray-600">
                <span  class="modelDisplay">模型: 
                    {{ store.getters.models[props.kb.model].name }}
                </span>
                <br>
                temperature: <span>{{ props.kb.temperature }}</span><br>
                搜尋嚴格度: <span>{{ props.kb.score_threshold }}</span><br>
                單次參考量上限: <span>{{ props.kb.search_item_limit }}</span><br>
            </p>
            <p class="mt-4 pt-4 text-gray-800 border-t border-t-2 text-right">
                <a href="#" class="text-blue-600" @click="chosekb">選擇知識庫 ></a>
            </p>
        </div>
    </div>
</template>

<script setup>
import {defineProps} from 'vue';
import { useStore } from 'vuex';


const props = defineProps({
    kb:{
        type: Object
    }
})

const store = useStore();

function chosekb(){
    // 觸發選擇知識庫事件
    const sendMessageEvent = new CustomEvent('sendMessage', {
        detail: {
            text: `/select ${props.kb.id}`
        }
    })
    document.dispatchEvent(sendMessageEvent);
}

</script>

<style>
.modelDisplay{
    text-overflow: ellipsis;
    max-lines: 1;
    overflow:hidden;
    white-space: nowrap;
    width: 80%;
}
</style>