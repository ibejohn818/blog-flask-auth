<template>
  <div class='link'>
    <a class="btn btn-primary" :href="uri" @click='handleLink'>{{this.text}}</a>
  </div>
</template>

<script>
export default {
  name: 'LinkTest',
  data () {
    return {

    }
  },
  props: {
    text: '',
    uri: ''
  },
  computed: {

  },
  watch: {

  },
  mounted () {

  },
  methods: {
    handleLink (e) {
      e.preventDefault()
      this.$store.dispatch('testUrl', {url: $(e.target).attr('href')})
    }
  }
}
</script>

<style lang='sass' scoped>

</style>
