import Vue from 'vue';
import VueRouter from 'vue-router';
import Frontview from './src/views/Frontview.vue';
import viewData from './src/views/viewData.vue';

Vue.use(VueRouter);

export default new VueRouter({
    mode:'history',
    routes:[
        {
            path:'/',
            name:'frontview',
            component: Frontview,
        },
        {
            path:'/data',
            name:'viewdata',
            component: viewData,

        },
       
            
    ],
})