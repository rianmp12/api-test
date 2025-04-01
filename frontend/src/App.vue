<template>
  <header>
    <div class="header-container">
      <img class="logo" src="./assets/intuitive-care_logo.png" alt="Intuitive Care Logo" />
    </div>
  </header>

  <main class="app">
    <SearchOperatorComponent />
  </main>
</template>

<script setup>
import SearchOperatorComponent from './components/SearchOperatorComponent.vue'
</script>

<style>
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  padding: 0;
  font-family: 'Roboto', sans-serif;
}

header {
  display: flex;
  justify-content: center;
  width: 100%;
  margin-top: 15rem;
}

.header-container {
  display: flex;
  width: 59rem;
  justify-content: center;
}

.logo {
  width: 14rem;
}

.app {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 59rem;
  margin: 0 auto;
  padding-top: 1rem;
}
</style>