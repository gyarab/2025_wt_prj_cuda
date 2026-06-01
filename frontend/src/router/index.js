import { createRouter, createWebHistory } from 'vue-router'

import TradeList from '../views/TradeList.vue'
import TradeDetail from '../views/TradeDetail.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'home',
            component: TradeList
        },
        {
            path: '/trade/:id',
            name: 'trade-detail',
            component: TradeDetail
        }
    ]
})

export default router