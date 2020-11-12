<template>
  <div>
    <SmallCard
      v-for="el in currencies"
      :key="el.currency"
      :currency="el.currency"
      :ammount="el.ammount"
    ></SmallCard>
  </div>
</template>
<script>
import SmallCard from "../components/SmallCard";
export default {
  data: () => ({
    currencies: [
      { currency: "dollar", ammount: 300.23 },
      { currency: "zlotys", ammount: 20.2 }
    ]
  }),
  components: {
    SmallCard
  }
};
</script>