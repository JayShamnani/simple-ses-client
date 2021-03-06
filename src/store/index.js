import axios from 'axios';
import { createStore } from 'vuex'

import url from './url.config';

axios.defaults.baseURL = url;

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
    async signIn({ commit }, { username, password }) {
      const response = await axios.post('/api/sign-in', { username, password });
      commit('setUserTokens', response.data);
      return response;
    },
    async signUp({ commit }, { username, email, password, is_admin, first_name, last_name, phone_number }) {
      const response = await axios.post('/api/create-user', { username, password, email, is_admin, first_name, last_name, phone_number });
      commit('setUserTokens', response.data);
      return response;
    },
    async respondToAuthChallenge({ commit }, { username, new_password, session }) {
      const response = await axios.post('/api/respond-to-auth-challenge', { username, new_password, session });
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
      const response = await axios.post('/api/get-emails', { access_token });
      commit('setUserMails', response.data);
      return response;
    },
  },
  mutations: {
    setUserTokens: (state, userTokens) => (state.userTokens = userTokens),
    setUserMails: (state, userMails) => (state.userMails = userMails),
  },
  modules: {
  }
})
