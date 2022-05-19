<template>
  <div>
    <div class="container-fluid">
      <div class="row">
        <div class="col-sm p-3 min-vh-100">
          <!-- content -->
          <table class="table">
            <thead>
                <tr>
                </tr>
            </thead>
            <tbody>
                <tr :key="item.timestamp" v-for="item in emails">
                  <td scope="row" v-html="item.from.M.html.S"></td>
                  <td scope="row">{{ item.subject.S }}</td>
                  <th scope="row">{{ item.timestamp.N }}</th>
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
    };
  },
  computed: mapGetters(["userTokens"]),
  methods: {
    ...mapActions(["getEmails"]),
  },
  async created() {
    localStorage.getItem("AuthenticationResult");
    let access_token = localStorage.getItem("AuthenticationResult");
    if (access_token) {
      access_token = JSON.parse(access_token).AccessToken;
      try {
        let response = await this.getEmails({ access_token });
        if (response.status === 200) {
          this.emails = response.data.Items;
        }
      } catch (e) {
        /*
        TODO:
        - Refreshing the access token
        */
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
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.1/font/bootstrap-icons.css");
.icon {
  width: 20px;
}
</style>
