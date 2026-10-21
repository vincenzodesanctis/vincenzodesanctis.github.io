---
title: "Request my cv"
type: page
show_date: false
reading_time: false
share: false
commentable: false
---

<div id="cv-form" class="w-full max-w-5xl mx-auto mt-0 not-prose">
  <div class="bg-white dark:bg-gray-800 rounded-2xl shadow-xl border border-gray-100 dark:border-gray-700 p-8 md:p-12 text-left">
    <div class="mb-8">
      <p class="text-gray-600 dark:text-gray-300 text-lg leading-relaxed">To protect my privacy, my full CV is available upon request. Please fill out the form below and I will send it to you shortly.</p>
    </div>
    <form action="https://formspree.io/f/mwlvglww" method="POST" class="space-y-5">
      <input type="hidden" name="_language" value="en">
      <input type="hidden" name="_next" value="http://localhost:1313/thank-you/">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
        <div>
          <label for="name" class="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-1">Your Name</label>
          <input type="text" name="name" id="name" required class="w-full rounded-lg border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white shadow-sm focus:border-primary-500 focus:ring-primary-500 px-4 py-3 transition-colors" placeholder="John Doe">
        </div>
        <div>
          <label for="company" class="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-1">Company / Organization</label>
          <input type="text" name="company" id="company" class="w-full rounded-lg border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white shadow-sm focus:border-primary-500 focus:ring-primary-500 px-4 py-3 transition-colors" placeholder="Acme Corp">
        </div>
      </div>
      <div>
        <label for="email" class="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-1">Your Email</label>
        <input type="email" name="email" id="email" required class="w-full rounded-lg border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white shadow-sm focus:border-primary-500 focus:ring-primary-500 px-4 py-3 transition-colors" placeholder="john@company.com">
      </div>
      <div>
        <label for="message" class="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-1">Message (Optional)</label>
        <textarea name="message" id="message" rows="3" class="w-full rounded-lg border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white shadow-sm focus:border-primary-500 focus:ring-primary-500 px-4 py-3 transition-colors" placeholder="Reason for your request..."></textarea>
      </div>
      <div class="pt-2">
        <button type="submit" class="w-full flex justify-center py-3 px-6 border border-transparent rounded-lg shadow-lg text-base font-medium text-white bg-gradient-to-r from-primary-600 to-secondary-500 hover:scale-[1.02] transition-transform duration-200">Request CV</button>
      </div>
    </form>
  </div>
</div>
