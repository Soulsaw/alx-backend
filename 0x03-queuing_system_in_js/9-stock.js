import express from "express";
import { createClient } from "redis";
const { promisify } = require('util');
//Express server handling
const app = express();
app.use(express.json())
const port = 1245;
//Redis client handling
const client = createClient();

const listProducts = [
    { Id: 1, name: "Suitcase 250", price: 50, stock: 4 },
    { Id: 2, name: "Suitcase 450", price: 100, stock: 10 },
    { Id: 3, name: "Suitcase 650", price: 350, stock: 2 },
    { Id: 4, name: "Suitcase 1050", price: 550, stock: 5 }
]
const get = promisify(client.get).bind(client);

client.on('error', (err) => {
    console.log(`Redis client not connected: ${err.message}`);
});

function getItemById(id) {
    return listProducts.filter(prod => prod.Id === id)[0]
}

function reserveStockById(itemId, stock) {
    client.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
    const stock = await get(`item.${itemId}`);
    return parseInt(stock, 10) || 0;
}

app.get('/list_products', (req, res) => {
    const products = listProducts.map(product =>(
        {
            itemId:product.Id,
            itemName: product.name,
            price: product.price,
            initialAvailableQuantity: product.stock
        }
    ))
    res.json(products);
})

app.get('/list_products/:itemId', async (req, res) => {
    const id = parseInt(req.params.itemId);
    const item = getItemById(id);
    if (item) {
        const reserveStock = await getCurrentReservedStockById(item.Id);
        const result = {
            "itemId": item.Id,
            "itemName": item.name,
            "price": item.price,
            "initialAvailableQuantity": item.stock,
            "currentQuantity": item.stock - reserveStock
        }
        res.json(result);
    }
    else {
        res.status(404).json({ 'status': 'Product not found' });
    }
})

app.get('/reserve_product/:itemId', async (req, res) => {
    const id = parseInt(req.params.itemId);
    const item = getItemById(id);
    if (item) {
        if (item.stock <= 0) {
            res.status(400).json({ "status": "Not enough stock available", 'itemId': item.Id })
        } else {
            const reserveStock = await getCurrentReservedStockById(item.Id);
            reserveStockById(item.Id, reserveStock + 1);
            res.json({ 'status': 'Reservation confirmed', 'itemId': item.Id })
        }
    }
    else {
        res.status(404).json({ 'status': 'Product not found' });
    }
})

app.listen(port, () => {
    console.log('....');
})
module.exports = getItemById;