import express from "express";

const app = express();

const port = 1245;

const listProducts = [
    { Id: 1, name: "Suitcase 250", price: 50, stock: 4 },
    { Id: 2, name: "Suitcase 450", price: 100, stock: 10 },
    { Id: 3, name: "Suitcase 650", price: 350, stock: 2 },
    { Id: 4, name: "Suitcase 1050", price: 550, stock: 5 }
]

function getItemById(id) {
    return listProducts.filter(prod => prod.Id == id)
}

app.get('/list_products', (req, res) => {
    res.send(listProducts);
})

app.listen(port, () => {
    console.log('....');
})
module.exports = getItemById;