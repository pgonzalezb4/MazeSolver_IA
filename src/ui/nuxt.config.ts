import { defineNuxtConfig } from "nuxt";

// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
  srcDir: "src",
  runtimeConfig: {
    public: {
      apiUrl: process.env.API_URL ?? "http://localhost:8000",
    },
  },
  css: ["@/assets/styles/global.css"],
});
