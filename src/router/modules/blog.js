/** When your routing table is too long, you can split it into small modules **/

// import Layout from '@/layout'

const blogRouter = {
  path: '/blogs',
  component: () => import('@/views/blog/index'),
  meta: {
    title: 'BlogList',
    icon: 'example'
  },
  children: [
    {
      path: '',
      component: () => import('@/views/blog/blogs'),
      name: 'Blogs',
      meta: {
        title: 'Blogs'
      }
    },
    {
      path: 'create',
      component: () => import('@/views/blog/create-blog'),
      name: 'CreateBlog',
      meta: {
        title: 'Create Blog'
      },
      hidden: true
    },
    {
      path: ':id(\\d+)',
      component: () => import('@/views/blog/blog-detail'),
      name: 'BlogDetail',
      meta: {
        title: 'BlogDetail'
      },
      hidden: true
    },
    {
      path: 'tags/:tag(\\w*)',
      component: () => import('@/views/blog/timeline'),
      name: 'Timeline',
      meta: {
        title: 'Timeline'
      },
      hidden: true
    }
  ]
}
export default blogRouter
