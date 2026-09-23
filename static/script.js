const SINGLE_OPERAND_OPS = new Set(["square", "cube"]);

const resultEl = document.getElementById("result");
const aInput = document.getElementById("a");
const bInput = document.getElementById("b");

function setResult(text, mode) {
  resultEl.textContent = text;
  resultEl.classList.remove("pending", "err");
  if (mode) resultEl.classList.add(mode);
}

async function calc(operation) {
  const a = parseFloat(aInput.value);
  const b = parseFloat(bInput.value);
  const needsB = !SINGLE_OPERAND_OPS.has(operation);

  if (Number.isNaN(a) || (needsB && Number.isNaN(b))) {
    setResult("Enter " + (needsB ? "both numbers" : "a number") + " first.", "err");
    return;
  }

  setResult("Calculating…", "pending");

  const body = needsB ? { a, b } : { a };

  try {
    const response = await fetch("/" + operation, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });

    if (!response.ok) {
      const errData = await response.json().catch(() => ({}));
      setResult(errData.error || "Something went wrong (" + response.status + ")", "err");
      return;
    }

    const data = await response.json();
    setResult(data.result);
  } catch (error) {
    setResult("Could not reach the server: " + error.message, "err");
  }
}

document.querySelectorAll(".key[data-op]").forEach((btn) => {
  btn.addEventListener("click", () => calc(btn.dataset.op));
});

document.getElementById("clear").addEventListener("click", () => {
  aInput.value = "";
  bInput.value = "";
  setResult("—");
});
