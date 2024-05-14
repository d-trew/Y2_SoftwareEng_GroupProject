<template>
	<nav class="py-5 px-8 border-b bg-white border-gray-200 fixed top-0 w-full z-30">
        <div class="max-w-7xl mx-auto">
            <div class="flex items-center justify-between">
                <div class="menu-left">
                    <a href="/">
                        <img src="/namelogo.png" alt="CareerVue Logo" class="text-xl" style="height: 35px;">
                    </a>
                </div>

                <div class="menu-right flex space-x-12" v-if="userStore.user.isAuthenticated">
                    <RouterLink to="/feed">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6">
                            <path d="M11.47 3.841a.75.75 0 0 1 1.06 0l8.69 8.69a.75.75 0 1 0 1.06-1.061l-8.689-8.69a2.25 2.25 0 0 0-3.182 0l-8.69 8.69a.75.75 0 1 0 1.061 1.06l8.69-8.689Z" />
                            <path d="m12 5.432 8.159 8.159c.03.03.06.058.091.086v6.198c0 1.035-.84 1.875-1.875 1.875H15a.75.75 0 0 1-.75-.75v-4.5a.75.75 0 0 0-.75-.75h-3a.75.75 0 0 0-.75.75V21a.75.75 0 0 1-.75.75H5.625a1.875 1.875 0 0 1-1.875-1.875v-6.198a2.29 2.29 0 0 0 .091-.086L12 5.432Z" />
                        </svg>
                    </RouterLink>

                    <RouterLink to="/chat">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6">
                            <path fill-rule="evenodd" d="M4.848 2.771A49.144 49.144 0 0 1 12 2.25c2.43 0 4.817.178 7.152.52 1.978.292 3.348 2.024 3.348 3.97v6.02c0 1.946-1.37 3.678-3.348 3.97a48.901 48.901 0 0 1-3.476.383.39.39 0 0 0-.297.17l-2.755 4.133a.75.75 0 0 1-1.248 0l-2.755-4.133a.39.39 0 0 0-.297-.17 48.9 48.9 0 0 1-3.476-.384c-1.978-.29-3.348-2.024-3.348-3.97V6.741c0-1.946 1.37-3.68 3.348-3.97ZM6.75 8.25a.75.75 0 0 1 .75-.75h9a.75.75 0 0 1 0 1.5h-9a.75.75 0 0 1-.75-.75Zm.75 2.25a.75.75 0 0 0 0 1.5H12a.75.75 0 0 0 0-1.5H7.5Z" clip-rule="evenodd" />
                        </svg>                            
                    </RouterLink>

                    <RouterLink to="/notifications">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6">
                            <path d="M5.85 3.5a.75.75 0 0 0-1.117-1 9.719 9.719 0 0 0-2.348 4.876.75.75 0 0 0 1.479.248A8.219 8.219 0 0 1 5.85 3.5ZM19.267 2.5a.75.75 0 1 0-1.118 1 8.22 8.22 0 0 1 1.987 4.124.75.75 0 0 0 1.48-.248A9.72 9.72 0 0 0 19.266 2.5Z" />
                            <path fill-rule="evenodd" d="M12 2.25A6.75 6.75 0 0 0 5.25 9v.75a8.217 8.217 0 0 1-2.119 5.52.75.75 0 0 0 .298 1.206c1.544.57 3.16.99 4.831 1.243a3.75 3.75 0 1 0 7.48 0 24.583 24.583 0 0 0 4.83-1.244.75.75 0 0 0 .298-1.205 8.217 8.217 0 0 1-2.118-5.52V9A6.75 6.75 0 0 0 12 2.25ZM9.75 18c0-.034 0-.067.002-.1a25.05 25.05 0 0 0 4.496 0l.002.1a2.25 2.25 0 1 1-4.5 0Z" clip-rule="evenodd" />
                        </svg>                             
                    </RouterLink>

                    <RouterLink to="/search">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6">
                            <path d="M8.25 10.875a2.625 2.625 0 1 1 5.25 0 2.625 2.625 0 0 1-5.25 0Z" />
                            <path fill-rule="evenodd" d="M12 2.25c-5.385 0-9.75 4.365-9.75 9.75s4.365 9.75 9.75 9.75 9.75-4.365 9.75-9.75S17.385 2.25 12 2.25Zm-1.125 4.5a4.125 4.125 0 1 0 2.338 7.524l2.007 2.006a.75.75 0 1 0 1.06-1.06l-2.006-2.007a4.125 4.125 0 0 0-3.399-6.463Z" clip-rule="evenodd" />
                        </svg>                                                        
                    </RouterLink>

                    <template v-if="userStore.user.isAuthenticated && userStore.user.id">
                        <RouterLink :to="{name: 'profile', params:{'id': userStore.user.id}}">
                        <!-- Include the 'media' prefix in the avatar URL -->
                        <img :src="getAvatarURL(userStore.user.avatar)" class="rounded-full w-8">
                        </RouterLink>
                    </template>

                    <template v-else>
                        <RouterLink to="/login" class="mr-4 py-4 px-6 bg-black text-white rounded-lg">Log in</RouterLink>
                        <RouterLink to="/signup" class="py-4 px-6 bg-blue-500 text-white rounded-lg">Sign up</RouterLink>
                    </template>
                </div>

                <!-- <div class="menu-right">
                    <template v-if="userStore.user.isAuthenticated && userStore.user.id">
                        <RouterLink :to="{name: 'profile', params:{'id': userStore.user.id}}">
                        <img :src="userStore.user.avatar" class="w-12 rounded-full">
                        </RouterLink>
                    </template>

                    <template v-else>
                        <RouterLink to="/login" class="mr-4 py-4 px-6 bg-gray-600 text-white rounded-lg">Log in</RouterLink>
                        <RouterLink to="/signup" class="py-4 px-6 bg-purple-600 text-white rounded-lg">Sign up</RouterLink>
                    </template>
                </div> -->
            </div>
        </div>
    </nav>

    <main class="px-8 py-10 border-b bg-black border-gray-200 min-h-screen">
        <RouterView />
    </main>

    <Toast />
</template>

<script>
import axios from 'axios'
import Toast from '@/components/Toast.vue'
import { useUserStore } from '@/stores/user'
import { computed, onMounted } from 'vue';

export default {
    setup() {
        const userStore = useUserStore()

        // Ensure that user is reactive
        const user = computed(() => userStore.user)
        const WEBSITE_URL = 'http://127.0.0.1:8000'
        // Initialize store on component mount
        onMounted(() => {
            userStore.initStore()

            const token = user.value.access

            if (token) {
                axios.defaults.headers.common["Authorization"] = "Bearer " + token;
            } else {
                axios.defaults.headers.common["Authorization"] = "";
            }
        })

        return {
            user,
            userStore,
            WEBSITE_URL
        }
    },

    components: {
        Toast
    },

    methods: {
        getAvatarURL(avatarPath) {
            if (avatarPath) {
                // Assuming WEBSITE_URL is a global variable that holds the base URL of your website
                return this.WEBSITE_URL + avatarPath;
            } else {
                // Fallback to default avatar URL
                return 'http://127.0.0.1:8000/media/avatars/default.png';  // Replace with the actual URL
            }
        },
    }

}
</script>
