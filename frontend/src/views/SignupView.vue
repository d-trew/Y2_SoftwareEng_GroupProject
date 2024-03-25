<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <h1 class="mb-6 text-2xl">Sign up</h1>

                <p class="mb-6 text-gray-500">
                    CareerVue is a platform for job seekers and employers to connect. 
                    This is your gateway to a whole new world of employment opportunities. 
                    Sign up to get started!
                </p>

                <p class="font-bold">
                    Already have an account? <RouterLink :to="{'name': 'login'}" class="underline">Click here</RouterLink> to login instead!
                </p>
            </div>
        </div>
        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6" v-on:submit.prevent=submitForm()>
                    <div>
                        <label>Name</label><br>
                        <input type="text" v-model="form.name" placeholder="Your Full Name" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>Email</label><br>
                        <input type="email" v-model="form.email" placeholder="Your Email Address" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>Password</label><br>
                        <input type="password" v-model="form.password1" placeholder="Your Password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>Repeat Password</label><br>
                        <input type="password" v-model="form.password2" placeholder="Repear Your Password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <template v-if="errors.length > 0">
                        <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                            <p v-for="error in errors">{{ error }}</p>
                        </div>
                    </template>

                    <div>
                        <button class="py-4 px-6 bg-blue-500 text-white rounded-lg">Sign Up</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { useToastStore } from '@/stores/toast'

export default {
    setup(){
        const toastStore = useToastStore()

        return {
            toastStore
        }   
    },

    data(){
        return {
            form: {
                name: '',
                email: '',
                password1: '',
                password2: ''
            },
            errors: [],
        }
    },

    methods: {
        submitForm(){
            this.errors = []

            if(this.form.name === ''){
                this.errors.push('Name is required')
            }

            if(this.form.email === ''){
                this.errors.push('Email is required')
            }

            if(this.form.password1 === ''){
                this.errors.push('Password is required')
            }

            if(this.form.password1 !== this.form.password2){
                this.errors.push('Passwords do not match')
            }

            if(this.errors.length === 0){
                axios
                    .post('/api/signup', this.form)
                    .then(response => {
                        if (response.data.message === 'success') {
                            this.toastStore.showToast(5000,'Account created successfully', 'bg-emerald-500')

                            this.form = {
                                name: '',
                                email: '',
                                password1: '',
                                password2: ''
                            }
                        } else {
                            this.toastStore.showToast(5000,'An error occurred', 'bg-red-300')
                        }
                    })
                    .catch(error => {
                        console.log('error',error)
                    })
            }
        }
    }
}
</script>
