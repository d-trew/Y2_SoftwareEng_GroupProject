<template>
    <div class="max-w-7xl mx-auto grid grid-cols-5 gap-4 pt-14">
        <div class="main-left col-span-1">
            <div class="p-0 pt-4 pb-4 bg-white border border-gray-200 text-center rounded-lg flex flex-col items-center justify-center">
                <img :src="getAvatarURL(user.avatar)" class="mb-6 rounded-full" style="height: 150px;">

                <p><strong>{{ user.name }}</strong></p>

                <div class="mt-6 flex space-x-8 justify-around">
                    <RouterLink :to="{name: 'connections', params: {id: user.id}}" class="text-xs text-gray-500">{{ user.connections_count }} Connections</RouterLink>
                    <p class="text-xs text-gray-500">0 Job Listings</p>
                </div>
            </div>
        </div>

        <div class="main-center col-span-3 space-y-4">
            <div class="bg-white border border-gray-200 rounded-lg">
                <FeedForm 
                    v-bind:user="null" 
                    v-bind:posts="posts"
                />
            </div>

            <div 
                v-for="post in posts"
                v-bind:key="post.id"
            >
                <FeedItem v-bind:post="post" v-on:deletePost="deletePost" />
            </div>
        </div>

        <div class="main-right col-span-1 space-y-4">
            <YouMayKnow />

            <Industries />
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import YouMayKnow from '../components/YouMayKnow.vue'
import Industries from '../components/Industries.vue'
import FeedItem from '../components/FeedItem.vue'
import FeedForm from '../components/FeedForm.vue'
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'

export default {
    name: 'FeedView',

    components: {
        YouMayKnow,
        Industries,
        FeedItem,
        FeedForm
    },

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
        getFeed() {
            axios
                .get('/api/posts/')
                .then(response => {
                    console.log('data', response.data)

                    this.posts = response.data
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        getAvatarURL(avatarPath) {
            if (avatarPath) {
                // Assuming WEBSITE_URL is a global variable that holds the base URL of your website
                return this.WEBSITE_URL + avatarPath;
            } else {
                // Fallback to default avatar URL
                return 'https://vectorified.com/images/no-profile-picture-icon-14.png';  // Replace with the actual URL
            }
        },

        deletePost(id) {
            this.posts = this.posts.filter(post => post.id !== id)
        },
    }
}
</script>