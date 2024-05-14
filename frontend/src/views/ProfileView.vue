<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
                <img :src="getAvatarURL(user.avatar)" class="mb-6 rounded-full">
                
                <p><strong>{{ user.name }}</strong></p>
                <p><strong>{{ user.id }}</strong></p>

                <div class="mt-6 flex space-x-8 justify-around" v-if="user.id">
                    <RouterLink :to="{name: 'connections', params: {id: user.id}}" class="text-xs text-gray-500">{{ user.connections_count }} connections</RouterLink>
                    <p class="text-xs text-gray-500">{{ user.posts_count }} posts</p>
                </div>

                <div class="mt-6">
                    <button 
                        class="inline-block py-4 px-3 bg-purple-600 text-xs text-white rounded-lg" 
                        @click="sendconnectionRequest"
                        v-if="userStore.user.id !== user.id && can_send_connection_request"
                    >
                        Send connection request
                    </button>

                    <button 
                        class="inline-block mt-4 py-4 px-3 bg-purple-600 text-xs text-white rounded-lg" 
                        @click="sendDirectMessage"
                        v-if="userStore.user.id !== user.id"
                    >
                        Send direct message
                    </button>

                    <RouterLink 
                        class="inline-block mr-2 py-4 px-3 bg-purple-600 text-xs text-white rounded-lg" 
                        to="/profile/edit"
                        v-if="userStore.user.id === user.id"
                    >
                        Edit profile
                    </RouterLink>

                    <button 
                        class="inline-block py-4 px-3 bg-red-600 text-xs text-white rounded-lg" 
                        @click="logout"
                        v-if="userStore.user.id === user.id"
                    >
                        Log out
                    </button>
                </div>
            </div>
        </div>

        <div class="main-center col-span-2 space-y-4">
            <div 
                class="bg-white border border-gray-200 rounded-lg"
                v-if="userStore.user.id === user.id"
            >
                <FeedForm 
                    v-bind:user="user" 
                    v-bind:posts="posts"
                />
            </div>

            <div 
                class="p-4 bg-white border border-gray-200 rounded-lg"
                v-for="post in posts"
                v-bind:key="post.id"
            >
                <FeedItem v-bind:post="post" v-on:deletePost="deletePost"/>
            </div>
        </div>

        <div class="main-right col-span-1 space-y-4">
            <YouMayKnow />

            <!-- <Trends /> -->
        </div>
    </div>
</template>

<style>
input[type="file"] {
    display: none;
}

.custom-file-upload {
    border: 1px solid #ccc;
    display: inline-block;
    padding: 6px 12px;
    cursor: pointer;
}
</style>

<script>
import axios from 'axios'
import YouMayKnow from '../components/YouMayKnow.vue'
import FeedItem from '../components/FeedItem.vue'
import FeedForm from '../components/FeedForm.vue'
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'

export default {
    name: 'ProfileView',

    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore()
        const WEBSITE_URL = 'http://127.0.0.1:8000';
        return {
            userStore,
            toastStore,
            WEBSITE_URL
        }
    },
    
    data() {
        return {
            posts: [],
            user :{
                    id: '',
                    name: '',
                    email: '',
                    avatar: '',
                    connections_count: 0
                },
                can_send_connection_request: null,
        }
    },

    created() {
        // Fetch user data asynchronously
        const fetchUserData = async () => {
            try {
                const response = await axios.get('/api/me/')
                const userData = response.data
                this.user.id = userData.id
                this.user.name = userData.name
                this.user.email = userData.email
                this.user.avatar = userData.avatar
                this.user.connections_count = userData.connections_count
                this.user.get_avatar = userData.avatar
                this.user.created_at = userData.created_at
            } catch (error) {
                console.error('Error fetching user data:', error)
                // Handle error if necessary
            }
        }

        // Call fetchUserData asynchronously
        fetchUserData()
    },

    components: {
        YouMayKnow,
        // Trends,
        FeedItem,
        FeedForm
    },
    mounted() {
        this.getFeed()
    },

    watch: { 
        '$route.params.id': {
            handler: function() {
                this.getFeed()
            },
            deep: true,
            immediate: true
        }
    },

    methods: {
        // deletePost(id) {
        //     this.posts = this.posts.filter(post => post.id !== id)
        // },
        getAvatarURL(avatarPath) {
            if (avatarPath) {
                // Assuming WEBSITE_URL is a global variable that holds the base URL of your website
                return this.WEBSITE_URL + avatarPath;
            } else {
                // Fallback to default avatar URL
                return 'http://127.0.0.1:8000/media/avatars/default.png';  // Replace with the actual URL
            }
        },
        sendDirectMessage() {
            console.log('sendDirectMessage')

            axios
                .get(`/api/chat/${this.$route.params.id}/get-or-create/`)
                .then(response => {
                    console.log(response.data)

                    this.$router.push('/chat')
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        sendConnectionRequest() {
            axios
                .post(`/api/connections/${this.$route.params.id}/request/`)
                .then(response => {
                    console.log('data', response.data)

                    this.can_send_connection_request = false

                    if (response.data.message == 'request already sent') {
                        this.toastStore.showToast(5000, 'The request has already been sent!', 'bg-red-300')
                    } else {
                        this.toastStore.showToast(5000, 'The request was sent!', 'bg-emerald-300')
                    }
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
        // no jobs create by users rn
        getFeed() {
            axios
                .get(`/api/posts/profile/${this.$route.params.id}/`)
                .then(response => {
                    console.log('data', response.data)
                    console.log('user', response.data.user)
                    this.posts = response.data.posts
                    this.user = response.data.user
                    this.can_send_friendship_request = response.data.can_send_friendship_request
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        logout() {
            console.log('Log out')

            this.userStore.removeToken()

            this.$router.push('/login')
        }
    }
}
</script>