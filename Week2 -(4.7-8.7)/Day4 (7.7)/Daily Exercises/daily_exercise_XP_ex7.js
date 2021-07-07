let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

let shoppingList=["banana", "orange", "apple", "tomato"];


function mybill(){
    let total=0;
    //for each item in our shopping list we check.......
    for(let i in shoppingList){
             //we reset this flag for every new shoppingList item-to know if the item is ever in stock
            let flag=0; //0=doesn't exist yet
            //we check if that item exists
            for(const x in stock){
                    if(x==shoppingList[i]){
                       //if it exists we check if it is in stock
                       flag=1; //it exists!
                       if(stock[x]>0){
                            //we add the price to our total
                            total+=prices[x];
                            //we can break the inner loop here-we have already found what we are searching for
                            break;
                         //we decrease the item stock by one
                         stock[x]-=1;
                       }
                       else{
                        //we reach this 'else' if the item exits in 'stock' but there remain ZERO currently IN stock
                        console.log(`I'm sorry, but ${x} is out of stock. Can we interest you in something else?`);
                       }

                     }   
            }

            //if we have gone through the entire stock and it doesnt exist (in the stock options) we obviously can't buy it
            if(flag==0){
                    console.log(`I'm sorry, we do not carry the product ${shoppingList[i]}`);

             }
    }

//finally, at the very end. We return the total size of our bill
return total;
}



//we call the function here- but we need to actually print it if we want to see the total
//mybill();
//example:
console.log(mybill());