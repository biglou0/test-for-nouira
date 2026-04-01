const express = require("express");
const app = express();
const PORT = 3000;

app.use(express.json());
app.use(express.static("public"));

app.post("/calculate", (req, res) => {
  const { a, b, operator } = req.body;

  if (a == null || b == null || !operator) {
    return res.status(400).json({ error: "Missing fields: a, b, operator" });
  }

  const num1 = parseFloat(a);
  const num2 = parseFloat(b);

  if (isNaN(num1) || isNaN(num2)) {
    return res.status(400).json({ error: "Invalid numbers" });
  }

  let result;
  switch (operator) {
    case "+": result = num1 + num2; break;
    case "-": result = num1 - num2; break;
    case "*": result = num1 * num2; break;
    case "/":
      if (num2 === 0) return res.status(400).json({ error: "Cannot divide by zero" });
      result = num1 / num2;
      break;
    default:
      return res.status(400).json({ error: `Unknown operator '${operator}'` });
  }

  res.json({ result });
});

app.listen(PORT, () => {
  console.log(`Calculator running at http://localhost:${PORT}`);
});
