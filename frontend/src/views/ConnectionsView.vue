<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
                <img :src="user.get_avatar" class="mb-6 rounded-full">
                
                <p><strong>{{ user.name }}</strong></p>

                <div class="mt-6 flex space-x-8 justify-around">
                    <p class="text-xs text-gray-500">{{ user.connections_count }} connections</p>
                    <!-- <p class="text-xs text-gray-500">{{ user.posts_count }} posts</p> -->
                </div>
            </div>
        </div>

        <div class="main-center col-span-2 space-y-4">
            <div 
                class="p-4 bg-white border border-gray-200 rounded-lg"
                v-if="connectionRequests.length"
            >
                <h2 class="mb-6 text-xl">connection requests</h2>

                <div 
                    class="p-4 text-center bg-gray-100 rounded-lg"
                    v-for="connectionRequest in connectionRequests"
                    v-bind:key="connection.id"
                >
                    <img :src="connectionRequest.created_by.get_avatar" class="mb-6 mx-auto rounded-full">
                
                    <p>
                        <strong>
                            <RouterLink :to="{name: 'profile', params:{'id': connectionRequest.created_by.id}}">{{ connectionRequest.created_by.name }}</RouterLink>
                        </strong>
                    </p>

                    <div class="mt-6 flex space-x-8 justify-around">
                        <p class="text-xs text-gray-500">{{ user.connections_count }} connections</p>
                        <!-- <p class="text-xs text-gray-500">{{ user.posts_count }} posts</p> -->
                    </div>

                    <div class="mt-6 space-x-4">
                        <button class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg" @click="handleRequest('accepted', connectionRequest.created_by.id)">Accept</button>
                        <button class="inline-block py-4 px-6 bg-red-600 text-white rounded-lg" @click="handleRequest('rejected', connectionRequest.created_by.id)">Reject</button>
                    </div>
                </div>

                <hr>
            </div>

            <div 
                class="p-4 bg-white border border-gray-200 rounded-lg grid grid-cols-2 gap-4"
                v-if="connections.length"
            >
                <div 
                    class="p-4 text-center bg-gray-100 rounded-lg"
                    v-for="user in connections"
                    v-bind:key="user.id"
                >
                    <img :src="user.get_avatar" class="mb-6 rounded-full">
                
                    <p>
                        <strong>
                            <RouterLink :to="{name: 'profile', params:{'id': user.id}}">{{ user.name }}</RouterLink>
                        </strong>
                    </p>

                    <div class="mt-6 flex space-x-8 justify-around">
                        <p class="text-xs text-gray-500">{{ user.connections_count }} connections</p>
                        <!-- <p class="text-xs text-gray-500">{{ user.posts_count }} posts</p> -->
                    </div>
                </div>
            </div>
        </div>

        <div class="main-right col-span-1 space-y-4">
            <YouMayKnow />

            <!-- <Trends /> -->
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import YouMayKnow from '../components/YouMayKnow.vue'
// import Trends from '../components/Trends.vue'
// import FeedItem from '../components/FeedItem.vue'
import { useUserStore } from '@/stores/user'

export default {
    name: 'ConnectionsView',

    setup() {
        const userStore = useUserStore()

        return {
            userStore
        }
    },

    components: {
        YouMayKnow,
        // Trends
    },

    data() {
        return {
            user: {},
            connectionRequests: [],
            connections: []
        }
    },

    mounted() {
        this.getConnections()
    },

    methods: {
        getConnections() {
            axios
                .get(`/api/connections/${this.$route.params.id}/`)
                .then(response => {
                    console.log('data', response.data)

                    this.connectionRequests = response.data.requests
                    this.connections = response.data.connections
                    this.user = response.data.user
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        handleRequest(status, pk) {
            console.log('handleRequest', status)

            axios
                .post(`/api/connections/${pk}/${status}/`)
                .then(response => {
                    console.log('data', response.data)
                })
                .catch(error => {
                    console.log('error', error)
                })
        }
    }
}
</script>