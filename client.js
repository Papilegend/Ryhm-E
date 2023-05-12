// deklarareein HTML elemendid (IP address input, username input, message container, message input, send button)
const ipInput = document.getElementById('ip-input');
const usernameInput = document.getElementById('username-input');
const messagesContainer = document.getElementById('messages-container');
const messageInput = document.getElementById('message-input');
const sendButton = document.querySelector('button[type="button"]');

let ws; // deklareerin websocketi muutuja

// funktsioon kutsutakse välja kui kasutaja vajutab nuppu 'connect'
function connect() {
  // ip aadressi ja kasutajanime saamine sisendi väljadest
  const ip = ipInput.value.trim();
  const username = usernameInput.value.trim();

  // mõlemad väljad peavad olema täidetud
  if (ip && username) {
    // teeb uue websocketi ja ühendub serveriga
    ws = new WebSocket(`ws://${ip}:12345`);

    // kui ühendus serveriga õnnestus
    ws.onopen = () => {
      // saadab sõnumi serverile
      const new_user_notice = `${username} connected to a server`;
      ws.send(new_user_notice);

      // lubab sõnumi sisendi ja send buttoni kui connection õnnestus
      messageInput.disabled = false;
      sendButton.disabled = false;

      // keyup event listener sisendi väljale
      messageInput.addEventListener('keyup', (event) => {
        if (event.key === 'Enter') {
          sendMessage();
        }
      });
    };

    ws.onmessage = (event) => {
      // convertib saabunud sõnumi data stringks
      const message = event.data.toString();
      // teeb uue <p> elemendi et näidata sõnumit
      const messageElement = document.createElement('p');
      // assignib 'message' väärtuse textContenti '<p>' elemendi külge
      messageElement.textContent = message;
      // appendib '<p>' elemendi, mis sisaldab messaget chati konteinerisse
      messagesContainer.appendChild(messageElement);
    };
  }
}

function sendMessage() {
  // teeb sõnumi, kus enne sõnumit on kasutajanimi
  const message = `${usernameInput.value.trim()}: ${messageInput.value.trim()}`;
  // saadab sõnumi websocketi connectioni kaudu
  ws.send(message);
  // kustutab sõnumi saatmise inputi välja, et kasutaja saaks saata uue sõnumi
  messageInput.value = '';
}