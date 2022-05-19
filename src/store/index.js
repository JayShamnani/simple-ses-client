import axios from 'axios';
import { createStore } from 'vuex'

export default createStore({
  state: {
    userTokens: {},
    userMails: {},
    userProfile: {},
  },
  getters: {
    userTokens: state => state.userTokens,
    userMails: state => state.userMails,
    userProfile: state => state.userProfile,
  },
  actions: {
    async signIn({ commit }, { email, password }) {
      const response = await axios.post('/api/sign-in', { email, password });
      commit('setUserTokens', response.data);
    },
    async signUp({ commit }, { email, password, is_admin }) {
      const response = await axios.post('/api/create-user', { email, password, is_admin });
      commit('setUserTokens', response.data);
    },
    async respondToAuthChallenge({ commit }, { access_token, email, challenge_name, challenge_response }) {
      const response = await axios.post('/api/respond-to-auth-challenge', { access_token, email, challenge_name, challenge_response });
      commit('setUserTokens', response.data);
    },
    async changePassword({ commit }, { access_token, old_password, new_password }) {
      const response = await axios.post('/api/change-password', { access_token, old_password, new_password });
      commit('setUserTokens', response.data);
    },
    async getUserProfile({ commit }, { access_token }) {
      const response = await axios.post('/api/get-user-profile', { access_token });
      commit('setUserProfile', response.data);
    },
    async getEmails({ commit }, { access_token }) {
      const response = await axios.post('/api/get-emails', { headers: { access_token } });
      commit('setUserMails', response.data);
    },
  },
  mutations: {
    setUserTokens: (state, userTokens) => (state.userTokens = userTokens),
    setUserMails: (state, userMails) => (state.userMails = userMails),
  },
  modules: {
  }
})
