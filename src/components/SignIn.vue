<template>
<div id="app">
<v-app id="inspire">
  <v-content>
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md4>
          <v-card class="elevation-12">
            <v-toolbar dark color="primary">
              <v-toolbar-title>로그인</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-tooltip bottom>
                <v-btn
                  icon
                  large
                  :href="source"
                  target="_blank"
                  slot="activator"
                >
                </v-btn>
                <span>Source</span>
              </v-tooltip>
            </v-toolbar>
            <v-card-text>
              <v-form>
                <v-text-field name="login" label="Email" type="text"></v-text-field>
                <v-text-field name="password" label="Password" id="password" type="password"></v-text-field>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn router-link to="/signUp">Sign Up</v-btn>
              <v-btn router-link to="/mainpage" color="primary">Sing In</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</v-app>
</div>
</template>

<script>
</script>

<style>

</style>
