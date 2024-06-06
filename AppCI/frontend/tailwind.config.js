/** @type {import('tailwindcss').Config} */
// import colors from 'daisyui/src/theming/themes';
import colors from 'tailwindcss/colors';
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
      colors: {
        "vtd-primary": colors.sky, // Light mode Datepicker color
        "vtd-secondary": colors.cyan, // Dark mode Datepicker color
      },
    },
  },
  plugins: [
    require("@tailwindcss/typography"), 
    // eslint-disable-next-line @typescript-eslint/no-var-requires
    require("@tailwindcss/forms")({
      strategy: 'class',
    }),
    require("daisyui"),
  ],
}

