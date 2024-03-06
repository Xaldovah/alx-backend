const express = require('express');
const { promisify } = require('util');
const redis = require('redis');

const app = express();
const port = 1245;

// Data
const listProducts = [
    { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
    { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
    { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
    { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 }
];

// Data access
const getItemById = id => listProducts.find(item => item.itemId === id);

// Server
app.listen(port, () => {
    console.log(`Server is listening on port ${port}`);
});

// Products
app.get('/list_products', (req, res) => {
    res.json(listProducts.map(item => ({
        itemId: item.itemId,
        itemName: item.itemName,
        price: item.price,
        initialAvailableQuantity: item.initialAvailableQuantity
    })));
});

// Redis client
const client = redis.createClient();
const reserveStockById = promisify(client.set).bind(client);
const getCurrentReservedStockById = promisify(client.get).bind(client);

// Product detail
app.get('/list_products/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    const item = getItemById(itemId);
    if (!item) {
        return res.json({ status: 'Product not found' });
    }
    const currentQuantity = await getCurrentReservedStockById(`item.${itemId}`);
    res.json({ itemId, itemName: item.itemName, price: item.price, initialAvailableQuantity: item.initialAvailableQuantity, currentQuantity: currentQuantity || 0 });
});

// Reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    const item = getItemById(itemId);
    if (!item) {
        return res.json({ status: 'Product not found' });
    }
    const currentQuantity = await getCurrentReservedStockById(`item.${itemId}`);
    if (!currentQuantity || currentQuantity < 1) {
        return res.json({ status: 'Not enough stock available', itemId: itemId });
    }
    await reserveStockById(`item.${itemId}`, currentQuantity - 1);
    res.json({ status: 'Reservation confirmed', itemId: itemId });
});
