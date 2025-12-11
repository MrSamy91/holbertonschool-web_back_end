function getPaymentTokenFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success) {
      resolve({ data: 'Successful response from the API' });
    }
    // Si success=false, la promesse reste non résolue
  });
}

module.exports = getPaymentTokenFromAPI;
