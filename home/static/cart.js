export class cart {
    cartItems = [];
    #key

    constructor(itemKey){
        this.#key = itemKey;
    }

    loadFromStorage() {
        let storage = localStorage.getItem(this.#key);
        
        if(storage){
            this.cartItems = JSON.parse(storage)
        }else{
            localStorage.setItem(this.#key, JSON.stringify([]));
        }
    }

    saveItem(item){
        let name = item.get('productName')

        if(this.cartItems.length == 0){

            this.cartItems.push({
                name: item.get('productName'),
                color: item.get('productColor'),
                quantity: item.get('productQuantity'),
                price: item.get('productPrice'),
                size: item.get('productSize')
            });
        }else{

            this.cartItems.forEach(product=>{
            
                if(name == product.name){
                    product.quantity += item.get('productQuantity')
                }else{

                    this.cartItems.push({
                        name: item.get('productName'),
                        color: item.get('productColor'),
                        quantity: item.get('productQuantity'),
                        price: item.get('productPrice'),
                        size: item.get('productSize')
                    });
                }
            })

        }



        localStorage.setItem(this.#key, JSON.stringify(this.cartItems));
    }

    addProductToElement(container){
    
        let html = '';
    
        this.cartItems.forEach(item => {

            html += `
                <div id="itemContainer" class="col">
                    <div class="row row-cols-3">
                    <div class="col px-4 pb-4">
                        <img class="image-fluid w-75" id="itemImage" src="/static/images/${item.color}" alt="">
                    </div>
                    <div class="col">
                        <p id="itemName">${item.name}</p>
                    </div>
                    <div class="col">
                        <p id="Quantity">${item.quantity}</p>
                    </div>
                    </div>
                </div>
            `
        })

        container.innerHTML += html;

    }

}