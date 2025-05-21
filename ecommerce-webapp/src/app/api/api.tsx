import axios from "axios";  
import ICartProduct from "../Interfaces/ICartProduct";

export async function getProducts({ query = "", id = "", pageSize = 10, currentPage = 1 }: { query?: string; id?: string; pageSize?:number; currentPage?:number }) {
    let url: string
    if(id){
        url = `/api/product/${id}`
    } else{
        url = `/api/products?query=${query}&pageSize=${pageSize}&currentPage=${currentPage}`
    }
    return fetch(url)
    .then((response: Response) => response.json());
}

export async function getCart(code: string) {
    return fetch(`/api/cart/${code}`)
    .then((response: Response) => response.json());
}

export async function updateCart(code: string, products: ICartProduct[]) {
    return axios.put(`/api/cart/${code}`, products);
}

export async function createOrder(code: string) {
    return axios.post(`/api/order/`, {cart_code:code});
}