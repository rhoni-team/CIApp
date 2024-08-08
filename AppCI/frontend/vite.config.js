/// <reference types="vitest" />
import { fileURLToPath, URL } from "node:url";
import path from "node:path";
import { defineConfig, loadEnv } from "vite";
import vue from "@vitejs/plugin-vue";
import vueJsx from "@vitejs/plugin-vue-jsx";


// https://vitejs.dev/config/
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '');
  console.log("NODE_ENV", env.NODE_ENV);

  const isProduction = mode === "production";
  console.log("Is production:", isProduction);

  return {
    plugins: [vue(), vueJsx()],
    test: {
      include: ["**/__tests__/**"],
      exclude: ["**/node_modules/**", "**/dist/**"],
      environment: "jsdom",
    },
    resolve: {
      alias: {
        "@": fileURLToPath(new URL("./src", import.meta.url)),
      },
    },
    root: path.resolve("./src"),
    base: isProduction ? "" : "/static/",
    build: {
      outDir: path.resolve("./static/dist"),
      assetsDir: "",
      manifest: true,
      emptyOutDir: true,
      target: "es2015",
      rollupOptions: {
        input: {
          main: path.resolve("./src/main.ts"),
        },
        output: {
          chunkFileNames: undefined,
        },
      },
    },
    server: {
      origin: "http://localhost:3000",
      host: "localhost",
      port: 3000,
      open: false,
      watch: {
        usePolling: true,
        disableGlobbing: false,
      },
    },
  }
});
