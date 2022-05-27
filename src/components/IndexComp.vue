<template>
    <div>
        <div class="container-fluid">
            <div class="row">
                <div class="col-sm p-3 min-vh-100">
                    <va-progress-bar :indeterminate="isLoading" :size="loaderSize" />
                    <!-- content -->
                    <table class="table">
                        <thead>
                            <tr>
                            </tr>
                        </thead>
                        <tbody>
                            <tr :key="item.timestamp" v-for="item in emails">
                                <td scope="row">{{ item.from.value[0].address }}</td>
                                <td scope="row">{{ item.subject }}</td>
                                <th scope="row">{{ item.timestamp }}</th>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import image from "../assets/logo.png";
export default {
    name: "IndexComp",
    data() {
        return {
            image: image,
            emails: [],
            isLoading: false,
            loaderSize: 0,
        };
    },
    computed: mapGetters(["userTokens"]),
    methods: {
        ...mapActions(["getEmails"]),
    },
    async created() {
        this.isLoading = true;
        this.loaderSize = 10;
        localStorage.getItem("AuthenticationResult");
        let access_token = localStorage.getItem("AuthenticationResult");
        if (access_token) {
            access_token = JSON.parse(access_token).AccessToken;
            try {
                this.isFetching = true;
                let response = await this.getEmails({ access_token });
                this.isLoading = false;
                this.loaderSize = 0;
                if (response.status === 200) {
                    this.emails = response.data;
                }
            } catch (e) {
                /*
                TODO:
                - Refreshing the access token
                */
                this.isLoading = false;
                this.loaderSize = 0;
                console.log("error", e.response.status);
                if (e.response.status === 403) {
                    this.$router.push("/login");
                }
            }
        }
    },
};
</script>

<style scoped>
/* @import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.1/font/bootstrap-icons.css"); */
.icon {
    width: 20px;
}
</style>
