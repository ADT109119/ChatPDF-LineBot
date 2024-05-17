<template>
	<div style="display: grid; grid-template-columns: 1fr">
		<span class="text-gray-400">使用模型:</span>
		<div class="models pb-2">
			<span
				:class="'cityButton ' + (index == data.model ? 'active' : '')"
				v-for="(item, index) in store.getters.models"
				@click="data.model = item.id"
				:key="item.id"
			>
				{{ item.name }}
			</span>
		</div>
		<div class="mt-2">
			<div class="relative w-full min-w-[200px] h-10">
				<input
					v-model="data.name"
					class="peer w-full h-full bg-gray-100 text-blue-gray-700 font-sans font-normal outline outline-0 focus:outline-0 disabled:bg-blue-gray-50 disabled:border-0 transition-all placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 border focus:border-2 border-t-transparent focus:border-t-transparent text-sm px-3 py-2.5 rounded-[7px] border-blue-gray-200 focus:border-gray-900"
					placeholder=" "
				/><label
					class="flex w-full h-full select-none pointer-events-none absolute left-0 font-normal !overflow-visible truncate peer-placeholder-shown:text-blue-gray-500 leading-tight peer-focus:leading-tight peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500 transition-all -top-1.5 peer-placeholder-shown:text-sm text-[11px] peer-focus:text-[11px] before:content[' '] before:block before:box-border before:w-2.5 before:h-1.5 before:mt-[6.5px] before:mr-1 peer-placeholder-shown:before:border-transparent before:rounded-tl-md before:border-t peer-focus:before:border-t-2 before:border-l peer-focus:before:border-l-2 before:pointer-events-none before:transition-all peer-disabled:before:border-transparent after:content[' '] after:block after:flex-grow after:box-border after:w-2.5 after:h-1.5 after:mt-[6.5px] after:ml-1 peer-placeholder-shown:after:border-transparent after:rounded-tr-md after:border-t peer-focus:after:border-t-2 after:border-r peer-focus:after:border-r-2 after:pointer-events-none after:transition-all peer-disabled:after:border-transparent peer-placeholder-shown:leading-[3.75] text-gray-500 peer-focus:text-gray-900 before:border-blue-gray-200 peer-focus:before:!border-gray-900 after:border-blue-gray-200 peer-focus:after:!border-gray-900"
				>
					知識庫名稱
				</label>
			</div>
		</div>

		<div class="mt-2">
			<div class="relative w-full min-w-[200px] h-10">
				<input
					type="number"
					max="1"
					min="0"
					v-model="data.temperature"
					class="peer w-full h-full bg-gray-100 text-blue-gray-700 font-sans font-normal outline outline-0 focus:outline-0 disabled:bg-blue-gray-50 disabled:border-0 transition-all placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 border focus:border-2 border-t-transparent focus:border-t-transparent text-sm px-3 py-2.5 rounded-[7px] border-blue-gray-200 focus:border-gray-900"
					placeholder=" "
				/><label
					class="flex w-full h-full select-none pointer-events-none absolute left-0 font-normal !overflow-visible truncate peer-placeholder-shown:text-blue-gray-500 leading-tight peer-focus:leading-tight peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500 transition-all -top-1.5 peer-placeholder-shown:text-sm text-[11px] peer-focus:text-[11px] before:content[' '] before:block before:box-border before:w-2.5 before:h-1.5 before:mt-[6.5px] before:mr-1 peer-placeholder-shown:before:border-transparent before:rounded-tl-md before:border-t peer-focus:before:border-t-2 before:border-l peer-focus:before:border-l-2 before:pointer-events-none before:transition-all peer-disabled:before:border-transparent after:content[' '] after:block after:flex-grow after:box-border after:w-2.5 after:h-1.5 after:mt-[6.5px] after:ml-1 peer-placeholder-shown:after:border-transparent after:rounded-tr-md after:border-t peer-focus:after:border-t-2 after:border-r peer-focus:after:border-r-2 after:pointer-events-none after:transition-all peer-disabled:after:border-transparent peer-placeholder-shown:leading-[3.75] text-gray-500 peer-focus:text-gray-900 before:border-blue-gray-200 peer-focus:before:!border-gray-900 after:border-blue-gray-200 peer-focus:after:!border-gray-900"
				>
					temperature
				</label>
			</div>
		</div>

		<div class="mt-2">
			<div class="relative w-full min-w-[200px] h-10">
				<input
					type="number"
					max="1"
					min="0"
					v-model="data.score_threshold"
					class="peer w-full h-full bg-gray-100 text-blue-gray-700 font-sans font-normal outline outline-0 focus:outline-0 disabled:bg-blue-gray-50 disabled:border-0 transition-all placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 border focus:border-2 border-t-transparent focus:border-t-transparent text-sm px-3 py-2.5 rounded-[7px] border-blue-gray-200 focus:border-gray-900"
					placeholder=" "
				/><label
					class="flex w-full h-full select-none pointer-events-none absolute left-0 font-normal !overflow-visible truncate peer-placeholder-shown:text-blue-gray-500 leading-tight peer-focus:leading-tight peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500 transition-all -top-1.5 peer-placeholder-shown:text-sm text-[11px] peer-focus:text-[11px] before:content[' '] before:block before:box-border before:w-2.5 before:h-1.5 before:mt-[6.5px] before:mr-1 peer-placeholder-shown:before:border-transparent before:rounded-tl-md before:border-t peer-focus:before:border-t-2 before:border-l peer-focus:before:border-l-2 before:pointer-events-none before:transition-all peer-disabled:before:border-transparent after:content[' '] after:block after:flex-grow after:box-border after:w-2.5 after:h-1.5 after:mt-[6.5px] after:ml-1 peer-placeholder-shown:after:border-transparent after:rounded-tr-md after:border-t peer-focus:after:border-t-2 after:border-r peer-focus:after:border-r-2 after:pointer-events-none after:transition-all peer-disabled:after:border-transparent peer-placeholder-shown:leading-[3.75] text-gray-500 peer-focus:text-gray-900 before:border-blue-gray-200 peer-focus:before:!border-gray-900 after:border-blue-gray-200 peer-focus:after:!border-gray-900"
				>
					Score Threshold(搜尋相關度)
				</label>
			</div>
		</div>

		<div class="mt-2">
			<div class="relative w-full min-w-[200px] h-10">
				<input
					type="number"
					min="1"
					v-model="data.search_item_limit"
					class="peer w-full h-full bg-gray-100 text-blue-gray-700 font-sans font-normal outline outline-0 focus:outline-0 disabled:bg-blue-gray-50 disabled:border-0 transition-all placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 border focus:border-2 border-t-transparent focus:border-t-transparent text-sm px-3 py-2.5 rounded-[7px] border-blue-gray-200 focus:border-gray-900"
					placeholder=" "
				/><label
					class="flex w-full h-full select-none pointer-events-none absolute left-0 font-normal !overflow-visible truncate peer-placeholder-shown:text-blue-gray-500 leading-tight peer-focus:leading-tight peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500 transition-all -top-1.5 peer-placeholder-shown:text-sm text-[11px] peer-focus:text-[11px] before:content[' '] before:block before:box-border before:w-2.5 before:h-1.5 before:mt-[6.5px] before:mr-1 peer-placeholder-shown:before:border-transparent before:rounded-tl-md before:border-t peer-focus:before:border-t-2 before:border-l peer-focus:before:border-l-2 before:pointer-events-none before:transition-all peer-disabled:before:border-transparent after:content[' '] after:block after:flex-grow after:box-border after:w-2.5 after:h-1.5 after:mt-[6.5px] after:ml-1 peer-placeholder-shown:after:border-transparent after:rounded-tr-md after:border-t peer-focus:after:border-t-2 after:border-r peer-focus:after:border-r-2 after:pointer-events-none after:transition-all peer-disabled:after:border-transparent peer-placeholder-shown:leading-[3.75] text-gray-500 peer-focus:text-gray-900 before:border-blue-gray-200 peer-focus:before:!border-gray-900 after:border-blue-gray-200 peer-focus:after:!border-gray-900"
				>
					單次詢問搜尋資料量上限
				</label>
			</div>
		</div>

		<div class="mt-4 text-center mb-4">
			<button
				type="button"
				id="addFileToKnowledgeBase"
				@click="save_or_create_knowledge_base"
				class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
			>
				{{ data.id == 0 ? "創建知識庫" : "儲存" }}
			</button>
			<button
				v-show="data.id != 0"
				type="button"
				id="addFileToKnowledgeBase"
				@click="delete_knowledge_base"
				class="ml-4 text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-4 py-2"
			>
				刪除知識庫
			</button>
			<button
				type="button"
				id="addFileToKnowledgeBase"
				@click="save_or_create_knowledge_base"
				class="ml-4 text-gray-500 bg-transparent border-gray-500 border-2 hover:bg-gray-500 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2"
			>
				取消
			</button>
		</div>
	</div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useStore } from "vuex";
import Swal from "sweetalert2";

const store = useStore();
const data = ref({
	id: 0,
	name: "新建知識庫",
	model: 0,
	temperature: 0.3,
	score_threshold: 0.5,
	search_item_limit: 4,
});

onMounted(async () => {
	document.addEventListener("changeKnowledgeBase", (e) => {
		data.value = e.detail.data;
	});
});

async function save_or_create_knowledge_base() {
	if (data.value.id != 0) {
		// create
		let response = await fetch(`/api/knowledge_base/${data.value.id}`, {
			method: "PUT",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(data.value),
		});
		let jsondata = await response.json();
		if (jsondata["status"] == "success") {
			Swal.fire({
				title: "儲存成功!",
				text: "變更已儲存",
				icon: "success",
			});

			const event = new CustomEvent("refreshKB_List");
			document.dispatchEvent(event);
		}
	} else {
		let response = await fetch("/api/knowledge_base", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(data.value),
		});
		let jsondata = await response.json();
		if (jsondata["status"] == "success") {
			Swal.fire({
				title: "創建成功!",
				text: "知識庫已成功創建",
				icon: "success",
			});

			const event = new CustomEvent("refreshKB_List");
			document.dispatchEvent(event);
		}
		console.log(jsondata);
	}
}

async function delete_knowledge_base() {
	Swal.fire({
		title: "是否確定要刪除知識庫?",
		text: "刪除的知識庫不可復原，但是檔案並不會被刪除",
		icon: "warning",
		showCancelButton: true,
        confirmButtonColor: "#d33",
		confirmButtonText: "刪除",
        cancelButtonText: "取消",
	}).then(async(result) => {
		if (result.isConfirmed) {

            if (data.value.id != 0) {
                // create
                let response = await fetch(`/api/knowledge_base/${data.value.id}`, {
                    method: "DELETE",
                });
                let jsondata = await response.json();
                if (jsondata["status"] == "success") {
                    Swal.fire({
                        title: "已成功刪除!",
                        text: "此知識庫已成功刪除",
                        icon: "success",
                    });
                    const event = new CustomEvent("delete_kb");
                    document.dispatchEvent(event);
                }
            }
			
		}
	});

}
</script>

<style>
.models {
	display: flex;
	flex-direction: row;
	gap: 1rem;
	overflow-x: scroll;
	width: 100%;
}

.models span.cityButton {
	padding: 0.5rem;
	border-radius: 6px;
	border: 2px gray solid;
	text-wrap: nowrap;
	transition: 0.1s;
	cursor: pointer;
}

.models span.cityButton.active {
	color: rgba(59, 130, 246, 1);
	border: 2px rgba(59, 130, 246, 1) solid;
}

.areaNum {
	font-size: 12px;
	background-color: gray;
	color: white;
	border-radius: 10000px;
	padding: 0.2rem 0.7rem;
	vertical-align: text-top;
}

.areaNum.active {
	background-color: rgba(59, 130, 246, 1);
}

/*
#selectAll{
    position: relative;
}

#selectAll:has(~ label input:checked)::before{
    content: "-";
    position: absolute;
    left: 0;
    top: 0;
    background: rgb(0, 117, 255);
}
*/
</style>
