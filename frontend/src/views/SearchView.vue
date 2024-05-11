<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4 pt-14">
        <div class="main-left col-span-3 space-y-4">
            <div class="p-4 bg-white border border-gray-200 rounded-lg">
                <div class="p-4 flex space-x-4">
                    <input type="search" class = "p-4 w-full bg-gray-100 rounded-lg" placeholder="Who are you looking for?">
                    <a href="#" class="inline-block py-4 px-6 bg-blue-500 text-white rounded-lg">Search</a>
                </div>
            </div>

            <div class="p-4 bg-white border border-gray-200 rounded-lg grid grid-cols-4 gap-4">
                <div class="p-4 text-center bg-gray-100 rounded-lg flex flex-col items-center justify-center">
                    <img src="https://vectorified.com/images/no-profile-picture-icon-14.png" class="mb-6 rounded-full" style="height: 150px;">

                    <p><strong>User Name</strong></p>

                    <div class="mt-6 flex space-x-8 justify-around">
                        <p class="text-xs text-gray-500">0 Connections</p>
                        <p class="text-xs text-gray-500">0 Job Listings</p>
                    </div>
                </div>

                <div class="p-4 text-center bg-gray-100 rounded-lg flex flex-col items-center justify-center">
                    <img src="https://vectorified.com/images/no-profile-picture-icon-14.png" class="mb-6 rounded-full" style="height: 150px;">

                    <p><strong>User Name</strong></p>

                    <div class="mt-6 flex space-x-8 justify-around">
                        <p class="text-xs text-gray-500">0 Connections</p>
                        <p class="text-xs text-gray-500">0 Job Listings</p>
                    </div>
                </div>

                <div class="p-4 text-center bg-gray-100 rounded-lg flex flex-col items-center justify-center">
                    <img src="https://vectorified.com/images/no-profile-picture-icon-14.png" class="mb-6 rounded-full" style="height: 150px;">

                    <p><strong>User Name</strong></p>

                    <div class="mt-6 flex space-x-8 justify-around">
                        <p class="text-xs text-gray-500">0 Connections</p>
                        <p class="text-xs text-gray-500">0 Job Listings</p>
                    </div>
                </div>

                <div class="p-4 text-center bg-gray-100 rounded-lg flex flex-col items-center justify-center">
                    <img src="https://vectorified.com/images/no-profile-picture-icon-14.png" class="mb-6 rounded-full" style="height: 150px;">

                    <p><strong>User Name</strong></p>

                    <div class="mt-6 flex space-x-8 justify-around">
                        <p class="text-xs text-gray-500">0 Connections</p>
                        <p class="text-xs text-gray-500">0 Job Listings</p>
                    </div>
                </div>

                <div class="p-4 text-center bg-gray-100 rounded-lg flex flex-col items-center justify-center">
                    <img src="https://vectorified.com/images/no-profile-picture-icon-14.png" class="mb-6 rounded-full" style="height: 150px;">

                    <p><strong>User Name</strong></p>

                    <div class="mt-6 flex space-x-8 justify-around">
                        <p class="text-xs text-gray-500">0 Connections</p>
                        <p class="text-xs text-gray-500">0 Job Listings</p>
                    </div>
                </div>
                
            </div>
            
        </div>
            
        <div class="main-right col-span-1">
            <YouMayKnow />

            <Industries />
        </div>
    </div>
</template>

<script>
import YouMayKnow from '../components/YouMayKnow.vue';
import Industries from '../components/Industries.vue';

export default {
    name: "SearchView",
    components: {
        YouMayKnow,
        Industries
    }
}
</script>