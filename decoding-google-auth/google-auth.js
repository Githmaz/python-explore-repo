const axios = require('axios');

const code = "4/0AeaYSHDl_yJ1KY_4JhPPUL04RgR1tVAWa2fDZhGxflVkcSk9SsLMeSl-DkBIzZlz3hGxWw";
const clientId = "your_client_id";
const clientSecret = "your_client_secret";
const redirectUri = "your_redirect_uri";

axios.post('https://oauth2.googleapis.com/token', {
  code: code,
  client_id: clientId,
  client_secret: clientSecret,
  redirect_uri: redirectUri,
  grant_type: 'authorization_code'
})
.then(response => {
  console.log('Access token:', response.data.access_token);
})
.catch(error => {
  console.error('Error exchanging code for access token:', error);
});
