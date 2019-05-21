<template>
<div id="app">
<v-app id="inspire">
  <v-content>
    <v-container fluid grid-list-md>
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md4>
        <Toolbar></Toolbar>
        <v-toolbar color="primary" id="toolbar">
              <v-btn @click="$router.go(-1)" icon>
                <v-icon>arrow_back</v-icon>
              </v-btn>
              <v-spacer></v-spacer>
              <v-toolbar-title><v-btn flat href="/mainpage">Security_chat</v-btn></v-toolbar-title>
              <v-spacer></v-spacer>
              <v-icon>person</v-icon>
        </v-toolbar>
          <v-btn outline color="indigo" block="true" router-link to="/newChat">new chat</v-btn>

          <div id="app">
            <v-app id="inspire">
              <v-layout row warp>
                <v-flex xs12>
                  <v-card>
                    <v-card-title primary-title>
                      <div>
                        <div class="headline">security chat_1</div>
                        <v-spacer></v-spacer>
                        <span class="grey--text">1 person</span>
                      </div>
                    </v-card-title>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn flat color="blue"><v-icon>input</v-icon></v-btn>
                  </v-card-actions>
                </v-card>

                <v-card>
                  <v-card-title primary-title>
                    <div>
                      <div class="headline">security chat_2</div>
                      <v-spacer></v-spacer>
                      <span class="grey--text">1 person</span>
                    </div>
                  </v-card-title>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn flat color="blue"><v-icon>input</v-icon></v-btn>
                </v-card-actions>
              </v-card>

              <v-card>
                <v-card-title primary-title>
                  <div>
                    <div class="headline">security chat_3</div>
                    <v-spacer></v-spacer>
                    <span class="grey--text">1 person</span>
                  </div>
                </v-card-title>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn flat color="blue"><v-icon>input</v-icon></v-btn>
              </v-card-actions>
            </v-card>

              </v-flex>
            </v-layout>
          </v-app>
        </div>



        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</v-app>
</div>
</template>


<script>
export default {
  name: 'default',
  data () {
    return {
    }
  },
  methods: {}
}
</script>


<style scoped>
</style>
