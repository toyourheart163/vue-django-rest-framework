<template>
  <div class="button-counter">
    <alert-box />
    <alert-box />
    <alert-box />
  </div>
</template>

<script>
import alertBox from './alert-box'

export default {
  name: 'Test',
  components: { alertBox }
}
</script>
