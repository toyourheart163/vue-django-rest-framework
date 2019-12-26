/** When your routing table is too long, you can split it into small modules **/

import Layout from '@/layout'

const demoRouter = {
  path: '/demos',
  component: Layout,
  redirect: 'demos/bar-list',
  meta: {
    title: 'Demos',
    icon: 'example'
  },
  children: [
    {
      path: 'bar-list',
      component: () => import('@/views/demo/bar-list'),
      name: 'Demos',
      meta: {
        title: 'Demos'
      }
    },
    {
      path: 'form',
      component: () => import('@/views/demo/demo-form'),
      name: 'DemoForm',
      meta: {
        title: 'DemoForm'
      }
    }
  ]
}

export default demoRouter
