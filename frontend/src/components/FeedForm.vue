<template>
    <form v-on:submit.prevent="submitForm" method="post">
        <div class="p-4">  
            <input v-model="title" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="Job Title" />

            <textarea v-model="description" class="p-4 w-full bg-gray-100 rounded-lg mt-4" placeholder="Insert your Job description and advertisement."></textarea>

            <div id="preview" v-if="url">
                <img :src="url" class="w-[100px] mt-3 rounded-xl" />
            </div>

            <input type="date" v-model="deadline" class="p-4 w-full bg-gray-100 rounded-lg mt-4" placeholder="Deadline" />
        </div>

        <div class="p-4 border-t border-gray-100 flex justify-between">
            <label class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg">
                <input type="file" ref="file" @change="onFileChange">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="m18.375 12.739-7.693 7.693a4.5 4.5 0 0 1-6.364-6.364l10.94-10.94A3 3 0 1 1 19.5 7.372L8.552 18.32m.009-.01-.01.01m5.699-9.941-7.81 7.81a1.5 1.5 0 0 0 2.112 2.13" />
                </svg>
            </label>

            <button class="inline-block py-4 px-6 bg-blue-500 text-white rounded-lg">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6">
                    <path d="M3.478 2.404a.75.75 0 0 0-.926.941l2.432 7.905H13.5a.75.75 0 0 1 0 1.5H4.984l-2.432 7.905a.75.75 0 0 0 .926.94 60.519 60.519 0 0 0 18.445-8.986.75.75 0 0 0 0-1.218A60.517 60.517 0 0 0 3.478 2.404Z" />
                </svg>
            </button>
        </div>
    </form>
</template>

<script>
import axios from 'axios'

export default {
    props: {
        user: Object,
        posts: Array
    },

    data() {
        return {
            title: '',
            description: '',
            // is_remote: false,
            deadline: '',
            url: null,
        }
    },

    methods: {
        submitForm() {
            console.log('submitForm', this.description)

            let formData = new FormData()
            formData.append('document', this.$refs.file.files[0])
            formData.append('title', this.title)
            formData.append('description', this.description)
            // formData.append('is_remote', this.is_remote)
            formData.append('deadline', this.deadline)

            axios
                .post('/api/posts/create/', formData, {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    }
                })
                .then(response => {
                    console.log('data', response.data)

                    this.posts.unshift(response.data)
                    this.title = ''
                    this.description = ''
                    // this.is_remote = false
                    this.$refs.file.value = null
                    this.url = null

                    if (this.user) {
                        this.user.posts_count += 1
                    }
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        onFileChange(event) {
            const file = event.target.files[0];
            this.url = URL.createObjectURL(file);
        }
    }
}
</script>
