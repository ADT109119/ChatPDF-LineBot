import { createStore } from 'vuex'

export default createStore({
    state: {
        files:[],
        basicSetting:{
            "id": 0,
            "name":"新建知識庫",
            "model":0,
            "temperature": 0.3,
            "score_threshold": 0.5,
            "search_item_limit": 4
        },
        searchHistory: localStorage.getItem('searchHistory')!=null?JSON.parse(localStorage.getItem('searchHistory')):[],
        models: [],
        knowledgebase: []
    },
    getters: {
        getData(state){
            return state.nowData;
        },
        getHistory(state){
            return state.searchHistory;
        },
        getSetting(state){
            return state.basicSetting;
        },
        models(state){
            return state.models;
        },
        knowledgebase(state){
            return state.knowledgebase;
        },
        files(state){
            return state.files;
        },
    },
    mutations: {
        setData(state, val){
            state.nowData = val;
        },
        addHistory(state){
            state.searchHistory.unshift(JSON.parse(JSON.stringify(state.nowData)));
            localStorage.setItem('searchHistory', JSON.stringify(state.searchHistory))

            state.searchHistory.forEach((item, i)=> i>=10?state.searchHistory.pop():true )
        },
        setSetting(state, val){
            state.basicSetting = val;
        },
        setModels(state, val){
            state.models = val;
        },
        setKnowledgebase(state, val){
            state.knowledgebase = val;
        },
        setFiles(state, val){
            state.files = val;
        },
    },
    actions: {
        setData({ commit }, data){
            commit("setData", data)
        },
        addHistory({ commit }){
            commit("addHistory")
        },
        setSetting({ commit }, data){
            commit("setSetting", data)
        },
        setModels({ commit }, data){
            commit("setModels", data)
        },
        setKnowledgebase({ commit }, data){
            commit("setKnowledgebase", data)
        },
        setFiles({ commit }, data){
            commit("setFiles", data)
        }
    },
    modules: {
    }
})
