import Vue from "vue";
export default{
    async getStockNames(){
        return Vue.axios.get("/stocks/getNameList/" );
    },
    async getStockPrices(stockName){
        return Vue.axios.get("/stocks/getPrices/" ,{ params: { stockName: stockName } });
    }

};