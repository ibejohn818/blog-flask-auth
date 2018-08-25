<template>
  <div class='result'>
    <div :class="getClass">
      <p><strong> Status Code: </strong> {{ result.status }} <strong>Status: </strong> {{ result.statusText }}</p>
      <hr>
      <p>{{ result.response }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Result',
  data () {
    return {

    }
  },
  props: {
    result: {
      default () { return {} }
    }
  },
  computed: {
    getClass () {
      var c = ['alert']
      if (this.result.status == 200) {
        c.push('alert-success')
      } else {
        c.push('alert-danger')
      }
      return c.join(' ')
    }
  },
  watch: {

  },
  mounted () {

  },
  methods: {

  }
}
</script>

<style lang='sass' scoped>

</style>
