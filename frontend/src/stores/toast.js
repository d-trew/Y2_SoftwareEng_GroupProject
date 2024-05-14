import { defineStore } from 'pinia'

export const useToastStore = defineStore({
    id: 'toast',

    state: () => ({
        ms: 0,
        message: '',
        classes: '',
        isVisible: false
    }),

    actions: {
        showToast({ ms, message, classes }) {
            console.log('Classes before setting:', this.classes); // Check the value of this.classes before setting it
            this.ms = parseInt(ms)
            this.message = message
            this.classes = classes
            console.log('Classes after setting:', this.classes); // Check the value of this.classes after setting it
    
            setTimeout(() => {
                console.log('Before addition:', this.classes);
                this.classes += ' -translate-y-28'
            }, 10)
    
            setTimeout(() => {
                console.log('Before replacement:', this.classes);
                this.classes = this.classes.replace(' -translate-y-28', '')
            }, this.ms - 500)
    
            setTimeout(() => {
                this.isVisible = false
            }, this.ms)
        }    
    }
})