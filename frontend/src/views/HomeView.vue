<template>
  <main class="pt-14">
    <div class="p-4 bg-white border border-gray-200 rounded-lg">
      <div class="max-w-[85rem] mx-auto px-4 sm:px-6 lg:px-8">
        <!-- Grid -->
        <div class="grid md:grid-cols-2 gap-4 md:gap-8 xl:gap-20 md:items-center">
          <div>
            <h1 class="block text-3xl font-bold text-gray-800 sm:text-4xl lg:text-6xl lg:leading-tight">Start your journey with <span class="text-blue-600">CareerVue</span></h1>
            <p class="mt-3 text-lg text-gray-800">CareerVue is a platform for job seekers and employers to connect. Sail the seas of employment.</p>

            <!-- Buttons -->
            <div class="mt-7 grid gap-3 w-full sm:inline-flex">
              <a class="py-3 px-4 inline-flex justify-center items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50 disabled:pointer-events-none" href="/signup">
                Sign Up
                <svg class="flex-shrink-0 size-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
              </a>
              <a class="py-3 px-4 inline-flex justify-center items-center gap-x-2 text-sm font-medium rounded-lg border border-gray-200 bg-white text-gray-800 shadow-sm hover:bg-gray-50 disabled:opacity-50 disabled:pointer-events-none" href="/about">
                About Us
              </a>
            </div>
            <!-- End Buttons -->

            <!-- Review -->
            <div class="mt-6 lg:mt-10 grid grid-cols-2 gap-x-5">
              <!-- Review -->
              <div class="py-5 col-span-2">
                <p class="mt-3 text-sm text-gray-800">
                  "CareerVue is the future of employement. Nothing better can be found elsewhere."
                </p>

                <div class="mt-5">
                  <h3 class="text-sm font-semibold text-gray-800">- Tejas Aiyar: CEO, Founder, Majority Shareholder and Chairman of the Board of Directors</h3>
                </div>
              </div>
              <!-- End Review -->
            </div>
          </div>

          <div class="relative ms-4">
            <img class="w-full rounded-md" src="https://images.pexels.com/photos/2102416/pexels-photo-2102416.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" alt="Image Description">
            <div class="absolute inset-0 -z-[1] bg-gradient-to-tr from-gray-200 via-white/0 to-white/0 size-full rounded-md mt-4 -mb-4 me-4 -ms-4 lg:mt-6 lg:-mb-6 lg:me-6 lg:-ms-6"></div>

            <!-- SVG-->
            <div class="absolute bottom-0 start-0">
              <svg class="w-2/3 ms-auto h-auto text-white" width="630" height="451" viewBox="0 0 630 451" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="531" y="352" width="99" height="99" fill="currentColor"/>
                <rect x="140" y="352" width="106" height="99" fill="currentColor"/>
                <rect x="482" y="402" width="64" height="49" fill="currentColor"/>
                <rect x="433" y="402" width="63" height="49" fill="currentColor"/>
                <rect x="384" y="352" width="49" height="50" fill="currentColor"/>
                <rect x="531" y="328" width="50" height="50" fill="currentColor"/>
                <rect x="99" y="303" width="49" height="58" fill="currentColor"/>
                <rect x="99" y="352" width="49" height="50" fill="currentColor"/>
                <rect x="99" y="392" width="49" height="59" fill="currentColor"/>
                <rect x="44" y="402" width="66" height="49" fill="currentColor"/>
                <rect x="234" y="402" width="62" height="49" fill="currentColor"/>
                <rect x="334" y="303" width="50" height="49" fill="currentColor"/>
                <rect x="581" width="49" height="49" fill="currentColor"/>
                <rect x="581" width="49" height="64" fill="currentColor"/>
                <rect x="482" y="123" width="49" height="49" fill="currentColor"/>
                <rect x="507" y="124" width="49" height="24" fill="currentColor"/>
                <rect x="531" y="49" width="99" height="99" fill="currentColor"/>
              </svg>
            </div>
            <!-- End SVG-->
          </div>
          <!-- End Col -->
        </div>
        <!-- End Grid -->
      </div>
      <!-- End Hero -->
    </div>
  </main>
</template>
