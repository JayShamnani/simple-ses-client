<template>
  <div class="d-flex align-items-center min-vh-100">
    <div class="container">
      <div class="row justify-content-md-center">
        <div class="col-12 col-sm-12 col-md-6">
          <div class="col">
            <img :src="image" class="logo" />
          </div>
          <div class="col">
              <h3>Welcome to Unexpressed Mailing System!!!</h3>
          </div>
          <hr>
          <div class="col">
            <label>New Password</label>
          </div>
          <div class="col">
            <input type="password" v-model="newPassword" required />
          </div>
          <div class="col">
            <label>New Password (Confirm)</label>
          </div>
          <div class="col">
            <input type="password" v-model="newPasswordConfirm" required />
          </div>
          <div class="col">
            <button class="btn btn-outline-light" @click="save">Save Password</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import image from "../assets/logo.png";

export default {
  data() {
    return {
      image: image,
      newPassword: "",
      newPasswordConfirm: "",
    };
  },
    computed: mapGetters(["userTokens"]),
  methods: {
    ...mapActions(["respondToAuthChallenge"]),
    async save() {
      const user = {
        username: this.email,
        new_password: this.password,
        session: ''
      };
      const response = await this.respondToAuthChallenge(user);
      localStorage.setItem("AuthenticationResult", JSON.stringify(response.data.AuthenticationResult));
      localStorage.setItem("ChallengeParameters", JSON.stringify(response.data.ChallengeParameters));
      console.log("response", response);
      if (response.status === 200) {
        this.$router.push("/");
      }
    },
  },
};
</script>

<style>
.logo {
  max-width: 200px;
}

.container {
  color: #fff;
  padding: 0px 20px;
}

.col-12 {
  border-radius: 8px;
  padding: 20px 0px;
  background-color: #222;
  box-shadow: 3px 5px 20px #181818;
}

.col input {
  border-radius: 4px;
  width: 60%;
  margin-bottom: 5px;
}
.col label {
  width: 100%;
  margin-bottom: 5px;
  font-size: 1.2rem;
}
.col button {
  margin: 20px 0px;
}
</style>
