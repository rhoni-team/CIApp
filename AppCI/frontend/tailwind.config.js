/** @type {import('tailwindcss').Config} */
// import colors from 'tailwindcss/colors';
// const colors = require("tailwindcss/colors");

export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    "./node_modules/vue-tailwind-datepicker/**/*.js",
  ],
  theme: {
    extend: {
      backgroundImage: {
        // "texture-pattern": "url('@/assets/img/texture.svg')",
      },
      // colors: {
      //   "vtd-primary": colors.sky, // Light mode Datepicker color
      //   "vtd-secondary": colors.gray, // Dark mode Datepicker color
      // },
    },
  },
  plugins: [
    require("@tailwindcss/typography"), 
    require("@tailwindcss/forms"),
    require("daisyui"),
  ],
}

