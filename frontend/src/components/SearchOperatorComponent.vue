<template>
  <div class="app">
    <div v-if="modoBusca" class="caixa-busca">
      <input v-model="query" type="text" placeholder="Digite a razão social..." />
      <button :disabled="!query.trim()" @click="buscarOperadoras">Buscar</button>
    </div>

    <div v-else class="caixa-resultados">
      <h2>Resultados da busca por: <span class="termo">{{ query }}</span></h2>
      <ul>
        <li v-for="item in resultados" :key="item.Registro_ANS">
          <strong>{{ item.Razao_Social }}</strong><br />
          Registro ANS: {{ item.Registro_ANS }}<br />
          Localização: {{ item.Cidade }} - {{ item.UF }}
        </li>
      </ul>
      <button @click="voltar">Nova Busca</button>
    </div>
  </div>
</template>


<script setup>
import { ref } from 'vue'

const query = ref('')
const resultados = ref([])
const modoBusca = ref(true)

const buscarOperadoras = async () => {
  try {
    const res = await fetch(`http://localhost:8000/operadora/buscar?q=${encodeURIComponent(query.value)}`)
    const data = await res.json()
    resultados.value = data
    modoBusca.value = false
  } catch (error) {
    console.error('Erro na busca:', error)
  }
}

const voltar = () => {
  resultados.value = []
  query.value = ''
  modoBusca.value = true
}
</script>

<style scoped>


.caixa-busca, .caixa-resultados {
  display: flex;
  flex-direction: column;
  width: 50vw;
  justify-content: center;

}

.caixa-resultados {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}


input {
  padding: 0.8rem;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 1rem;
  margin-bottom: 1rem;
  border: 1px solid rgb(158, 151, 184);
}

input:focus {
  border: 1px solid #6a4fbf;
  outline: none;
}

button {
  padding: 0.8rem;
  font-size: 1rem;
  background: #6a4fbf;
  color: white;
  border: none;
  border-radius: 1rem;
  cursor: pointer;
  transition: background 0.2s ease;
  margin-bottom: 2rem;
}

button:disabled {
  background: #bbb;
  cursor: not-allowed;
}

button:hover:enabled {
  background: #5539a2;
}

ul {
  list-style: none;
  padding: 0;
  margin-top: 1rem;
}

li {
  background: #f9f9f9;
  border-radius: 0.5rem;
  padding: 1rem;
  margin-bottom: 1rem;
  line-height: 1.5;
}

.termo {
  color: #6a4fbf;
}
</style>