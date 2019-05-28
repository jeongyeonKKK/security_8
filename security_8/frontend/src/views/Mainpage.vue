<template>
 <div class="container">
    <div class="card login">
      <div class="card-body">
        <h2 class="card-title text-center">Security_chat</h2>
        <form @submit.prevent="ChatList" class="text-center">
          <div class="headline">security chat_1
          </div>
          <router-link to="/Chat" class="btn btn-primary">Enter Chat</router-link>
          //
          <p></p>
          <div class="headline">security chat_2
          </div>
          <router-link to="/Chat2" class="btn btn-primary">Enter Chat</router-link>
          <p></p>
          <div class="headline">security chat_3
          </div>
          <router-link to="/Chat3" class="btn btn-primary">Enter Chat</router-link>
          <p></p>
        </form>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  name: 'default',
  data () {
    return {
    }
  },
  methods: {

  }
}
</script>


<style scoped>
</style>
