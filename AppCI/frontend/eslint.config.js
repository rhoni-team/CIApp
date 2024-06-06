import globals from "globals";
import pluginJs from "@eslint/js";
import pluginVue from "eslint-plugin-vue";
import eslint from '@eslint/js';
import tseslint from 'typescript-eslint';

// export default [
//   pluginJs.configs.recommended,
//   ...pluginVue.configs["flat/recommended"],
//   {
//     ignores: ["**/static/"],
//   },
//   { 
//     languageOptions: { 
//       globals: { 
//         ...globals.browser, 
//         ...globals.node 
//       } 
//     } 
//   },
// ];

export default tseslint.config(
  eslint.configs.recommended,
  ...tseslint.configs.recommended,
  ...pluginVue.configs["flat/recommended"],
  pluginJs.configs.recommended,
  {
    ignores: ["**/static/"],
  },
  { 
    languageOptions: { 
      globals: { 
        ...globals.browser, 
        ...globals.node 
      } 
    } 
  },
  {
    plugins: {
      'typescript-eslint': tseslint.plugin,
    },
    languageOptions: {
      parserOptions: {
        parser: tseslint.parser,
        // project: './tsconfig.app.json',
        extraFileExtensions: ['.vue'],
        sourceType: 'module',
      },
    },
  }
);