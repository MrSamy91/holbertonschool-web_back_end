const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', () => {
  let logSpy;

  // Avant chaque test, créer le spy sur console.log
  beforeEach(() => {
    logSpy = sinon.spy(console, 'log');
  });

  // Après chaque test, restaurer le spy
  afterEach(() => {
    logSpy.restore();
  });

  it('should log "The total is: 120" when called with 100, 20', () => {
    sendPaymentRequestToApi(100, 20);

    expect(logSpy.calledOnce).to.be.true;
    expect(logSpy.calledWith('The total is: 120')).to.be.true;
  });

  it('should log "The total is: 20" when called with 10, 10', () => {
    sendPaymentRequestToApi(10, 10);

    expect(logSpy.calledOnce).to.be.true;
    expect(logSpy.calledWith('The total is: 20')).to.be.true;
  });
});
