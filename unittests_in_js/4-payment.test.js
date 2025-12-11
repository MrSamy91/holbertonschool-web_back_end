const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', () => {
  it('should call Utils.calculateNumber and log the correct message', () => {
    // Stub : remplacer la fonction par un retour fixe
    const stub = sinon.stub(Utils, 'calculateNumber').returns(10);

    // Spy sur console.log
    const logSpy = sinon.spy(console, 'log');

    // Appel de la fonction
    sendPaymentRequestToApi(100, 20);

    // Vérification du stub
    expect(stub.calledOnce).to.be.true;
    expect(stub.calledWith('SUM', 100, 20)).to.be.true;

    // Vérification du spy
    expect(logSpy.calledOnce).to.be.true;
    expect(logSpy.calledWith('The total is: 10')).to.be.true;

    // Restaurer stub et spy
    stub.restore();
    logSpy.restore();
  });
});
