<template>
    <div class="d-flex align-items-center min-vh-100">
        <div class="container">
            <div class="row justify-content-md-center">
                <div class="col-12 col-sm-12 col-md-6">
                    <div class="col">
                        <img :src="image" class="logo" />
                    </div>
                    <div class="col">
                        <label>Username</label>
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
                        <va-button outline class="mr-4" @click="login">login</va-button>
                    </div>
                    <va-progress-bar :indeterminate="isLoading" :size="loaderSize" />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import image from "../assets/logo.png";
export default {
    name: "loginComp",
    data() {
        return {
            image: image,
            email: "",
            password: "",
            isLoading: false,
            loaderSize: 0,
        };
    },
    props: ["indeterminate"],
    computed: mapGetters(["userTokens"]),
    methods: {
        ...mapActions(["signIn"]),
        async login() {
            this.isLoading = true;
            this.loaderSize = 10;
            const user = {
                username: this.email,
                password: this.password,
            };
            const response = await this.signIn(user);
            localStorage.setItem(
                "AuthenticationResult",
                JSON.stringify(response.data.AuthenticationResult)
            );
            localStorage.setItem(
                "ChallengeParameters",
                JSON.stringify(response.data.ChallengeParameters)
            );
            console.log("response", response);
            this.isLoading = false;
            this.loaderSize = 0;
            if (
                response.data.ChallengeParameters.ChallengeName ==
                "NEW_PASSWORD_REQUIRED"
            ) {
                this.$router.push("/createNewPassword");
            } else if (response.status === 200) {
                this.$router.push("/");
            }
        },
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

.loader div {
    display: block;
}
</style>
