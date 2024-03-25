<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4 pt-14">
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <h1 class="mb-6 text-2xl">Login</h1>

                <p class="mb-6 text-gray-500">
                    CareerVue is a platform for job seekers and employers to connect. 
                    Sail the seas of employment. 
                    Login to discover your opportunity today!
                </p>

                <p class="font-bold">
                    Don't have an account? <RouterLink :to="{'name': 'signup'}" class="underline">Click here</RouterLink> to Sign Up instead!
                </p>
            </div>
        </div>
        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6">
                    <div>
                        <label>Email</label><br>
                        <input type="email" placeholder="Your Email Address" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>Password</label><br>
                        <input type="password" placeholder="Your Password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <button class="py-4 px-6 bg-blue-500 text-white rounded-lg">Login</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>