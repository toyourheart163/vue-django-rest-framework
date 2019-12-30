<template>
  <div class="dashboard-container">
    <github-corner style="position: absolute; top: 0px; border: 0; right: 0;" />
    <div class="dashboard-text">name: {{ name }}</div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import GithubCorner from '@/components/GithubCorner/index'

export default {
  name: 'Dashboard',
  components: { GithubCorner },
  computed: {
    ...mapGetters([
      'name'
    ])
  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
</style>
