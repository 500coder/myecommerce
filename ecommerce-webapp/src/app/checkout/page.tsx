'use client'
import { ReactElement, useEffect, useState } from "react";
import styles from "../styles/checkout.module.css";
import { toBRL } from "../utils/utils";
import { useRouter } from "next/navigation";

interface IProduct {
  id: number;
  quantity: number;
  thumbnailUrl: string;
  title: string;
  unitPrice: string;
}

interface IOrderData {
  amount: string;
  created_at: string;
  id: number;
  products: IProduct[];
  updated_at: string;
  status: string;
}

interface IResponseData {
  data: IOrderData;
  status: number;
  statusText: string;
  headers: Record<string, string>;
  config: any;     
  request: any;
}

export default function Checkout(): ReactElement{
    const router = useRouter();
    const [order, setOrder] = useState<IResponseData>();
    useEffect(()=>{
        const saved: string = localStorage.getItem('orderObject')!;
        if(saved){
            try{
                setOrder(JSON.parse(saved));
            }catch (error){
                console.error('Erro ao parsear JSON do localStorage', error);
            }
        }
    }, []);

    return (
        <div className={styles.container}>
            <div className={styles.hero}><h2>PEDIDO FINALIZADO 🎉</h2></div>
            <div className={styles.rowItem}>
                <p> O seu pedido foi finlizado com sucesso. </p>
                <table>
                    <thead>
                        <tr><td>Id</td><td>Status</td><td>Total</td></tr>
                    </thead>
                    <tbody>
                       
                        <tr><td>{order?.data.id}</td><td>{order?.data.status}</td><td>{toBRL(+order?.data.amount!)}</td></tr>
                       
                    </tbody>
                </table>
                <table>
                    <thead>
                        <tr><td>Produtos</td><td>Qtde</td><td>Preço unitário</td><td>Total</td></tr>
                    </thead>
                    <tbody>
                        {order?.data.products.map((x) => (
                        <tr key={x.id}><td>{x.title}</td><td>{x.quantity}</td><td>{toBRL(+x.unitPrice)}</td><td>{toBRL(+x.unitPrice * x.quantity)}</td></tr>
                        ))}
                    </tbody>
                    <tfoot>
                        <tr><td></td><td></td><td></td><td>{toBRL(+order?.data.amount!)}</td></tr>
                    </tfoot>
                </table>
                <p>
                    Se isso fosse um e-commerce de verdade, provavelmente você receberia alguma coisa.
                    Porém, este é apenas um exercício. Então, não vamos lhe entregar nada.
                </p>
                <p>
                    De qualquer forma, obrigado pela preferência!
                </p>
                <button className={styles.btn_back_to_products_list} onClick={(e)=> {e.preventDefault(); router.push('/')}}>Ver mais produtos</button>
            </div>
        </div>
    );
}