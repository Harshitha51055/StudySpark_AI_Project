const content = document.getElementById("content");
const charCount = document.getElementById("charCount");
const generateBtn = document.getElementById("generateBtn");
const clearBtn = document.getElementById("clearBtn");
const copyBtn = document.getElementById("copyBtn");
const statusBox = document.getElementById("status");
const resultBox = document.getElementById("result");
let selectedTask = "notes";

content.addEventListener("input", () => {
  charCount.textContent = `${content.value.length.toLocaleString()} / 12,000 characters`;
});
document.querySelectorAll(".task").forEach(button => {
  button.addEventListener("click", () => {
    document.querySelectorAll(".task").forEach(b => b.classList.remove("active"));
    button.classList.add("active");
    selectedTask = button.dataset.task;
  });
});
clearBtn.addEventListener("click", () => {
  content.value = "";
  charCount.textContent = "0 / 12,000 characters";
  content.focus();
});
generateBtn.addEventListener("click", async () => {
  const value = content.value.trim();
  if (value.length < 3) {
    statusBox.hidden = false;
    statusBox.textContent = "Please enter a topic or paste some study material first.";
    resultBox.hidden = true;
    return;
  }
  generateBtn.disabled = true;
  generateBtn.innerHTML = "Generating... <span>◌</span>";
  statusBox.hidden = false;
  statusBox.textContent = "StudySpark AI is preparing your content. This may take a few seconds...";
  resultBox.hidden = true;
  copyBtn.disabled = true;
  try {
    const response = await fetch("/generate", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({content: value, task: selectedTask})
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || "Something went wrong.");
    resultBox.textContent = data.result;
    resultBox.hidden = false;
    statusBox.hidden = true;
    copyBtn.disabled = false;
  } catch (error) {
    statusBox.textContent = error.message || "Unable to generate content. Please try again.";
    resultBox.hidden = true;
  } finally {
    generateBtn.disabled = false;
    generateBtn.innerHTML = 'Generate study content <span>→</span>';
  }
});
copyBtn.addEventListener("click", async () => {
  if (!resultBox.hidden) {
    try {
      await navigator.clipboard.writeText(resultBox.textContent);
      copyBtn.textContent = "Copied!";
      setTimeout(() => copyBtn.textContent = "Copy result", 1400);
    } catch {
      copyBtn.textContent = "Copy unavailable";
    }
  }
});
