<template>
  <div id='login'>
    <div class="card">
      <div class="card-header">
        Mock Login
      </div>
      <div class="card-body">

        <div
          v-if='getSession == false'
          class="alert alert-danger">
          No login session
        </div>

        <div
          v-if='getSession != false && getSession != null'
          class="alert alert-success">
          <p><strong>Username:</strong> {{getSession.username}}
          <strong>Groups:</strong> {{getSession.groups}}</p>
        </div>


        <form v-on:submit.prevent="handleSubmit" accept-charset="utf-8">
          <div class="form-group">
            <label for="">Username</label>
            <input class="form-control" type="text" v-model='username'>
          </div>
          <div class="form-group">
            <label for="">Groups <small><i>(comma-separate multiple groups)</i></small></label>
            <input class="form-control" type="text" v-model='groups'>
          </div>
          <div class="form-actions clearfix">
            <div class="float-right">
              <button
                :disabled='disableLogin'
                class="btn btn-success" type='submit'>
                Login
              </button>
              <button
                @click='handleLogout'
                class="btn btn-danger" type='button'>
                Logout
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  name: 'LoginForm',
  data () {
    return {
      username: '',
      groups: '',
      sessionInterval: false
    }
  },
  props: {

  },
  computed: {
    ...mapGetters([
      'getSession'
    ]),
    disableLogin () {
      var res = true
      if (this.username.length >0 && this.groups.length >0) {
        res = false
      }
      return res
    }
  },
  watch: {

  },
  created () {
    this.$store.dispatch('checkSession')
    this.sessionInterval = setInterval(() => {
      this.$store.dispatch('checkSession')
    }, 3000)
  },
  mounted () {

  },
  methods: {
    handleLogout () {
      this.$store.dispatch('logout').then(
        (res) => {
          this.$store.dispatch('checkSession')
        }
      )
    },
    handleSubmit () {
      var groups = this.groups.split(',')
      for (var a in groups) {
        groups[a] = groups[a].trim()
      }
      this.$store.dispatch('login', {username: this.username, groups: groups}).then(
        (res) => {
          this.$store.dispatch('checkSession')
        }
      )
      this.username = ''
      this.groups = ''
    }
  }
}
</script>

<style lang='sass' scoped>

</style>
