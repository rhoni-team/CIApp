/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      backgroundImage: {
        // "texture-pattern": "url('@/assets/img/texture.svg')",
      },
    },
  },
  plugins: [
    require("@tailwindcss/typography"), 
    require("daisyui")
  ],
}

