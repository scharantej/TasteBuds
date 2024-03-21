## Flask Application Design

### HTML Files

#### `index.html`
- Main page of the website
- Contains a form for users to search for restaurants and order food
- Submit button triggers a POST request to the `/order` route

#### `order.html`
- Order confirmation page
- Displays the order details
- Allows users to edit or cancel their order

### Routes

#### `/`
- GET: Renders the `index.html` page
- POST: Receives the order details and processes the order
- Redirects to `order.html` upon successful order placement

#### `/order`
- GET: Renders the `order.html` page with the order details
- POST: Updates or cancels the order based on user input
- Redirects to `index.html` upon order update or cancellation