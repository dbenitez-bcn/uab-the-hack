/**
 * Import function triggers from their respective submodules:
 *
 * const {onCall} = require("firebase-functions/v2/https");
 * const {onDocumentWritten} = require("firebase-functions/v2/firestore");
 *
 * See a full list of supported triggers at https://firebase.google.com/docs/functions
 */

const {onRequest} = require("firebase-functions/v2/https");
const logger = require("firebase-functions/logger");

const { initializeApp, applicationDefault, cert } = require('firebase-admin/app');
const { getFirestore, Timestamp, FieldValue, Filter } = require('firebase-admin/firestore');

// Create and deploy your first functions
// https://firebase.google.com/docs/functions/get-started

exports.helloWorld = onRequest((request, response) => {
   logger.info("Hello logs!", {structuredData: true});
   response.send("Hello from Firebase!");
});

initializeApp();

const db = getFirestore();

// ADD DATA

const docRef = db.collection('users').doc('alovelace');

await docRef.set({
  first: 'Ada',
  last: 'Lovelace',
  born: 1815
});


const aTuringRef = db.collection('users').doc('aturing');

await aTuringRef.set({
  'first': 'Alan',
  'middle': 'Mathison',
  'last': 'Turing',
  'born': 1912
});

// READ DATA

const snapshot = await db.collection('users').get();

snapshot.forEach((doc) => {
  console.log(doc.id, '=>', doc.data());
});

