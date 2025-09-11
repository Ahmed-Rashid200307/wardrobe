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
        let color = item.get('productColor')

        if(this.cartItems.length == 0){

            this.cartItems.push({
                name: item.get('productName'),
                color: item.get('productColor'),
                quantity: Number(item.get('productQuantity')),
                price: item.get('productPrice'),
                size: item.get('productSize')
            });
        }else{

            this.cartItems.forEach(product=>{
            
                if(name == product.name && color == product.color){
                    product.quantity += Number(item.get('productQuantity'));
                }else{

                    this.cartItems.push({
                        name: item.get('productName'),
                        color: item.get('productColor'),
                        quantity: Number(item.get('productQuantity')),
                        price: item.get('productPrice'),
                        size: item.get('productSize')
                    });
                }
            })

        }



        localStorage.setItem(this.#key, JSON.stringify(this.cartItems));
    }

    renderProducts(container){
    
        let html = '';
    
        this.cartItems.forEach(item => {

            html += `
                <div id="itemContainer" class="col">
                    <div class="row">
                        <div class="col-3 py-2">
                            <img class="image-fluid w-100" id="itemImage" src="/static/images/${item.color}" alt="">
                        </div>

                        <div class="col-8">
                        <div class="row row-cols-1 py-2">
                            <div class="col mb-4">
                                <p id="itemName">${item.name}</p>
                            </div>
                            <div class="col">
                                <p id="Quantity">${item.quantity}X</p>
                            </div>
                        </div>
                        </div>

                        <div class="col-1 p-0 align-items-end">
                            <img src="/static/delete.svg" alt="">
                        </div>
                    </div>
                </div>
            `
        })

        container.innerHTML = html;

    }

}

const customerCart = new cart('wardrobeCart');
customerCart.loadFromStorage();

export default customerCart;