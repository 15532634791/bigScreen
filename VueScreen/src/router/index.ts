import {createRouter, createWebHistory} from 'vue-router'
import Login from '@/views/login/Login.vue'
import ScreenHome from '@/views/BigScreen/ScreenHome.vue';
const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            redirect: '/login'
        },
        {
            path: '/login',
            name: 'login',
            component: Login
        },
        {
            path: '/screen',
            name: 'home',
            component: ScreenHome,
            meta: {islogin : true},
            children: [
                {
                    path: '/page1',
                    name: 'page1',
                    component: () => import('@/views/BigScreen/ScreenHome.vue'),
                    meta: {islogin : true}
                },
                {
                    path: '/page2',
                    name: 'page2',
                    component: () => import('@/views/BigScreen/ScreenPage1.vue'),
                    meta: {islogin : true}
                },
            ]
        },
    ]
})
router.beforeEach((to, from, next) => {
      console.log(to)
      console.log(from)
    if (to.meta.islogin){
        let token = localStorage.getItem('token') //获取存储对象
        if (token == null){
            return  next({path: '/login'})
        }

    }
      return next()
    }
)
export default router