<template>
    <div class="max-w-4xl mx-auto sm:px-6 lg:px-8">
        <label for="default-search" class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white">Search</label>
        <div class="relative">
            <div class="absolute inset-y-0 left-2.5 flex items-center ps-3 pointer-events-none">
                <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
                </svg>
            </div>
            <input type="search" id="default-search" v-model="inputText" class="block w-full p-4 pl-12 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="詢問知識庫" required>
            <button type="submit" id="searchButton" @click="submit" class="text-white absolute right-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">傳送</button>
        </div>
        <!-- <trendList></trendList> -->
    </div>
</template>

<script setup>
import { onMounted, ref, watch } from 'vue';
import { useStore } from 'vuex';
import liff from "@line/liff";

const inputText = ref('');
const store = useStore();

onMounted(async ()=>{
    document.addEventListener('loadSearchHistory', (e)=>{
        inputText.value = e.detail.history.title;
    })

    let response = await fetch("/liffid");
    let data = await response.json();
    let liffId = data['liff_id'];
    await liff.init({
        liffId: liffId, // 從LIFF頁面中拿到的ID
    })
    .then(async() => {

        //獲取 IDToken 並呼叫 API 驗證 以作為後端帳號
        if (liff.isLoggedIn()) {
            const idToken = liff.getIDToken();
            if (idToken) {
                fetch("/line_id/"+idToken);
            }
        }

        //監聽 sendMessage 事件
        document.addEventListener('sendMessage', (e)=>{
            console.log(e.detail.text);
            liff.sendMessages([
                {
                    type: 'text',
                    text: e.detail.text
                }

            ]).then(res => {console.log(res);liff.closeWindow()})
                .catch(error => console.log(error));
        })

    })
    .catch((err) => {
        console.log(err.code, err.message);
    });

})

function submit(){
    const sendMessageEvent = new CustomEvent('sendMessage', {
        detail: {
            text: inputText.value
        }
    })
    document.dispatchEvent(sendMessageEvent);
}

watch(store.state.nowData, (newVal)=>{
    inputText.value = newVal.title;
})

watch(inputText, (newVal)=>{
    let nowData = store.getters.getData;
    nowData.title = newVal
    store.dispatch('setData', nowData)
})

</script>
