const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', () => {
  it('should call Utils.calculateNumber with SUM and the correct arguments', () => {
    // Créer le spy
    const spy = sinon.spy(Utils, 'calculateNumber');

    // Appeler la fonction
    sendPaymentRequestToApi(100, 20);

    // Vérifier que le spy a été appelé avec les bons arguments
    expect(spy.calledOnce).to.be.true;
    expect(spy.calledWith('SUM', 100, 20)).to.be.true;

    // Restaurer le spy
    spy.restore();
  });
});
