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
            <input type="text" required />
          </div>
          <div class="col">
            <label>Last Name</label>
          </div>
          <div class="col">
            <input type="text" required />
          </div>
          <div class="col">
            <label>Phone Number</label>
          </div>
          <div class="col">
            <input type="tel" required />
          </div>
          <div class="col">
            <label>Email</label>
          </div>
          <div class="col">
            <input type="email" required />
          </div>
          <div class="col">
            <label>Password</label>
          </div>
          <div class="col">
            <input type="password" required />
          </div>
          <div class="col">
            <label>Re Enter Password</label>
          </div>

          <div class="col">
            <input type="password" required />
          </div>
          <div class="col">
            <button class="btn btn-outline-light">Create User</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import image from "../assets/logo.png";
export default {
  name: "CreateUser",
  data() {
    return {
      image: image,
    };
  },
};
</script>

<style  scoped>
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