ptotal = document.querySelector('#total');
cart = document.querySelector('#cart');
pcart = document.querySelector('#productcart12');
products = document.querySelector('#productlist123');
addCart();
function addProduct(id){
    var nameid = "#product" + id;
    var priceid = "#productprice" + id;
    var categoryid = "#category" + id;
    var aciliid = "#acili" + id;
    var acisizid = "#acisiz" + id;
    var name = document.querySelector(nameid).innerHTML;
    var price = document.querySelector(priceid).innerHTML;
    var category = document.querySelector(categoryid).innerHTML;
    var acisiz = document.querySelector(aciliid);
    var acili = document.querySelector(acisizid);
    var total = localStorage.getItem('total');
    var orders = JSON.parse(localStorage.getItem('orders'));
    var cartSize = orders.length;
    
        
        
    
    if( category == 'Kebaplar' || category == 'Pideler'){
        if(acili.checked){
            acivar = acili.value;
            orders[cartSize] = [id ,name, price, acivar];
            orders = localStorage.setItem('orders', JSON.stringify(orders));
            orders = JSON.parse(localStorage.getItem('orders'));
            total = localStorage.getItem('total');
            total = Number(total) + Number(price);
            total = localStorage.setItem('total', total);
            addCart();
            
        }else{
            acivar = acisiz.value;
            orders[cartSize] = [id, name, price, acivar];
            orders = localStorage.setItem('orders', JSON.stringify(orders));
            orders = JSON.parse(localStorage.getItem('orders'));
            total = localStorage.getItem('total');
            total = Number(total) + Number(price);
            total = localStorage.setItem('total', total);
            addCart();
        }   
    }
    else{
        orders[cartSize] = [id, name, price, ''];
        orders = localStorage.setItem('orders', JSON.stringify(orders));
        orders = JSON.parse(localStorage.getItem('orders'));
        total = localStorage.getItem('total');
        total = Number(total) + Number(price);
        total = localStorage.setItem('total', total);
        addCart();
    }
}
function addCart() {
    orders = JSON.parse(localStorage.getItem('orders'));
    total = localStorage.getItem('total');
    cartSize = orders.length;
    cart.innerHTML = cartSize;
    pcart.innerHTML = "";
    for (let i = 0; i < cartSize; i++) {
        button = '<button id = "deleteBtn" onclick = "removeP('  + i + ')">X</button>'
        pcart.innerHTML += "<li class='text-white my-1'>" + orders[i][0] + ' ' + orders[i][1] + ' ' + orders[i][2]+ ' ₺ ' + orders[i][3] + button +  "</li>";
        products.innerHTML += "<input style='display: none;' type='text' class='form-control' name='proid" + orders[i][0] + "' id='proname' value='" + orders[i][0] + "'></input>";
    }
    ptotal.innerHTML = "Toplam : " + total + " ₺";
}



function removeP(n){
    orders = JSON.parse(localStorage.getItem('orders'));
    total = localStorage.getItem('total');
    total = Number(total) - Number(orders[n][2]);
    orders.splice(n, 1);
    orders = localStorage.setItem('orders', JSON.stringify(orders));
    total = localStorage.setItem('total', total);
    addCart();
}

document.getElementById("reset").addEventListener("click", reset);
function reset(){
    localStorage.setItem('orders', JSON.stringify([]));
    localStorage.setItem('total', 0);
    pcart.innerHTML = "";
    cart.innerHTML = "0";
    ptotal.innerHTML = "Toplam : 0 ₺";
}
