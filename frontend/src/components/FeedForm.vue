<template>
    <form v-on:submit.prevent="submitForm" method="post">
        <div class="p-4">  
            <input v-model="title" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="Title" />

            <textarea v-model="description" class="p-4 w-full bg-gray-100 rounded-lg mt-4" placeholder="What do you want to advertise about the job?"></textarea>

            <div id="preview" v-if="url">
                <img :src="url" class="w-[100px] mt-3 rounded-xl" />
            </div>

            <input type="date" v-model="deadline" class="p-4 w-full bg-gray-100 rounded-lg mt-4" placeholder="Deadline" />
        </div>

        <div class="p-4 border-t border-gray-100 flex justify-between">
            <label class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg">
                <input type="file" ref="file" @change="onFileChange">
                Attach document
            </label>

            <button class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">Post</button>
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
