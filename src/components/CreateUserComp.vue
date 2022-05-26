<template>
  <div class="d-flex align-items-center min-vh-100">
    <div class="container">
      <div class="row justify-content-md-center">
        <div class="col-12 col-sm-12 col-md-6">
          <div class="col">
            <img :src="image" class="logo" />
          </div>
          <div class="col">
            <label>First Name</label>
          </div>
          <div class="col">
            <input type="text" v-model="firstName" required @blur="validateName" />
          </div>
          <div class="col">
            <label>Last Name</label>
          </div>
          <div class="col">
            <input type="text" v-model="lastName" required @blur="validateName" />
          </div>
          <div class="col">
            <label>Phone Number</label>
          </div>
          <div class="col">
            <input type="tel" v-model="phoneNumber" required />
          </div>
          <div class="col">
            <label>Email</label>
          </div>
          <div class="col">
            <input type="email" v-model="email" required />
          </div>
          <div class="col">
            <label>Password</label>
          </div>
          <div class="col">
            <input type="password" v-model="password" required />
          </div>
          <div class="col">
            <label>Re Enter Password</label>
          </div>

          <div class="col">
            <input type="password" v-model="rePassword" required />
          </div>

          <div class="col">
            <label>is Admin ?</label>
            <input type="checkbox" v-model="isAdmin" required />
          </div>

          <div class="col">
            <label>your newly generated email:</label>
            <p>{{ username }}</p>
          </div>

          <div class="col">
            <button class="btn btn-outline-light" @click="createUserEvent">Create User</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import image from "../assets/logo.png";

import { mapGetters, mapActions } from "vuex";

export default {
  name: "CreateUser",
  data() {
    return {
      image: image,
      firstName: "",
      lastName: "",
      phoneNumber: "",
      email: "",
      password: "",
      rePassword: "",
      isAdmin: false,
      username: ''
    };
  },
  computed: mapGetters(["userTokens"]),
  methods: {
    ...mapActions(["signUp", "signIn"]),
    async createUserEvent() {
      const user = {
        first_name: this.firstName,
        last_name: this.lastName,
        phone_number: this.phoneNumber,
        username: this.username,
        email: this.email,
        password: this.password,
        is_admin: String(this.isAdmin).toUpperCase()
      };
      try{
        let response = await this.signUp(user);
      console.log("response", response);
      if ("data" in response) 
        if ('User' in response.data) {
          if (response.data.User.UserStatus == "FORCE_CHANGE_PASSWORD") {
            /*
            TODO:
              1. auto sign in
              2. redirect to change password page
            */
            const user = {
              username: this.username,
              password: this.password,
            };
            const signin_response = await this.signIn(user);
            localStorage.setItem("AuthenticationResult", JSON.stringify(response.data.AuthenticationResult));
            localStorage.setItem("ChallengeParameters", JSON.stringify(response.data.ChallengeParameters));
            console.log("signin_response", signin_response);
            this.$router.push("/createNewPassword");
            }
          else console.log(response)
        }
      } catch (error) {
        if ('response' in error)
          if ('data' in error.response) {
            if (error.response.data.errorCode === "UsernameExistsException") alert(error.response.data.errorMessage)
            else if (error.response.data.errorCode === "NotAuthorizedException") alert(error.response.data.errorMessage)
            else if (error.response.data.errorCode === "InvalidPasswordException") alert(error.response.data.errorMessage)
            else if (error.response.data.errorCode === "InvalidParameterException") alert(error.response.data.errorMessage)
            else if (error.response.data.errorCode === "InternalErrorException") alert(error.response.data.errorMessage)
            else alert("Unknown Error")
          }
      }
    },
    validateName() {
      this.firstName = this.firstName.replace(/[^a-zA-Z0-9]/g, '');
      this.lastName = this.lastName.replace(/[^a-zA-Z0-9]/g, '');
      this.username = this.firstName.toLocaleLowerCase() + "." + this.lastName.toLocaleLowerCase() + "@unexpressed.in";
    }
  },
};
</script>

<style scoped>
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
  /* border-radius: 8px; */
  width: 60%;
  margin-bottom: 5px;
  height: 35px;
  background-color: transparent;
  color: #fff;
  text-align: center;
  border: 0px;
  border-bottom: 1px solid white;
  box-shadow: none;
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
