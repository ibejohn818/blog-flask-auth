<template>
  <div id='results'>
    <h4>Results</h4>
      <result
        v-if='getResults.length > 0'
        v-for='(v, k) in getResults'
        :key='k'
        :result='v'
      />
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
import Result from '@/components/Result'

export default {
  name: 'Results',
  components: {
    Result
  },
  data () {
    return {

    }
  },
  props: {

  },
  computed: {
    ...mapGetters([
      'getResults'
    ])
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
