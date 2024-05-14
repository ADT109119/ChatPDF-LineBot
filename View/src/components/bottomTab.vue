<template>
  <div class="max-w-4xl mx-auto sm:px-6 lg:px-8 w-full">
    <div class="relative right-0">
      <ul
        class="relative flex flex-wrap p-1 list-none rounded-xl bg-blue-gray-50/60"
        data-tabs="tabs"
        role="list"
      >
        <li class="z-30 flex-auto text-center"  @click="changeTab(0)">
          <a
            class="z-30 flex items-center justify-center w-full px-0 py-1 mb-0 transition-all ease-in-out border-0 rounded-lg cursor-pointer text-slate-700 bg-inherit"
          >
            <span class="ml-1 text-gray-600 text-xl font-bold border-b-4 border-gray-300 buttonText text-blue-500">知識庫</span>
          </a>
        </li>
        <li class="z-30 flex-auto text-center" @click="changeTab(1)">
          <a
            class="z-30 flex items-center justify-center w-full px-0 py-1 mb-0 transition-all ease-in-out border-0 rounded-lg cursor-pointer text-slate-700 bg-inherit"
          >
            <span class="ml-1 text-gray-600 text-xl font-bold border-gray-300 buttonText">知識庫設定</span>
          </a>
        </li>
        <li class="z-30 flex-auto text-center" @click="changeTab(2)">
          <a
            class="z-30 flex items-center justify-center w-full px-0 py-1 mb-0 transition-all ease-in-out border-0 rounded-lg cursor-pointer text-slate-700 bg-inherit"
          >
            <span class="ml-1 text-gray-600 text-xl font-bold border-gray-300 buttonText">檔案管理</span>
          </a>
        </li>
      </ul>
      <div data-tab-content="" class="">
        <div class="block opacity-100 tabContent" id="knowledge_base" role="tabpanel">
          <p class="block font-sans text-base antialiased font-light leading-relaxed text-inherit text-blue-gray-500">
            <knowledgeBase></knowledgeBase>
          </p>
        </div>
        <div class="hidden opacity-0 tabContent" id="allfile" role="tabpanel">
          <p class="block font-sans text-base antialiased font-light leading-relaxed text-inherit text-blue-gray-500">
            <knowledgeBaseSetting></knowledgeBaseSetting>
          </p>
        </div>
        <div class="hidden opacity-0 tabContent" id="detailSearch" role="tabpanel">
          <p class="block font-sans text-base antialiased font-light leading-relaxed text-inherit text-blue-gray-500">
            <fileManager></fileManager>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import knowledgeBaseSetting from './knowledgeBaseSetting.vue';
import knowledgeBase from './knowledgeBase.vue';
import fileManager from './fileManager.vue';

onMounted(()=>{
})

function changeTab(tab){
    document.querySelectorAll('.buttonText').forEach((item, i) => {
        if(i != tab)
            item.classList.remove('border-b-4');
        else
            item.classList.add('border-b-4')

        if(i != tab)
            item.classList.remove('text-blue-500');
        else
            item.classList.add('text-blue-500')

    })

    document.querySelectorAll('.tabContent').forEach((item, i) => {
        if(i != tab)
            item.className = "hidden opacity-0 tabContent"
        else
            item.className = "block opacity-100 tabContent"
    })
}

</script>