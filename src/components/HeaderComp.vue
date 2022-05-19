<template>
  <header class="mb-1 border-bottom">
    <div class="container">
      <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
        <a href="/" class="d-flex align-items-center mb-2 mb-lg-0 text-dark text-decoration-none">
          <img :src="logo" class="logo">
        </a>

        <ul class="nav col-lg-auto me-lg-auto justify-content-center mb-md-0">

        </ul>

        <div class="dropdown text-end">
          <a href="#" class="d-block link-dark text-decoration-none dropdown-toggle" id="dropdownUser1" data-bs-toggle="dropdown" aria-expanded="false">
            <img src="https://github.com/mdo.png" alt="mdo" width="32" height="32" class="rounded-circle">
          </a>
          <ul class="dropdown-menu text-small" aria-labelledby="dropdownUser1">
            <li><a class="dropdown-item" href="#">Profile</a></li>
            <li><a class="dropdown-item" href="#">Settings</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Sign out</a></li>
          </ul>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
import logo from "../assets/logo.png"
export default {
    data() {
        return {
            logo: logo,
        }
    }

}
</script>

<style scoped>
.logo {
    width: 150px;
}
.dropdown {
  margin-left: 10px;
}

header {
  background-color: #111;
  box-shadow: 0 1px 2px rgba(0,0,0,.1);
  z-index: 1;
}
</style>