<template>
  <v-card display="block" class="mb-4">
    <v-card-title class="body-2"> Money transfer </v-card-title>
    <v-card-text
      ><p v-if="title"> Title: {{ title }}</p>
      <div v-if="isOutgoing">
        To: {{ this.userTo }}
        <div class="float-right">
          <strong class="red--text text--lighten-1">
            -{{ this.amount.toFixed(2) }} {{ this.currency }}</strong
          >
        </div>
      </div>
      <div v-else>
        From: {{ this.userFrom }}
        <div class="float-right">
          <strong class="green--text text--lighten-1">
            {{ this.amount.toFixed(2) }} {{ this.currency}}</strong
          >
        </div>
      </div>
    </v-card-text>

    <v-divider />
  </v-card>
</template>

<script>
export default {
  props: {
    title: {
      type: String
    },

    userId:{
      type:Number
    },
    userTo:{
      type:String
    },
    userFrom:{
      type:String
    },
    userFromId:{
      type:Number
    },
    otherUser: {
      type: String
    },
    amount: {
      type: Number
    },
    currency: {
      type: String
    },
    time: {}
  },
  computed: {
    shortcut: function() {
      return this.getShortcut(this.currency);
    },
    isOutgoing: function(){
      var x=this.userFromId==this.userId
      return x
    }
  },
  methods: {
    getShortcut(currency) {
      console.log(currency);
    }
  }
};
</script>
