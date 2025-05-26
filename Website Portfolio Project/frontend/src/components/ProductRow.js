import React from "react";
import ProductQuantity from "./ProductQuantity";

function ProductRow(input) {
  return (
    <tr>
      <td>{input.item.company}</td>
      <td>{input.item.product}</td>
      <td>{input.item.price}</td>
      <td>
        <ProductQuantity />
      </td>
    </tr>
  );
}

export default ProductRow;
