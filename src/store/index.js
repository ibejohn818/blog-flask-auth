import Vue from 'vue'
import Vuex from 'vuex'
import Promise from 'promise'

Vue.use(Vuex)

const state = () => {
  return {
    results: [],
    session: null
  }
}
const actions = {
  login (c, d) {
    return new Promise((resolve, reject) => {
      $.ajax({
        type: 'post',
        headers: {
          'accept': 'application/json'
        },
        contentType: 'application/json',
        url: '/api/login',
        success: function (res, status, xhr) {
          resolve(xhr)
        },
        error: function (xhr) {
          resolve(xhr)
        },
        data: JSON.stringify(d)
      })
    })
  },
  logout (ctx, d) {
    return new Promise((resolve, reject) => {
      $.ajax({
        type: 'post',
        headers: {
          'accept': 'application/json'
        },
        contentType: 'application/json',
        url: '/api/logout',
        success: function (res, status, xhr) {
          ctx.commit('addResult', xhr)
          resolve(xhr)
        },
        error: function (xhr) {
          ctx.commit('addResult', xhr)
          resolve(xhr)
        }
      })
    })
  },
  checkSession (ctx, data) {
    return new Promise((resolve, reject) => {
      $.ajax({
        type: 'get',
        headers: {
          'accept': 'application/json'
        },
        contentType: 'application/json',
        dataType: 'json',
        url: '/api/session',
        success: function (res, status, xhr) {
          ctx.commit('setSession', res['result'])
          resolve(xhr)
        },
        error: function (xhr) {
          ctx.commit('setSession', false)
          resolve(xhr)
        },
      })
    })
  },
  testUrl (ctx, d) {
    return new Promise((resolve, reject) => {
      $.ajax({
        type: 'get',
        headers: {
          'accept': 'application/json'
        },
        contentType: 'application/json',
        dataType: 'json',
        url: d.url,
        success: function (res, status, xhr) {
          ctx.commit('addResult', xhr)
          resolve(xhr)
        },
        error: function (xhr) {
          ctx.commit('addResult', xhr)
          resolve(xhr)
        },
      })
    })
  }
}
const mutations = {
  setSession (state, val) {
    state.session = val
  },
  addResult (state, xhr) {
    var data = {
      'status': xhr.status,
      'statusText': xhr.statusText,
      'response': xhr.responseText
    }
    state.results.unshift(data)
  }
}
const getters = {
  getSession (state) {
    return state.session
  },
  getResults (state) {
    return state.results
  }
}
export default new Vuex.Store({
  strict: true,
  state,
  mutations,
  actions,
  getters
})
