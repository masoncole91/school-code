import React, { useState } from "react";
import { MdThumbUp, MdThumbDown } from "react-icons/md";

function ProductQuantity() {
  const [num, change] = useState(0);

  const up = () => {
    if (num < 10) {
      change(num + 1);
    };
  };

  const down = () => {
    if (num > 0) {
      change(num - 1);
    }
  };

  return (
    <div class="react">
      <MdThumbUp type="up" onClick={up} />
      {num}
      <MdThumbDown onClick={down} />
    </div>
  );
}

export default ProductQuantity;
