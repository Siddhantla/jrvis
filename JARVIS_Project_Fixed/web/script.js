window.onload = function () {
  const bootAudio = document.getElementById("boot-audio");
  const greetingAudio = document.getElementById("greeting-audio");

  if (bootAudio) {
    bootAudio.play().catch(() => {
      document.body.addEventListener("click", () => bootAudio.play(), { once: true });
    });
  }

  setTimeout(() => {
    const boot = document.getElementById("boot-screen");
    if (boot) boot.style.display = "none";

    if (greetingAudio) {
      greetingAudio.play().catch(() => {
        document.body.addEventListener("click", () => greetingAudio.play(), { once: true });
      });
    }
  }, 3000);
};

async function startListening() {
  const response = await eel.listen_command()();
  document.getElementById("output").innerText = response;
}

async function sendCommand() {
  const inputBox = document.getElementById("chatbox");
  const input = inputBox.value.trim();
  if (input === "") return;
  const response = await eel.handle_command(input)();
  document.getElementById("output").innerText = response;
  inputBox.value = "";
}
