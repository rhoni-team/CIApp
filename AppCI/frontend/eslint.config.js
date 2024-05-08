import globals from "globals";
import pluginJs from "@eslint/js";
import pluginVue from "eslint-plugin-vue";

export default [
  pluginJs.configs.recommended,
  ...pluginVue.configs["flat/recommended"],
  {
    languageOptions: { 
      globals: { 
        ...globals.browser, 
        ...globals.node 
      } 
    },
  },
  {
    ignores: ["**/node_modules/**", "**/dist/**"], 
  },
];
