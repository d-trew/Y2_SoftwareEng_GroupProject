import { defineStore } from "pinia"
import axios from "axios"

export const useUserStore = defineStore({
    id: "user",
    state: () => ({
        user: {
            id: null,
            name: null,
            email: null,
            access: null,
            refresh: null,
        }
    }),

    actions: {
        initStore() {
            if (localStorage.getItem("user")) {
                // this.user = JSON.parse(localStorage.getItem("user"))
                this.user.access = localStorage.getItem("user.access")
                this.user.refresh = localStorage.getItem("user.refresh")
                this.user.id = localStorage.getItem("user.id")
                this.user.name = localStorage.getItem("user.name")
                this.user.email = localStorage.getItem("user.email")
                this.user.isAuthentificated = true

                this.refreshToken()

                console.log("initilized user: ", this.user)
            }
        },

        setToken(data){
            console.log("setToken", data)

            this.user.access = data.access
            this.user.refresh = data.refresh
            this.user.isAuthentificated = true

            localStorage.setItem("user.access", data.access)
            localStorage.setItem("user.refresh", data.refresh)
        },

        removeToken(){
            this.user.access = null
            this.user.refresh = null
            this.user.isAuthentificated = false
            this.user.id = null
            this.user.name = null
            this.user.email = null

            localStorage.setItem("user.access", '')
            localStorage.setItem("user.refresh", '')
            localStorage.setItem("user.id", '')
            localStorage.setItem("user.name", '')
            localStorage.setItem("user.email", '')
        },

        setUserInfor(user){
            console.log("setUserInfor", user)

            this.user.id = user.id
            this.user.name = user.name
            this.user.email = user.email

            localStorage.setItem("user.id", user.id)
            localStorage.setItem("user.name", user.name)
            localStorage.setItem("user.email", user.email)

            console.log("user:", this.user)
        },

        refreshToken(){
            axios.post('/api/account/refresh/', {
                refresh: this.user.refresh
            })
                .then(response => {
                    this.user.access = response.data.access
                    
                    localStorage.setItem("user.access", response.data.access)

                    axios.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access
                })
                .catch(error => {
                    console.log("refreshToken error: ", error)

                    this.removeToken()
                })
            }

    }
})