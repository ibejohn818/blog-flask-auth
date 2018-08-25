<template>
  <div id='home'>
    <div class="row">
      <div class="col-md-12">
        <h1>Flask Auth Demo</h1>
        <hr>
      </div>
    </div>
    <div class="row">
      <div class="col-md-6">
        <login-form

        />
      <br />

        <div class="card links">
          <div class="card-header">Test Links</div>
          <div class="card-body">
              <link-test
                v-for='(v, k) in links'
                :key='"l-"+k'
                :text='v.text'
                :uri='v.uri'
              />
          </div>
        </div>


      </div>
      <div class="col-md-6">
        <results />
      </div>
    </div>
  </div>
</template>

<script>
import LoginForm from '@/components/LoginForm'
import Results from '@/components/Results'
import LinkTest from '@/components/LinkTest'

export default {
  name: 'Home',
  components: {
    LoginForm,
    Results,
    LinkTest
  },
  data () {
    return {
      links: [
        {
          text: 'Check login, no groups',
          uri: '/api/check-login'
        },
        {
          text: 'Check for group Member',
          uri: '/api/check-member'
        },
        {
          text: 'Check for groups Manager or Subscriber',
          uri: '/api/check-multiple'
        },
      ]
    }
  },
  props: {

  },
  computed: {
  },
  watch: {

  },
  mounted () {

  },
  methods: {

  }
}
</script>

<style lang='sass' >
</style>
