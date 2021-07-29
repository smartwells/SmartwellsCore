<template>

  <div>

    <p>Hello World</p>

  </div>

</template>

<script>
  import axios from 'axios'
  export default{
    name: 'CompanyData',
    data(){
      return {
      	directory: []
      }
    },
    async mounted () {
    	try {
    		var result = await axios({
    			method: 'POST',
    			url: 'http://78.25.88.10:6515/graphql/',
                        //url: 'http://78.25.88.10:8000/graphql/',
    			data: {
    				query: `
    				{
					  allTitles {
					    edges {
					      node {
					        id
					        titleName
					      }
					    }
					  }
					}
    				`
    			}
    		})
    		this.directory = result.data.data.allTitles
    	} catch (error) {
    		console.error(error)
    	}
    }
  }
</script>

<style scoped>
</style>
