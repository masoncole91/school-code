import React from "react";
import ProductRow from "../components/ProductRow.js";

function OrderPage({ products }) {
  return (
    <div>
      <h2>Order</h2>
      <article>
        <p>
          Business websites often offer products and services with order forms.
          Users can purchase up to five different pet novelty items below. Phone
          calls or face-to-face isn't necessary; submitting their contact,
          purchase, and delivery information suffices.
          <br></br>
          <br></br>
          Order forms should offer multiple payment options, and sites should
          protect sensitive information like addresses or credit card numbers.
          <br></br>
          <br></br>
          User data can optimize customer experience with personalized
          recommendations and tracked purchase history. Some have argued this is
          unethical, but most agree companies should inform users what data is
          saved.
        </p>
        <fieldset>
          <form action="/order" method="POST"></form>
          <legend>About You</legend>
          <p>
            <label for="name" class="required">
              Name:
            </label>
            <input
              type="text"
              name="firstlast"
              required
              placeholder="First and Last"
              autofocus
            ></input>
          </p>
          <p>
            <label for="email" class="required">
              Email:
            </label>
            <input
              type="email"
              name="contactemail"
              required
              placeholder="username@host.com"
            ></input>
          </p>
          <p>
            <label for="address" class="required">
              Address:
            </label>
            <input
              type="text"
              name="address"
              required
              placeholder="123 Maple St."
            ></input>
          </p>
        </fieldset>
        <fieldset>
          <legend>Order Form</legend>
          <table>
            <caption>These items are in stock.</caption>
            <thead>
              <tr>
                <th>Company</th>
                <th>Product</th>
                <th>Price</th>
                <th>Quantity</th>
              </tr>
            </thead>
            <tbody>
              {products.map((currentProduct, index) => (
                <ProductRow item={currentProduct} key={index} />
              ))}
            </tbody>
          </table>
          <label for="message" class="required">
            Delivery Instructions:
          </label>
          <textarea
            name="instructions"
            maxlength="500"
            required
            placeholder="500 characters or less"
          ></textarea>
          <button type="submit">Submit</button>
        </fieldset>
      </article>
    </div>
  );
}

export default OrderPage;
